from PySide2 import QtWidgets, QtCore, QtGui

class DragDropImageLabel(QtWidgets.QLabel):

    def __init__(self, press_callback_function, move_callback_function, release_callback_function):
        QtWidgets.QLabel.__init__(self)

class DragDropTextLabel(QtWidgets.QLabel):

    def __init__(self, press_callback_function, move_callback_function, release_callback_function):
        QtWidgets.QLabel.__init__(self)