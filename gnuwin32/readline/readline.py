import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.targets['5.0.1'] = "http://downloads.sourceforge.net/sourceforge/gnuwin32/readline-5.0-1-lib.zip"
        #self.targetDigests['5.0.1'] = 'ff74599cbdf8e970b7f3246da8b4b73909867c66'
        self.defaultTarget = '5.0.1'


from Package.BinaryPackageBase import *


class Package(BinaryPackageBase):
    def __init__(self):
        BinaryPackageBase.__init__(self)
