# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 50, 160, 491))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.brushButton = QPushButton(self.verticalLayoutWidget)
        self.brushButton.setObjectName(u"brushButton")
        self.brushButton.setEnabled(False)
        self.brushButton.setCheckable(True)

        self.verticalLayout.addWidget(self.brushButton)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(160, 50, 631, 491))
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 639, 499))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.fileopenButton = QPushButton(self.centralwidget)
        self.fileopenButton.setObjectName(u"fileopenButton")
        self.fileopenButton.setGeometry(QRect(700, 0, 81, 51))
        self.fileopenButton.setTabletTracking(False)
        self.zoomButton = QPushButton(self.centralwidget)
        self.zoomButton.setObjectName(u"zoomButton")
        self.zoomButton.setEnabled(False)
        self.zoomButton.setGeometry(QRect(90, 0, 71, 51))
        self.zoomButton.setCheckable(True)
        self.moveButton = QPushButton(self.centralwidget)
        self.moveButton.setObjectName(u"moveButton")
        self.moveButton.setEnabled(False)
        self.moveButton.setGeometry(QRect(0, 0, 71, 51))
        self.moveButton.setCheckable(True)
        self.brushcolorlabel = QLabel(self.centralwidget)
        self.brushcolorlabel.setObjectName(u"brushcolorlabel")
        self.brushcolorlabel.setGeometry(QRect(380, 0, 41, 20))
        self.brushcolorlabel.setAlignment(Qt.AlignCenter)
        self.brushcolorButton = QPushButton(self.centralwidget)
        self.brushcolorButton.setObjectName(u"brushcolorButton")
        self.brushcolorButton.setGeometry(QRect(430, 0, 51, 51))
        self.noteButton = QPushButton(self.centralwidget)
        self.noteButton.setObjectName(u"noteButton")
        self.noteButton.setGeometry(QRect(500, 0, 81, 51))
        self.filesaveButton = QPushButton(self.centralwidget)
        self.filesaveButton.setObjectName(u"filesaveButton")
        self.filesaveButton.setEnabled(False)
        self.filesaveButton.setGeometry(QRect(600, 0, 81, 51))
        self.resetZoomButton = QPushButton(self.centralwidget)
        self.resetZoomButton.setObjectName(u"resetZoomButton")
        self.resetZoomButton.setEnabled(True)
        self.resetZoomButton.setGeometry(QRect(180, 0, 71, 51))
        self.brushSizeButton = QPushButton(self.centralwidget)
        self.brushSizeButton.setObjectName(u"brushSizeButton")
        self.brushSizeButton.setGeometry(QRect(320, 0, 51, 51))
        self.brushsizelabel = QLabel(self.centralwidget)
        self.brushsizelabel.setObjectName(u"brushsizelabel")
        self.brushsizelabel.setGeometry(QRect(280, 0, 31, 31))
        self.brushsizelabel.setWordWrap(True)
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
        self.brushButton.setText(QCoreApplication.translate("MainWindow", u"Brush", None))
        self.fileopenButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.zoomButton.setText(QCoreApplication.translate("MainWindow", u"Zoom", None))
        self.moveButton.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.brushcolorlabel.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.brushcolorButton.setText("")
        self.noteButton.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.filesaveButton.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.resetZoomButton.setText(QCoreApplication.translate("MainWindow", u"Reset zoom", None))
        self.brushSizeButton.setText("")
        self.brushsizelabel.setText(QCoreApplication.translate("MainWindow", u"Brush Size:", None))
    # retranslateUi

