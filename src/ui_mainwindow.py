# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow-resizable.ui'
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
        MainWindow.resize(1920, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 639, 499))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 1, 2, 1, 14)

        self.fileopenButton = QPushButton(self.centralwidget)
        self.fileopenButton.setObjectName(u"fileopenButton")
        self.fileopenButton.setMaximumSize(QSize(81, 51))
        self.fileopenButton.setTabletTracking(False)

        self.gridLayout_3.addWidget(self.fileopenButton, 0, 15, 1, 1)

        self.undoButton = QPushButton(self.centralwidget)
        self.undoButton.setObjectName(u"undoButton")
        self.undoButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.undoButton, 0, 3, 1, 1)

        self.brushcolorlabel = QLabel(self.centralwidget)
        self.brushcolorlabel.setObjectName(u"brushcolorlabel")
        self.brushcolorlabel.setMaximumSize(QSize(51, 16777215))
        self.brushcolorlabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.brushcolorlabel, 0, 10, 1, 1)

        self.folderButton = QPushButton(self.centralwidget)
        self.folderButton.setObjectName(u"folderButton")
        self.folderButton.setMaximumSize(QSize(91, 51))

        self.gridLayout_3.addWidget(self.folderButton, 0, 7, 1, 1)

        self.brushsizelabel = QLabel(self.centralwidget)
        self.brushsizelabel.setObjectName(u"brushsizelabel")
        self.brushsizelabel.setMaximumSize(QSize(51, 16777215))
        self.brushsizelabel.setWordWrap(True)

        self.gridLayout_3.addWidget(self.brushsizelabel, 0, 8, 1, 1)

        self.resetZoomButton = QPushButton(self.centralwidget)
        self.resetZoomButton.setObjectName(u"resetZoomButton")
        self.resetZoomButton.setEnabled(True)
        self.resetZoomButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.resetZoomButton, 0, 2, 1, 1)

        self.noteButton = QPushButton(self.centralwidget)
        self.noteButton.setObjectName(u"noteButton")
        self.noteButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.noteButton, 0, 12, 1, 1)

        self.cropButton = QPushButton(self.centralwidget)
        self.cropButton.setObjectName(u"cropButton")
        self.cropButton.setEnabled(False)
        self.cropButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.cropButton, 0, 5, 1, 1)

        self.infoButton = QPushButton(self.centralwidget)
        self.infoButton.setObjectName(u"infoButton")
        self.infoButton.setEnabled(False)
        self.infoButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.infoButton, 0, 13, 1, 1)

        self.redoButton = QPushButton(self.centralwidget)
        self.redoButton.setObjectName(u"redoButton")
        self.redoButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.redoButton, 0, 4, 1, 1)

        self.filesaveButton = QPushButton(self.centralwidget)
        self.filesaveButton.setObjectName(u"filesaveButton")
        self.filesaveButton.setEnabled(False)
        self.filesaveButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.filesaveButton, 0, 14, 1, 1)

        self.brushcolorButton = QPushButton(self.centralwidget)
        self.brushcolorButton.setObjectName(u"brushcolorButton")
        self.brushcolorButton.setMaximumSize(QSize(51, 51))

        self.gridLayout_3.addWidget(self.brushcolorButton, 0, 11, 1, 1)

        self.brushSizeButton = QPushButton(self.centralwidget)
        self.brushSizeButton.setObjectName(u"brushSizeButton")
        self.brushSizeButton.setMaximumSize(QSize(51, 51))

        self.gridLayout_3.addWidget(self.brushSizeButton, 0, 9, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.brushButton = QPushButton(self.centralwidget)
        self.brushButton.setObjectName(u"brushButton")
        self.brushButton.setEnabled(False)
        self.brushButton.setMinimumSize(QSize(0, 51))
        self.brushButton.setCheckable(True)

        self.verticalLayout.addWidget(self.brushButton)

        self.pickerButton = QPushButton(self.centralwidget)
        self.pickerButton.setObjectName(u"pickerButton")
        self.pickerButton.setEnabled(False)
        self.pickerButton.setMinimumSize(QSize(0, 51))
        self.pickerButton.setCheckable(True)

        self.verticalLayout.addWidget(self.pickerButton)

        self.eraserButton = QPushButton(self.centralwidget)
        self.eraserButton.setObjectName(u"eraserButton")
        self.eraserButton.setEnabled(False)
        self.eraserButton.setMinimumSize(QSize(0, 51))
        self.eraserButton.setCheckable(True)

        self.verticalLayout.addWidget(self.eraserButton)

        self.selectButton = QPushButton(self.centralwidget)
        self.selectButton.setObjectName(u"selectButton")
        self.selectButton.setEnabled(False)
        self.selectButton.setMinimumSize(QSize(0, 51))
        self.selectButton.setCheckable(True)

        self.verticalLayout.addWidget(self.selectButton)

        self.lineButton = QPushButton(self.centralwidget)
        self.lineButton.setObjectName(u"lineButton")
        self.lineButton.setEnabled(False)
        self.lineButton.setMinimumSize(QSize(0, 51))
        self.lineButton.setCheckable(True)

        self.verticalLayout.addWidget(self.lineButton)

        self.rectButton = QPushButton(self.centralwidget)
        self.rectButton.setObjectName(u"rectButton")
        self.rectButton.setEnabled(False)
        self.rectButton.setMinimumSize(QSize(0, 51))
        self.rectButton.setCheckable(True)

        self.verticalLayout.addWidget(self.rectButton)

        self.cirButton = QPushButton(self.centralwidget)
        self.cirButton.setObjectName(u"cirButton")
        self.cirButton.setEnabled(False)
        self.cirButton.setMinimumSize(QSize(0, 51))
        self.cirButton.setCheckable(True)

        self.verticalLayout.addWidget(self.cirButton)


        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.zoomButton = QPushButton(self.centralwidget)
        self.zoomButton.setObjectName(u"zoomButton")
        self.zoomButton.setEnabled(False)
        self.zoomButton.setMaximumSize(QSize(147, 51))
        self.zoomButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.zoomButton, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fileopenButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.undoButton.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.brushcolorlabel.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.folderButton.setText(QCoreApplication.translate("MainWindow", u"Change\n"
" camera folder", None))
        self.brushsizelabel.setText(QCoreApplication.translate("MainWindow", u"Brush Size:", None))
        self.resetZoomButton.setText(QCoreApplication.translate("MainWindow", u"Reset zoom", None))
        self.noteButton.setText(QCoreApplication.translate("MainWindow", u"Exif\n"
"Comments", None))
        self.cropButton.setText(QCoreApplication.translate("MainWindow", u"Crop", None))
        self.infoButton.setText(QCoreApplication.translate("MainWindow", u"Image\n"
"Info", None))
        self.redoButton.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.filesaveButton.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.brushcolorButton.setText("")
        self.brushSizeButton.setText("")
        self.brushButton.setText(QCoreApplication.translate("MainWindow", u"Brush", None))
        self.pickerButton.setText(QCoreApplication.translate("MainWindow", u"Colour Picker", None))
        self.eraserButton.setText(QCoreApplication.translate("MainWindow", u"Eraser", None))
        self.selectButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.lineButton.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.rectButton.setText(QCoreApplication.translate("MainWindow", u"Rectangle", None))
        self.cirButton.setText(QCoreApplication.translate("MainWindow", u"Ellipse", None))
        self.zoomButton.setText(QCoreApplication.translate("MainWindow", u"Zoom", None))
    # retranslateUi

