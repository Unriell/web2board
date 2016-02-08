import os
import shutil
import sys

import subprocess

import libs.utils as utils
from libs.PathsManager import PathsManager

if __name__ == '__main__':
    web2boardPath = '"' + os.path.join(PathsManager.PROGRAM_PATH, "web2board" + utils.getOsExecutableExtension()) + '"'
    print "web2boardPath: {}".format(web2boardPath)
    # utils.killProcess("web2board")

    if (len(sys.argv) > 1 and sys.argv[1].lower() == "factoryreset") or not os.path.exists(PathsManager.PROGRAM_PATH):
        if os.path.exists(PathsManager.PROGRAM_PATH):
            shutil.rmtree(PathsManager.PROGRAM_PATH)
        print "Extracting web2board..."
        shutil.copytree(utils.getModulePath() + os.sep + "web2board", PathsManager.PROGRAM_PATH)
        subprocess.call(web2boardPath + " --afterInstall")
    else:
        subprocess.call(web2boardPath)
