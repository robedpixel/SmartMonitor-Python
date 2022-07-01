from PyQt5 import QtCore
from collections import deque
from PyQt5 import QtCore


class Tool:
    def __init__(self):
        self.height = 0
        self.width = 0

    def set_image(self):
        pass

    def on_select_tool(self):
        pass

    def on_deselect_tool(self):
        pass

    def set_canvas_size(self, height: int, width: int):
        self.height = height
        self.width = width

    def draw(self, x_pos: int, y_pos: int, effects: deque):
        raise NotImplementedError()

    def apply_effect(self, effects: deque):
        raise NotImplementedError()
