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
        self.help_text = None
        self.help_str = ""

    def set_image(self, image: [QtGui.QImage]):
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

    def apply_effect(self, action, image: [QtGui.QImage]):
        raise NotImplementedError()

    def get_effect_type(self):
        raise NotImplementedError()

    def set_help_text(self, help_text):
        self.help_text = help_text
        self.help_text.setPlainText(self.help_str)


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
        self.help_str = "Brush:\nTap and drag to draw on the canvas"

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
        self.help_text.clear()
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = True
        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.lastPoint = new_pos
        self.current_effect = []
        self.current_effect.append(Effect(new_pos))
        painter = QtGui.QPainter(self.image[0])
        painter.setPen(QtGui.QPen(self.color[0], int(self.paint_sizes[self.paint_radius[0]]),
                                  QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        painter.drawPoint(self.lastPoint)

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

    def apply_effect(self, action, image: [QtGui.QImage]):
        first = True
        painter = QtGui.QPainter(image[0])
        last_point = QtCore.QPoint()
        painter.setPen(QtGui.QPen(action.color, action.radius,
                                  QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        for effect in action.effects:
            if first:
                last_point = effect.pos
                first = False
            else:
                painter.drawLine(last_point, effect.pos)
                last_point = effect.pos

    def get_effect_type(self):
        return EffectType.RGB


class PanTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.push_button = None
        self.image = None
        self.activated = False
        self.lastPoint = QtCore.QPoint()
        self.scroll_area = None
        self.horizontal_scroll_bar = None
        self.vertical_scroll_bar = None
        self.help_str = "Panning:\nTap and drag on the canvas to pan the image"

    def set_scroll_area(self, area: QtWidgets.QScrollArea):
        self.scroll_area = area
        self.horizontal_scroll_bar = self.scroll_area.horizontalScrollBar()
        self.vertical_scroll_bar = self.scroll_area.verticalScrollBar()

    def set_image(self, image: [QtGui.QImage]):
        self.image = image

    def set_button(self, QPushButton):
        self.push_button = QPushButton

    def on_deselect_tool(self):
        self.help_text.clear()
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

    def apply_effect(self, action, image: [QtGui.QImage]):
        pass

    def get_effect_type(self):
        return EffectType.NONE


class ScaleTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.zoom_bar = None
        self.zoom_bar_display = None
        self.push_button = None
        self.image = None
        self.activated = False
        self.lastPoint = QtCore.QPoint()
        self.scaling = [float(1)]
        self.lastScale = self.scaling[0]
        self.help_str = "Zoom:\nTap and drag left to zoom out, Tap and drag right to zoom in.\n You can also use the " \
                        "slider to zoom in and out "

    def __init__(self, scale: list[float], zoom_bar, zoom_bar_display):
        Tool.__init__(self)
        self.zoom_bar = zoom_bar
        self.zoom_bar_display = zoom_bar_display
        self.push_button = None
        self.image = None
        self.activated = False
        self.lastPoint = QtCore.QPoint()
        self.scaling = scale
        self.lastScale = self.scaling[0]
        self.zoom_bar.setMinimum(0)
        self.zoom_bar.setMaximum(375)
        self.zoom_bar.setValue(int(100 * (self.scaling[0] - 0.25)))
        self.zoom_bar.setVisible(True)
        self.zoom_bar.setEnabled(True)
        self.zoom_bar_display.setVisible(True)
        self.zoom_bar_display.setEnabled(True)
        self.help_str = "Zoom:\nTap and drag left to zoom out, Tap and drag right to zoom in.\n You can also use the " \
                        "slider to zoom in and out "

    def set_image(self, image: [QtGui.QImage]):
        self.image = image

    def set_scale_control(self, scale: list[float]):
        self.scaling = scale

    def set_button(self, QPushButton):
        self.push_button = QPushButton

    def on_deselect_tool(self):
        self.help_text.clear()
        self.zoom_bar.setEnabled(False)
        self.zoom_bar.setVisible(False)
        self.zoom_bar_display.setEnabled(False)
        self.zoom_bar_display.setVisible(False)
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
            self.zoom_bar.setValue(int(100 * (self.scaling[0] - 0.25)))
            self.zoom_bar_display.setText("zoom: " + "{:.2f}".format(100 * self.scaling[0]) + "%")

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        self.activated = False

    def apply_effect(self, action, image: [QtGui.QImage]):
        pass

    def get_effect_type(self):
        return EffectType.NONE


class ColourPickerTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.scale = None
        self.push_button = None
        self.image = None
        self.activated = False
        self.color = None
        self.lastPoint = QtCore.QPoint()
        self.color_button = None
        self.help_str = "Color Picker:\nTap on the canvas to set the brush color to the tapped color"

    def set_color_button(self, color_button: QtWidgets.QPushButton):
        self.color_button = color_button

    def set_color_variable(self, color: list[QtGui.QColor]):
        self.color = color

    def set_scale(self, scale: list[float]):
        self.scale = scale

    def set_image(self, image: [QtGui.QImage]):
        self.image = image

    def set_button(self, push_button: QtWidgets.QPushButton):
        self.push_button = push_button

    def on_deselect_tool(self):
        self.help_text.clear()
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.color[0] = self.image[0].pixelColor(new_pos)
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
        self.help_str = "Eraser:\nTap and drag to erase the canvas"

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
        self.help_text.clear()
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = True
        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.lastPoint = new_pos
        self.current_effect = []
        self.current_effect.append(Effect(new_pos))
        painter = QtGui.QPainter(self.image[0])
        painter.setPen(QtGui.QPen(self.color, self.paint_radius,
                                  QtCore.Qt.SolidLine, QtCore.Qt.SquareCap, QtCore.Qt.BevelJoin))
        painter.drawPoint(self.lastPoint)

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

    def apply_effect(self, action, image: [QtGui.QImage]):
        first = True
        painter = QtGui.QPainter(image[0])
        last_point = QtCore.QPoint()
        painter.setPen(QtGui.QPen(QtGui.QColor(QtCore.Qt.white), self.paint_radius,
                                  QtCore.Qt.SolidLine, QtCore.Qt.SquareCap, QtCore.Qt.BevelJoin))
        for effect in action.effects:
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


class SelectTool(Tool):
    SELECT_STATE = 0
    DRAG_STATE = 1

    def __init__(self, child_buttons_list):
        Tool.__init__(self)
        self.child_buttons = child_buttons_list
        self.selection = [QtCore.QRect()]
        self.startPoint = QtCore.QPoint()
        self.push_button = None
        self.image = None
        self.drawing = False
        self.lastPoint = QtCore.QPoint()
        self.color = QtGui.QColor(QtCore.Qt.white)
        self.scale = [float(1)]
        self.current_effect = None
        self.help_str = "Selection Tool:\nTap and drag to select an Area on the Canvas\nPress the crop button to crop " \
                        "the selected area "
        for button in self.child_buttons:
            button.setVisible(True)
            button.setEnabled(True)

    def set_image(self, image: [QtGui.QImage]):
        self.image = image

    def set_scale(self, scale: list[float]):
        self.scale = scale

    def set_selection(self, selection: list[QtCore.QRect]):
        self.selection = selection

    def set_button(self, QPushButton):
        self.push_button = QPushButton

    def add_child_button(self, QPushButton):
        self.child_buttons.append(QPushButton)

    # def set_paint_radius(self, paint_sizes: dict, paint_brush_size: list):
    #    self.paint_sizes = paint_sizes
    #    self.paint_radius = paint_brush_size

    def on_deselect_tool(self):
        self.help_text.clear()
        self.selection[0].setRect(0, 0, 0, 0)
        for button in self.child_buttons:
            button.setEnabled(False)
            button.setVisible(False)
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

    def apply_effect(self, action, image: [QtGui.QImage]):
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


class CropTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.selection = [QtCore.QRect()]
        self.image = None
        self.scale = [float(1)]
        self.current_effect = None

    def set_image(self, image: [QtGui.QImage]):
        self.image = image

    def set_scale(self, scale: list[float]):
        self.scale = scale

    def set_selection(self, selection: list[QtCore.QRect]):
        self.selection = selection

    def set_button(self, QPushButton):
        pass

    # def set_paint_radius(self, paint_sizes: dict, paint_brush_size: list):
    #    self.paint_sizes = paint_sizes
    #    self.paint_radius = paint_brush_size

    def on_deselect_tool(self):
        pass

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        pass

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        pass

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        pass

    def crop(self):
        if self.selection[0].isValid:
            # TODO: set cropped image as new image
            self.current_effect = list()
            self.current_effect.append(self.selection[0].topLeft().x())  # x
            self.current_effect.append(self.selection[0].topLeft().y())  # y
            self.current_effect.append(self.selection[0].width())  # width
            self.current_effect.append(self.selection[0].height())  # height

            self.image[0] = self.image[0].copy(self.selection[0])
            self.selection[0].setRect(0, 0, 0, 0)

            stop_index = len(self.action_list) - self.action_list_state[0]
            self.action_list.insert(stop_index, Action(self, self.current_effect, EffectType.CROP))
            while len(self.action_list) > stop_index + 1:
                self.action_list.pop()
            self.action_list_state[0] = 0

    def apply_effect(self, action, image: [QtGui.QImage]):
        selection = QtCore.QRect(action.effects[0], action.effects[1], action.effects[2], action.effects[3])
        image[0] = image[0].copy(selection)

    def set_action_list(self, action_list, action_list_state):
        self.action_list = action_list
        self.action_list_state = action_list_state

    def get_effect_type(self):
        return EffectType.CROP


class LineTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.push_button = None
        self.image = None
        self.paint_radius = list()
        self.paint_sizes = dict()
        self.drawing = False
        self.startPoint = QtCore.QPoint()
        self.lastPoint = QtCore.QPoint()
        self.color = QtGui.QColor(QtCore.Qt.black)
        self.scale = [float(1)]
        self.current_effect = None
        self.image_copy = None
        self.image_copy_two = None
        self.help_str = "Line Tool:\nTap and drag draw a straight line on the canvas"

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
        self.help_text.clear()
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = True
        self.image_copy = QtGui.QImage(self.image[0])
        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.startPoint = new_pos
        self.current_effect = []
        self.current_effect.append(Effect(new_pos))

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        if self.drawing:
            self.image_copy_two = QtGui.QImage(self.image_copy)
            painter = QtGui.QPainter(self.image_copy_two)
            painter.setPen(QtGui.QPen(self.color[0], int(self.paint_sizes[self.paint_radius[0]]),
                                      QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
            painter.drawLine(self.startPoint, new_pos)
            self.image[0] = self.image_copy_two

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = False

        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.current_effect.append(Effect(new_pos))

        stop_index = len(self.action_list) - self.action_list_state[0]
        self.action_list.insert(stop_index, PaintAction(self, self.current_effect, EffectType.RGB,
                                                        int(self.paint_sizes[self.paint_radius[0]]), self.color[0]))
        while len(self.action_list) > stop_index + 1:
            self.action_list.pop()
        self.action_list_state[0] = 0

    def apply_effect(self, action, image: [QtGui.QImage]):
        first = True
        painter = QtGui.QPainter(image[0])
        start_point = QtCore.QPoint()
        painter.setPen(QtGui.QPen(action.color, action.radius,
                                  QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        for effect in action.effects:
            if first:
                start_point = effect.pos
                first = False
            else:
                painter.drawLine(start_point, effect.pos)

    def get_effect_type(self):
        return EffectType.RGB


class RectTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.push_button = None
        self.image = None
        self.paint_radius = list()
        self.paint_sizes = dict()
        self.drawing = False
        self.startPoint = QtCore.QPoint()
        self.lastPoint = QtCore.QPoint()
        self.color = QtGui.QColor(QtCore.Qt.black)
        self.scale = [float(1)]
        self.current_effect = None
        self.image_copy = None
        self.image_copy_two = None
        self.help_str = "Rectangle Tool:\nTap and drag draw a rectangle on the canvas"

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
        self.help_text.clear()
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = True
        self.image_copy = QtGui.QImage(self.image[0])
        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.startPoint = new_pos
        self.current_effect = []
        self.current_effect.append(Effect(new_pos))

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        if self.drawing:
            self.image_copy_two = QtGui.QImage(self.image_copy)
            painter = QtGui.QPainter(self.image_copy_two)
            painter.setPen(QtGui.QPen(self.color[0], int(self.paint_sizes[self.paint_radius[0]]),
                                      QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
            pos1 = QtCore.QPoint(self.startPoint.x(), new_pos.y())  # Bottom left point
            pos2 = QtCore.QPoint(new_pos.x(), self.startPoint.y())  # Top right point
            painter.drawLine(self.startPoint, pos2)  # top line
            painter.drawLine(self.startPoint, pos1)  # left line
            painter.drawLine(pos2, new_pos)  # right line
            painter.drawLine(pos1, new_pos)  # bottom line
            self.image[0] = self.image_copy_two

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = False

        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.current_effect.append(Effect(new_pos))

        stop_index = len(self.action_list) - self.action_list_state[0]
        self.action_list.insert(stop_index, PaintAction(self, self.current_effect, EffectType.RGB,
                                                        int(self.paint_sizes[self.paint_radius[0]]), self.color[0]))
        while len(self.action_list) > stop_index + 1:
            self.action_list.pop()
        self.action_list_state[0] = 0

    def apply_effect(self, action, image: [QtGui.QImage]):
        first = True
        painter = QtGui.QPainter(image[0])
        start_point = QtCore.QPoint()
        painter.setPen(QtGui.QPen(action.color, action.radius,
                                  QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        for effect in action.effects:
            if first:
                start_point = effect.pos
                first = False
            else:
                pos1 = QtCore.QPoint(start_point.x(), effect.pos.y())  # Bottom left point
                pos2 = QtCore.QPoint(effect.pos.x(), start_point.y())  # Top right point
                painter.drawLine(start_point, pos2)  # top line
                painter.drawLine(start_point, pos1)  # left line
                painter.drawLine(pos2, effect.pos)  # right line
                painter.drawLine(pos1, effect.pos)  # bottom line

    def get_effect_type(self):
        return EffectType.RGB


class CircleTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.push_button = None
        self.image = None
        self.paint_radius = list()
        self.paint_sizes = dict()
        self.drawing = False
        self.startPoint = QtCore.QPoint()
        self.lastPoint = QtCore.QPoint()
        self.color = QtGui.QColor(QtCore.Qt.black)
        self.scale = [float(1)]
        self.current_effect = None
        self.image_copy = None
        self.image_copy_two = None
        self.help_str = "Ellipse Tool:\nTap and drag draw an ellipse on the canvas"

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
        self.help_text.clear()
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = True
        self.image_copy = QtGui.QImage(self.image[0])
        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.startPoint = new_pos
        self.current_effect = []
        self.current_effect.append(Effect(new_pos))

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        if self.drawing:
            self.image_copy_two = QtGui.QImage(self.image_copy)
            painter = QtGui.QPainter(self.image_copy_two)
            painter.setPen(QtGui.QPen(self.color[0], int(self.paint_sizes[self.paint_radius[0]]),
                                      QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
            rect = QtCore.QRectF(QtCore.QPointF(self.startPoint), QtCore.QPointF(new_pos))
            painter.drawArc(rect, 0, 5760)
            self.image[0] = self.image_copy_two

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = False

        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.current_effect.append(Effect(new_pos))

        stop_index = len(self.action_list) - self.action_list_state[0]
        self.action_list.insert(stop_index, PaintAction(self, self.current_effect, EffectType.RGB,
                                                        int(self.paint_sizes[self.paint_radius[0]]), self.color[0]))
        while len(self.action_list) > stop_index + 1:
            self.action_list.pop()
        self.action_list_state[0] = 0

    def apply_effect(self, action, image: [QtGui.QImage]):
        first = True
        painter = QtGui.QPainter(image[0])
        start_point = QtCore.QPoint()
        painter.setPen(QtGui.QPen(action.color, action.radius,
                                  QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        for effect in action.effects:
            if first:
                start_point = effect.pos
                first = False
            else:
                rect = QtCore.QRectF(QtCore.QPointF(start_point), QtCore.QPointF(effect.pos))
                painter.drawArc(rect, 0, 5760)

    def get_effect_type(self):
        return EffectType.RGB


class ImageTool(Tool):

    def __init__(self):
        Tool.__init__(self)
        self.push_button = None
        self.image = None
        self.drawing = False
        self.startPoint = QtCore.QPoint()
        self.lastPoint = QtCore.QPoint()
        self.scale = [float(1)]
        self.current_effect = None
        self.image_to_insert = None
        self.image_copy = None
        self.image_copy_two = None
        # self.help_str = "Ellipse Tool:\nTap and drag draw an ellipse on the canvas"

    def set_image(self, image: [QtGui.QImage]):
        self.image = image

    def set_insert_image(self, image: [QtGui.QImage]):
        self.image_to_insert = image

    def set_scale(self, scale: list[float]):
        self.scale = scale

    def set_action_list(self, action_list, action_list_state):
        self.action_list = action_list
        self.action_list_state = action_list_state

    def set_button(self, QPushButton):
        self.push_button = QPushButton

    def on_deselect_tool(self):
        self.help_text.clear()
        self.push_button.setChecked(False)

    def on_click(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = True
        self.image_copy = QtGui.QImage(self.image[0])
        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.startPoint = new_pos
        self.current_effect = []
        self.current_effect.append(Effect(new_pos))

    def on_drag(self, pos: QtCore.QPoint, effects: deque):
        if self.drawing:
            self.image_copy_two = QtGui.QImage(self.image_copy)
            painter = QtGui.QPainter(self.image_copy_two)
            new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
            rect = QtCore.QRectF(QtCore.QPointF(self.startPoint), QtCore.QPointF(new_pos))
            painter.drawImage(rect, self.image_to_insert)
            self.image[0] = self.image_copy_two

    def on_release(self, pos: QtCore.QPoint, effects: deque):
        self.drawing = False

        new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
        self.current_effect.append(Effect(new_pos))

        stop_index = len(self.action_list) - self.action_list_state[0]
        self.action_list.insert(stop_index, Action(self, self.current_effect, EffectType.IMAGE))
        while len(self.action_list) > stop_index + 1:
            self.action_list.pop()
        self.action_list_state[0] = 0

    def apply_effect(self, action, image: [QtGui.QImage]):
        first = True
        painter = QtGui.QPainter(image[0])
        start_point = QtCore.QPoint()
        for effect in action.effects:
            if first:
                start_point = effect.pos
                first = False
            else:
                rect = QtCore.QRectF(QtCore.QPointF(start_point), QtCore.QPointF(effect.pos))
                painter.drawImage(rect, self.image_to_insert)

    def get_effect_type(self):
        return EffectType.IMAGE
