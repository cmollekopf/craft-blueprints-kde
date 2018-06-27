# -*- coding: utf-8 -*-
import info


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ['0.9.22']:
            self.targets[ver] = 'https://github.com/LMDB/lmdb/archive/LMDB_' + ver + '.tar.gz'
            self.targetInstSrc[ver] = 'lmdb-LMDB_' + ver + '/libraries/liblmdb'
            self.patchToApply[ver] = [('lmdb-LMDB_0.9.16-20151004.diff', 3)]

        self.svnTargets['sparsewin32'] = "https://github.com/cmollekopf/lmdb.git|0.9.22_sparsewin32"
        self.targetInstSrc['sparsewin32'] = 'libraries/liblmdb'

        self.description = 'in memory database from the openldap project'

        if OsUtils.isWin():
            self.defaultTarget = '0.9.22'
        else:
            self.defaultTarget = '0.9.22'

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.args = "-DBUILD_TESTS=OFF -DBUILD_TOOLS=OFF"
