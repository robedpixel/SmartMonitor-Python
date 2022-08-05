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
        MainWindow.resize(1303, 672)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 50, 161, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.brushButton = QPushButton(self.verticalLayoutWidget)
        self.brushButton.setObjectName(u"brushButton")
        self.brushButton.setEnabled(False)
        self.brushButton.setMinimumSize(QSize(0, 51))
        self.brushButton.setCheckable(True)

        self.verticalLayout.addWidget(self.brushButton)

        self.pickerButton = QPushButton(self.verticalLayoutWidget)
        self.pickerButton.setObjectName(u"pickerButton")
        self.pickerButton.setEnabled(False)
        self.pickerButton.setMinimumSize(QSize(0, 51))
        self.pickerButton.setCheckable(True)

        self.verticalLayout.addWidget(self.pickerButton)

        self.eraserButton = QPushButton(self.verticalLayoutWidget)
        self.eraserButton.setObjectName(u"eraserButton")
        self.eraserButton.setEnabled(False)
        self.eraserButton.setMinimumSize(QSize(0, 51))
        self.eraserButton.setCheckable(True)

        self.verticalLayout.addWidget(self.eraserButton)

        self.selectButton = QPushButton(self.verticalLayoutWidget)
        self.selectButton.setObjectName(u"selectButton")
        self.selectButton.setEnabled(False)
        self.selectButton.setMinimumSize(QSize(0, 51))
        self.selectButton.setCheckable(True)

        self.verticalLayout.addWidget(self.selectButton)

        self.lineButton = QPushButton(self.verticalLayoutWidget)
        self.lineButton.setObjectName(u"lineButton")
        self.lineButton.setEnabled(False)
        self.lineButton.setMinimumSize(QSize(0, 51))
        self.lineButton.setCheckable(True)

        self.verticalLayout.addWidget(self.lineButton)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(160, 50, 1131, 581))
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 639, 499))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.fileopenButton = QPushButton(self.centralwidget)
        self.fileopenButton.setObjectName(u"fileopenButton")
        self.fileopenButton.setGeometry(QRect(1210, 0, 81, 51))
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
        self.brushcolorlabel.setGeometry(QRect(860, 0, 41, 20))
        self.brushcolorlabel.setAlignment(Qt.AlignCenter)
        self.brushcolorButton = QPushButton(self.centralwidget)
        self.brushcolorButton.setObjectName(u"brushcolorButton")
        self.brushcolorButton.setGeometry(QRect(910, 0, 51, 51))
        self.noteButton = QPushButton(self.centralwidget)
        self.noteButton.setObjectName(u"noteButton")
        self.noteButton.setGeometry(QRect(990, 0, 81, 51))
        self.filesaveButton = QPushButton(self.centralwidget)
        self.filesaveButton.setObjectName(u"filesaveButton")
        self.filesaveButton.setEnabled(False)
        self.filesaveButton.setGeometry(QRect(1100, 0, 81, 51))
        self.resetZoomButton = QPushButton(self.centralwidget)
        self.resetZoomButton.setObjectName(u"resetZoomButton")
        self.resetZoomButton.setEnabled(True)
        self.resetZoomButton.setGeometry(QRect(180, 0, 71, 51))
        self.brushSizeButton = QPushButton(self.centralwidget)
        self.brushSizeButton.setObjectName(u"brushSizeButton")
        self.brushSizeButton.setGeometry(QRect(780, 0, 51, 51))
        self.brushsizelabel = QLabel(self.centralwidget)
        self.brushsizelabel.setObjectName(u"brushsizelabel")
        self.brushsizelabel.setGeometry(QRect(740, 0, 31, 31))
        self.brushsizelabel.setWordWrap(True)
        self.undoButton = QPushButton(self.centralwidget)
        self.undoButton.setObjectName(u"undoButton")
        self.undoButton.setGeometry(QRect(270, 0, 71, 51))
        self.redoButton = QPushButton(self.centralwidget)
        self.redoButton.setObjectName(u"redoButton")
        self.redoButton.setGeometry(QRect(360, 0, 71, 51))
        self.folderButton = QPushButton(self.centralwidget)
        self.folderButton.setObjectName(u"folderButton")
        self.folderButton.setGeometry(QRect(610, 0, 91, 51))
        self.cropButton = QPushButton(self.centralwidget)
        self.cropButton.setObjectName(u"cropButton")
        self.cropButton.setEnabled(False)
        self.cropButton.setGeometry(QRect(450, 0, 71, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1303, 22))
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
        self.pickerButton.setText(QCoreApplication.translate("MainWindow", u"Colour Picker", None))
        self.eraserButton.setText(QCoreApplication.translate("MainWindow", u"Eraser", None))
        self.selectButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.lineButton.setText(QCoreApplication.translate("MainWindow", u"Line", None))
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
        self.undoButton.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.redoButton.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.folderButton.setText(QCoreApplication.translate("MainWindow", u"Change\n"
" camera folder", None))
        self.cropButton.setText(QCoreApplication.translate("MainWindow", u"Crop", None))
    # retranslateUi

