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
        self.brushcolorlabel = QLabel(self.centralwidget)
        self.brushcolorlabel.setObjectName(u"brushcolorlabel")
        self.brushcolorlabel.setMaximumSize(QSize(51, 16777215))
        self.brushcolorlabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.brushcolorlabel, 0, 13, 1, 1)

        self.brushsizelabel = QLabel(self.centralwidget)
        self.brushsizelabel.setObjectName(u"brushsizelabel")
        self.brushsizelabel.setMaximumSize(QSize(51, 16777215))
        self.brushsizelabel.setWordWrap(True)

        self.gridLayout_3.addWidget(self.brushsizelabel, 0, 11, 1, 1)

        self.infoButton = QPushButton(self.centralwidget)
        self.infoButton.setObjectName(u"infoButton")
        self.infoButton.setEnabled(False)
        self.infoButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.infoButton, 0, 16, 1, 1)

        self.panButton = QPushButton(self.centralwidget)
        self.panButton.setObjectName(u"panButton")
        self.panButton.setEnabled(False)
        self.panButton.setMaximumSize(QSize(71, 51))
        icon = QIcon()
        icon.addFile(u"resources/panningicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.panButton.setIcon(icon)
        self.panButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.panButton, 0, 0, 1, 1)

        self.folderButton = QPushButton(self.centralwidget)
        self.folderButton.setObjectName(u"folderButton")
        self.folderButton.setMaximumSize(QSize(91, 51))

        self.gridLayout_3.addWidget(self.folderButton, 0, 10, 1, 1)

        self.filesaveButton = QPushButton(self.centralwidget)
        self.filesaveButton.setObjectName(u"filesaveButton")
        self.filesaveButton.setEnabled(False)
        self.filesaveButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.filesaveButton, 0, 17, 1, 1)

        self.zoomButton = QPushButton(self.centralwidget)
        self.zoomButton.setObjectName(u"zoomButton")
        self.zoomButton.setEnabled(False)
        self.zoomButton.setMaximumSize(QSize(71, 51))
        icon1 = QIcon()
        icon1.addFile(u"resources/zoom icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomButton.setIcon(icon1)
        self.zoomButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.zoomButton, 0, 1, 1, 1)

        self.noteButton = QPushButton(self.centralwidget)
        self.noteButton.setObjectName(u"noteButton")
        self.noteButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.noteButton, 0, 15, 1, 1)

        self.fileopenButton = QPushButton(self.centralwidget)
        self.fileopenButton.setObjectName(u"fileopenButton")
        self.fileopenButton.setMaximumSize(QSize(81, 51))
        self.fileopenButton.setTabletTracking(False)

        self.gridLayout_3.addWidget(self.fileopenButton, 0, 18, 1, 1)

        self.brushcolorButton = QPushButton(self.centralwidget)
        self.brushcolorButton.setObjectName(u"brushcolorButton")
        self.brushcolorButton.setMaximumSize(QSize(51, 51))

        self.gridLayout_3.addWidget(self.brushcolorButton, 0, 14, 1, 1)

        self.redoButton = QPushButton(self.centralwidget)
        self.redoButton.setObjectName(u"redoButton")
        self.redoButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.redoButton, 0, 5, 1, 1)

        self.brushSizeButton = QPushButton(self.centralwidget)
        self.brushSizeButton.setObjectName(u"brushSizeButton")
        self.brushSizeButton.setMaximumSize(QSize(51, 51))

        self.gridLayout_3.addWidget(self.brushSizeButton, 0, 12, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.zoomBar = QScrollBar(self.centralwidget)
        self.zoomBar.setObjectName(u"zoomBar")
        self.zoomBar.setEnabled(False)
        self.zoomBar.setMinimumSize(QSize(300, 41))
        self.zoomBar.setMaximumSize(QSize(300, 41))
        self.zoomBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.zoomBar)

        self.cropButton = QPushButton(self.centralwidget)
        self.cropButton.setObjectName(u"cropButton")
        self.cropButton.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cropButton.sizePolicy().hasHeightForWidth())
        self.cropButton.setSizePolicy(sizePolicy)
        self.cropButton.setMaximumSize(QSize(81, 51))

        self.horizontalLayout.addWidget(self.cropButton)

        self.zoomdisplaylabel = QLabel(self.centralwidget)
        self.zoomdisplaylabel.setObjectName(u"zoomdisplaylabel")
        self.zoomdisplaylabel.setEnabled(False)

        self.horizontalLayout.addWidget(self.zoomdisplaylabel)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 6, 1, 2)

        self.helpEdit = QPlainTextEdit(self.centralwidget)
        self.helpEdit.setObjectName(u"helpEdit")

        self.gridLayout_3.addWidget(self.helpEdit, 1, 17, 1, 2)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 639, 499))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 1, 5, 1, 12)

        self.resetZoomButton = QPushButton(self.centralwidget)
        self.resetZoomButton.setObjectName(u"resetZoomButton")
        self.resetZoomButton.setEnabled(True)
        self.resetZoomButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.resetZoomButton, 0, 2, 1, 1)

        self.undoButton = QPushButton(self.centralwidget)
        self.undoButton.setObjectName(u"undoButton")
        self.undoButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.undoButton, 0, 3, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabBar::tab { height: 50px; width: 70px; }")
        self.tooltab = QWidget()
        self.tooltab.setObjectName(u"tooltab")
        self.verticalLayoutWidget_2 = QWidget(self.tooltab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 141, 631))
        self.toolLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.toolLayout.setObjectName(u"toolLayout")
        self.toolLayout.setContentsMargins(0, 0, 0, 0)
        self.brushButton = QPushButton(self.verticalLayoutWidget_2)
        self.brushButton.setObjectName(u"brushButton")
        self.brushButton.setEnabled(False)
        self.brushButton.setMinimumSize(QSize(0, 51))
        self.brushButton.setMaximumSize(QSize(147, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"resources/paint-brush.png", QSize(), QIcon.Normal, QIcon.Off)
        self.brushButton.setIcon(icon2)
        self.brushButton.setCheckable(True)

        self.toolLayout.addWidget(self.brushButton)

        self.eraserButton = QPushButton(self.verticalLayoutWidget_2)
        self.eraserButton.setObjectName(u"eraserButton")
        self.eraserButton.setEnabled(False)
        self.eraserButton.setMinimumSize(QSize(0, 51))
        self.eraserButton.setMaximumSize(QSize(147, 16777215))
        icon3 = QIcon()
        icon3.addFile(u"resources/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eraserButton.setIcon(icon3)
        self.eraserButton.setCheckable(True)

        self.toolLayout.addWidget(self.eraserButton)

        self.lineButton = QPushButton(self.verticalLayoutWidget_2)
        self.lineButton.setObjectName(u"lineButton")
        self.lineButton.setEnabled(False)
        self.lineButton.setMinimumSize(QSize(0, 51))
        self.lineButton.setMaximumSize(QSize(147, 16777215))
        icon4 = QIcon()
        icon4.addFile(u"resources/line-tool.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lineButton.setIcon(icon4)
        self.lineButton.setCheckable(True)

        self.toolLayout.addWidget(self.lineButton)

        self.rectButton = QPushButton(self.verticalLayoutWidget_2)
        self.rectButton.setObjectName(u"rectButton")
        self.rectButton.setEnabled(False)
        self.rectButton.setMinimumSize(QSize(0, 51))
        icon5 = QIcon()
        icon5.addFile(u"resources/rectangle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rectButton.setIcon(icon5)
        self.rectButton.setCheckable(True)

        self.toolLayout.addWidget(self.rectButton)

        self.cirButton = QPushButton(self.verticalLayoutWidget_2)
        self.cirButton.setObjectName(u"cirButton")
        self.cirButton.setEnabled(False)
        self.cirButton.setMinimumSize(QSize(0, 51))
        icon6 = QIcon()
        icon6.addFile(u"resources/ellipse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cirButton.setIcon(icon6)
        self.cirButton.setCheckable(True)

        self.toolLayout.addWidget(self.cirButton)

        self.verticalLayoutWidget = QWidget(self.tooltab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(160, 0, 141, 631))
        self.iconLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.iconLayout.setObjectName(u"iconLayout")
        self.iconLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tooltab, "")
        self.icontab = QWidget()
        self.icontab.setObjectName(u"icontab")
        self.tabWidget.addTab(self.icontab, "")

        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.brushcolorlabel.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.brushsizelabel.setText(QCoreApplication.translate("MainWindow", u"Brush Size:", None))
        self.infoButton.setText(QCoreApplication.translate("MainWindow", u"Image\n"
"Info", None))
        self.panButton.setText("")
        self.folderButton.setText(QCoreApplication.translate("MainWindow", u"Change\n"
" camera folder", None))
        self.filesaveButton.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.zoomButton.setText("")
        self.noteButton.setText(QCoreApplication.translate("MainWindow", u"Exif\n"
"Comments", None))
        self.fileopenButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.brushcolorButton.setText("")
        self.redoButton.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.brushSizeButton.setText("")
        self.cropButton.setText(QCoreApplication.translate("MainWindow", u"Crop", None))
        self.zoomdisplaylabel.setText(QCoreApplication.translate("MainWindow", u"zoom:", None))
        self.resetZoomButton.setText(QCoreApplication.translate("MainWindow", u"Reset zoom", None))
        self.undoButton.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.brushButton.setText("")
        self.eraserButton.setText("")
        self.lineButton.setText("")
        self.rectButton.setText("")
        self.cirButton.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tooltab), QCoreApplication.translate("MainWindow", u"Tools", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.icontab), QCoreApplication.translate("MainWindow", u"Icons", None))
    # retranslateUi

