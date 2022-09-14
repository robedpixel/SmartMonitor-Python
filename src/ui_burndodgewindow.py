# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'burndodgewindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(407, 129)
        self.plus2Button = QPushButton(Dialog)
        self.plus2Button.setObjectName(u"plus2Button")
        self.plus2Button.setGeometry(QRect(260, 50, 51, 41))
        self.plus1Button = QPushButton(Dialog)
        self.plus1Button.setObjectName(u"plus1Button")
        self.plus1Button.setGeometry(QRect(190, 50, 51, 41))
        self.plus3Button = QPushButton(Dialog)
        self.plus3Button.setObjectName(u"plus3Button")
        self.plus3Button.setGeometry(QRect(330, 50, 51, 41))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 10, 121, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.plus2Button.setText(QCoreApplication.translate("Dialog", u"+2", None))
        self.plus1Button.setText(QCoreApplication.translate("Dialog", u"+1", None))
        self.plus3Button.setText(QCoreApplication.translate("Dialog", u"+3", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Dodge/Burn Amount:", None))
    # retranslateUi

