from enum import Enum
from PyQt5 import QtCore


class EffectType(Enum):
    RGB = 0


class Effect:
    def __init__(self, pos: QtCore.QPoint):
        self.pos = pos
