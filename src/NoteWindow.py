from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import Qt
from ui_notewindow import Ui_MainWindow


class NoteWindow(QtWidgets.QMainWindow):
    def __init__(self, notes: [str]):
        super(NoteWindow, self).__init__()  # Call the inherited classes __init__ method
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = notes
        self.selected_note = None
        self.selected_button = None
        self.buttons = list()
        self.add_button = self.findChild(QtWidgets.QPushButton, 'addNoteButton')
        self.add_button.clicked.connect(self.on_add_note_button_clicked)
        self.remove_button = self.findChild(QtWidgets.QPushButton, 'removeNoteButton')
        self.text_edit = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit')
        self.note_layout = self.findChild(QtWidgets.QVBoxLayout, 'noteLayout')
        self.note_layout.setAlignment(Qt.AlignTop)
        if self.notes:
            for row in self.notes:
                button = QtWidgets.QPushButton()
                button.setText(row)
                button.setCheckable(True)
                self.buttons.append(button)
                self.note_layout.insertWidget(0, button)
            self.notes.reverse()

    def on_add_note_button_clicked(self):
        text = self.text_edit.toPlainText()
        if text:
            self.notes.append(text)
            button = QtWidgets.QPushButton()
            button.setText(text)
            self.buttons.append(button)
            self.note_layout.addWidget(button)

    def on_remove_note_button_clicked(self):
        if self.selected_note:
            self.notes.remove(self.selected_note)
            self.buttons.remove(self.selected_button)
            self.selected_note = None
            self.selected_button = None
