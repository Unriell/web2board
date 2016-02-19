# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_web2board.ui'
#
# Created: Fri Feb 19 12:12:05 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Web2board(object):
    def setupUi(self, Web2board):
        Web2board.setObjectName("Web2board")
        Web2board.resize(1002, 471)
        self.centralwidget = QtGui.QWidget(Web2board)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.forceCloseButton = QtGui.QPushButton(self.centralwidget)
        self.forceCloseButton.setObjectName("forceCloseButton")
        self.horizontalLayout.addWidget(self.forceCloseButton)
        self.settingsButton = QtGui.QPushButton(self.centralwidget)
        self.settingsButton.setText("")
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayout.addWidget(self.settingsButton)
        self.serialMonitorButton = QtGui.QPushButton(self.centralwidget)
        self.serialMonitorButton.setText("")
        self.serialMonitorButton.setObjectName("serialMonitorButton")
        self.horizontalLayout.addWidget(self.serialMonitorButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.clean = QtGui.QPushButton(self.centralwidget)
        self.clean.setText("")
        self.clean.setObjectName("clean")
        self.horizontalLayout.addWidget(self.clean)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ports = QtGui.QComboBox(self.centralwidget)
        self.ports.setMinimumSize(QtCore.QSize(100, 0))
        self.ports.setObjectName("ports")
        self.ports.addItem("")
        self.horizontalLayout.addWidget(self.ports)
        self.searchPorts = QtGui.QPushButton(self.centralwidget)
        self.searchPorts.setObjectName("searchPorts")
        self.horizontalLayout.addWidget(self.searchPorts)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.console = QtGui.QTextEdit(self.centralwidget)
        self.console.setReadOnly(True)
        self.console.setObjectName("console")
        self.verticalLayout_2.addWidget(self.console)
        self.updateGroupbox = QtGui.QGroupBox(self.centralwidget)
        self.updateGroupbox.setObjectName("updateGroupbox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.updateGroupbox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.progressBar = QtGui.QProgressBar(self.updateGroupbox)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.info = QtGui.QLabel(self.updateGroupbox)
        self.info.setObjectName("info")
        self.verticalLayout_3.addWidget(self.info)
        self.verticalLayout_2.addWidget(self.updateGroupbox)
        Web2board.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(Web2board)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1002, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuTest = QtGui.QMenu(self.menuBar)
        self.menuTest.setObjectName("menuTest")
        self.menuPlugins_2 = QtGui.QMenu(self.menuBar)
        self.menuPlugins_2.setObjectName("menuPlugins_2")
        Web2board.setMenuBar(self.menuBar)
        self.actionPlugins = QtGui.QAction(Web2board)
        self.actionPlugins.setObjectName("actionPlugins")
        self.actionSerialMonitor = QtGui.QAction(Web2board)
        self.actionSerialMonitor.setObjectName("actionSerialMonitor")
        self.actionSettings = QtGui.QAction(Web2board)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtGui.QAction(Web2board)
        self.actionAbout.setObjectName("actionAbout")
        self.actionForceClose = QtGui.QAction(Web2board)
        self.actionForceClose.setObjectName("actionForceClose")
        self.menuTest.addAction(self.actionSettings)
        self.menuTest.addSeparator()
        self.menuTest.addAction(self.actionForceClose)
        self.menuPlugins_2.addAction(self.actionSerialMonitor)
        self.menuBar.addAction(self.menuTest.menuAction())
        self.menuBar.addAction(self.menuPlugins_2.menuAction())

        self.retranslateUi(Web2board)
        QtCore.QMetaObject.connectSlotsByName(Web2board)

    def retranslateUi(self, Web2board):
        Web2board.setWindowTitle(QtGui.QApplication.translate("Web2board", "Web2board", None, QtGui.QApplication.UnicodeUTF8))
        self.forceCloseButton.setToolTip(QtGui.QApplication.translate("Web2board", "Totally close web2board", None, QtGui.QApplication.UnicodeUTF8))
        self.forceCloseButton.setText(QtGui.QApplication.translate("Web2board", "Force close", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsButton.setToolTip(QtGui.QApplication.translate("Web2board", "Open settings window", None, QtGui.QApplication.UnicodeUTF8))
        self.serialMonitorButton.setToolTip(QtGui.QApplication.translate("Web2board", "open serial monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.clean.setToolTip(QtGui.QApplication.translate("Web2board", "Clean the console", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Web2board", "ports:", None, QtGui.QApplication.UnicodeUTF8))
        self.ports.setItemText(0, QtGui.QApplication.translate("Web2board", "AUTO", None, QtGui.QApplication.UnicodeUTF8))
        self.searchPorts.setToolTip(QtGui.QApplication.translate("Web2board", "Search usb ports and connected board", None, QtGui.QApplication.UnicodeUTF8))
        self.searchPorts.setText(QtGui.QApplication.translate("Web2board", "Search ports", None, QtGui.QApplication.UnicodeUTF8))
        self.updateGroupbox.setTitle(QtGui.QApplication.translate("Web2board", "Downloading", None, QtGui.QApplication.UnicodeUTF8))
        self.info.setText(QtGui.QApplication.translate("Web2board", "Info:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTest.setTitle(QtGui.QApplication.translate("Web2board", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlugins_2.setTitle(QtGui.QApplication.translate("Web2board", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlugins.setText(QtGui.QApplication.translate("Web2board", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSerialMonitor.setText(QtGui.QApplication.translate("Web2board", "SerialMonitor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSerialMonitor.setToolTip(QtGui.QApplication.translate("Web2board", "Serial monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("Web2board", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("Web2board", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionForceClose.setText(QtGui.QApplication.translate("Web2board", "Force close", None, QtGui.QApplication.UnicodeUTF8))

