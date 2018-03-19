import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = "git://anongit.kde.org/kdav2"
        self.defaultTarget = 'master'
        self.description = "KDav2 library"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["frameworks/tier1/kcoreaddons"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
