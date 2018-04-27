import shutil

import info
from Package.BinaryPackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        for version in ['1.10.0']:
            self.targets[version] = "http://www.foobar.org/gpgme-1.10.0.7z"
        # self.targetDigests['1.10.0'] = '34df759e1ffe4acce301887007cccb62f9496ea0'

        self.description = "gpgme"
        self.defaultTarget = '1.10.0'

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
