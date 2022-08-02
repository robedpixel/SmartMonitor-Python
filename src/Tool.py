from PySide2 import QtCore, QtGui, QtWidgets
from collections import deque
from Effect import *
from Action import Action, PaintAction, EffectType


# TODO: use QPainter to draw a dotted line for rect selection after normal drawing functions
class Tool:
    def __init__(self):
        self.height = 0
        self.width = 0
        self.action_list = []
        self.action_list_state = []

    def set_image(self, image: [QtGui.QImage]):
        pass

    def on_select_tool(self):
        pass

    def on_deselect_tool(self):
        pass

    def set_effect(self, effect_list):
        pass

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        raise NotImplementedError()

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        raise NotImplementedError()

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        raise NotImplementedError()

    def apply_effect(self, action, image: QtGui.QImage):
        raise NotImplementedError()

    def get_effect_type(self):
        raise NotImplementedError()


class PaintTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.push_button = None
        self.image = None
        self.paint_radius = list()
        self.paint_sizes = dict()
        self.drawing = False
        self.lastPoint = QtCore.QPoint()
        self.color = QtGui.QColor(QtCore.Qt.black)
        self.scale = [float(1)]
        self.current_effect = None

    def set_image(self, image: [QtGui.QImage]):
        self.image = image

    def set_color(self, color: list[QtGui.QColor]):
        self.color = color

    def set_scale(self, scale: list[float]):
        self.scale = scale

    def set_action_list(self, action_list, action_list_state):
        self.action_list = action_list
        self.action_list_state = action_list_state

    def set_button(self, QPushButton):
        self.push_button = QPushButton

    def set_paint_radius(self, paint_sizes: dict, paint_brush_size: list):
        self.paint_sizes = paint_sizes
        self.paint_radius = paint_brush_size

    def on_deselect_tool(self):
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = True
        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.lastPoint = new_pos
        self.current_effect = []
        self.current_effect.append(Effect(new_pos))

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        if self.drawing:
            painter = QtGui.QPainter(self.image[0])
            painter.setPen(QtGui.QPen(self.color[0], int(self.paint_sizes[self.paint_radius[0]]),
                                      QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
            painter.drawLine(self.lastPoint, new_pos)
            self.lastPoint = new_pos
            self.current_effect.append(Effect(new_pos))

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = False
        stop_index = len(self.action_list) - self.action_list_state[0]
        self.action_list.insert(stop_index, PaintAction(self, self.current_effect, EffectType.RGB,
                                                        int(self.paint_sizes[self.paint_radius[0]]), self.color[0]))
        while len(self.action_list) > stop_index + 1:
            self.action_list.pop()
        self.action_list_state[0] = 0

    def apply_effect(self, action, image: QtGui.QImage):
        first = True
        painter = QtGui.QPainter(image)
        last_point = QtCore.QPoint()
        painter.setPen(QtGui.QPen(action.color, action.radius,
                                  QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        for effect in reversed(action.effects):
            if first:
                last_point = effect.pos
                first = False
            else:
                painter.drawLine(last_point, effect.pos)
                last_point = effect.pos

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

    def set_image(self, image: [QtGui.QImage]):
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
            self.horizontal_scroll_bar.setValue(self.horizontal_scroll_bar.value() + (self.lastPoint.x() - pos.x()))
            self.vertical_scroll_bar.setValue(self.vertical_scroll_bar.value() + (self.lastPoint.y() - pos.y()))

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        self.activated = False

    def apply_effect(self, action, image: QtGui.QImage):
        pass

    def get_effect_type(self):
        return EffectType.NONE


class ScaleTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.push_button = None
        self.image = None
        self.activated = False
        self.lastPoint = QtCore.QPoint()
        self.scaling = [float(1)]
        self.lastScale = self.scaling[0]

    def __init__(self, scale: list[float]):
        Tool.__init__(self)
        self.push_button = None
        self.image = None
        self.activated = False
        self.lastPoint = QtCore.QPoint()
        self.scaling = scale
        self.lastScale = self.scaling[0]

    def set_image(self, image: [QtGui.QImage]):
        self.image = image

    def set_scale_control(self, scale: list[float]):
        self.scaling = scale

    def set_button(self, QPushButton):
        self.push_button = QPushButton

    def on_deselect_tool(self):
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        self.activated = True
        self.lastPoint = pos
        self.lastScale = self.scaling[0]

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        if self.activated:
            self.scaling[0] = self.lastScale + (float(pos.x() - self.lastPoint.x()) / 100.0)
            if self.scaling[0] > 4.0:
                self.scaling[0] = 4.0
            if self.scaling[0] < 0.25:
                self.scaling[0] = 0.25

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        self.activated = False

    def apply_effect(self, action, image: QtGui.QImage):
        pass

    def get_effect_type(self):
        return EffectType.NONE


class ColourPickerTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.push_button = None
        self.image = None
        self.activated = False
        self.color = None
        self.lastPoint = QtCore.QPoint()
        self.color_button = None

    def set_color_button(self, color_button: QtWidgets.QPushButton):
        self.color_button = color_button

    def set_color_variable(self, color: list[QtGui.QColor]):
        self.color = color

    def set_image(self, image: [QtGui.QImage]):
        self.image = image

    def set_button(self, push_button: QtWidgets.QPushButton):
        self.push_button = push_button

    def on_deselect_tool(self):
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        self.color[0] = self.image[0].pixelColor(pos)
        if self.color[0].isValid():
            qss = "background-color: " + (self.color[0].name())
            self.color_button.setStyleSheet(qss)

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        pass

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        pass

    def apply_effect(self, action, image: QtGui.QImage):
        pass

    def get_effect_type(self):
        return EffectType.NONE


class EraserTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.push_button = None
        self.image = None
        self.paint_radius = 5
        # self.paint_sizes = dict()
        self.drawing = False
        self.lastPoint = QtCore.QPoint()
        self.color = QtGui.QColor(QtCore.Qt.white)
        self.scale = [float(1)]
        self.current_effect = None

    def set_image(self, image: [QtGui.QImage]):
        self.image = image

    def set_scale(self, scale: list[float]):
        self.scale = scale

    def set_button(self, QPushButton):
        self.push_button = QPushButton

    # def set_paint_radius(self, paint_sizes: dict, paint_brush_size: list):
    #    self.paint_sizes = paint_sizes
    #    self.paint_radius = paint_brush_size

    def on_deselect_tool(self):
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = True
        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.lastPoint = new_pos
        self.current_effect = []
        self.current_effect.append(Effect(new_pos))

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        if self.drawing:
            painter = QtGui.QPainter(self.image[0])
            painter.setPen(QtGui.QPen(self.color, self.paint_radius,
                                      QtCore.Qt.SolidLine, QtCore.Qt.SquareCap, QtCore.Qt.BevelJoin))
            new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
            painter.drawLine(self.lastPoint, new_pos)
            self.lastPoint = new_pos
            self.current_effect.append(Effect(new_pos))

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = False
        stop_index = len(self.action_list) - self.action_list_state[0]
        self.action_list.insert(stop_index, PaintAction(self, self.current_effect, EffectType.RGB,
                                                        self.paint_radius, self.color))
        while len(self.action_list) > stop_index + 1:
            self.action_list.pop()
        self.action_list_state[0] = 0

    def apply_effect(self, action, image: QtGui.QImage):
        first = True
        painter = QtGui.QPainter(image)
        last_point = QtCore.QPoint()
        painter.setPen(QtGui.QPen(QtGui.QColor(QtCore.Qt.white), self.paint_radius,
                                  QtCore.Qt.SolidLine, QtCore.Qt.SquareCap, QtCore.Qt.BevelJoin))
        for effect in reversed(action.effects):
            if first:
                last_point = effect.pos
                first = False
            else:
                painter.drawLine(last_point, effect.pos)
                last_point = effect.pos

    def set_action_list(self, action_list, action_list_state):
        self.action_list = action_list
        self.action_list_state = action_list_state

    def get_effect_type(self):
        return EffectType.RGB


# TODO: two states, selecting and dragging
# TODO: dragging happens when user clicks within bounds of selection
class SelectTool(Tool):
    SELECT_STATE = 0
    DRAG_STATE = 1

    def __init__(self):
        Tool.__init__(self)
        self.selection = [QtCore.QRect()]
        self.startPoint = QtCore.QPoint()
        self.push_button = None
        self.image = None
        self.drawing = False
        self.lastPoint = QtCore.QPoint()
        self.color = QtGui.QColor(QtCore.Qt.white)
        self.scale = [float(1)]
        self.current_effect = None

    def set_image(self, image: [QtGui.QImage]):
        self.image = image

    def set_scale(self, scale: list[float]):
        self.scale = scale

    def set_selection(self, selection: list[QtCore.QRect]):
        self.selection = selection

    def set_button(self, QPushButton):
        self.push_button = QPushButton

    # def set_paint_radius(self, paint_sizes: dict, paint_brush_size: list):
    #    self.paint_sizes = paint_sizes
    #    self.paint_radius = paint_brush_size

    def on_deselect_tool(self):
        self.selection[0].setCoords(0, 0, 0, 0)
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = True
        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.startPoint = new_pos
        self.lastPoint = new_pos

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        if self.drawing:
            new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
            self.lastPoint = new_pos
            self.selection[0].setTopLeft(self.startPoint)
            self.selection[0].setBottomRight(self.lastPoint)

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = False
        self.selection[0].setTopLeft(self.startPoint)
        self.selection[0].setBottomRight(self.lastPoint)

    def apply_effect(self, action, image: QtGui.QImage):
        """first = True
        painter = QtGui.QPainter(image)
        last_point = QtCore.QPoint()
        painter.setPen(QtGui.QPen(QtGui.QColor(QtCore.Qt.white), self.paint_radius,
                                  QtCore.Qt.SolidLine, QtCore.Qt.SquareCap, QtCore.Qt.BevelJoin))
        for effect in reversed(action.effects):
            if first:
                last_point = effect.pos
                first = False
            else:
                painter.drawLine(last_point, effect.pos)
                last_point = effect.pos"""

    def set_action_list(self, action_list, action_list_state):
        self.action_list = action_list
        self.action_list_state = action_list_state

    def get_effect_type(self):
        return EffectType.NONE
