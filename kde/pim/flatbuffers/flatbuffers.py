import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = "https://github.com/google/flatbuffers"
        self.defaultTarget = 'master'
        self.description = "flatbuffers"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"

from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
