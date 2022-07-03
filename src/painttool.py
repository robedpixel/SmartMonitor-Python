from Tool import Tool
from Effect import Effect, EffectType
from PyQt5 import QtCore, QtGui
from collections import deque


class PaintTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.push_button = None
        self.image = None
        self.paint_radius = 5
        self.drawing = False
        self.lastPoint = QtCore.QPoint()

    def set_image(self, image: QtGui.QImage):
        self.image = image

    def set_button(self, QPushButton):
        self.push_button = QPushButton

    def on_deselect_tool(self):
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects : deque):
        self.drawing = True
        self.lastPoint = pos
        # SET PIXEL AT COORDINATES TO BLACK
        # start_x_pos = x_pos - 2
        # start_y_pos = y_pos - 2
        # if x_pos - 2 < 0:
        #    start_x_pos = 0
        # if y_pos - 2 < 0:
        #    start_y_pos = 0
        # for x in range(start_x_pos, start_x_pos + 5):
        #    for y in range(start_y_pos, start_y_pos + 5):
        #        if y > self.image.height():
        #            break
        #        else:
        #            self.image.setPixel()

    def on_drag(self, pos: QtCore.QPoint, effects : deque):
        if self.drawing:
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 20,
                             QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            painter.drawLine(self.lastPoint, pos)
            self.lastPoint = pos

    def on_release(self, pos: QtCore.QPoint, effects : deque):
        self.drawing = False

    def get_effect_type(self):
        return EffectType.RGB
