import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets["master"] = "https://github.com/uclouvain/openjpeg.git"

        for ver in ["2.1.2", "2.3.0"]:
            self.targets[ver] = f"https://github.com/uclouvain/openjpeg/archive/v{ver}.tar.gz"
            self.archiveNames[ver] = f"openjpeg-{ver}.tar.gz"
            self.targetInstSrc[ver] = f"openjpeg-{ver}"
        self.targetDigests['2.1.2'] = (['4ce77b6ef538ef090d9bde1d5eeff8b3069ab56c4906f083475517c2c023dfa7'], CraftHash.HashAlgorithm.SHA256)
        self.targetDigests['2.3.0'] = (['3dc787c1bb6023ba846c2a0d9b1f6e179f1cd255172bde9eb75b01f1e6c7d71a'], CraftHash.HashAlgorithm.SHA256)

        self.description = "OpenJPEG is an open-source JPEG 2000 codec written in C language."
        self.webpage = "http://www.openjpeg.org/"
        self.defaultTarget = "2.3.0"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["win32libs/tiff"] = "default"
        self.runtimeDependencies["win32libs/libpng"] = "default"
        self.runtimeDependencies["win32libs/lcms2"] = "default"
        self.runtimeDependencies["win32libs/zlib"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
