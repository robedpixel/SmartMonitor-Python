# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notewindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(40, 90, 741, 391))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 739, 389))
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 741, 391))
        self.noteLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.noteLayout.setObjectName(u"noteLayout")
        self.noteLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.addNoteButton = QPushButton(self.centralwidget)
        self.addNoteButton.setObjectName(u"addNoteButton")
        self.addNoteButton.setGeometry(QRect(590, 40, 71, 41))
        self.removeNoteButton = QPushButton(self.centralwidget)
        self.removeNoteButton.setObjectName(u"removeNoteButton")
        self.removeNoteButton.setGeometry(QRect(700, 40, 71, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addNoteButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeNoteButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
    # retranslateUi

