import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['1.4.5'] = "https://github.com/cmollekopf/xapian-core.git|master"
        self.defaultTarget = '1.4.5'
        self.description = "Open Source Search Engine library"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["win32libs/zlib"] = "default"


from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
