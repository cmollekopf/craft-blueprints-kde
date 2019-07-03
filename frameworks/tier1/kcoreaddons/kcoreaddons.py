import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()
        self.description = "KCoreAddons"
        self.patchToApply["5.51.0"] = [("kcoreaddons-5.51.0.diff", 1)]

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        #Qt will fall back to it's own internal copy of shared-mime-info http://doc.qt.io/qt-5/qmimedatabase.html
        #self.runtimeDependencies["win32libs/shared-mime-info"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
