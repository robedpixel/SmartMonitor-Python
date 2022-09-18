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
        self.noteButton = QPushButton(self.centralwidget)
        self.noteButton.setObjectName(u"noteButton")
        self.noteButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.noteButton, 0, 22, 1, 1)

        self.redoButton = QPushButton(self.centralwidget)
        self.redoButton.setObjectName(u"redoButton")
        self.redoButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.redoButton, 0, 5, 1, 1)

        self.labelButton_thirds = QPushButton(self.centralwidget)
        self.labelButton_thirds.setObjectName(u"labelButton_thirds")
        self.labelButton_thirds.setEnabled(True)
        self.labelButton_thirds.setMaximumSize(QSize(71, 51))
        self.labelButton_thirds.setCheckable(False)

        self.gridLayout_3.addWidget(self.labelButton_thirds, 0, 9, 1, 1)

        self.folderButton = QPushButton(self.centralwidget)
        self.folderButton.setObjectName(u"folderButton")
        self.folderButton.setMaximumSize(QSize(91, 51))

        self.gridLayout_3.addWidget(self.folderButton, 0, 17, 1, 1)

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


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 13, 1, 2)

        self.brushcolorlabel = QLabel(self.centralwidget)
        self.brushcolorlabel.setObjectName(u"brushcolorlabel")
        self.brushcolorlabel.setMaximumSize(QSize(51, 16777215))
        self.brushcolorlabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.brushcolorlabel, 0, 20, 1, 1)

        self.undoButton = QPushButton(self.centralwidget)
        self.undoButton.setObjectName(u"undoButton")
        self.undoButton.setMaximumSize(QSize(71, 51))

        self.gridLayout_3.addWidget(self.undoButton, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 6, 1, 1)

        self.brushSizeButton = QPushButton(self.centralwidget)
        self.brushSizeButton.setObjectName(u"brushSizeButton")
        self.brushSizeButton.setMaximumSize(QSize(51, 51))

        self.gridLayout_3.addWidget(self.brushSizeButton, 0, 19, 1, 1)

        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"QTabBar::tab { height: 50px; width: 138px; }")
        self.icontab = QWidget()
        self.icontab.setObjectName(u"icontab")
        self.verticalLayoutWidget = QWidget(self.icontab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 141, 621))
        self.iconLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.iconLayout.setObjectName(u"iconLayout")
        self.iconLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2.addTab(self.icontab, "")

        self.gridLayout_3.addWidget(self.tabWidget_2, 1, 2, 1, 2)

        self.brushcolorButton = QPushButton(self.centralwidget)
        self.brushcolorButton.setObjectName(u"brushcolorButton")
        self.brushcolorButton.setMaximumSize(QSize(51, 51))

        self.gridLayout_3.addWidget(self.brushcolorButton, 0, 21, 1, 1)

        self.resetZoomButton = QPushButton(self.centralwidget)
        self.resetZoomButton.setObjectName(u"resetZoomButton")
        self.resetZoomButton.setEnabled(True)
        self.resetZoomButton.setMaximumSize(QSize(71, 51))

        self.gridLayout_3.addWidget(self.resetZoomButton, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 12, 1, 1)

        self.labelButton_fourths = QPushButton(self.centralwidget)
        self.labelButton_fourths.setObjectName(u"labelButton_fourths")
        self.labelButton_fourths.setEnabled(True)
        self.labelButton_fourths.setMaximumSize(QSize(71, 51))
        self.labelButton_fourths.setCheckable(False)

        self.gridLayout_3.addWidget(self.labelButton_fourths, 0, 8, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 639, 499))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 1, 5, 1, 19)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabBar::tab { height: 50px; width: 100px; }")
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
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
        icon = QIcon()
        icon.addFile(u"resources/paint-brush.png", QSize(), QIcon.Normal, QIcon.Off)
        self.brushButton.setIcon(icon)
        self.brushButton.setCheckable(True)

        self.toolLayout.addWidget(self.brushButton)

        self.eraserButton = QPushButton(self.verticalLayoutWidget_2)
        self.eraserButton.setObjectName(u"eraserButton")
        self.eraserButton.setEnabled(False)
        self.eraserButton.setMinimumSize(QSize(0, 51))
        self.eraserButton.setMaximumSize(QSize(147, 16777215))
        icon1 = QIcon()
        icon1.addFile(u"resources/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eraserButton.setIcon(icon1)
        self.eraserButton.setCheckable(True)

        self.toolLayout.addWidget(self.eraserButton)

        self.arrowButton = QPushButton(self.verticalLayoutWidget_2)
        self.arrowButton.setObjectName(u"arrowButton")
        self.arrowButton.setEnabled(False)
        self.arrowButton.setMinimumSize(QSize(0, 51))
        self.arrowButton.setMaximumSize(QSize(147, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"resources/arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.arrowButton.setIcon(icon2)
        self.arrowButton.setCheckable(True)

        self.toolLayout.addWidget(self.arrowButton)

        self.rectButton = QPushButton(self.verticalLayoutWidget_2)
        self.rectButton.setObjectName(u"rectButton")
        self.rectButton.setEnabled(False)
        self.rectButton.setMinimumSize(QSize(0, 51))
        icon3 = QIcon()
        icon3.addFile(u"resources/rectangle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rectButton.setIcon(icon3)
        self.rectButton.setCheckable(True)

        self.toolLayout.addWidget(self.rectButton)

        self.cirButton = QPushButton(self.verticalLayoutWidget_2)
        self.cirButton.setObjectName(u"cirButton")
        self.cirButton.setEnabled(False)
        self.cirButton.setMinimumSize(QSize(0, 51))
        icon4 = QIcon()
        icon4.addFile(u"resources/ellipse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cirButton.setIcon(icon4)
        self.cirButton.setCheckable(True)

        self.toolLayout.addWidget(self.cirButton)

        self.tabWidget.addTab(self.tooltab, "")

        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 2)

        self.panButton = QPushButton(self.centralwidget)
        self.panButton.setObjectName(u"panButton")
        self.panButton.setEnabled(False)
        self.panButton.setMaximumSize(QSize(71, 51))
        icon5 = QIcon()
        icon5.addFile(u"resources/panningicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.panButton.setIcon(icon5)
        self.panButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.panButton, 0, 0, 1, 1)

        self.filesaveButton = QPushButton(self.centralwidget)
        self.filesaveButton.setObjectName(u"filesaveButton")
        self.filesaveButton.setEnabled(False)
        self.filesaveButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.filesaveButton, 0, 24, 1, 1)

        self.brushsizelabel = QLabel(self.centralwidget)
        self.brushsizelabel.setObjectName(u"brushsizelabel")
        self.brushsizelabel.setMaximumSize(QSize(51, 16777215))
        self.brushsizelabel.setWordWrap(True)

        self.gridLayout_3.addWidget(self.brushsizelabel, 0, 18, 1, 1)

        self.zoomButton = QPushButton(self.centralwidget)
        self.zoomButton.setObjectName(u"zoomButton")
        self.zoomButton.setEnabled(False)
        self.zoomButton.setMaximumSize(QSize(71, 51))
        icon6 = QIcon()
        icon6.addFile(u"resources/zoom icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomButton.setIcon(icon6)
        self.zoomButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.zoomButton, 0, 1, 1, 1)

        self.infoButton = QPushButton(self.centralwidget)
        self.infoButton.setObjectName(u"infoButton")
        self.infoButton.setEnabled(False)
        self.infoButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.infoButton, 0, 23, 1, 1)

        self.fileopenButton = QPushButton(self.centralwidget)
        self.fileopenButton.setObjectName(u"fileopenButton")
        self.fileopenButton.setMaximumSize(QSize(81, 51))
        self.fileopenButton.setTabletTracking(False)

        self.gridLayout_3.addWidget(self.fileopenButton, 0, 25, 1, 1)

        self.labelButton_ints = QPushButton(self.centralwidget)
        self.labelButton_ints.setObjectName(u"labelButton_ints")
        self.labelButton_ints.setEnabled(True)
        self.labelButton_ints.setMaximumSize(QSize(71, 51))
        self.labelButton_ints.setCheckable(False)

        self.gridLayout_3.addWidget(self.labelButton_ints, 0, 11, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 7, 1, 1)

        self.helpEdit = QPlainTextEdit(self.centralwidget)
        self.helpEdit.setObjectName(u"helpEdit")

        self.gridLayout_3.addWidget(self.helpEdit, 1, 24, 1, 2)

        self.labelButton_halfs = QPushButton(self.centralwidget)
        self.labelButton_halfs.setObjectName(u"labelButton_halfs")
        self.labelButton_halfs.setEnabled(True)
        self.labelButton_halfs.setMaximumSize(QSize(71, 51))
        self.labelButton_halfs.setCheckable(False)

        self.gridLayout_3.addWidget(self.labelButton_halfs, 0, 10, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.noteButton.setText(QCoreApplication.translate("MainWindow", u"Exif\n"
"Comments", None))
        self.redoButton.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.labelButton_thirds.setText(QCoreApplication.translate("MainWindow", u"1/3", None))
        self.folderButton.setText(QCoreApplication.translate("MainWindow", u"Change\n"
" camera folder", None))
        self.cropButton.setText(QCoreApplication.translate("MainWindow", u"Crop", None))
        self.zoomdisplaylabel.setText(QCoreApplication.translate("MainWindow", u"zoom:", None))
        self.brushcolorlabel.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.undoButton.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.brushSizeButton.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.icontab), QCoreApplication.translate("MainWindow", u"Drag-and-drop Labels", None))
        self.brushcolorButton.setText("")
        self.resetZoomButton.setText(QCoreApplication.translate("MainWindow", u"Reset zoom", None))
        self.labelButton_fourths.setText(QCoreApplication.translate("MainWindow", u"1/4", None))
        self.brushButton.setText("")
        self.eraserButton.setText("")
        self.arrowButton.setText("")
        self.rectButton.setText("")
        self.cirButton.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tooltab), QCoreApplication.translate("MainWindow", u"Drawing Tools", None))
        self.panButton.setText("")
        self.filesaveButton.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.brushsizelabel.setText(QCoreApplication.translate("MainWindow", u"Brush Size:", None))
        self.zoomButton.setText("")
        self.infoButton.setText(QCoreApplication.translate("MainWindow", u"Image\n"
"Info", None))
        self.fileopenButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.labelButton_ints.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"label increments:", None))
        self.labelButton_halfs.setText(QCoreApplication.translate("MainWindow", u"1/2", None))
    # retranslateUi

