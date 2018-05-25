import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.addCachedAutotoolsBuild(f"https://files.kde.org/craft/autotools/2018.02/windows/mingw_{CraftCore.compiler.bits}/gcc/Release/", "autotools/gpgme-src")

    def setDependencies(self):
        self.runtimeDependencies['virtual/base'] = 'default'
        self.runtimeDependencies["win32libs/mingw-crt4msvc"] = "default"
        self.runtimeDependencies['win32libs/assuan2'] = 'default'
        self.runtimeDependencies["win32libs/gpg-error"] = "default"
        self.runtimeDependencies["win32libs/pthreads"] = "default"


from Package.BinaryPackageBase import *

class Package(BinaryPackageBase):
    def __init__(self, **args):
        BinaryPackageBase.__init__(self)

    def unpack(self):
        if not BinaryPackageBase.unpack(self): return False
        utils.copyFile(os.path.join(self.imageDir(), "libexec", "gpgme-w32spawn.exe"),
                       os.path.join(self.imageDir(), "bin", "gpgme-w32spawn.exe"))
        shutil.rmtree(os.path.join(self.imageDir(), "libexec"))
        return True
