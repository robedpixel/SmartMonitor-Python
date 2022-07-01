from PyQt5 import QtWidgets


class ImageDisplay(QtWidgets.QLabel):
    def __init__(self):
        QtWidgets.QLabel.__init__(self)

    def mousePressEvent(self, QMouseEvent):
        print("click detected")
