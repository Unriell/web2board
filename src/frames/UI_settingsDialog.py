# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\SoftwareProjects\web2board\src\frames\UI_settingsDialog.ui'
#
# Created: Sun Mar 13 20:34:08 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(573, 343)
        self.verticalLayout = QtGui.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(SettingsDialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.wsIP = QtGui.QLineEdit(self.groupBox)
        self.wsIP.setObjectName("wsIP")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.wsIP)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.wsPort = QtGui.QSpinBox(self.groupBox)
        self.wsPort.setMaximum(99999)
        self.wsPort.setProperty("value", 9876)
        self.wsPort.setObjectName("wsPort")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.wsPort)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setEnabled(False)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.proxy = QtGui.QLineEdit(self.groupBox)
        self.proxy.setEnabled(False)
        self.proxy.setObjectName("proxy")
        self.horizontalLayout_7.addWidget(self.proxy)
        self.checkProxy = QtGui.QPushButton(self.groupBox)
        self.checkProxy.setEnabled(False)
        self.checkProxy.setObjectName("checkProxy")
        self.horizontalLayout_7.addWidget(self.checkProxy)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_4 = QtGui.QGroupBox(SettingsDialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_4)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.librariesDir = QtGui.QLineEdit(self.groupBox_4)
        self.librariesDir.setObjectName("librariesDir")
        self.horizontalLayout_3.addWidget(self.librariesDir)
        self.searchLibrariesDirButton = QtGui.QPushButton(self.groupBox_4)
        self.searchLibrariesDirButton.setMaximumSize(QtCore.QSize(45, 16777215))
        self.searchLibrariesDirButton.setObjectName("searchLibrariesDirButton")
        self.horizontalLayout_3.addWidget(self.searchLibrariesDirButton)
        self.formLayout_3.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_2 = QtGui.QGroupBox(SettingsDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logLevelDebug = QtGui.QRadioButton(self.groupBox_2)
        self.logLevelDebug.setObjectName("logLevelDebug")
        self.horizontalLayout.addWidget(self.logLevelDebug)
        self.logLevelInfo = QtGui.QRadioButton(self.groupBox_2)
        self.logLevelInfo.setChecked(True)
        self.logLevelInfo.setObjectName("logLevelInfo")
        self.horizontalLayout.addWidget(self.logLevelInfo)
        self.logLevelWarnig = QtGui.QRadioButton(self.groupBox_2)
        self.logLevelWarnig.setObjectName("logLevelWarnig")
        self.horizontalLayout.addWidget(self.logLevelWarnig)
        self.logLevelError = QtGui.QRadioButton(self.groupBox_2)
        self.logLevelError.setObjectName("logLevelError")
        self.horizontalLayout.addWidget(self.logLevelError)
        self.logLevelCritial = QtGui.QRadioButton(self.groupBox_2)
        self.logLevelCritial.setObjectName("logLevelCritial")
        self.horizontalLayout.addWidget(self.logLevelCritial)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(SettingsDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkUpdates = QtGui.QCheckBox(self.groupBox_3)
        self.checkUpdates.setChecked(True)
        self.checkUpdates.setObjectName("checkUpdates")
        self.verticalLayout_2.addWidget(self.checkUpdates)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.ok = QtGui.QPushButton(SettingsDialog)
        self.ok.setObjectName("ok")
        self.horizontalLayout_2.addWidget(self.ok)
        self.cancel = QtGui.QPushButton(SettingsDialog)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SettingsDialog", "Connectivity", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsDialog", "Websocket IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.wsIP.setText(QtGui.QApplication.translate("SettingsDialog", "localhost", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingsDialog", "Websocket Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("SettingsDialog", "Not apply for offline", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SettingsDialog", "Proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy.setToolTip(QtGui.QApplication.translate("SettingsDialog", "Not apply for offline", None, QtGui.QApplication.UnicodeUTF8))
        self.checkProxy.setToolTip(QtGui.QApplication.translate("SettingsDialog", "Not apply for offline", None, QtGui.QApplication.UnicodeUTF8))
        self.checkProxy.setText(QtGui.QApplication.translate("SettingsDialog", "Check", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("SettingsDialog", "Work space", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SettingsDialog", "libraires directory", None, QtGui.QApplication.UnicodeUTF8))
        self.searchLibrariesDirButton.setText(QtGui.QApplication.translate("SettingsDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("SettingsDialog", "Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SettingsDialog", "Level:", None, QtGui.QApplication.UnicodeUTF8))
        self.logLevelDebug.setText(QtGui.QApplication.translate("SettingsDialog", "DEBUG", None, QtGui.QApplication.UnicodeUTF8))
        self.logLevelInfo.setText(QtGui.QApplication.translate("SettingsDialog", "INFO", None, QtGui.QApplication.UnicodeUTF8))
        self.logLevelWarnig.setText(QtGui.QApplication.translate("SettingsDialog", "WARNING", None, QtGui.QApplication.UnicodeUTF8))
        self.logLevelError.setText(QtGui.QApplication.translate("SettingsDialog", "ERROR", None, QtGui.QApplication.UnicodeUTF8))
        self.logLevelCritial.setText(QtGui.QApplication.translate("SettingsDialog", "CRITICAL", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("SettingsDialog", "Update process", None, QtGui.QApplication.UnicodeUTF8))
        self.checkUpdates.setText(QtGui.QApplication.translate("SettingsDialog", "Automatically check for updates", None, QtGui.QApplication.UnicodeUTF8))
        self.ok.setText(QtGui.QApplication.translate("SettingsDialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("SettingsDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
