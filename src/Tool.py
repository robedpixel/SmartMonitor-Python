from PyQt5 import QtCore
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

    def on_click(self, pos: QtCore.QPoint, effects : deque):
        raise NotImplementedError()

    def on_drag(self, pos: QtCore.QPoint, effects : deque):
        raise NotImplementedError()

    def on_release(self, pos: QtCore.QPoint, effects : deque):
        raise NotImplementedError()

    def apply_effect(self, effects: deque, effect_type: EffectType):
        raise NotImplementedError()

    def get_effect_type(self):
        raise NotImplementedError()

