from PySide2 import QtWidgets


class ImageDisplay(QtWidgets.QLabel):
    def __init__(self, press_callback_function, move_callback_function, release_callback_function):
        QtWidgets.QLabel.__init__(self)
        self.mouse_down = False
        self.press_callback_function = press_callback_function
        self.move_callback_function = move_callback_function
        self.release_callback_function = release_callback_function

    def mousePressEvent(self, QMouseEvent):
        self.mouse_down = True
        self.press_callback_function(QMouseEvent)

    def mouseMoveEvent(self, QMouseEvent):
        if self.mouse_down:
            self.move_callback_function(QMouseEvent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.mouse_down = False
        self.release_callback_function(QMouseEvent)
