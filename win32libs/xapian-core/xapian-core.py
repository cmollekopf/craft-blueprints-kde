import info

#from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def setTargets(self):
        self.targets['1.2.25'] = 'http://oligarchy.co.uk/xapian/1.2.25/xapian-core-1.2.25.tar.xz'
        self.targetDigests['1.2.25'] = '4c305585c3f1d9f595eec875549406b4650fd29d'
        self.targetInstSrc['1.2.25'] = 'xapian-core-1.2.25'
        self.description = "Open Source Search Engine library"
        #self.patchToApply['1.2.25'] = [("xapian-core-1.2.24-20170626.diff", 1)]
        self.defaultTarget = '1.2.25'

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
