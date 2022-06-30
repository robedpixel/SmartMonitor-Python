from PyQt5 import QtCore
from collections import deque


class PaintTool:
    def __init__(self):
        self.canvas_size = QtCore.QSize()

    def set_canvas_size(self, size: QtCore.Qsize):
        self.canvas_size = size

    def draw(self, image_location, effects: deque):
        raise NotImplementedError()

    def apply_effect(self, effects: deque):
        raise NotImplementedError()
