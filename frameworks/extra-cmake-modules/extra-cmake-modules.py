import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = "https://github.com/cmollekopf/extra-cmake-modules.git"
        self.defaultTarget = 'master'
        self.description = "Extra Cmake Modules"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["dev-util/png2ico"] = "default"
        # needed for many kf5's
        self.buildDependencies["dev-util/winflexbison"] = "default"
        self.buildDependencies["libs/qt5/qttools"] = "default"

        if CraftCore.settings.getboolean("CMake", "KDE_L10N_AUTO_TRANSLATIONS", False):
            self.buildDependencies["dev-util/ruby"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
