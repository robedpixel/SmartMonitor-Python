from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import Qt
from ui_notewindow import Ui_MainWindow
from NoteButton import NoteButton
import subprocess


def show_virtual_keyboard():
    try:
        subprocess.Popen(["matchbox-keyboard"])
    except FileNotFoundError:
        print("no virtual keyboard found")


class NoteWindow(QtWidgets.QMainWindow):
    def __init__(self, notes: [str]):
        super(NoteWindow, self).__init__()  # Call the inherited classes __init__ method
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Comments")
        self.notes = notes
        self.selected_note = list()
        self.selected_button = list()
        self.buttons = list()
        self.add_button = self.findChild(QtWidgets.QPushButton, 'addNoteButton')
        self.add_button.clicked.connect(self.on_add_note_button_clicked)
        self.remove_button = self.findChild(QtWidgets.QPushButton, 'removeNoteButton')
        self.remove_button.clicked.connect(self.on_remove_note_button_clicked)
        self.keyboard_button = self.findChild(QtWidgets.QPushButton, 'keyboardButton')
        self.keyboard_button.clicked.connect(self.on_keyboard_button_clicked)
        self.text_edit = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEdit')
        self.note_layout = self.findChild(QtWidgets.QVBoxLayout, 'noteLayout')
        self.note_layout.setAlignment(Qt.AlignTop)
        if self.notes:
            for row in self.notes:
                button = NoteButton()
                button.setText(row)
                button.setCheckable(True)
                button.set_button(self.selected_button)
                button.set_note(self.selected_note)
                self.buttons.append(button)
                self.note_layout.insertWidget(0, button)
            self.notes.reverse()

    def on_add_note_button_clicked(self):
        text = self.text_edit.toPlainText()
        if text:
            self.notes.append(text)
            button = NoteButton()
            button.setText(text)
            button.setCheckable(True)
            button.set_button(self.selected_button)
            button.set_note(self.selected_note)
            self.buttons.append(button)
            self.note_layout.insertWidget(0,button)

    def on_remove_note_button_clicked(self):
        if self.selected_note:
            self.note_layout.removeWidget(self.selected_button[0])
            self.notes.remove(self.selected_note[0])
            self.buttons.remove(self.selected_button[0])
            self.selected_button[0].deleteLater()
            self.selected_note = None
            self.selected_button = None

    def on_keyboard_button_clicked(self):
        show_virtual_keyboard()


