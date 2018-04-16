import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.targets['1.4'] = 'https://github.com/xapian/xapian/archive/RELEASE/1.4.tar.gz'
        self.targetInstSrc['1.4'] = 'xapian-core-1.4'
        #self.svnTargets['1.4'] = 'https://github.com/xapian/xapian.git|RELEASE/1.4'
        self.description = "Open Source Search Engine library"
        self.patchToApply['1.4'] = [("xapian-core-1.4.5-20180320.diff", 1)]
        self.defaultTarget = '1.4'

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
            self.subinfo.options.configure.args += " LD='ld' LIBS='C:\\Users\\User\\CraftRoot\\lib\\zlib.lib' --disable-backend-remote"
        #print("INSTALL ARGS: " + self.subinfo.options.install.args)
        #self.subinfo.options.install.args += " install "

    def install(self):
        #print("INSTALL ARGS during install: " + self.subinfo.options.install.args)
        if not AutoToolsPackageBase.install(self):
            return False
        return self.copyToMsvcImportLib()
