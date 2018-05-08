import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['develop'] = "git://anongit.kde.org/sink|develop"
        self.defaultTarget = 'develop'
        self.description = "Sink"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["frameworks/tier1/kcoreaddons"] = "default"
        self.runtimeDependencies["kde/pim/kmime"] = "default"
        self.runtimeDependencies["extragear/kimap2"] = "default"
        self.runtimeDependencies["extragear/kdav2"] = "default"
        self.runtimeDependencies["extragear/kasync"] = "default"
        self.runtimeDependencies["kde/pim/kcontacts"] = "default"
        self.runtimeDependencies["kde/pim/kcalcore"] = "default"
        self.runtimeDependencies["kdesupport/flatbuffers"] = "default"
        self.runtimeDependencies["win32libs/lmdb"] = "default"
        self.runtimeDependencies["win32libs/xapian-core"] = "default"
        self.runtimeDependencies["win32libs/libcurl"] = "default"
        self.runtimeDependencies["gnuwin32/readline"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
