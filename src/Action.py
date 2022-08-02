from PySide2 import QtCore
from collections import deque
from Effect import Effect
from enum import Enum


class EffectType(Enum):
    NONE = 0
    RGB = 1
    ERASER = 2
    CROP = 3


class Action:
    def __init__(self, tool, effect, effect_type: EffectType):
        self.tool = tool
        self.effects = effect
        self.effect_type = effect_type

    def get_tool(self):
        return self.tool

    # Returns a deque of Effects
    def get_effects(self) -> deque:
        return self.effects


class PaintAction(Action):

    def __init__(self, tool, effect, effect_type: EffectType, radius, color):
        Action.__init__(self, tool, effect, effect_type)
        self.radius = radius
        self.color = color
