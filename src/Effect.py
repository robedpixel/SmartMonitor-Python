from enum import Enum
from PySide2 import QtCore


class EffectType(Enum):
    NONE = 0
    RGB = 1


class Effect:
    def __init__(self, pos: QtCore.QPoint):
        self.pos = pos
