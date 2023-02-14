from PySide2 import QtCore
from collections import deque
from Effect import Effect
from enum import Enum


class EffectType(Enum):
    NONE = 0
    RGB = 1
    CROP = 2
    IMAGE = 3
    LABEL = 4

class ToolType(Enum):
    PAINT = 0
    ERASER = 1
    ARROW = 2
    LINE = 3
    RECT = 4
    CIRCLE = 5
    IMAGE = 6
    LABEL = 7

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
