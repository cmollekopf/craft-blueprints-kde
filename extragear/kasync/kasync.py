import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = "git://anongit.kde.org/kasync"
        self.defaultTarget = 'master'
        self.description = "Library for writing asynchronous code."

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
