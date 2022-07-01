from Tool import Tool
from Effect import Effect, EffectType
from PyQt5 import QtGui
from collections import deque

class PaintTool(Tool):

    def __init__(self):
        Tool.__init__()
        self.push_button = None
        self.image = None

    def set_image(self, image: QtGui.QImage):
        self.image = image

    def set_button(self, QPushButton):
        self.push_button = QPushButton

    def on_deselect_tool(self):
        self.push_button.setChecked(False)

    def draw(self, x_pos: int, y_pos: int, effects: deque):
        deque.append(EffectType.RGB, self, x_pos, y_pos)
        # SET PIXEL AT COORDINATES TO BLACK
