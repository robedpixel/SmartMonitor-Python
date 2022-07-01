from PyQt5 import QtCore
from collections import deque


class Tool:
    def __init__(self):
        self.canvas_size = QtCore.QSize()

    def on_select_tool(self):
        pass

    def on_deselect_tool(self):
        pass

    def set_canvas_size(self, size: QtCore.Qsize):
        self.canvas_size = size

    def draw(self, image_location, effects: deque):
        raise NotImplementedError()

    def apply_effect(self, effects: deque):
        raise NotImplementedError()
