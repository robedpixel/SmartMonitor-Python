# Import required packages
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtGui import QImageReader

import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('mainwindow.ui', self)  # Load the .ui file

        self.scale_factor = float(1.0)
        self.file_open_button = self.findChild(QtWidgets.QPushButton, 'fileopenButton')
        self.scroll_area = self.findChild(QtWidgets.QScrollArea, 'scrollArea')

        self.display = QtWidgets.QLabel()
        self.original_image = QtGui.QImage()

        self.scroll_area.setWidget(self.display)

        self.file_open_button.clicked.connect(self.on_file_open_button_clicked)

        self.show()  # Show the GUI

    def load_image(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Image', '/', "Image Files (*.png *.jpg *.bmp *.nef)")
        self.load_image_from_file(filename[0])

    def load_image_from_file(self, filename: str) -> bool:
        reader = QImageReader()
        reader.setFileName(filename)
        reader.setAutoTransform(True)
        new_image = reader.read()
        if new_image.isNull():
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle(QtGui.QGuiApplication.applicationDisplayName())
            msg_box.setText("Cannot load " + QtCore.QDir.fromNativeSeparators(filename) + ": " + reader.errorString())
            msg_box.exec()
            return False
        self.set_image(new_image)
        QtWidgets.QWidget.setWindowFilePath(self,filename)
        return True

    def set_image(self, new_image: QtGui.QImage):
        self.original_image = new_image
        if self.original_image.colorSpace().isValid():
            self.original_image.convertToColorSpace(QtGui.QColorSpace.SRgb)
        self.display.setPixmap(QtGui.QPixmap.fromImage(self.original_image))
        self.scale_factor = 1.0

        self.scroll_area.setVisible(True)
        self.display.adjustSize()

    def on_file_open_button_clicked(self):
        self.load_image()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
