from PySide2 import QtCore
from collections import deque
from Tool import Tool
from Effect import Effect, EffectType


class Action:
    def __init__(self, tool: Tool, effect_type : EffectType):
        self.tool = tool
        self.effects = deque()
        self.effect_type = effect_type

    def get_tool(self):
        return self.tool

    # Returns a deque of Effects
    def get_effects(self) -> deque:
        return self.effects

