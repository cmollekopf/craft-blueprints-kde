import info
from CraftOS.osutils import OsUtils

class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['develop'] = "git://anongit.kde.org/kube|develop"
        self.defaultTarget = 'develop'
        self.description = "Kube"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.buildDependencies["dev-util/pkg-config"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["libs/qt5/qtgraphicaleffects"] = "default"
        self.runtimeDependencies["libs/qt5/qtmultimedia"] = "default"
        self.runtimeDependencies["libs/qt5/qtquickcontrols"] = "default"
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = "default"
        self.runtimeDependencies["libs/qt5/qtsvg"] = "default"
        self.runtimeDependencies["libs/qt5/qtwinextras"] = "default"
        self.runtimeDependencies["libs/qt5/qtwebengine"] = "default"
        self.runtimeDependencies["frameworks/tier1/kcoreaddons"] = "default"
        self.runtimeDependencies["kde/pim/kmime"] = "default"
        self.runtimeDependencies["kde/pim/kcalcore"] = "default"
        self.runtimeDependencies["extragear/sink"] = "default"
        self.runtimeDependencies["extragear/kasync"] = "default"
        if OsUtils.isWin():
            self.runtimeDependencies["win32libs/gpgme"] = "default"
        else:
            self.runtimeDependencies["autotools/gpgme-src"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)

    def preArchive(self):
        # Install the qml files
        targetDir = os.path.join(self.archiveDir(), "Applications/KDE/kube.app/Contents/Resources/qml/")
        utils.createDir(targetDir)
        utils.copyDir(os.path.join(self.imageDir(), "lib", "qml", "org"), os.path.join(targetDir, "org"))
        return True

    def macdeployqt(self, appPath, targetLibdir, env):
        print("Running macdeployqt %s %s" % (appPath, targetLibdir))

        #This is used in the base implementation, but it doesn't look like we need it?
        #if not utils.systemWithoutShell(["dylibbundler", "-of", "-b", "-p", "@executable_path/../Frameworks", "-d", targetLibdir, "-x", f"{appPath}/Contents/MacOS/{self.defines['appname']}"], env=env):
        #    CraftCore.log.warning("Failed to run dylibbundler")

        macdeploycmd = ["macdeployqt",
            appPath,
            "-qmldir=%s/Contents/Resources/qml" % appPath,
            "-verbose=2",
            "-executable=%s/Contents/MacOS/sinksh -executable=%s/Contents/MacOS/sink_synchronizer" % (appPath, appPath),
            "-executable=%s/Contents/PlugIns/sink/resources/libsink_resource_caldav.dylib" % appPath,
            "-executable=%s/Contents/PlugIns/sink/resources/libsink_resource_carddav.dylib" % appPath,
            "-executable=%s/Contents/PlugIns/sink/resources/libsink_resource_imap.dylib" % appPath,
            "-executable=%s/Contents/PlugIns/sink/resources/libsink_resource_maildir.dylib" % appPath,
            "-executable=%s/Contents/PlugIns/sink/resources/libsink_resource_mailtransport.dylib" % appPath,
            "-executable=%s/Contents/PlugIns/sink/resources/libsink_resource_dummy.dylib" % appPath,
            "-executable=%s/Contents/Resources/qml/org/kube/framework/libframeworkplugin.dylib" % appPath,
            "-executable=%s/Contents/Resources/qml/org/kube/accounts/kolabnow/libkolabnowaccountplugin.dylib" % appPath,
            "-executable=%s/Contents/Resources/qml/org/kube/accounts/maildir/libmaildiraccountplugin.dylib" % appPath,
            "-executable=%s/Contents/Resources/qml/org/kube/accounts/imap/libimapaccountplugin.dylib" % appPath,
            "-executable=%s/Contents/Resources/qml/org/kube/accounts/gmail/libgmailaccountplugin.dylib" % appPath,
            "-libpath=%s/Contents/Resources/qml/org/kube/framework/" % appPath,
            ]

        if not utils.systemWithoutShell(macdeploycmd, env=env):
            CraftCore.log.warning("Failed to run macdeployqt!")

        # Fixup libframeworkplugin paths in remaining libs
        for plugin in ["imap", "kolabnow", "maildir", "gmail"]:
            #FIXME I've hardcoded the expected path in the library
            cmd = ["install_name_tool",
                "-change",
                "%s/lib/libframeworkplugin.dylib" % "/Users/kolab/CraftRoot",
                "@loader_path/../../framework/libframeworkplugin.dylib",
                "%s/Contents/Resources/qml/org/kube/accounts/%s/lib%saccountplugin.dylib" % (appPath, plugin, plugin)
                ]
            if not utils.systemWithoutShell(cmd, env=env):
                CraftCore.log.warning("Failed to run dylibbundler!")

        if not utils.systemWithoutShell(["macdeployqt", appPath, "-dmg"], env=env):
            CraftCore.log.warning("Failed to run macdeployqt!")

    def createPackage(self):
        self.defines["productname"] = "Kube"
        self.defines["executable"] = "bin\\kube.exe"
        self.defines["icon"] = os.path.join(self.packageDir(), "kube.ico")
        self.defines["website"] = "kube.kde.org"

        if OsUtils.isWin():
            self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist.txt'))
            self.scriptname = os.path.join(self.packageDir(), "NullsoftInstaller.nsi")
            self.ignoredPackages.append("binary/mysql")
            self.ignoredPackages.append("win32libs/dbus")
        if OsUtils.isMac():
            self.defines["apppath"] = "Applications/KDE"

        return TypePackager.createPackage(self)
