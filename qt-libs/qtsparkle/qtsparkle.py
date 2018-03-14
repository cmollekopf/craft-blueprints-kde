# -*- coding: utf-8 -*-
import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setDependencies(self):
        self.runtimeDependencies["libs/qt5"] = "default"

    def setTargets(self):
        self.svnTargets['master'] = 'https://github.com/davidsansome/qtsparkle.git'
        self.defaultTarget = 'master'


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
