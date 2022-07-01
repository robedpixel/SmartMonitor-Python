from enum import Enum
from Tool import Tool


class EffectType(Enum):
    RGB = 0


class Effect:
    def __init__(self, paint_tool: Tool, paint_effect_type: EffectType, x_pos: int, y_pos: int):
        self.paint_tool = paint_tool
        self.paint_effect_type = paint_effect_type
        self.x_pos = x_pos
        self.y_pos = y_pos

    def get_paint_effect_type(self) -> int:
        return self.paint_effect_type
