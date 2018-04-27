import shutil

import info
from Package.BinaryPackageBase import *

class subinfo(info.infoclass):
    def setTargets(self):
        for version in ['1.27']:
            self.targets[version] = "http://www.foobar.org/libgpg-error-1.27.7z"

        self.description = "libgpg-error"
        self.defaultTarget = '1.27'

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
