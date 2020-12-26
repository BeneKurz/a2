# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scope_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from a2qt.QtCore import *
from a2qt.QtGui import *
from a2qt.QtWidgets import *

from a2widget.a2button_field import A2ButtonField
from a2widget.a2list import A2ListCompact


class Ui_ScopeWidget(object):
    def setupUi(self, ScopeWidget):
        if not ScopeWidget.objectName():
            ScopeWidget.setObjectName(u"ScopeWidget")
        ScopeWidget.resize(500, 146)
        ScopeWidget.setWindowTitle(u"Form")
#if QT_CONFIG(tooltip)
        ScopeWidget.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.verticalLayout = QVBoxLayout(ScopeWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.type_radio_widget = QWidget(ScopeWidget)
        self.type_radio_widget.setObjectName(u"type_radio_widget")
        self.horizontalLayout = QHBoxLayout(self.type_radio_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scopeMode_0 = QRadioButton(self.type_radio_widget)
        self.scopeMode_0.setObjectName(u"scopeMode_0")
        self.scopeMode_0.setChecked(True)

        self.horizontalLayout.addWidget(self.scopeMode_0)

        self.scopeMode_1 = QRadioButton(self.type_radio_widget)
        self.scopeMode_1.setObjectName(u"scopeMode_1")
        self.scopeMode_1.setChecked(False)

        self.horizontalLayout.addWidget(self.scopeMode_1)

        self.scopeMode_2 = QRadioButton(self.type_radio_widget)
        self.scopeMode_2.setObjectName(u"scopeMode_2")
        self.scopeMode_2.setChecked(False)

        self.horizontalLayout.addWidget(self.scopeMode_2)


        self.horizontalLayout_2.addWidget(self.type_radio_widget, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.scope_help = QToolButton(ScopeWidget)
        self.scope_help.setObjectName(u"scope_help")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scope_help.sizePolicy().hasHeightForWidth())
        self.scope_help.setSizePolicy(sizePolicy)
        self.scope_help.setMaximumSize(QSize(50, 35))
#if QT_CONFIG(tooltip)
        self.scope_help.setToolTip(u"Help on Scopes")
#endif // QT_CONFIG(tooltip)
        self.scope_help.setText(u"h")
        self.scope_help.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.scope_help)

        self.tool_buttons_widget = QWidget(ScopeWidget)
        self.tool_buttons_widget.setObjectName(u"tool_buttons_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.tool_buttons_widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scope_pick = QToolButton(self.tool_buttons_widget)
        self.scope_pick.setObjectName(u"scope_pick")
        sizePolicy.setHeightForWidth(self.scope_pick.sizePolicy().hasHeightForWidth())
        self.scope_pick.setSizePolicy(sizePolicy)
        self.scope_pick.setMaximumSize(QSize(50, 35))
#if QT_CONFIG(tooltip)
        self.scope_pick.setToolTip(u"Pick from a Window")
#endif // QT_CONFIG(tooltip)
        self.scope_pick.setText(u"p")
        self.scope_pick.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.scope_pick)

        self.scope_delete = QToolButton(self.tool_buttons_widget)
        self.scope_delete.setObjectName(u"scope_delete")
        sizePolicy.setHeightForWidth(self.scope_delete.sizePolicy().hasHeightForWidth())
        self.scope_delete.setSizePolicy(sizePolicy)
        self.scope_delete.setMaximumSize(QSize(50, 35))
#if QT_CONFIG(tooltip)
        self.scope_delete.setToolTip(u"Delete Selected Scope")
#endif // QT_CONFIG(tooltip)
        self.scope_delete.setText(u"-")
        self.scope_delete.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.scope_delete)

        self.scope_add = QToolButton(self.tool_buttons_widget)
        self.scope_add.setObjectName(u"scope_add")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scope_add.sizePolicy().hasHeightForWidth())
        self.scope_add.setSizePolicy(sizePolicy1)
        self.scope_add.setMaximumSize(QSize(50, 35))
#if QT_CONFIG(tooltip)
        self.scope_add.setToolTip(u"Add a Scope")
#endif // QT_CONFIG(tooltip)
        self.scope_add.setText(u"+")
        self.scope_add.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.scope_add)


        self.horizontalLayout_2.addWidget(self.tool_buttons_widget, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.cfg_scope = A2ListCompact(ScopeWidget)
        self.cfg_scope.setObjectName(u"cfg_scope")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cfg_scope.sizePolicy().hasHeightForWidth())
        self.cfg_scope.setSizePolicy(sizePolicy2)
        self.cfg_scope.setMinimumSize(QSize(500, 40))
        self.cfg_scope.setMaximumSize(QSize(16777215, 16777215))
#if QT_CONFIG(tooltip)
        self.cfg_scope.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.cfg_scope.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.cfg_scope)

        self.fields_widget = QWidget(ScopeWidget)
        self.fields_widget.setObjectName(u"fields_widget")
        self.formLayout_2 = QFormLayout(self.fields_widget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.fields_widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.scope_title = A2ButtonField(self.fields_widget)
        self.scope_title.setObjectName(u"scope_title")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.scope_title)

        self.label_3 = QLabel(self.fields_widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.scope_class = A2ButtonField(self.fields_widget)
        self.scope_class.setObjectName(u"scope_class")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.scope_class)

        self.label_4 = QLabel(self.fields_widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.scope_exe = A2ButtonField(self.fields_widget)
        self.scope_exe.setObjectName(u"scope_exe")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.scope_exe)


        self.verticalLayout.addWidget(self.fields_widget)


        self.retranslateUi(ScopeWidget)

        QMetaObject.connectSlotsByName(ScopeWidget)
    # setupUi

    def retranslateUi(self, ScopeWidget):
#if QT_CONFIG(tooltip)
        self.scopeMode_0.setToolTip(QCoreApplication.translate("ScopeWidget", u"global - Makes it work anywhere in the system.", None))
#endif // QT_CONFIG(tooltip)
        self.scopeMode_0.setText(QCoreApplication.translate("ScopeWidget", u"golbal", None))
#if QT_CONFIG(tooltip)
        self.scopeMode_1.setToolTip(QCoreApplication.translate("ScopeWidget", u"include - To make it work ONLY in certain windows.", None))
#endif // QT_CONFIG(tooltip)
        self.scopeMode_1.setText(QCoreApplication.translate("ScopeWidget", u"include:", None))
#if QT_CONFIG(tooltip)
        self.scopeMode_2.setToolTip(QCoreApplication.translate("ScopeWidget", u"exclude - To make it work anywhere BUT not in given windows.", None))
#endif // QT_CONFIG(tooltip)
        self.scopeMode_2.setText(QCoreApplication.translate("ScopeWidget", u"exclude:", None))
        self.label_2.setText(QCoreApplication.translate("ScopeWidget", u"title", None))
        self.label_3.setText(QCoreApplication.translate("ScopeWidget", u"window class", None))
        self.label_4.setText(QCoreApplication.translate("ScopeWidget", u"executable", None))
        pass
    # retranslateUi

