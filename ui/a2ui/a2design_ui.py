# -*- coding: utf-8 -*-

"""
Form generated from reading UI file 'a2design.ui'

Created by: Qt User Interface Compiler version 6.2.3

WARNING! All changes made in this file will be lost when recompiling UI file!
"""

from a2qt.QtGui import QAction, QFont
from a2qt.QtWidgets import QMenu, QMenuBar, QSplitter, QVBoxLayout, QWidget
from a2qt.QtCore import QCoreApplication, QMetaObject, QRect, QSize

from a2widget.a2module_list import A2ModuleList
from a2widget.a2module_view import A2ModuleView

class Ui_a2MainWindow:
    def setupUi(self, a2MainWindow):
        if not a2MainWindow.objectName():
            a2MainWindow.setObjectName(u"a2MainWindow")
        font = QFont()
        font.setPointSize(10)
        a2MainWindow.setFont(font)
        a2MainWindow.setWindowTitle(u"a2")
        self.actionAbout_a2 = QAction(a2MainWindow)
        self.actionAbout_a2.setObjectName(u"actionAbout_a2")
        self.actionAbout_a2.setText(u"About a2")
        self.actionEdit_module = QAction(a2MainWindow)
        self.actionEdit_module.setObjectName(u"actionEdit_module")
        self.actionEdit_module.setText(u"Edit Module")
        self.actionEdit_module.setShortcut(u"Ctrl+E")
        self.actionDisable_all_modules = QAction(a2MainWindow)
        self.actionDisable_all_modules.setObjectName(u"actionDisable_all_modules")
        self.actionDisable_all_modules.setText(u"Disable All Modules")
        self.actionExplore_to = QAction(a2MainWindow)
        self.actionExplore_to.setObjectName(u"actionExplore_to")
        self.actionExplore_to.setText(u"Explore to Module ...")
        self.actionExplore_to.setShortcut(u"Alt+E")
        self.actionAbout_Autohotkey = QAction(a2MainWindow)
        self.actionAbout_Autohotkey.setObjectName(u"actionAbout_Autohotkey")
        self.actionAbout_Autohotkey.setText(u"About Autohotkey")
        self.actionExplore_to_a2_dir = QAction(a2MainWindow)
        self.actionExplore_to_a2_dir.setObjectName(u"actionExplore_to_a2_dir")
        self.actionExplore_to_a2_dir.setText(u"Explore to a2 ...")
        self.actionA2_settings = QAction(a2MainWindow)
        self.actionA2_settings.setObjectName(u"actionA2_settings")
        self.actionA2_settings.setText(u"a2 Settings")
        self.actionExit_a2ui = QAction(a2MainWindow)
        self.actionExit_a2ui.setObjectName(u"actionExit_a2ui")
        self.actionExit_a2ui.setText(u"Exit a2UI")
        self.actionRefresh_UI = QAction(a2MainWindow)
        self.actionRefresh_UI.setObjectName(u"actionRefresh_UI")
        self.actionRefresh_UI.setText(u"Refresh UI")
        self.actionRefresh_UI.setShortcut(u"F5")
        self.action_report_bug = QAction(a2MainWindow)
        self.action_report_bug.setObjectName(u"action_report_bug")
        self.action_report_bug.setText(u"Report a bug")
        self.actionNew_Module_Dialog = QAction(a2MainWindow)
        self.actionNew_Module_Dialog.setObjectName(u"actionNew_Module_Dialog")
        self.actionNew_Module_Dialog.setText(u"Create New Module")
        self.actionNew_Module_Dialog.setShortcut(u"Ctrl+N")
        self.actionBuild_A2_Package = QAction(a2MainWindow)
        self.actionBuild_A2_Package.setObjectName(u"actionBuild_A2_Package")
        self.actionBuild_A2_Package.setText(u"Build A2 Package")
        self.actionBuild_A2_Package.setShortcut(u"")
        self.actionCreate_New_Element = QAction(a2MainWindow)
        self.actionCreate_New_Element.setObjectName(u"actionCreate_New_Element")
        self.actionCreate_New_Element.setText(u"Create New Element")
        self.actionCreate_New_Element.setShortcut(u"")
        self.actionHelp_on_Module = QAction(a2MainWindow)
        self.actionHelp_on_Module.setObjectName(u"actionHelp_on_Module")
        self.actionHelp_on_Module.setText(u"Help on Module")
        self.actionHelp_on_Module.setShortcut(u"")
        self.actionRevert_Settings = QAction(a2MainWindow)
        self.actionRevert_Settings.setObjectName(u"actionRevert_Settings")
        self.actionRevert_Settings.setText(u"Revert Settings")
        self.actionRevert_Settings.setShortcut(u"")
        self.actionReload_a2_Runtime = QAction(a2MainWindow)
        self.actionReload_a2_Runtime.setObjectName(u"actionReload_a2_Runtime")
        self.actionReload_a2_Runtime.setText(u"Reload a2 Runtime")
        self.actionReload_a2_Runtime.setShortcut(u"")
        self.actionUnload_a2_Runtime = QAction(a2MainWindow)
        self.actionUnload_a2_Runtime.setObjectName(u"actionUnload_a2_Runtime")
        self.actionUnload_a2_Runtime.setText(u"Unload a2 Runtime")
        self.actionLoad_a2_Runtime = QAction(a2MainWindow)
        self.actionLoad_a2_Runtime.setObjectName(u"actionLoad_a2_Runtime")
        self.actionLoad_a2_Runtime.setText(u"Load a2 Runtime")
        self.actionExplore_to_a2_data_dir = QAction(a2MainWindow)
        self.actionExplore_to_a2_data_dir.setObjectName(u"actionExplore_to_a2_data_dir")
        self.actionExplore_to_a2_data_dir.setText(u"Explore to a2 data ...")
        self.actionExplore_to_a2_data_dir.setShortcut(u"")
        self.actionUninstall_a2 = QAction(a2MainWindow)
        self.actionUninstall_a2.setObjectName(u"actionUninstall_a2")
        self.actionUninstall_a2.setText(u"Uninstall a2")
        self.action_report_sugg = QAction(a2MainWindow)
        self.action_report_sugg.setObjectName(u"action_report_sugg")
        self.action_report_sugg.setText(u"Suggest a feature")
        self.actionExport_Settings = QAction(a2MainWindow)
        self.actionExport_Settings.setObjectName(u"actionExport_Settings")
        self.actionExport_Settings.setText(u"Export Settings")
        self.actionImport_Settings = QAction(a2MainWindow)
        self.actionImport_Settings.setObjectName(u"actionImport_Settings")
        self.actionImport_Settings.setText(u"Import Settings")
        self.actionChat_on_Gitter = QAction(a2MainWindow)
        self.actionChat_on_Gitter.setObjectName(u"actionChat_on_Gitter")
        self.actionChat_on_Telegram = QAction(a2MainWindow)
        self.actionChat_on_Telegram.setObjectName(u"actionChat_on_Telegram")
        self.actionSet_a2_Version = QAction(a2MainWindow)
        self.actionSet_a2_Version.setObjectName(u"actionSet_a2_Version")
        self.centralwidget = QWidget(a2MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setChildrenCollapsible(False)
        self.module_list = A2ModuleList(self.splitter)
        self.module_list.setObjectName(u"module_list")
        self.module_list.setMinimumSize(QSize(150, 0))
        self.module_list.setMaximumSize(QSize(500, 16777215))
        self.splitter.addWidget(self.module_list)
        self.module_view = A2ModuleView(self.splitter)
        self.module_view.setObjectName(u"module_view")
        self.module_view.setMinimumSize(QSize(500, 0))
        self.splitter.addWidget(self.module_view)
        self.verticalLayout.addWidget(self.splitter)
        a2MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(a2MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 753, 24))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setTitle(u"&Help")
        self.menuDev = QMenu(self.menubar)
        self.menuDev.setObjectName(u"menuDev")
        self.menuDev.setTitle(u"&Dev")
        self.menuRollback_Changes = QMenu(self.menuDev)
        self.menuRollback_Changes.setObjectName(u"menuRollback_Changes")
        self.menuRollback_Changes.setTitle(u"Rollback Changes")
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName(u"menuMain")
        self.menuMain.setTitle(u"&Main")
        self.menuModule = QMenu(self.menubar)
        self.menuModule.setObjectName(u"menuModule")
        self.menuModule.setTitle(u"Module")
        a2MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuModule.menuAction())
        self.menubar.addAction(self.menuDev.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.action_report_bug)
        self.menuHelp.addAction(self.action_report_sugg)
        self.menuHelp.addAction(self.actionChat_on_Gitter)
        self.menuHelp.addAction(self.actionChat_on_Telegram)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_a2)
        self.menuHelp.addAction(self.actionAbout_Autohotkey)
        self.menuDev.addAction(self.actionNew_Module_Dialog)
        self.menuDev.addAction(self.actionEdit_module)
        self.menuDev.addAction(self.actionExplore_to)
        self.menuDev.addAction(self.menuRollback_Changes.menuAction())
        self.menuDev.addSeparator()
        self.menuDev.addAction(self.actionDisable_all_modules)
        self.menuDev.addAction(self.actionExplore_to_a2_dir)
        self.menuDev.addAction(self.actionExplore_to_a2_data_dir)
        self.menuDev.addSeparator()
        self.menuDev.addAction(self.actionCreate_New_Element)
        self.menuDev.addAction(self.actionBuild_A2_Package)
        self.menuDev.addAction(self.actionSet_a2_Version)
        self.menuMain.addAction(self.actionA2_settings)
        self.menuMain.addAction(self.actionRefresh_UI)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionReload_a2_Runtime)
        self.menuMain.addAction(self.actionLoad_a2_Runtime)
        self.menuMain.addAction(self.actionUnload_a2_Runtime)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionUninstall_a2)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionExit_a2ui)
        self.menuModule.addSeparator()
        self.menuModule.addAction(self.actionHelp_on_Module)
        self.menuModule.addAction(self.actionRevert_Settings)
        self.menuModule.addAction(self.actionExport_Settings)
        self.menuModule.addAction(self.actionImport_Settings)
        self.retranslateUi(a2MainWindow)
        QMetaObject.connectSlotsByName(a2MainWindow)
    def retranslateUi(self, a2MainWindow):
        self.actionChat_on_Gitter.setText(QCoreApplication.translate("a2MainWindow", u"Chat on Gitter", None))
        self.actionChat_on_Telegram.setText(QCoreApplication.translate("a2MainWindow", u"Chat on Telegram", None))
        self.actionSet_a2_Version.setText(QCoreApplication.translate("a2MainWindow", u"Set a2 Version", None))
        pass
