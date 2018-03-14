# -*- coding: utf-8 -*-
import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.description = "The Qwt library contains GUI Components and utility classes which are primarily useful for programs with a technical background"
        for ver in ["6.0.1", "6.0.2"]:
            self.targets[ver] = "http://downloads.sourceforge.net/sourceforge/qwt/qwt-%s.tar.bz2" % ver
            self.targetInstSrc[ver] = "qwt-%s" % ver
            self.patchToApply[ver] = [('qwt-6.0.1-20110807.diff', 1)]
        self.patchToApply["6.0.1"] = [('qwt-6.0.1-x64-fix.diff', 1)]
        self.targetDigests['6.0.1'] = '301cca0c49c7efc14363b42e082b09056178973e'
        self.targetDigests['6.0.2'] = 'cbdd00b29521987c9e7bc6aa51092f0474b9428d'
        self.defaultTarget = "6.0.2"

    def setDependencies(self):
        self.runtimeDependencies["libs/qt5"] = "default"


from Package.QMakePackageBase import *


class Package(QMakePackageBase):
    def __init__(self, **args):
        QMakePackageBase.__init__(self)
        self.subinfo.options.configure.args = ' "QWT_INSTALL_PREFIX = %s" ' % self.imageDir().replace("\\", "/")
        if CraftCore.compiler.isMinGW():
            self.subinfo.options.make.supportsMultijob = False

    def install(self):
        if not QMakePackageBase.install(self):
            return False
        # sic.: the .lib file is placed under bin dir in hupnp)
        os.mkdir(os.path.join(self.installDir(), "bin"))
        # copy over dlls as required by KDE convention
        for file in os.listdir(os.path.join(self.installDir(), "lib")):
            if file.endswith(".dll"):
                utils.copyFile(os.path.join(self.installDir(), "lib", file),
                               os.path.join(self.installDir(), "bin", file))
        return True
