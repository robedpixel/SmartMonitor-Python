# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow-resizable-3.ui'
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
        self.resetZoomButton = QPushButton(self.centralwidget)
        self.resetZoomButton.setObjectName(u"resetZoomButton")
        self.resetZoomButton.setEnabled(True)
        self.resetZoomButton.setMaximumSize(QSize(71, 51))

        self.gridLayout_3.addWidget(self.resetZoomButton, 0, 10, 1, 1)

        self.brushcolorlabel = QLabel(self.centralwidget)
        self.brushcolorlabel.setObjectName(u"brushcolorlabel")
        self.brushcolorlabel.setMaximumSize(QSize(51, 16777215))
        self.brushcolorlabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.brushcolorlabel, 0, 21, 1, 1)

        self.filesaveButton = QPushButton(self.centralwidget)
        self.filesaveButton.setObjectName(u"filesaveButton")
        self.filesaveButton.setEnabled(False)
        self.filesaveButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.filesaveButton, 0, 25, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 639, 499))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 1, 12, 5, 13)

        self.helpEdit = QPlainTextEdit(self.centralwidget)
        self.helpEdit.setObjectName(u"helpEdit")
        font = QFont()
        font.setPointSize(12)
        self.helpEdit.setFont(font)

        self.gridLayout_3.addWidget(self.helpEdit, 1, 25, 5, 2)

        self.AreaTab = QTabWidget(self.centralwidget)
        self.AreaTab.setObjectName(u"AreaTab")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AreaTab.sizePolicy().hasHeightForWidth())
        self.AreaTab.setSizePolicy(sizePolicy)
        self.AreaTab.setMinimumSize(QSize(150, 0))
        self.AreaTab.setMaximumSize(QSize(150, 180))
        self.AreaTab.setStyleSheet(u"QTabBar::tab { height: 50px; font-size: 11px; width: 138px; }")
        self.Areatab = QWidget()
        self.Areatab.setObjectName(u"Areatab")
        self.gridLayout_4 = QGridLayout(self.Areatab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.selectionLayout = QGridLayout()
        self.selectionLayout.setObjectName(u"selectionLayout")
        self.rectButton = QPushButton(self.Areatab)
        self.rectButton.setObjectName(u"rectButton")
        self.rectButton.setEnabled(False)
        self.rectButton.setMinimumSize(QSize(0, 50))
        self.rectButton.setMaximumSize(QSize(60, 16777215))
        self.rectButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"resources/rectanglefinger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rectButton.setIcon(icon)
        self.rectButton.setIconSize(QSize(32, 32))
        self.rectButton.setCheckable(True)

        self.selectionLayout.addWidget(self.rectButton, 1, 1, 1, 1)

        self.cirButton = QPushButton(self.Areatab)
        self.cirButton.setObjectName(u"cirButton")
        self.cirButton.setEnabled(False)
        self.cirButton.setMinimumSize(QSize(0, 50))
        self.cirButton.setMaximumSize(QSize(60, 16777215))
        self.cirButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"resources/ellipsefinger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cirButton.setIcon(icon1)
        self.cirButton.setIconSize(QSize(32, 32))
        self.cirButton.setCheckable(True)

        self.selectionLayout.addWidget(self.cirButton, 1, 0, 1, 1)

        self.arrowButton = QPushButton(self.Areatab)
        self.arrowButton.setObjectName(u"arrowButton")
        self.arrowButton.setEnabled(False)
        self.arrowButton.setMinimumSize(QSize(0, 50))
        self.arrowButton.setMaximumSize(QSize(60, 16777215))
        self.arrowButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"resources/arrowfinger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.arrowButton.setIcon(icon2)
        self.arrowButton.setIconSize(QSize(32, 32))
        self.arrowButton.setCheckable(True)

        self.selectionLayout.addWidget(self.arrowButton, 0, 1, 1, 1)

        self.brushButton = QPushButton(self.Areatab)
        self.brushButton.setObjectName(u"brushButton")
        self.brushButton.setEnabled(False)
        self.brushButton.setMinimumSize(QSize(0, 50))
        self.brushButton.setMaximumSize(QSize(60, 16777215))
        self.brushButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"resources/squigglefinger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.brushButton.setIcon(icon3)
        self.brushButton.setIconSize(QSize(32, 32))
        self.brushButton.setCheckable(True)

        self.selectionLayout.addWidget(self.brushButton, 0, 0, 1, 1)

        self.labelButton = QPushButton(self.Areatab)
        self.labelButton.setObjectName(u"labelButton")
        self.labelButton.setEnabled(False)
        self.labelButton.setMinimumSize(QSize(0, 50))
        self.labelButton.setMaximumSize(QSize(60, 16777215))
        self.labelButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"resources/draglabel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.labelButton.setIcon(icon4)
        self.labelButton.setIconSize(QSize(32, 32))
        self.labelButton.setCheckable(True)

        self.selectionLayout.addWidget(self.labelButton, 1, 2, 1, 1)


        self.gridLayout_4.addLayout(self.selectionLayout, 0, 0, 1, 1)

        self.AreaTab.addTab(self.Areatab, "")

        self.gridLayout_3.addWidget(self.AreaTab, 3, 10, 1, 1)

        self.brushSizeButton = QPushButton(self.centralwidget)
        self.brushSizeButton.setObjectName(u"brushSizeButton")
        self.brushSizeButton.setMaximumSize(QSize(51, 51))

        self.gridLayout_3.addWidget(self.brushSizeButton, 0, 20, 1, 1)

        self.folderButton = QPushButton(self.centralwidget)
        self.folderButton.setObjectName(u"folderButton")
        self.folderButton.setMaximumSize(QSize(91, 51))

        self.gridLayout_3.addWidget(self.folderButton, 0, 18, 1, 1)

        self.UndoTab = QTabWidget(self.centralwidget)
        self.UndoTab.setObjectName(u"UndoTab")
        self.UndoTab.setMinimumSize(QSize(150, 0))
        self.UndoTab.setMaximumSize(QSize(150, 100))
        self.UndoTab.setStyleSheet(u"QTabBar::tab { height: 50px; font-size: 11px; width: 138px; }")
        self.UndoTab_2 = QWidget()
        self.UndoTab_2.setObjectName(u"UndoTab_2")
        self.gridLayout_2 = QGridLayout(self.UndoTab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.undoButton = QPushButton(self.UndoTab_2)
        self.undoButton.setObjectName(u"undoButton")
        self.undoButton.setMaximumSize(QSize(71, 51))

        self.horizontalLayout_3.addWidget(self.undoButton)

        self.redoButton = QPushButton(self.UndoTab_2)
        self.redoButton.setObjectName(u"redoButton")
        self.redoButton.setMaximumSize(QSize(81, 51))

        self.horizontalLayout_3.addWidget(self.redoButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.UndoTab.addTab(self.UndoTab_2, "")

        self.gridLayout_3.addWidget(self.UndoTab, 1, 10, 1, 1, Qt.AlignTop)

        self.brushcolorButton = QPushButton(self.centralwidget)
        self.brushcolorButton.setObjectName(u"brushcolorButton")
        self.brushcolorButton.setMinimumSize(QSize(50, 0))
        self.brushcolorButton.setMaximumSize(QSize(51, 51))

        self.gridLayout_3.addWidget(self.brushcolorButton, 0, 22, 1, 1)

        self.infoButton = QPushButton(self.centralwidget)
        self.infoButton.setObjectName(u"infoButton")
        self.infoButton.setEnabled(False)
        self.infoButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.infoButton, 0, 24, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(150, 16777215))
        self.tabWidget.setStyleSheet(u"QTabBar::tab { height: 50px;  font-size: 11px; width: 100px; }")
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

        self.removeButton = QPushButton(self.verticalLayoutWidget_2)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setEnabled(False)
        self.removeButton.setMinimumSize(QSize(0, 51))
        self.removeButton.setMaximumSize(QSize(147, 16777215))
        self.removeButton.setCheckable(True)

        self.toolLayout.addWidget(self.removeButton)

        self.liquifyButton = QPushButton(self.verticalLayoutWidget_2)
        self.liquifyButton.setObjectName(u"liquifyButton")
        self.liquifyButton.setEnabled(False)
        self.liquifyButton.setMinimumSize(QSize(0, 51))
        self.liquifyButton.setMaximumSize(QSize(147, 16777215))
        self.liquifyButton.setCheckable(True)

        self.toolLayout.addWidget(self.liquifyButton)

        self.blurButton = QPushButton(self.verticalLayoutWidget_2)
        self.blurButton.setObjectName(u"blurButton")
        self.blurButton.setEnabled(False)
        self.blurButton.setMinimumSize(QSize(0, 51))
        self.blurButton.setMaximumSize(QSize(147, 16777215))
        self.blurButton.setCheckable(True)

        self.toolLayout.addWidget(self.blurButton)

        self.tabWidget.addTab(self.tooltab, "")

        self.gridLayout_3.addWidget(self.tabWidget, 1, 4, 5, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.panButton = QPushButton(self.centralwidget)
        self.panButton.setObjectName(u"panButton")
        self.panButton.setEnabled(False)
        self.panButton.setMaximumSize(QSize(71, 51))
        icon5 = QIcon()
        icon5.addFile(u"resources/panningicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.panButton.setIcon(icon5)
        self.panButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.panButton)

        self.zoomButton = QPushButton(self.centralwidget)
        self.zoomButton.setObjectName(u"zoomButton")
        self.zoomButton.setEnabled(False)
        self.zoomButton.setMaximumSize(QSize(71, 51))
        icon6 = QIcon()
        icon6.addFile(u"resources/zoom icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomButton.setIcon(icon6)
        self.zoomButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.zoomButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 4, 1, 1)

        self.fileopenButton = QPushButton(self.centralwidget)
        self.fileopenButton.setObjectName(u"fileopenButton")
        self.fileopenButton.setMaximumSize(QSize(81, 51))
        self.fileopenButton.setTabletTracking(False)

        self.gridLayout_3.addWidget(self.fileopenButton, 0, 26, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.zoomBar = QScrollBar(self.centralwidget)
        self.zoomBar.setObjectName(u"zoomBar")
        self.zoomBar.setEnabled(False)
        self.zoomBar.setMinimumSize(QSize(300, 41))
        self.zoomBar.setMaximumSize(QSize(300, 41))
        self.zoomBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.zoomBar)

        self.zoomdisplaylabel = QLabel(self.centralwidget)
        self.zoomdisplaylabel.setObjectName(u"zoomdisplaylabel")
        self.zoomdisplaylabel.setEnabled(False)

        self.horizontalLayout.addWidget(self.zoomdisplaylabel)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 12, 1, 1)

        self.noteButton = QPushButton(self.centralwidget)
        self.noteButton.setObjectName(u"noteButton")
        self.noteButton.setMaximumSize(QSize(81, 51))

        self.gridLayout_3.addWidget(self.noteButton, 0, 23, 1, 1)

        self.brushsizelabel = QLabel(self.centralwidget)
        self.brushsizelabel.setObjectName(u"brushsizelabel")
        self.brushsizelabel.setMaximumSize(QSize(51, 16777215))
        self.brushsizelabel.setWordWrap(True)

        self.gridLayout_3.addWidget(self.brushsizelabel, 0, 19, 1, 1)

        self.LabelTab = QTabWidget(self.centralwidget)
        self.LabelTab.setObjectName(u"LabelTab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LabelTab.sizePolicy().hasHeightForWidth())
        self.LabelTab.setSizePolicy(sizePolicy1)
        self.LabelTab.setMinimumSize(QSize(150, 0))
        self.LabelTab.setMaximumSize(QSize(150, 16777215))
        self.LabelTab.setStyleSheet(u"QTabBar::tab { height: 50px; font-size: 11px; width: 138px; }")
        self.icontab = QWidget()
        self.icontab.setObjectName(u"icontab")
        self.gridLayout = QGridLayout(self.icontab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.iconLayout = QGridLayout()
        self.iconLayout.setObjectName(u"iconLayout")

        self.gridLayout.addLayout(self.iconLayout, 0, 0, 1, 1)

        self.LabelTab.addTab(self.icontab, "")

        self.gridLayout_3.addWidget(self.LabelTab, 4, 10, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 17))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.AreaTab.setCurrentIndex(0)
        self.UndoTab.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.LabelTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SmartMonitor", None))
        self.resetZoomButton.setText(QCoreApplication.translate("MainWindow", u"Reset zoom", None))
        self.brushcolorlabel.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.filesaveButton.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.rectButton.setText("")
        self.cirButton.setText("")
        self.arrowButton.setText("")
        self.brushButton.setText("")
        self.labelButton.setText("")
        self.AreaTab.setTabText(self.AreaTab.indexOf(self.Areatab), QCoreApplication.translate("MainWindow", u"Area Selection", None))
        self.brushSizeButton.setText("")
        self.folderButton.setText(QCoreApplication.translate("MainWindow", u"Change\n"
" camera folder", None))
        self.undoButton.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.redoButton.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.UndoTab.setTabText(self.UndoTab.indexOf(self.UndoTab_2), QCoreApplication.translate("MainWindow", u"Undo/Redo", None))
        self.brushcolorButton.setText("")
        self.infoButton.setText(QCoreApplication.translate("MainWindow", u"Image\n"
"Info", None))
        self.burnButton.setText(QCoreApplication.translate("MainWindow", u"Brighten", None))
        self.dodgeButton.setText(QCoreApplication.translate("MainWindow", u"Darken", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.liquifyButton.setText(QCoreApplication.translate("MainWindow", u"Liquify", None))
        self.blurButton.setText(QCoreApplication.translate("MainWindow", u"Blur", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tooltab), QCoreApplication.translate("MainWindow", u"Action", None))
        self.panButton.setText("")
        self.zoomButton.setText("")
        self.fileopenButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.zoomdisplaylabel.setText(QCoreApplication.translate("MainWindow", u"zoom:", None))
        self.noteButton.setText(QCoreApplication.translate("MainWindow", u"Exif\n"
"Comments", None))
        self.brushsizelabel.setText(QCoreApplication.translate("MainWindow", u"Brush Size:", None))
        self.LabelTab.setTabText(self.LabelTab.indexOf(self.icontab), QCoreApplication.translate("MainWindow", u"Annotation Labels", None))
    # retranslateUi

