import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.addCachedAutotoolsBuild(f"https://files.kde.org/craft/autotools/2018.02/windows/mingw_{CraftCore.compiler.bits}/gcc/Release/", "autotools/gpg-error-src")

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["win32libs/mingw-crt4msvc"] = "default"

from Package.BinaryPackageBase import *

class BinPackage(BinaryPackageBase):
    def __init__(self, **args):
        BinaryPackageBase.__init__(self)
