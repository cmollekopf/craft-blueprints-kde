import info

#from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def setTargets(self):
        self.targets['1.4.5'] = 'http://oligarchy.co.uk/xapian/1.4.5/xapian-core-1.4.5.tar.xz'
        self.targetDigests['1.4.5'] = '56eca1467328794a406133c5f178b30f63bb992f'
        self.targetInstSrc['1.4.5'] = 'xapian-core-1.4.5'
        self.description = "Open Source Search Engine library"
        #self.patchToApply['1.4.5'] = [("xapian-core-1.2.24-20170626.diff", 1)]
        self.patchToApply['1.4.5'] = [("xapian-core-1.4.5-20180320.diff", 1)]
        self.defaultTarget = '1.4.5'

    def setDependencies(self):
        self.runtimeDependencies["win32libs/libxslt"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"


#class Package(CMakePackageBase):
#    def __init__(self, **args):
#        CMakePackageBase.__init__(self)

from Package.AutoToolsPackageBase import *

class Package(AutoToolsPackageBase):
    def __init__(self, **args):
        AutoToolsPackageBase.__init__(self)
        #self.subinfo.options.configure.args += " --disable-static --enable-shared "
        #print("INSTALL ARGS: " + self.subinfo.options.install.args)
        #self.subinfo.options.install.args += " install "

    def install(self):
        #print("INSTALL ARGS during install: " + self.subinfo.options.install.args)
        if not AutoToolsPackageBase.install(self):
            return False
        return self.copyToMsvcImportLib()
