import info
from CraftOS.osutils import OsUtils

class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['develop'] = "git://anongit.kde.org/kube|develop"
        self.defaultTarget = 'develop'
        self.description = "Kube"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["dev-util/pkg-config"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["libs/qt5/qtgraphicaleffects"] = "default"
        self.runtimeDependencies["libs/qt5/qtmultimedia"] = "default"
        self.runtimeDependencies["libs/qt5/qtquickcontrols"] = "default"
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = "default"
        self.runtimeDependencies["libs/qt5/qtsvg"] = "default"
        self.runtimeDependencies["libs/qt5/qtwinextras"] = "default"
        self.runtimeDependencies["libs/qt5/qtwebengine"] = "default"
        self.runtimeDependencies["frameworks/tier1/kcoreaddons"] = "default"
        self.runtimeDependencies["kde/pim/kmime"] = "default"
        self.runtimeDependencies["kde/pim/kcalcore"] = "default"
        self.runtimeDependencies["extragear/sink"] = "default"
        self.runtimeDependencies["extragear/kasync"] = "default"
        if OsUtils.isWin():
            self.runtimeDependencies["win32libs/gpgme"] = "default"
        else:
            self.runtimeDependencies["autotools/gpgme-src"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)

    def createPackage(self):
        self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist.txt'))
        self.defines["productname"] = "Kube"
        self.defines["executable"] = "bin\\kube.exe"
        self.defines["icon"] = os.path.join(self.packageDir(), "kube.ico")
        self.defines["website"] = "kube.kde.org"
        # TODO:  find a way to extend the default script
        self.scriptname = os.path.join(self.packageDir(), "NullsoftInstaller.nsi")

        self.ignoredPackages.append("binary/mysql")
        self.ignoredPackages.append("win32libs/dbus")

        return TypePackager.createPackage(self)
