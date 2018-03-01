import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = "git://anongit.kde.org/kimap2"
        self.defaultTarget = 'master'
        self.description = "Imap library"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.buildDependencies["libs/qt5/qtbase"] = "default"
        self.buildDependencies["frameworks/tier1/kcoreaddons"] = "default"
        self.buildDependencies["kde/pim/kmime"] = "default"
        self.buildDependencies["win32libs/cyrus-sasl"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
