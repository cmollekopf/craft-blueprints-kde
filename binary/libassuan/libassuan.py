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


class PackageBin(BinaryPackageBase):
    def __init__(self):
        BinaryPackageBase.__init__(self)
        self.subinfo.options.package.withCompiler = False
        self.subinfo.options.package.withSources = False

class Package(PackageBin):
    def __init__(self):
        PackageBin.__init__(self)
