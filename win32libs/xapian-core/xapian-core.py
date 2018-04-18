import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.targets['1.4.5'] = 'http://oligarchy.co.uk/xapian/1.4.5/xapian-core-1.4.5.tar.xz'
        self.targetInstSrc['1.4.5'] = 'xapian-core-1.4.5'
        self.description = "Open Source Search Engine library"
        self.patchToApply['1.4.5'] = [("xapian-core-1.4.5-20180320.diff", 1)]
        self.defaultTarget = '1.4.5'

    def setDependencies(self):
        self.runtimeDependencies["win32libs/libxslt"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"
        if OsDetection.isWin():
            self.runtimeDependencies["win32libs/zlib"] = "default"
            self.buildDependencies["dev-util/msys"] = "default"


from Package.AutoToolsPackageBase import *

class Package(AutoToolsPackageBase):
    def __init__(self, **args):
        AutoToolsPackageBase.__init__(self)
        if OsDetection.isWin():
            self.subinfo.options.configure.args += " LD='lld-link.exe' OBJDUMP='llvm-objdump.exe' LIBS='C:\\Users\\User\\CraftRoot\\lib\\zlib.lib' --disable-backend-remote"
        #We typically run into LNK1160 (commandline args too long because the .exp files in .libs/ are too large.
        #By supplying -fuse-ld=ldd-link.exe we can use another linker which doesn't run into that problem, but then we end up with error: entry point must be defined.
        # Fuck. This. Shit.

    def install(self):
        #print("INSTALL ARGS during install: " + self.subinfo.options.install.args)
        if not AutoToolsPackageBase.install(self):
            return False
        return self.copyToMsvcImportLib()
