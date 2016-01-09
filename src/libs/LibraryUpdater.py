#!/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------#
#                                                                       #
# This file is part of the web2board project                            #
#                                                                       #
# Copyright (C) 2015 Mundo Reader S.L.                                  #
#                                                                       #
# Date: November 2015                                                   #
# Author: Irene Sanz Nieto <irene.sanz@bq.com>                          #
#                                                                       #
# -----------------------------------------------------------------------#
import distutils
import json
import logging
import os
import shutil
from distutils.dir_util import mkpath

from libs import utils
from libs.PathsManager import PathsManager
import libs.base

log = logging.getLogger(__name__)
__globalLibUpdater = None


##
# Class LibraryUpdater, created to check for downloaded libraries and update them if necessary
#
class LibraryUpdater:
    BITBLOQ_LIBS_URL_TEMPLATE = 'https://github.com/bq/bitbloqLibs/archive/v{}.zip'

    def __init__(self):
        self._bitbloqLibsVersion = self.getBitbloqLibsVersion()
        self.necessaryToDownloadLibs = False

    def __copyConfigInHomeIfNotExists(self):
        if not os.path.isfile(PathsManager.SETTINGS_CONFIG_PATH):
            shutil.copyfile(PathsManager.RES_CONFIG_PATH, PathsManager.SETTINGS_CONFIG_PATH)

    def _downloadLibs(self):
        log.info('Downloading new libs, version: {}'.format(self._bitbloqLibsVersion))
        downloadedFilePath = utils.downloadFile(self.BITBLOQ_LIBS_URL_TEMPLATE.format(self._bitbloqLibsVersion))

        log.info('extracting zip')
        utils.extractZip(downloadedFilePath, libs.base.sys_path.get_tmp_path())
        log.info('copying libraries in Arduino\'s libraries directory')
        self._copyLibsInTmpToBoardsLibsPath()

        self.setBitbloqLibsNames(self._getBitbloqLibsNamesFromDownloadedZip())

        # Remove .zip
        try:
            os.remove(downloadedFilePath)
        except OSError as e:
            log.error('exception: {} raised removing libraries zip file'.format(e))

        log.info("Bitbloq libs downloaded")

    def _copyLibsInTmpToBoardsLibsPath(self):
        tmpPath = PathsManager.getBitbloqLibsTempPath(self._bitbloqLibsVersion)
        versionNumber = self._getBitbloqLibsVersionNumber()
        if versionNumber <= 2:
            distutils.dir_util.copy_tree(tmpPath, PathsManager.SKETCHBOOK_LIBRARIES_PATH)
        elif versionNumber > 2:
            for name in os.listdir(tmpPath):
                if os.path.isdir(tmpPath + os.sep + name):
                    distutils.dir_util.copy_tree(tmpPath, PathsManager.SKETCHBOOK_LIBRARIES_PATH)

    def _getBitbloqLibsNamesFromDownloadedZip(self):
        tmpPath = PathsManager.getBitbloqLibsTempPath(self._bitbloqLibsVersion)
        versionNumber = self._getBitbloqLibsVersionNumber()
        if versionNumber <= 2:
            return ['bitbloqLibs']
        elif versionNumber > 2:
            return utils.listDirectoriesInPath(tmpPath)

    def _getBitbloqLibsVersionNumber(self):
        return int(self._bitbloqLibsVersion.replace('.', ''))

    def updateWeb2BoardVersion(self):
        # Get bitbloqLibs version from config file

        self.__copyConfigInHomeIfNotExists()

        with open(PathsManager.RES_CONFIG_PATH) as json_data_file:
            data = json.load(json_data_file)
            versionTrue = str(data.get('bitbloqLibsVersion', "0.0.0"))

        with open(PathsManager.SETTINGS_CONFIG_PATH, "r+") as json_data_file:
            data = json.load(json_data_file)
            versionLocal = str(data['bitbloqLibsVersion'])
            if versionLocal != versionTrue:
                data['bitbloqLibsVersion'] = versionTrue
                # todo: this function does not make any sense :S

    def getBitbloqLibsVersion(self):
        # Get bitbloqLibs version from config file
        self.__copyConfigInHomeIfNotExists()
        with open(PathsManager.SETTINGS_CONFIG_PATH) as json_data_file:
            data = json.load(json_data_file)
            version = str(data['bitbloqLibsVersion'])
        return version

    def getBitbloqLibsName(self):
        # Get bitbloqLibs name from config file
        self.__copyConfigInHomeIfNotExists()
        with open(PathsManager.SETTINGS_CONFIG_PATH) as json_data_file:
            data = json.load(json_data_file)
            bitbloqLibsName = []
            try:
                bitbloqLibsName = data['bitbloqLibsName']
            except:
                log.error('No bitbloqLibsName')
                pass
        return bitbloqLibsName

    def setBitbloqLibsVersion(self, newVersion):
        self.__copyConfigInHomeIfNotExists()
        with open(PathsManager.SETTINGS_CONFIG_PATH, "r") as jsonFile:
            data = json.load(jsonFile)

        data["bitbloqLibsVersion"] = newVersion

        with open(PathsManager.SETTINGS_CONFIG_PATH, "w+") as jsonFile:
            jsonFile.write(json.dumps(data))
        self.necessaryToDownloadLibs = True

    def setBitbloqLibsNames(self, bitbloqLibsNames):
        self.__copyConfigInHomeIfNotExists()
        if not hasattr(bitbloqLibsNames, "__iter__"):
            raise Exception("bitbloqLibsNames have to be a list, received: {}".format(bitbloqLibsNames))

        with open(PathsManager.SETTINGS_CONFIG_PATH, "r") as jsonFile:
            data = json.load(jsonFile)

        data["bitbloqLibsName"] = bitbloqLibsNames

        with open(PathsManager.SETTINGS_CONFIG_PATH, "w+") as jsonFile:
            jsonFile.write(json.dumps(data))

        log.info("config ready")

    def areWeMissingLibs(self):
        self.updateWeb2BoardVersion()

        libsNames = self.getBitbloqLibsName()
        if not os.path.exists(PathsManager.SKETCHBOOK_PATH):
            os.makedirs(PathsManager.SKETCHBOOK_PATH)
        if len(libsNames) < 1:
            return True
        else:
            for lib in libsNames:
                libPath = PathsManager.SKETCHBOOK_LIBRARIES_PATH + lib
                if not os.path.exists(libPath) or not os.listdir(libPath):
                    return True
        return False

    def downloadLibsIfNecessary(self):
        if self.areWeMissingLibs() or self.necessaryToDownloadLibs:
            log.warning("Necessary to update libraries")
            self._downloadLibs()
            self.necessaryToDownloadLibs = False
        else:
            log.info("Libraries are up to date")


def getLibUpdater():
    """
    :rtype: CompilerUploader
    """
    global __globalLibUpdater
    if __globalLibUpdater is None:
        __globalLibUpdater = LibraryUpdater()
    return __globalLibUpdater
