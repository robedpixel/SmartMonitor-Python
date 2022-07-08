from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import Qt
from ui_notewindow import Ui_MainWindow
from collections import deque


class NoteWindow(QtWidgets.QMainWindow):
    def __init__(self, notes):
        super(NoteWindow, self).__init__()  # Call the inherited classes __init__ method
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = notes
        self.selected_note = None
        self.buttons = list()
        self.note_layout = self.findChild(QtWidgets.QVBoxLayout, 'noteLayout')
        self.note_layout.setAlignment(Qt.AlignTop)
        if self.notes:
            for row in self.notes.reverse():
                button = QtWidgets.QPushButton()
                button.setText(row)
                self.buttons.append(button)
                self.note_layout.addWidget(button)

    def on_add_note_button_clicked(self):
        pass

    def on_remove_note_button_clicked(self):
        pass

