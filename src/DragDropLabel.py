from PySide2 import QtWidgets, QtCore, QtGui


class DragDropImageLabel(QtWidgets.QLabel):

    def __init__(self, press_callback_function, move_callback_function, release_callback_function):
        QtWidgets.QLabel.__init__(self)


class DragDropTextLabel(QtWidgets.QLabel):

    def __init__(self):
        QtWidgets.QLabel.__init__(self)
        self.drag_start_position = None
        self.image = None

    def update_image(self, image):
        self.image = image
        self.setPixmap(QtGui.QPixmap.fromImage(image))

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
        mimedata.setText(self.text())

        drag.setMimeData(mimedata)
        drag.setPixmap(QtGui.QPixmap.fromImage(self.image))
        drag.setHotSpot(event.pos())
        drag.exec_(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction)
