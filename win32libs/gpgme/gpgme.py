import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.addCachedAutotoolsBuild(f"https://files.kde.org/craft/autotools/2018.02/windows/mingw_{CraftCore.compiler.bits}/gcc/Release/", "autotools/gpgme-src")

    def setDependencies(self):
        self.runtimeDependencies['virtual/base'] = 'default'
        if OsUtils.isWin():
            self.runtimeDependencies["win32libs/mingw-crt4msvc"] = "default"
            self.runtimeDependencies['win32libs/assuan2'] = 'default'
            self.runtimeDependencies["win32libs/gpg-error"] = "default"
        else:
            self.runtimeDependencies["autotools/gpgme-src"] = "default"


from Package.BinaryPackageBase import *
from Package.MaybeVirtualPackageBase import *


class BinPackage(BinaryPackageBase):
    def __init__(self, **args):
        BinaryPackageBase.__init__(self)


class Package(MaybeVirtualPackageBase):
    def __init__(self):
        MaybeVirtualPackageBase.__init__(self, CraftCore.compiler.isMSVC(), classA=BinPackage)
