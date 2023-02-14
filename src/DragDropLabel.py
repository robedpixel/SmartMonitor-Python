import pickle

from PySide2 import QtWidgets, QtCore, QtGui



class DragDropImageLabel(QtWidgets.QLabel):

    def __init__(self):
        QtWidgets.QLabel.__init__(self)
        self.drag_start_position = None
        self.image = None
        self.labelcolor = None
        self.labeltext = None

    def update_image(self, color, text):
        self.labelcolor = color
        self.labeltext = text
        image = self.get_qimage_from_text(color, text)
        self.image = image
        self.setPixmap(QtGui.QPixmap.fromImage(image))

    def get_qimage_from_text(self, color, text: str):
        font = QtGui.QFont()
        font.setPixelSize(24)
        font.setWeight(QtGui.QFont.ExtraBold)
        fm = QtGui.QFontMetrics(font)
        pixelsWide = fm.horizontalAdvance(text)
        pixelsHigh = fm.height()
        image = QtGui.QImage(QtCore.QSize(pixelsWide, 35), QtGui.QImage.Format_ARGB32)
        image.fill(QtGui.qRgba(0, 0, 0, 0))
        painter = QtGui.QPainter(image)
        painter.setBrush(QtGui.QBrush(color))
        painter.setPen(QtGui.QPen(color))
        painter.setFont(font)
        painter.drawText(QtCore.QRect(0, 0, pixelsWide, 35), QtCore.Qt.TextFlag.TextSingleLine, text)
        painter.end()
        return image

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_start_position = event.pos()

    # def mouseMoveEvent(self, QMouseEvent):
    #    if self.mouse_down:
    #        self.move_callback_function(QMouseEvent)

    def mouseMoveEvent(self, event):
        if not (event.buttons() & QtCore.Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QtWidgets.QApplication.startDragDistance():
            return
        mimedata = QtCore.QMimeData()
        drag = QtGui.QDrag(self)
        data = QtCore.QByteArray()
        buffer = QtCore.QBuffer(data)
        buffer.open(QtCore.QIODevice.WriteOnly)
        self.image.save(buffer,"PNG")
        buffer.close()
        mimedata.setData("PNG", data)
        mimedata.setData("color", pickle.dumps(self.labelcolor))
        mimedata.setData("text", pickle.dumps(self.labeltext))
        mimedata.setText(self.text())
        drag.setMimeData(mimedata)
        drag.setPixmap(QtGui.QPixmap.fromImage(self.image))
        drag.setHotSpot(event.pos())
        drag.exec_(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction)
