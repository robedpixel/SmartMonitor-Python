from PySide2 import QtWidgets


class NoteButton(QtWidgets.QPushButton):

    def __init__(self):
        super(NoteButton, self).__init__()
        self.note = None
        self.button = None
        self.clicked.connect(self.on_clicked)

    def set_note(self, note: [str]):
        self.note = note

    def set_button(self, button: [QtWidgets.QPushButton]):
        self.button = button

    def on_clicked(self):

        if self.button:
            self.button[0].setChecked(False)
            self.note[0] = self.text()
            self.button[0] = self
        else:
            self.note.append(self.text())
            self.button.append(self)
