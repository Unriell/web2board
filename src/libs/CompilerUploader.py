#!/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------#
#                                                                       #
# This file is part of the web2board project                            #
#                                                                       #
# Copyright (C) 2015 Mundo Reader S.L.                                  #
#                                                                       #
# Date: April - May 2015                                                #
# Author: Irene Sanz Nieto <irene.sanz@bq.com>                          #
#                                                                       #
# -----------------------------------------------------------------------#
import logging
import os
import subprocess

from libs.Decorators.Asynchronous import asynchronous
from libs.PathsManager import PathsManager as pm
from libs.utils import isWindows, isMac, isLinux, listSerialPorts
from platformio.platformioUtils import run as platformioRun
from platformio import exception, util
from platformio.util import get_boards, memoized

log = logging.getLogger(__name__)
__globalCompilerUploader = None

ERROR_BOARD_NOT_SET = {"code": 0, "message": "Necessary to define board before to run/compile"}
ERROR_BOARD_NOT_SUPPORTED = {"code": 1, "message": "Board: {0} not Supported"}
ERROR_NO_PORT_FOUND = {"code": 2, "message": "No port found, check the board is connected"}
ERROR_MULTIPLE_BOARDS_CONNECTED = {"code": 3, "message": "More than one connected board was found. You should only have one board connected"}


class CompilerException(Exception):
    def __init__(self, error, *args):
        self.code = error["code"]
        self.message = error["message"].format(*args)
        super(CompilerException, self).__init__(self.message)


##
# Class CompilerUploader, created to support different compilers & uploaders
#
class CompilerUploader:
    def __init__(self):
        self.board = None  # we use the board name as the environment (check platformio.ini)

    def _getIniConfig(self, environment):
        """
        :type environment: str
            """
        with util.cd(pm.SETTINGS_PLATFORMIO_PATH):
            config = util.get_project_config()

            if not config.sections():
                raise exception.ProjectEnvsNotAvailable()

            known = set([s[4:] for s in config.sections()
                         if s.startswith("env:")])
            unknown = set((environment,)) - known
            if unknown:
                return None

            for section in config.sections():
                envName = section[4:]
                if environment and envName and envName == environment:
                    iniConfig = {k: v for k, v in config.items(section)}
                    iniConfig["boardData"] = get_boards(iniConfig["board"])
                    return iniConfig

    def _callAvrdude(self, args):
        if isWindows():
            cmd = os.path.join(pm.RES_PATH, 'avrdude.exe ') + "-C " + os.path.join(pm.RES_PATH, 'avrdude.conf ') + args
        elif isMac():
            avrPath = pm.MAIN_PATH + "/res/arduinoDarwin"
            cmd = avrPath + "avrdude -C " + avrPath + "avrdude.os.path.join(RES_PATH, 'avrdude.exe ') " + args
        elif isLinux():
            cmd = "avrdude " + args
        else:
            raise Exception("Platform not supported")
        log.info("Command executed: {}".format(cmd))
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             close_fds=(not isWindows()))
        output = p.stdout.read()
        err = p.stderr.read()
        log.debug(output)
        log.debug(err)
        return output, err

    def _searchPorts(self, mcu, baudRate):
        portsToUpload = listSerialPorts(lambda x: "Bluetooth" not in x[0])
        availablePorts = map(lambda x: x[0], portsToUpload)
        if len(availablePorts) <= 0:
            return []
        portsToUpload = []
        log.debug("Found available ports: {}".format(availablePorts))
        portResultHashMap = {}
        for port in availablePorts:
            portResultHashMap[port] = self._checkPort(port, mcu, baudRate)

        for port, resultObject in portResultHashMap.items():
            if resultObject.get():
                portsToUpload.append(port)
        return portsToUpload

    @asynchronous()
    def _checkPort(self, port, mcu, baudRate):
        args = "-P " + port + " -p " + mcu + " -b " + str(baudRate) + " -c arduino"
        output, err = self._callAvrdude(args)
        return 'Device signature =' in output or 'Device signature =' in err

    def _run(self, code, upload=False):
        self._checkBoardConfiguration()
        target = ("upload",) if upload else ()
        uploadPort = self.getPort() if upload else None

        with open(os.path.join(pm.SETTINGS_PLATFORMIO_PATH, "src", "main.cpp"), 'w') as mainCppFile:
            mainCppFile.write(code)

        return platformioRun(target=target, environment=(self.board,), project_dir=pm.SETTINGS_PLATFORMIO_PATH,
                             upload_port=uploadPort)[0]

    def _checkBoardConfiguration(self):
        if self.board is None:
            raise CompilerException(ERROR_BOARD_NOT_SET)
        if self._getIniConfig(self.board) is None:
            raise CompilerException(ERROR_BOARD_NOT_SUPPORTED, self.board)

    def getPort(self):
        self._checkBoardConfiguration()
        options = self._getIniConfig(self.board)
        portsToUpload = self._searchPorts(options["boardData"]["build"]["mcu"], options["boardData"]["upload"]["speed"])
        if len(portsToUpload) == 0:
            raise CompilerException(ERROR_NO_PORT_FOUND)
        elif len(portsToUpload) > 1:
            raise CompilerException(ERROR_MULTIPLE_BOARDS_CONNECTED)
        return portsToUpload[0]

    def setBoard(self, board):
        self.board = board
        self._checkBoardConfiguration()

    def compile(self, code):
        return self._run(code, upload=False)

    def upload(self, code):
        return self._run(code, upload=True)

    def uploadAvrHex(self, hexFilePath):
        self._checkBoardConfiguration()
        options = self._getIniConfig(self.board)
        port = self.getPort()
        mcu = options["boardData"]["build"]["mcu"]
        baudRate = str(options["boardData"]["upload"]["speed"])
        args = "-V " + " -P " + port + " -p " + mcu + " -b " + baudRate + " -c arduino -D -U flash:w:" + hexFilePath + ":i"
        return self._callAvrdude(args)


def getCompilerUploader():
    """
    :rtype: CompilerUploader
    """
    global __globalCompilerUploader
    if __globalCompilerUploader is None:
        __globalCompilerUploader = CompilerUploader()
    return __globalCompilerUploader


