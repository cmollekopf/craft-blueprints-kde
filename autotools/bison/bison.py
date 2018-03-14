# -*- coding: utf-8 -*-
import info
from Package.AutoToolsPackageBase import *


class subinfo(info.infoclass):
    def setDependencies(self):
        self.buildDependencies["dev-util/msys"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"

    def setTargets(self):
        self.description = "Bison is a general-purpose parser generator that converts an annotated context-free grammar into a deterministic LR or generalized LR (GLR) parser employing LALR(1) parser tables"
        self.svnTargets['master'] = 'git://git.savannah.gnu.org/bison.git'
        for ver in ["3.0.4"]:
            self.targets[ver] = f"http://ftp.gnu.org/gnu/bison/bison-{ver}.tar.xz"
            self.targetInstSrc[ver] = f"bison-{ver}"
        self.defaultTarget = '3.0.4'
        self.patchToApply["3.0.4"] = [("vasnprintf-macos.diff", 1)]


class Package(AutoToolsPackageBase):
    def __init__(self, **args):
        AutoToolsPackageBase.__init__(self)
        self.subinfo.options.configure.args += " --disable-static --enable-shared"

    def install(self):
        if not AutoToolsPackageBase.install(self):
            return False
        return self.copyToMsvcImportLib()
