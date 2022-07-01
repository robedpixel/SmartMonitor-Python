from Tool import Tool
from Effect import Effect, EffectType
from PyQt5 import QtGui
from collections import deque

class PaintTool(Tool):

    def __init__(self):
        Tool.__init__()
        self.push_button = None
        self.image = None
        self.paint_radius = 5

    def set_image(self, image: QtGui.QImage):
        self.image = image

    def set_button(self, QPushButton):
        self.push_button = QPushButton

    def on_deselect_tool(self):
        self.push_button.setChecked(False)

    def draw(self, x_pos: int, y_pos: int, effects: deque):
        deque.append(EffectType.RGB, self, x_pos, y_pos)
        # SET PIXEL AT COORDINATES TO BLACK
        start_x_pos = x_pos -2
        start_y_pos = y_pos -2
        if x_pos-2 <0:
            start_x_pos = 0
        if y_pos-2<0:
            start_y_pos = 0
        for x in range(start_x_pos,start_x_pos+5):
            for y in range(start_y_pos,start_y_pos+5):
                if y>self.image.height():
                    break
                else:
                    #self.image.setPixel()