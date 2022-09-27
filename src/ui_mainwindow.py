# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow-resizable-2.ui'
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

        self.gridLayout_3.addWidget(self.brushcolorlabel, 0, 20, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 6, 1, 1)

        self.resetZoomButton = QPushButton(self.centralwidget)
        self.resetZoomButton.setObjectName(u"resetZoomButton")
        self.resetZoomButton.setEnabled(True)
        self.resetZoomButton.setMaximumSize(QSize(71, 51))

        self.gridLayout_3.addWidget(self.resetZoomButton, 0, 2, 1, 1)

        self.fileopenButton = QPushButton(self.centralwidget)
        self.fileopenButton.setObjectName(u"fileopenButton")
        self.fileopenButton.setMaximumSize(QSize(81, 51))
        self.fileopenButton.setTabletTracking(False)

        self.gridLayout_3.addWidget(self.fileopenButton, 0, 25, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 7, 1, 1)

        self.LabelTab = QTabWidget(self.centralwidget)
        self.LabelTab.setObjectName(u"LabelTab")
        self.LabelTab.setStyleSheet(u"QTabBar::tab { height: 50px; font-size: 11px; width: 138px; }")
        self.icontab = QWidget()
        self.icontab.setObjectName(u"icontab")
        self.gridLayoutWidget_2 = QWidget(self.icontab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 141, 431))
        self.iconLayout = QGridLayout(self.gridLayoutWidget_2)
        self.iconLayout.setObjectName(u"iconLayout")
        self.iconLayout.setContentsMargins(0, 0, 0, 0)
        self.LabelTab.addTab(self.icontab, "")

        self.gridLayout_3.addWidget(self.LabelTab, 2, 2, 1, 2)

        self.folderButton = QPushButton(self.centralwidget)
        self.folderButton.setObjectName(u"folderButton")
        self.folderButton.setMaximumSize(QSize(91, 51))

        self.gridLayout_3.addWidget(self.folderButton, 0, 17, 1, 1)

        self.filesaveButton = QPushButton(self.centralwidget)
        self.filesaveButton.setObjectName(u"filesaveButton")
        self.filesaveButton.setEnabled(False)
        self.filesaveButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.filesaveButton, 0, 24, 1, 1)

        self.redoButton = QPushButton(self.centralwidget)
        self.redoButton.setObjectName(u"redoButton")
        self.redoButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.redoButton, 0, 5, 1, 1)

        self.brushsizelabel = QLabel(self.centralwidget)
        self.brushsizelabel.setObjectName(u"brushsizelabel")
        self.brushsizelabel.setMaximumSize(QSize(51, 16777215))
        self.brushsizelabel.setWordWrap(True)

        self.gridLayout_3.addWidget(self.brushsizelabel, 0, 18, 1, 1)

        self.zoomButton = QPushButton(self.centralwidget)
        self.zoomButton.setObjectName(u"zoomButton")
        self.zoomButton.setEnabled(False)
        self.zoomButton.setMaximumSize(QSize(71, 51))
        icon = QIcon()
        icon.addFile(u"resources/zoom icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomButton.setIcon(icon)
        self.zoomButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.zoomButton, 0, 1, 1, 1)

        self.noteButton = QPushButton(self.centralwidget)
        self.noteButton.setObjectName(u"noteButton")
        self.noteButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.noteButton, 0, 22, 1, 1)

        self.infoButton = QPushButton(self.centralwidget)
        self.infoButton.setObjectName(u"infoButton")
        self.infoButton.setEnabled(False)
        self.infoButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.infoButton, 0, 23, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 12, 1, 1)

        self.labelButton_thirds = QPushButton(self.centralwidget)
        self.labelButton_thirds.setObjectName(u"labelButton_thirds")
        self.labelButton_thirds.setEnabled(True)
        self.labelButton_thirds.setMaximumSize(QSize(71, 51))
        self.labelButton_thirds.setCheckable(False)

        self.gridLayout_3.addWidget(self.labelButton_thirds, 0, 9, 1, 1)

        self.undoButton = QPushButton(self.centralwidget)
        self.undoButton.setObjectName(u"undoButton")
        self.undoButton.setMaximumSize(QSize(71, 51))

        self.gridLayout_3.addWidget(self.undoButton, 0, 3, 1, 1)

        self.brushSizeButton = QPushButton(self.centralwidget)
        self.brushSizeButton.setObjectName(u"brushSizeButton")
        self.brushSizeButton.setMaximumSize(QSize(51, 51))

        self.gridLayout_3.addWidget(self.brushSizeButton, 0, 19, 1, 1)

        self.labelButton_ints = QPushButton(self.centralwidget)
        self.labelButton_ints.setObjectName(u"labelButton_ints")
        self.labelButton_ints.setEnabled(True)
        self.labelButton_ints.setMaximumSize(QSize(71, 51))
        self.labelButton_ints.setCheckable(False)

        self.gridLayout_3.addWidget(self.labelButton_ints, 0, 11, 1, 1)

        self.brushcolorButton = QPushButton(self.centralwidget)
        self.brushcolorButton.setObjectName(u"brushcolorButton")
        self.brushcolorButton.setMinimumSize(QSize(50, 0))
        self.brushcolorButton.setMaximumSize(QSize(51, 51))

        self.gridLayout_3.addWidget(self.brushcolorButton, 0, 21, 1, 1)

        self.panButton = QPushButton(self.centralwidget)
        self.panButton.setObjectName(u"panButton")
        self.panButton.setEnabled(False)
        self.panButton.setMaximumSize(QSize(71, 51))
        icon1 = QIcon()
        icon1.addFile(u"resources/panningicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.panButton.setIcon(icon1)
        self.panButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.panButton, 0, 0, 1, 1)

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

        self.labelButton_fourths = QPushButton(self.centralwidget)
        self.labelButton_fourths.setObjectName(u"labelButton_fourths")
        self.labelButton_fourths.setEnabled(True)
        self.labelButton_fourths.setMaximumSize(QSize(71, 51))
        self.labelButton_fourths.setCheckable(False)

        self.gridLayout_3.addWidget(self.labelButton_fourths, 0, 8, 1, 1)

        self.labelButton_halfs = QPushButton(self.centralwidget)
        self.labelButton_halfs.setObjectName(u"labelButton_halfs")
        self.labelButton_halfs.setEnabled(True)
        self.labelButton_halfs.setMaximumSize(QSize(71, 51))
        self.labelButton_halfs.setCheckable(False)

        self.gridLayout_3.addWidget(self.labelButton_halfs, 0, 10, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabBar::tab { height: 50px;  font-size: 11px; width: 100px; }")
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tooltab = QWidget()
        self.tooltab.setObjectName(u"tooltab")
        self.verticalLayoutWidget_2 = QWidget(self.tooltab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 121, 631))
        self.toolLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.toolLayout.setObjectName(u"toolLayout")
        self.toolLayout.setContentsMargins(0, 0, 0, 0)
        self.burnButton = QPushButton(self.verticalLayoutWidget_2)
        self.burnButton.setObjectName(u"burnButton")
        self.burnButton.setEnabled(False)
        self.burnButton.setMinimumSize(QSize(0, 51))
        self.burnButton.setMaximumSize(QSize(147, 16777215))
        self.burnButton.setCheckable(True)

        self.toolLayout.addWidget(self.burnButton)

        self.dodgeButton = QPushButton(self.verticalLayoutWidget_2)
        self.dodgeButton.setObjectName(u"dodgeButton")
        self.dodgeButton.setEnabled(False)
        self.dodgeButton.setMinimumSize(QSize(0, 51))
        self.dodgeButton.setMaximumSize(QSize(147, 16777215))
        self.dodgeButton.setCheckable(True)

        self.toolLayout.addWidget(self.dodgeButton)

        self.tabWidget.addTab(self.tooltab, "")

        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 2, 2)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 639, 499))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 1, 5, 2, 19)

        self.AreaTab = QTabWidget(self.centralwidget)
        self.AreaTab.setObjectName(u"AreaTab")
        self.AreaTab.setMaximumSize(QSize(16777215, 200))
        self.AreaTab.setStyleSheet(u"QTabBar::tab { height: 50px; font-size: 11px; width: 138px; }")
        self.Areatab = QWidget()
        self.Areatab.setObjectName(u"Areatab")
        self.gridLayoutWidget = QWidget(self.Areatab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 141, 141))
        self.selectionLayout = QGridLayout(self.gridLayoutWidget)
        self.selectionLayout.setObjectName(u"selectionLayout")
        self.selectionLayout.setContentsMargins(0, 0, 0, 0)
        self.cirButton = QPushButton(self.gridLayoutWidget)
        self.cirButton.setObjectName(u"cirButton")
        self.cirButton.setEnabled(False)
        self.cirButton.setMinimumSize(QSize(0, 50))
        self.cirButton.setMaximumSize(QSize(60, 16777215))
        self.cirButton.setCheckable(True)

        self.selectionLayout.addWidget(self.cirButton, 1, 0, 1, 1)

        self.brushButton = QPushButton(self.gridLayoutWidget)
        self.brushButton.setObjectName(u"brushButton")
        self.brushButton.setEnabled(False)
        self.brushButton.setMinimumSize(QSize(0, 50))
        self.brushButton.setMaximumSize(QSize(60, 16777215))
        self.brushButton.setCheckable(True)

        self.selectionLayout.addWidget(self.brushButton, 0, 0, 1, 1)

        self.rectButton = QPushButton(self.gridLayoutWidget)
        self.rectButton.setObjectName(u"rectButton")
        self.rectButton.setEnabled(False)
        self.rectButton.setMinimumSize(QSize(0, 50))
        self.rectButton.setMaximumSize(QSize(60, 16777215))
        self.rectButton.setCheckable(True)

        self.selectionLayout.addWidget(self.rectButton, 1, 1, 1, 1)

        self.arrowButton = QPushButton(self.gridLayoutWidget)
        self.arrowButton.setObjectName(u"arrowButton")
        self.arrowButton.setEnabled(False)
        self.arrowButton.setMinimumSize(QSize(0, 50))
        self.arrowButton.setMaximumSize(QSize(60, 16777215))
        self.arrowButton.setCheckable(True)

        self.selectionLayout.addWidget(self.arrowButton, 0, 1, 1, 1)

        self.AreaTab.addTab(self.Areatab, "")

        self.gridLayout_3.addWidget(self.AreaTab, 1, 2, 1, 2)

        self.helpEdit = QPlainTextEdit(self.centralwidget)
        self.helpEdit.setObjectName(u"helpEdit")

        self.gridLayout_3.addWidget(self.helpEdit, 1, 24, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.LabelTab.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.AreaTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.brushcolorlabel.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.resetZoomButton.setText(QCoreApplication.translate("MainWindow", u"Reset zoom", None))
        self.fileopenButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"label increments:", None))
        self.LabelTab.setTabText(self.LabelTab.indexOf(self.icontab), QCoreApplication.translate("MainWindow", u"Drag-and-drop Labels", None))
        self.folderButton.setText(QCoreApplication.translate("MainWindow", u"Change\n"
" camera folder", None))
        self.filesaveButton.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.redoButton.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.brushsizelabel.setText(QCoreApplication.translate("MainWindow", u"Brush Size:", None))
        self.zoomButton.setText("")
        self.noteButton.setText(QCoreApplication.translate("MainWindow", u"Exif\n"
"Comments", None))
        self.infoButton.setText(QCoreApplication.translate("MainWindow", u"Image\n"
"Info", None))
        self.labelButton_thirds.setText(QCoreApplication.translate("MainWindow", u"1/3", None))
        self.undoButton.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.brushSizeButton.setText("")
        self.labelButton_ints.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.brushcolorButton.setText("")
        self.panButton.setText("")
        self.cropButton.setText(QCoreApplication.translate("MainWindow", u"Crop", None))
        self.zoomdisplaylabel.setText(QCoreApplication.translate("MainWindow", u"zoom:", None))
        self.labelButton_fourths.setText(QCoreApplication.translate("MainWindow", u"1/4", None))
        self.labelButton_halfs.setText(QCoreApplication.translate("MainWindow", u"1/2", None))
        self.burnButton.setText(QCoreApplication.translate("MainWindow", u"Burn", None))
        self.dodgeButton.setText(QCoreApplication.translate("MainWindow", u"Dodge", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tooltab), QCoreApplication.translate("MainWindow", u"Action", None))
        self.cirButton.setText(QCoreApplication.translate("MainWindow", u"Ellipse", None))
        self.brushButton.setText(QCoreApplication.translate("MainWindow", u"Freehand", None))
        self.rectButton.setText(QCoreApplication.translate("MainWindow", u"Rectangle", None))
        self.arrowButton.setText(QCoreApplication.translate("MainWindow", u"Point", None))
        self.AreaTab.setTabText(self.AreaTab.indexOf(self.Areatab), QCoreApplication.translate("MainWindow", u"Area Selection", None))
    # retranslateUi

