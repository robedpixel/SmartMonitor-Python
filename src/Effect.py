from PySide2 import QtCore


class Effect:
    def __init__(self, pos: QtCore.QPoint):
        self.pos = pos

class LabelEffect(Effect):

    def __init__(self, pos: QtCore.QPoint, label: str):
        super(LabelEffect, self).__init__(pos)
        self.label = label
