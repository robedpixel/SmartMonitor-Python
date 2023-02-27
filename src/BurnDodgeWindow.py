from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import Qt
from ui_burndodgewindow import Ui_Dialog

class BurnDodgeWindow(QtWidgets.QDialog):

    def __init__(self):
        super(BurnDodgeWindow, self).__init__()  # Call the inherited classes __init__ method
        self.ui = Ui_Dialog()
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.ui.setupUi(self)
        self.string_output = ""
        self.plus_1_button = self.findChild(QtWidgets.QWidget, 'plus1Button')
        self.plus_1_button.clicked.connect(self.on_plus_1_button_clicked)
        self.plus_2_button = self.findChild(QtWidgets.QWidget, 'plus2Button')
        self.plus_2_button.clicked.connect(self.on_plus_2_button_clicked)
        self.plus_3_button = self.findChild(QtWidgets.QWidget, 'plus3Button')
        self.plus_3_button.clicked.connect(self.on_plus_3_button_clicked)
        self.minus_1_button = self.findChild(QtWidgets.QWidget, 'minus1Button')
        self.minus_1_button.clicked.connect(self.on_minus_1_button_clicked)
        self.minus_2_button = self.findChild(QtWidgets.QWidget, 'minus2Button')
        self.minus_2_button.clicked.connect(self.on_minus_2_button_clicked)
        self.minus_3_button = self.findChild(QtWidgets.QWidget, 'minus3Button')
        self.minus_3_button.clicked.connect(self.on_minus_3_button_clicked)

    def on_plus_1_button_clicked(self):
        self.string_output = "+1"
        self.accept()

    def on_plus_2_button_clicked(self):
        self.string_output = "+2"
        self.accept()

    def on_plus_3_button_clicked(self):
        self.string_output = "+3"
        self.accept()

    def on_minus_1_button_clicked(self):
        self.string_output = "-1"
        self.accept()

    def on_minus_2_button_clicked(self):
        self.string_output = "-2"
        self.accept()

    def on_minus_3_button_clicked(self):
        self.string_output = "-3"
        self.accept()