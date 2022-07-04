# Import required packages
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtGui import QImageReader
from collections import deque
import sys
from ImageDisplay import ImageDisplay
from Tool import PaintTool, MoveTool
from Action import Action


def set_button_color(color: QtGui.QColor, button: QtWidgets.QPushButton):
    if color.isValid():
        qss = "background-color: " + (color.name())
        button.setStyleSheet(qss)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('mainwindow.ui', self)  # Load the .ui file

        self.scale_factor = float(1.0)

        self.file_open_button = self.findChild(QtWidgets.QPushButton, 'fileopenButton')
        self.file_open_button.clicked.connect(self.on_file_open_button_clicked)

        self.scroll_area = self.findChild(QtWidgets.QScrollArea, 'scrollArea')
        self.display = ImageDisplay(self.on_image_display_clicked, self.on_image_display_move,
                                    self.on_image_display_release)
        self.display.setMouseTracking(True)
        self.original_image = QtGui.QImage()
        self.current_image = QtGui.QImage()
        self.scroll_area.setWidget(self.display)

        # Initialise buttons
        self.brush_button = self.findChild(QtWidgets.QPushButton, 'brushButton')
        self.brush_button.setStyleSheet(
            "QPushButton{background-color:grey;}QPushButton:checked{background-color:cyan;}")
        self.brush_button.clicked.connect(self.on_brush_button_clicked)

        self.move_button = self.findChild(QtWidgets.QPushButton, 'moveButton')
        self.move_button.setStyleSheet(
            "QPushButton{background-color:grey;}QPushButton:checked{background-color:cyan;}")

        self.move_button.clicked.connect(self.on_move_button_clicked)

        self.brush_color_button = self.findChild(QtWidgets.QWidget, 'brushcolorButton')
        self.brush_color_button.clicked.connect(self.on_brush_color_button_clicked)
        self.current_brush_color = [QtGui.QColor(QtCore.Qt.black)]
        set_button_color(self.current_brush_color[0], self.brush_color_button)
        self.brush_color_button.update()

        self.button_list = deque()
        self.button_list.append(self.brush_button)
        self.button_list.append(self.move_button)

        self.selected_tool = None
        self.selected_button = None

        # This is a deque of Actions
        self.actions = deque()
        self.current_action = None

        self.show()  # Show the GUI

    def load_image(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Image', '/', "Image Files (*.png *.jpg *.bmp "
                                                                                  "*.nef)")
        if filename[0]:
            self.load_image_from_file(filename[0])

    def load_image_from_file(self, filename: str) -> bool:
        reader = QImageReader()
        reader.setFileName(filename)
        reader.setAutoTransform(True)
        new_image = reader.read()
        if new_image.isNull():
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle(QtGui.QGuiApplication.applicationDisplayName())
            msg_box.setText("Cannot load " + QtCore.QDir.fromNativeSeparators(filename) + ": " + reader.errorString())
            msg_box.exec()
            return False
        self.original_image = new_image
        if self.original_image.colorSpace().isValid():
            self.original_image.convertToColorSpace(QtGui.QColorSpace(QtGui.QColorSpace.SRgb))
        self.set_image(new_image)
        QtWidgets.QWidget.setWindowFilePath(self, filename)
        return True

    def set_image(self, new_image: QtGui.QImage):
        self.current_image = new_image
        if self.current_image.colorSpace().isValid():
            self.current_image.convertToColorSpace(QtGui.QColorSpace(QtGui.QColorSpace.SRgb))
        self.display.setPixmap(QtGui.QPixmap.fromImage(self.current_image))
        self.scale_factor = 1.0

        self.scroll_area.setVisible(True)
        self.display.adjustSize()
        for button in self.button_list:
            button.setEnabled(True)

    def update_image(self):

        self.display.setPixmap(QtGui.QPixmap.fromImage(self.current_image))
        self.scale_factor = 1.0

        self.scroll_area.setVisible(True)
        self.display.adjustSize()

    def on_image_display_clicked(self, QMouseEvent):
        if self.selected_tool:
            self.selected_tool.on_click(QMouseEvent.pos(), None)
            self.update_image()

    def on_image_display_move(self, QMouseEvent):
        if self.selected_tool:
            self.selected_tool.on_drag(QMouseEvent.pos(), None)
            self.update_image()

    def on_image_display_release(self, QMouseEvent):
        if self.selected_tool:
            self.selected_tool.on_release(QMouseEvent.pos(), None)
            self.update_image()

    def on_file_open_button_clicked(self):
        self.load_image()

    def on_tool_select(self, new_tool):
        if self.selected_tool:
            self.selected_tool.on_deselect_tool()
        self.selected_tool = new_tool
        self.selected_tool.on_select_tool()

    def on_brush_button_clicked(self):
        if self.brush_button.isEnabled():
            if self.selected_button == self.brush_button:
                self.selected_tool = None
                self.selected_button = None
            else:
                new_tool = PaintTool()
                new_tool.set_button(self.brush_button)
                new_tool.set_image(self.current_image)
                new_tool.set_color(self.current_brush_color)
                self.on_tool_select(new_tool)
                self.selected_button = self.brush_button

    def on_move_button_clicked(self):
        if self.brush_button.isEnabled():
            if self.selected_button == self.move_button:
                self.selected_tool = None
                self.selected_button = None
            else:
                new_tool = MoveTool()
                new_tool.set_button(self.move_button)
                new_tool.set_image(self.current_image)
                new_tool.set_scroll_area(self.scroll_area)
                self.on_tool_select(new_tool)
                self.selected_button = self.move_button

    def on_brush_color_button_clicked(self):
        self.current_brush_color[0] = QtWidgets.QColorDialog.getColor()
        set_button_color(self.current_brush_color[0], self.brush_color_button)
        self.brush_color_button.update()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
