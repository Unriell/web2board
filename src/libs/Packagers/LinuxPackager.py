import getpass
from subprocess import call

from libs.Packagers.Packager import Packager
from libs.utils import *
from os.path import join


class LinuxPackager(Packager):
    RELEASE_TYPES = ({"path": "web2board", "desktopName": "Web2Board-PROD"},
                     {"path": "dev/bet", "desktopName": "Web2Board-BETA"},
                     {"path": "dev/qa", "desktopName": "Web2Board-QA"},
                     {"path": "dev/staging", "desktopName": "Web2Board-STAGING"})

    def __init__(self, architecture=Packager.ARCH_64):
        Packager.__init__(self)
        self.architecture = architecture
        self.installerPath = self.installerFolder + os.sep + "debian_{}".format(architecture)

        self.installerCreationPath = join(self.web2boardPath, "deb_web2board_{}_{}".format(architecture, self.version))
        self.installerCreationName = os.path.basename(self.installerCreationPath)
        self.installerCreationExecutablesPath = join(self.installerCreationPath, "executables")
        self.installerCreationDistPath = join(self.installerCreationPath, "opt", "web2board")

        self.pkgPlatformPath = join(self.pkgPath, "linux")
        self.resPlatformPath = join(self.resPath, "linux")
        self.web2boardExecutableName = "web2board"
        self.web2boardSpecPath = join(self.web2boardPath, "web2board-linux.spec")
        self.sconsExecutableName = "sconsScript"
        self.sconsSpecPath = join(self.web2boardPath, "scons-linux.spec")

        self.packageDebianMetadataPath = join(self.installerCreationPath, "DEBIAN")
        self.debianMetadataPath = join(self.pkgPlatformPath, "debian")
        with open(self.packagerResPath + os.sep + "Web2Board-template.desktop") as desktopFile:
            self.Web2BoardDesktopTemplate = desktopFile.read()

    def _makeMainDirs(self):
        Packager._makeMainDirs(self)

    def _addMetadataForInstaller(self):
        Packager._addMetadataForInstaller(self)
        copytree(self.debianMetadataPath, self.packageDebianMetadataPath)
        with open(self.packageDebianMetadataPath + os.sep + "control", "r") as controlFile:
            controlText = controlFile.read()
        with open(self.packageDebianMetadataPath + os.sep + "control", "w") as controlFile:
            controlFile.write(controlText.format(version=self.version, architecture=self.architecture))

        os.chmod(self.debianMetadataPath + os.sep + "postinst", int("775", 8))
        os.chmod(self.debianMetadataPath + os.sep + "postinst", int("775", 8))
        os.chmod(self.debianMetadataPath + os.sep + "control", int("655", 8))

    def _moveDebToInstallerPath(self):
        resultingDeb = self.web2boardPath + os.sep + self.installerCreationName + ".deb"
        shutil.move(resultingDeb, self.installerPath + os.sep + "web2boar.deb")

    def createPackage(self):
        try:
            self._createMainStructureAndExecutables()
            log.debug("Adding metadata for installer")
            self._addMetadataForInstaller()
            os.chdir(self.installerCreationPath)
            log.info("Creating Installer")
            # shutil.make_archive(self.installerCreationPath, "zip", self.installerCreationPath )
            os.system("chmod -R 777 " + self.installerCreationDistPath)
            os.system("gksudo \"chown -R root:root " + self.installerCreationPath + '"')
            call(["dpkg-deb", "--build", self.installerCreationPath])
            self._moveDebToInstallerPath()
            log.info("installer created successfully")
        finally:
            userName = getpass.getuser()
            os.system("gksudo \"chown -R {0} {1} \"".format(userName, self.installerCreationPath))
            log.debug("Cleaning files")
            os.chdir(self.web2boardPath)
            self._clearBuildFiles()
            # self._deleteInstallerCreationFolder()
