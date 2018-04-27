import shutil

import info
from Package.BinaryPackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        for version in ['1.10.0']:
            self.targets[version] = "http://www.foobar.org/gpgme-1.10.0.7z"
        # self.targetDigests['1.10.0'] = '34df759e1ffe4acce301887007cccb62f9496ea0'

        self.description = "gpgme"
        self.defaultTarget = '1.10.0'

    def setDependencies(self):
        self.runtimeDependencies["virtual/bin-base"] = "default"


class PackageBin(BinaryPackageBase):
    def __init__(self):
        BinaryPackageBase.__init__(self)
        self.subinfo.options.package.withCompiler = False
        self.subinfo.options.package.withSources = False

    def unpack(self):
        if not BinaryPackageBase.unpack(self): return False
        installpath=os.path.join(self.imageDir(), "gpgme-1.10.0")
        os.renames(os.path.join(installpath, "include"), os.path.join(self.imageDir(), "include"))
        os.renames(os.path.join(installpath, "bin"), os.path.join(self.imageDir(), "bin"))
        os.renames(os.path.join(installpath, "lib"), os.path.join(self.imageDir(), "lib"))
        os.renames(os.path.join(installpath, "libexec"), os.path.join(self.imageDir(), "libexec"))
        shutil.rmtree(installpath)
        return True


from Package.VirtualPackageBase import *

if CraftCore.compiler.isMSVC():
    class Package(PackageBin):
        def __init__(self):
            PackageBin.__init__(self)
else:
    class Package(VirtualPackageBase):
        def __init__(self):
            VirtualPackageBase.__init__(self)
