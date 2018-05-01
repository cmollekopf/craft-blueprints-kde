import shutil

import info
from Package.BinaryPackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        for version in ['1.10.0']:
            self.targets[version] = "http://www.foobar.org/gpgme-1.10.0.7z"
        # self.targetDigests['1.10.0'] = '34df759e1ffe4acce301887007cccb62f9496ea0'
        self.patch['1.10.0'] = '34df759e1ffe4acce301887007cccb62f9496ea0'
        self.patchToApply["1.10.0"] = [("gpgme-20180427.diff", 1)]

        self.description = "gpgme"
        self.defaultTarget = '1.10.0'

    def setDependencies(self):
        self.runtimeDependencies["virtual/bin-base"] = "default"
        self.buildDependencies["win32libs/pthreads"] = "default"
        self.runtimeDependencies["win32libs/mingw-crt4msvc"] = "default"
        self.runtimeDependencies["binary/libgpg-error"] = "default"
        self.runtimeDependencies["binary/libassuan"] = "default"

class Package(BinaryPackageBase):
    def __init__(self):
        BinaryPackageBase.__init__(self)

    def install(self):
        self.cleanImage()
        return utils.copyDir(os.path.join(self.sourceDir(), "gpgme-1.10.0"), self.installDir(), linkOnly=False)
