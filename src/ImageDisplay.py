from PySide2 import QtWidgets, QtCore, QtGui


class ImageDisplay(QtWidgets.QLabel):
    def __init__(self, press_callback_function, move_callback_function, release_callback_function,
                 update_image_callback_function, scale_factor, scroll_area):
        QtWidgets.QLabel.__init__(self)
        self.mouse_down = False
        self.activated = False
        self.press_callback_function = press_callback_function
        self.move_callback_function = move_callback_function
        self.release_callback_function = release_callback_function
        self.update_func = update_image_callback_function
        self.grabGesture(QtCore.Qt.GestureType.PinchGesture)
        self.grabGesture(QtCore.Qt.GestureType.PanGesture)
        self.scale_factor = scale_factor
        self.lastScale = self.scale_factor[0]
        self.scroll_area = scroll_area
        self.pan_point = QtCore.QPointF()

    def mousePressEvent(self, QMouseEvent):
        self.mouse_down = True
        self.press_callback_function(QMouseEvent)

    def mouseMoveEvent(self, QMouseEvent):
        if self.mouse_down:
            self.move_callback_function(QMouseEvent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.mouse_down = False
        self.release_callback_function(QMouseEvent)

    def event(self, e):
        if e.type() == QtCore.QEvent.Type.Gesture:
            return self.gesture_event(e)
        return super(ImageDisplay, self).event(e)

    def gesture_event(self, e):
        pan = e.gesture(QtCore.Qt.GestureType.PanGesture)
        pinch = e.gesture(QtCore.Qt.GestureType.PinchGesture)
        if pinch:
            self.pinch_triggered(pinch)
        if pan:
            self.pan_triggered(pan)
        self.update_func()
        e.accept()
        return True

    def pinch_triggered(self, gesture):
        if gesture.state() == QtCore.Qt.GestureState.GestureStarted:
            self.activated = True
            self.lastScale = self.scale_factor[0]
        elif gesture.state() == QtCore.Qt.GestureState.GestureUpdated:
            if self.activated:
                self.scale_factor[0] = self.scale_factor[0] * ((1 + gesture.scaleFactor())/2)
                if self.scale_factor[0] > 4.0:
                    self.scale_factor[0] = 4.0
                if self.scale_factor[0] < 0.25:
                    self.scale_factor[0] = 0.25
        elif gesture.state() == QtCore.Qt.GestureState.GestureFinished:
            self.activated = False
        else:
            pass

    def pan_triggered(self, gesture):
        if gesture.state() == QtCore.Qt.GestureState.GestureStarted:
            self.activated = True
            self.pan_point.setX(0)
            self.pan_point.setY(0)
        elif gesture.state() == QtCore.Qt.GestureState.GestureUpdated:
            if self.activated:
                self.pan_point = self.pan_point - gesture.delta()
                self.scroll_area.horizontalScrollBar().setValue(
                    self.scroll_area.horizontalScrollBar().value() + (self.pan_point.toPoint().x()))
                self.scroll_area.verticalScrollBar().setValue(
                    self.scroll_area.verticalScrollBar().value() + (self.pan_point.toPoint().y()))
        elif gesture.state() == QtCore.Qt.GestureState.GestureFinished:
            self.activated = False
        else:
            pass
