import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.targets["2.2.7_2018050"] = "https://www.gnupg.org/ftp/gcrypt/binary/gnupg-w32-2.2.7_20180502.exe"
        self.defaultTarget = "2.2.7_2018050"

    def setDependencies(self):
        self.runtimeDependencies['virtual/base'] = 'default'


from Package.BinaryPackageBase import *

class Package(BinaryPackageBase):
    def __init__(self, **args):
        BinaryPackageBase.__init__(self)
        #Disable windows UAC to avoid the dialog when running the installer
        self.subinfo.options.unpack.runInstaller = True
        self.subinfo.options.configure.args = "/S /D={0}".format(self.workDir())
