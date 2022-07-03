from PyQt5 import QtCore, QtGui, QtWidgets
from collections import deque
from Effect import EffectType


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

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        raise NotImplementedError()

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        raise NotImplementedError()

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        raise NotImplementedError()

    def apply_effect(self, effects: deque, effect_type: EffectType):
        raise NotImplementedError()

    def get_effect_type(self):
        raise NotImplementedError()


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

    def on_click(self, pos: QtCore.QPoint, effects: deque):
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

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        if self.drawing:
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 20,
                                      QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            painter.drawLine(self.lastPoint, pos)
            self.lastPoint = pos

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = False

    def apply_effect(self, effects: deque, effect_type: EffectType):
        pass

    def get_effect_type(self):
        return EffectType.RGB


class MoveTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.push_button = None
        self.image = None
        self.activated = False
        self.lastPoint = QtCore.QPoint()
        self.scroll_area = None
        self.horizontal_scroll_bar = None
        self.vertical_scroll_bar = None

    def set_scroll_area(self, area: QtWidgets.QScrollArea):
        self.scroll_area = area
        self.horizontal_scroll_bar = self.scroll_area.horizontalScrollBar()
        self.vertical_scroll_bar = self.scroll_area.verticalScrollBar()

    def set_image(self, image: QtGui.QImage):
        self.image = image

    def set_button(self, QPushButton):
        self.push_button = QPushButton

    def on_deselect_tool(self):
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        self.activated = True
        self.lastPoint = pos

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        if self.activated:
            self.horizontal_scroll_bar.setValue(self.horizontal_scroll_bar.value()+(self.lastPoint.x() - pos.x()))
            self.vertical_scroll_bar.setValue(self.vertical_scroll_bar.value()+(self.lastPoint.y() - pos.y()))

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        self.activated = False

    def apply_effect(self, effects: deque, effect_type: EffectType):
        pass

    def get_effect_type(self):
        return EffectType.NONE
