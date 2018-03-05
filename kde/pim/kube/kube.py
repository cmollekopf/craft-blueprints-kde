import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['develop'] = "git://anongit.kde.org/kube|develop"
        self.defaultTarget = 'develop'
        self.description = "Kube"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.buildDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["libs/qt5/qtgraphicaleffects"] = "default"
        self.runtimeDependencies["libs/qt5/qtmultimedia"] = "default"
        self.runtimeDependencies["libs/qt5/qtquickcontrols"] = "default"
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = "default"
        self.runtimeDependencies["libs/qt5/qtsvg"] = "default"
        self.runtimeDependencies["libs/qt5/qtwinextras"] = "default"
        self.runtimeDependencies["libs/qt5/qtwebengine"] = "default"
        self.buildDependencies["frameworks/tier1/kcoreaddons"] = "default"
        self.buildDependencies["kde/pim/kmime"] = "default"
        self.buildDependencies["kde/pim/sink"] = "default"
        self.buildDependencies["kde/pim/kasync"] = "default"
        if CraftCore.compiler.isGCCLike():
            self.runtimeDependencies["autotools/gpgme-src"] = "default"
        else:
            self.runtimeDependencies["win32libs/gpgme"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
