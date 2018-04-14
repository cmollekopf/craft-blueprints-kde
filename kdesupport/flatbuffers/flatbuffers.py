import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = "https://github.com/google/flatbuffers.git"
        self.defaultTarget = 'master'
        self.description = "flatbuffers"
        self.patchToApply["master"] = ("flatbuffers-20180414.patch", 1) #Install flatc for RelWithDebInfo builds

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"

from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
