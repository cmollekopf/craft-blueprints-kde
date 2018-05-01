import shutil

import info
from Package.BinaryPackageBase import *

class subinfo(info.infoclass):
    def setTargets(self):
        for version in ['2.5.1']:
            self.targets[version] = "http://www.foobar.org/libassuan-2.5.1.7z"

        self.description = "libassuan"
        self.defaultTarget = '2.5.1'

    def setDependencies(self):
        self.runtimeDependencies["virtual/bin-base"] = "default"

class Package(BinaryPackageBase):
    def __init__(self):
        BinaryPackageBase.__init__(self)

    def install(self):
        self.cleanImage()
        return utils.copyDir(os.path.join(self.sourceDir(), "libassuan-2.5.1"), self.installDir(), linkOnly=False)
