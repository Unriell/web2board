from wshubsapi.Hub import Hub

from libs.CompilerUploader import getCompilerUploader, CompilerException, ERROR_BOARD_NOT_SUPPORTED
from libs.Config import Config
from libs.MainApp import getMainApp
from libs.Updaters.BitbloqLibsUpdater import getBitbloqLibsUpdater
from libs.Updaters.Updater import VersionInfo
from libs.Updaters.Web2boardUpdater import getWeb2boardUpdater
from libs.WSCommunication.Hubs.CodeHub import CodeHub


class BoardConfigHubException(Exception):
    pass


class BoardConfigHub(Hub):

    def __init__(self):
        super(BoardConfigHub, self).__init__()
        self.compilerUploader = getCompilerUploader()

    def getVersion(self):
        # todo: check in bitbloq if this is what we want
        return Config.version

    def setBoard(self, board, _sender):
        """
        :param board: board type
        :type _sender: ConnectedClientsGroup
        """
        if not board or board == "undefined":
            raise BoardConfigHubException('BOARD UNDEFINED')

        CodeHub.tryToTerminateSerialCommProcess()

        _sender.isSettingBoard()
        try:
            self.compilerUploader.setBoard(board)
        except CompilerException as e:
            if e.code == ERROR_BOARD_NOT_SUPPORTED["code"]:
                raise BoardConfigHubException('NOT SUPPORTED BOARD')

        # todo: do we need to set the port here??
        try:
            port = self.compilerUploader.getPort()
            _sender.isSettingPort(port)
        except CompilerException:
            raise BoardConfigHubException('NO PORT FOUND')
        return True  # if return None, client is not informed that the request is done

    def setLibVersion(self, version):
        libUpdater = getBitbloqLibsUpdater()
        versionInfo = VersionInfo(version, Config.bitbloqLibsDownloadUrlTemplate.format(version=version))
        if libUpdater.isNecessaryToUpdate(versionToCompare=versionInfo):
            libUpdater.update(versionInfo)
        return True  # if return None, client is not informed that the request is done

    def setWeb2boardVersion(self, version):
        gui = getMainApp().w2bGui
        w2bUpdater = getWeb2boardUpdater()
        gui.startDownload(version)
        w2bUpdater.downloadVersion(version, gui.refreshProgressBar, gui.downloadEnded).get()
        w2bUpdater.makeAnAuxiliaryCopy()
        w2bUpdater.runAuxiliaryCopy(version)
