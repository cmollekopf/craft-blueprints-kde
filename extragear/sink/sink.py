import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['develop'] = "git://anongit.kde.org/sink|develop"
        self.defaultTarget = 'develop'
        self.description = "Sink"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.buildDependencies["libs/qt5/qtbase"] = "default"
        self.buildDependencies["frameworks/tier1/kcoreaddons"] = "default"
        self.buildDependencies["kde/pim/kmime"] = "default"
        self.buildDependencies["extragear/kimap2"] = "default"
        self.buildDependencies["extragear/kdav2"] = "default"
        self.buildDependencies["extragear/kasync"] = "default"
        self.buildDependencies["kde/pim/kcontacts"] = "default"
        self.buildDependencies["kdesupport/flatbuffers"] = "default"
        self.buildDependencies["win32libs/lmdb"] = "default"
        self.buildDependencies["win32libs/xapian-core"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
