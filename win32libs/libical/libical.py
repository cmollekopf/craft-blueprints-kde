import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['3.0'] = "https://github.com/cmollekopf/libical.git|3.0"
        self.defaultTarget = '3.0'

        self.description = "Reference implementation of the icalendar data type and serialization format"
        self.webpage = "http://libical.github.io/libical/"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["dev-util/winflexbison"] = "default"
        self.buildDependencies["win32libs/pthreads"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["win32libs/icu"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.args = f" -DUSE_BUILTIN_TZDATA=ON -DICAL_UNIX_NEWLINE=OFF -DICAL_GLIB=OFF -DSHARED_ONLY=ON -DICU_BASE={CraftCore.standardDirs.craftRoot()}"
