from PySide2 import QtWidgets, QtGui, QtCore
from ui_notewindow import Ui_MainWindow


class NoteWindow(QtWidgets.QMainWindow):
    def __init__(self, notes: [str]):
        super(NoteWindow, self).__init__()  # Call the inherited classes __init__ method
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = notes
