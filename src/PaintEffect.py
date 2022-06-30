from enum import Enum


class PaintEffectType(Enum):
    RGB = 0


class PaintEffect:
    def __init__(self):
        self.paint_tool = None
        self.paint_effect_type = int()
        self.x_pos = int()
        self.y_pos = int()

    def get_paint_effect_type(self) -> int:
        return self.paint_effect_type
