# TODO: test airnef
# TODO: add airnef function
# TODO: find way to connect dslr and detect changes in ubuntu
# Import required packages
import io
import os
import subprocess
import sys
import time
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QImageReader
from PySide2.QtWidgets import QWidget
from collections import deque
from Action import Action
from CameraFolderWatcher import CameraFolderWatcher
from ImageDisplay import ImageDisplay
from NoteModule import ExifNoteModule, AppendedDataNoteModule
from NoteWindow import NoteWindow
from Tool import *
from ui_mainwindow import Ui_MainWindow
from os import listdir
from os.path import isfile, join
from PIL import Image, ImageQt
from pathlib import Path


# TODO: init airnef connection window first
# TODO: start airnef by commandline

# os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"


def set_button_color(color: QtGui.QColor, button: QtWidgets.QPushButton):
    if color.isValid():
        qss = "background-color: " + (color.name())
        button.setStyleSheet(qss)


# Workaround function to make qtvirtualkeyboard not black in the top portion
"""def handleVisibleChanged():
    if not QtGui.QGuiApplication.inputMethod().isVisible():
        return
    for w in QtGui.QGuiApplication.allWindows():
        if w.metaObject().className() == "QtVirtualKeyboard::InputView":
            keyboard = w.findChild(QtCore.QObject, "keyboard")
            if keyboard is not None:
                r = w.geometry()
                r.moveTop(keyboard.property("y"))
                w.setMask(QtGui.QRegion(r))
                return
"""


# Function copied form StackOverflow
def convert_image_format(imgObj, outputFormat=None):
    """Convert image format
    Args:
        imgObj (Image): the Pillow Image instance
        outputFormat (str): Image format, eg: "JPEG"/"PNG"/"BMP"/"TIFF"/...
            more refer: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
    Returns:
        bytes, binary data of Image
    Raises:
    """
    new_img_obj = imgObj
    if outputFormat and (imgObj.format != outputFormat):
        img_io = io.BytesIO()
        imgObj.save(img_io, outputFormat)
        new_img_obj = Image.open(img_io)

    return new_img_obj


def show_virtual_keyboard():
    try:
        subprocess.Popen(["matchbox-keyboard"])
    except FileNotFoundError:
        print("no virtual keyboard found")


# Extracts preview image from DSLR jpg image and returns a path to the extracted preview image
def extract_preview_image(filename: str) -> str:
    # Set what preview image to extract with exiftool
    # preview_image = "-preview:MPImage3"
    # preview_image = "-preview:PreviewImage"
    # preview_image = "-preview:ThumbnailImage"

    clear_temp_folder()
    # run exiftool to extract the image to temp file
    # run exiftool -a -b -W <path to destination file>.%s -preview:MPImage3 <path to image>
    output_path = "temp/tempimage.jpg"
    """if os.name == 'nt':
        subprocess.call(
            ["tools/windows/exiftool", "-a", "-b", "-W", output_path, preview_image, filename])
    else:
        subprocess.call(
            ["tools/linux/exiftool", "-a", "-b", "-W", output_path, preview_image, filename])
    """

    img = Image.open(filename)
    new_img = convert_image_format(img, outputFormat="MPO")
    new_img.seek(2)
    new_img.save(output_path)
    # return path to the extracted image
    return output_path


def shrink_file_size(filename: str) -> str:
    # Clear temp file
    clear_temp_folder()
    file_extension = Path(filename).suffix
    # Make shrunken image
    temp_filename = Ui.TEMP_DIRECTORY + "/tempimage" + file_extension

    if os.path.getsize(filename) > 5000000:
        img = Image.open(filename)
        exif_data = img.getexif()
        width, height = img.size
        resized_img = img.resize((width // 8, height // 8))
        resized_img.save(temp_filename, exif=exif_data)
    else:
        img = Image.open(filename)
        exif_data = img.getexif()
        width, height = img.size
        resized_img = img.resize((width // 2, height // 2))
        resized_img.save(temp_filename, exif=exif_data)

    while os.path.getsize(temp_filename) > Ui.MAX_IMAGE_VIEW_SIZE_BYTES:
        img = Image.open(temp_filename)
        exif_data = img.getexif()
        width, height = img.size
        resized_img = img.resize((width // 2, height // 2))
        resized_img.save(temp_filename, exif=exif_data)

    # Return string to new image
    return temp_filename


def clear_temp_folder():
    [f.unlink() for f in Path(Ui.TEMP_DIRECTORY).glob("*") if f.is_file()]


class Ui(QtWidgets.QMainWindow):
    AIRNEF_PICTURE_DIRECTORY = "airnefpictures"
    TEMP_DIRECTORY = "temp"
    MAX_UNDO_SIZE = 5
    MAX_IMAGE_VIEW_SIZE_BYTES = 100000

    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        # Initialise window contents form ui python script

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_AcceptTouchEvents, False)

        # Initialise variables
        self.scale_factor = [float(1)]
        self.file_notes = list()
        self.note_module = ExifNoteModule()
        self.selected_tool = None
        self.selected_button = None
        self.brush_sizes = {1: '1', 2: '3', 3: '5', 4: '7'}
        self.current_brush_size = [1]
        self.file_dialog = None
        self.selection = [QtCore.QRect()]

        self.actions = deque()
        self.current_action = [0]
        self.original_image = QtGui.QImage()
        self.current_image = [QtGui.QImage()]

        self.note_window = None

        # Initialise buttons
        self.crop_button = self.findChild(QtWidgets.QPushButton, 'cropButton')
        self.crop_button.setVisible(False)
        self.crop_button.clicked.connect(self.on_crop_button_clicked)

        self.camera_folder_button = self.findChild(QtWidgets.QPushButton, 'folderButton')
        self.camera_folder_button.clicked.connect(self.on_camera_folder_button_clicked)

        self.file_open_button = self.findChild(QtWidgets.QPushButton, 'fileopenButton')
        self.file_open_button.clicked.connect(self.on_file_open_button_clicked)

        self.reset_zoom_button = self.findChild(QtWidgets.QPushButton, 'resetZoomButton')
        self.reset_zoom_button.clicked.connect(self.on_reset_zoom_button_clicked)

        self.undo_button = self.findChild(QtWidgets.QPushButton, 'undoButton')
        self.undo_button.clicked.connect(self.on_undo_button_clicked)

        self.redo_button = self.findChild(QtWidgets.QPushButton, 'redoButton')
        self.redo_button.clicked.connect(self.on_redo_button_clicked)

        self.scroll_area = self.findChild(QtWidgets.QScrollArea, 'scrollArea')
        self.display = ImageDisplay(self.on_image_display_clicked, self.on_image_display_move,
                                    self.on_image_display_release)
        self.display.setMouseTracking(True)
        self.scroll_area.setWidget(self.display)

        self.brush_button = self.findChild(QtWidgets.QPushButton, 'brushButton')
        self.brush_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.brush_button.clicked.connect(self.on_brush_button_clicked)

        self.color_picker_button = self.findChild(QtWidgets.QPushButton, 'pickerButton')
        self.color_picker_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.color_picker_button.clicked.connect(self.on_color_picker_button_clicked)

        self.eraser_button = self.findChild(QtWidgets.QPushButton, 'eraserButton')
        self.eraser_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.eraser_button.clicked.connect(self.on_eraser_button_clicked)

        self.select_button = self.findChild(QtWidgets.QPushButton, 'selectButton')
        self.select_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.select_button.clicked.connect(self.on_select_button_clicked)

        self.move_button = self.findChild(QtWidgets.QPushButton, 'moveButton')
        self.move_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")

        self.move_button.clicked.connect(self.on_move_button_clicked)

        self.zoom_button = self.findChild(QtWidgets.QWidget, 'zoomButton')
        self.zoom_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.zoom_button.clicked.connect(self.on_zoom_button_clicked)

        self.brush_color_button = self.findChild(QtWidgets.QWidget, 'brushcolorButton')
        self.brush_color_button.clicked.connect(self.on_brush_color_button_clicked)
        self.current_brush_color = [QtGui.QColor(QtCore.Qt.black)]
        set_button_color(self.current_brush_color[0], self.brush_color_button)
        self.brush_color_button.update()

        self.file_save_button = self.findChild(QtWidgets.QWidget, 'filesaveButton')
        self.file_save_button.clicked.connect(self.on_file_save_button_clicked)

        self.note_button = self.findChild(QtWidgets.QWidget, 'noteButton')
        self.note_button.clicked.connect(self.on_note_button_clicked)

        self.brush_size_button = self.findChild(QtWidgets.QWidget, 'brushSizeButton')
        self.brush_size_button.clicked.connect(self.on_brush_size_button_clicked)
        self.brush_size_pixmap = QtGui.QPixmap("resources/brush thickness " + str(self.current_brush_size[0]))
        self.brush_size_icon = QtGui.QIcon(self.brush_size_pixmap)
        self.brush_size_button.setIcon(self.brush_size_icon)
        self.brush_size_button.setIconSize(self.brush_size_pixmap.rect().size())

        self.button_list = deque()
        self.button_list.append(self.brush_button)
        self.button_list.append(self.move_button)
        self.button_list.append(self.zoom_button)
        self.button_list.append(self.color_picker_button)
        self.button_list.append(self.eraser_button)
        self.button_list.append(self.select_button)
        self.button_list.append(self.file_save_button)
        self.tool_list = deque()
        self.tool_list.append(self.zoom_button)
        self.tool_list.append(self.move_button)
        self.tool_list.append(self.brush_button)
        self.tool_list.append(self.color_picker_button)
        self.tool_list.append(self.select_button)
        self.tool_list.append(self.eraser_button)

        # Click all the buttons for the tools so that they work with touch when an image is loaded
        # Don't ask me why, I don't know why either
        for button in self.tool_list:
            button.animateClick()

        # TODO:Start airnef
        # Make sure airnef picture folder and temp folder exists
        os.makedirs(Ui.AIRNEF_PICTURE_DIRECTORY, exist_ok=True)
        os.makedirs(Ui.TEMP_DIRECTORY, exist_ok=True)
        self.image_file_list = [join(Ui.AIRNEF_PICTURE_DIRECTORY, f) for f in listdir(Ui.AIRNEF_PICTURE_DIRECTORY) if
                                isfile(join(Ui.AIRNEF_PICTURE_DIRECTORY, f))]
        # subprocess.run(["python", "airnef/airnefcmd.py","--outputdir", Ui.AIRNEF_PICTURE_DIRECTORY , "--realtimedownload",
        # "only"])

        # Setup filewatcher
        self.file_watcher = CameraFolderWatcher()
        self.file_watcher.monitor_directory(Ui.AIRNEF_PICTURE_DIRECTORY)
        self.file_watcher.register_callback(self.on_folder_changed_event)
        self.show()  # Show the GUI

    def show_open_dialog(self):
        self.file_dialog = QtWidgets.QFileDialog(self, 'Open Image', '/')
        self.file_dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        self.file_dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, False)
        self.file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        self.file_dialog.setNameFilter("Image Files (*.png *.jpg *.nef)")
        self.file_dialog.fileSelected.connect(self.load_image)
        self.file_dialog.show()

    def load_image(self, filename: str):

        if filename:
            self.load_image_from_file(filename)

    def load_image_from_file(self, filename: str) -> bool:
        fileinfo = QtCore.QFileInfo(filename)
        new_image = QtGui.QImage()
        image_to_read = None
        if fileinfo.suffix() == "nef":
            # Sse rawpy to read nef file then load as QImage
            with rawpy.imread(path) as raw:
                src = raw.postprocess()
                h, w, ch = src.shape
                bytesPerLine = ch * w
                buf = src.data.tobytes()  # or bytes(src.data)
                new_image = QtGui.QImage(buf, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
        else:
            if fileinfo.size() > Ui.MAX_IMAGE_VIEW_SIZE_BYTES:
                #    print("image too large! shrinking image for viewing and editing...")
                # Uncomment this line if SmartMonitor is set to read any kind of jpg file
                # image_to_read = shrink_file_size(filename)
                # Uncomment this line if SmartMonitor is going to be set to read nikon DSLR images only
                image_to_read = extract_preview_image(filename)
            else:
                image_to_read = filename
            # Load in image
            reader = QImageReader()
            reader.setFileName(image_to_read)
            reader.setAutoTransform(True)
            new_image = reader.read()
            self.note_module.read_notes_from_file(image_to_read)
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

    # This method is for loading in a new image into SmartMonitor
    def set_image(self, new_image: QtGui.QImage):
        self.current_image[0] = QtGui.QImage(new_image)
        if self.current_image[0].colorSpace().isValid():
            self.current_image[0].convertToColorSpace(QtGui.QColorSpace(QtGui.QColorSpace.SRgb))
        self.display.setPixmap(QtGui.QPixmap.fromImage(self.current_image[0]))
        self.scale_factor[0] = 1.0
        self.current_action[0] = 0
        self.actions.clear()
        self.reset_zoom_button.setEnabled(True)

        self.scroll_area.setVisible(True)
        self.display.adjustSize()
        for button in self.button_list:
            button.setEnabled(True)

    # This method is for updating the image display on SmartMonitor when a change is made
    def update_image(self):
        # display_image = self.current_image[0].scaledToWidth(int(display_image.width() * self.scale_factor[0]))

        # Remove this code block if selection implementation takes up too much memory

        # DRAW SELECTION BOX CODE START #
        display_image = QtGui.QImage(self.current_image[0])
        if self.selection[0].isValid():
            painter = QtGui.QPainter(display_image)
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 5,
                                      QtCore.Qt.DotLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            # new_pos = QtCore.QPoint(int(pos.x() / self.scale[0]), int(pos.y() / self.scale[0]))
            painter.drawRect(self.selection[0])
            painter.end()

        display_image = display_image.scaledToWidth(int(display_image.width() * self.scale_factor[0]))
        # DRAW SELECTION BOX CODE END #

        self.display.setPixmap(QtGui.QPixmap.fromImage(display_image))

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
            self.limit_action_list_size()

    def on_file_open_button_clicked(self):
        self.show_open_dialog()
        # self.load_image()

    def show_save_dialog(self):
        show_virtual_keyboard()
        self.file_dialog = QtWidgets.QFileDialog(self, 'Save Image', '/')
        self.file_dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        self.file_dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, False)
        self.file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        self.file_dialog.setNameFilter("JPG Image (*.jpg)")
        self.file_dialog.fileSelected.connect(self.save_image)
        self.file_dialog.show()

    def save_image(self, filename: str):

        # filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Image', '/', "JPG Image (*.jpg)",options=QtWidgets.QFileDialog.DontUseNativeDialog)
        # add extension if none is found.
        if filename:
            if not filename.endswith(".jpg"):
                filename += ".jpg"
            success = self.current_image[0].save(filename)
            self.note_module.save_notes_to_file(filename)

    def on_file_save_button_clicked(self):
        self.show_save_dialog()
        # self.save_image()

    # Method to do setup on buttons that are linked to selecting tools, tool_button is the button associated with the
    # tool, new_tool_setup_func is the function to call for extra tool setup code
    def select_tool(self, tool_button: QtWidgets.QPushButton, new_tool_setup_func):
        if tool_button.isEnabled():
            if self.selected_button == tool_button:
                self.selected_tool = None
                self.selected_button = None
            else:
                new_tool = new_tool_setup_func()
                if self.selected_tool:
                    self.selected_tool.on_deselect_tool()
                self.selected_tool = new_tool
                self.selected_tool.on_select_tool()
                self.selected_button = tool_button
                self.update_image()

    def on_brush_button_clicked(self):
        self.select_tool(self.brush_button, self.brush_tool_setup)

    def on_move_button_clicked(self):
        self.select_tool(self.move_button, self.move_tool_setup)

    def on_brush_color_button_clicked(self):
        self.current_brush_color[0] = QtWidgets.QColorDialog.getColor()
        set_button_color(self.current_brush_color[0], self.brush_color_button)
        self.brush_color_button.update()

    def on_zoom_button_clicked(self):
        self.select_tool(self.zoom_button, self.zoom_tool_setup)

    def on_reset_zoom_button_clicked(self):
        self.scale_factor[0] = 1.0
        self.update_image()

    def on_note_button_clicked(self):
        self.note_window = NoteWindow(self.note_module.notes)
        self.note_window.show()

    def on_brush_size_button_clicked(self):
        self.current_brush_size[0] = (self.current_brush_size[0] % 4) + 1
        self.brush_size_pixmap = QtGui.QPixmap("resources/brush thickness " + str(self.current_brush_size[0]))
        self.brush_size_icon = QtGui.QIcon(self.brush_size_pixmap)
        self.brush_size_button.setIcon(self.brush_size_icon)
        self.brush_size_button.setIconSize(self.brush_size_pixmap.rect().size())

    def on_color_picker_button_clicked(self):
        self.select_tool(self.color_picker_button, self.color_picker_tool_setup)

    def on_eraser_button_clicked(self):
        self.select_tool(self.eraser_button, self.eraser_tool_setup)

    def on_select_button_clicked(self):
        self.select_tool(self.select_button, self.select_tool_setup)

    def on_crop_button_clicked(self):
        if self.selection[0].isValid:
            # TODO: set cropped image as new image
            self.current_image[0] = self.current_image[0].copy(self.selection[0])
            self.selection[0].setRect(0, 0, 0, 0)
            self.update_image()

    def on_redo_button_clicked(self):
        self.redo_action()

    def on_undo_button_clicked(self):
        self.undo_action()

    def on_camera_folder_button_clicked(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "Select Directory", "/")
        if directory:
            self.file_watcher.monitor_directory(QtCore.QFileInfo(directory[0]).dir().absolutePath())

    def brush_tool_setup(self) -> PaintTool:
        new_tool = PaintTool()
        new_tool.set_button(self.brush_button)
        new_tool.set_image(self.current_image)
        new_tool.set_color(self.current_brush_color)
        new_tool.set_scale(self.scale_factor)
        new_tool.set_paint_radius(self.brush_sizes, self.current_brush_size)
        new_tool.set_action_list(self.actions, self.current_action)
        return new_tool

    def move_tool_setup(self) -> MoveTool:
        new_tool = MoveTool()
        new_tool.set_button(self.move_button)
        new_tool.set_image(self.current_image)
        new_tool.set_scroll_area(self.scroll_area)
        return new_tool

    def zoom_tool_setup(self) -> ScaleTool:
        new_tool = ScaleTool(self.scale_factor)
        new_tool.set_button(self.zoom_button)
        new_tool.set_image(self.current_image)
        return new_tool

    def color_picker_tool_setup(self):
        new_tool = ColourPickerTool()
        new_tool.set_button(self.color_picker_button)
        new_tool.set_color_button(self.brush_color_button)
        new_tool.set_image(self.current_image)
        new_tool.set_color_variable(self.current_brush_color)
        return new_tool

    def eraser_tool_setup(self) -> EraserTool:
        new_tool = EraserTool()
        new_tool.set_button(self.eraser_button)
        new_tool.set_image(self.current_image)
        new_tool.set_scale(self.scale_factor)
        new_tool.set_action_list(self.actions, self.current_action)
        return new_tool

    def select_tool_setup(self) -> SelectTool:
        new_tool = SelectTool([self.crop_button])
        new_tool.set_button(self.select_button)
        new_tool.set_image(self.current_image)
        new_tool.set_scale(self.scale_factor)
        new_tool.set_selection(self.selection)
        new_tool.set_action_list(self.actions, self.current_action)
        return new_tool

    def on_folder_changed_event(self, folder_changed_url: str):
        changed_files = [join(folder_changed_url, f) for f in listdir(folder_changed_url) if
                         isfile(join(folder_changed_url, f)) and join(folder_changed_url, f).endswith('.JPG')]
        if len(changed_files) > len(self.image_file_list):
            self.image_file_list = changed_files
            # Iterate through list to find latest file
            latest_file = max(self.image_file_list, key=os.path.getctime)
            # Sleep command to wait for image to finish loading in the raspberry pi before displaying it in
            # SmartMonitor, adjust time or find more reliable workaround
            time.sleep(1)
            self.load_image_from_file(latest_file)
        else:
            self.image_file_list = changed_files

    def undo_action(self):
        if self.current_action[0] < (len(self.actions)):
            self.current_action[0] += 1
            self.redraw_image()

    def redo_action(self):
        if self.current_action[0] > 0:
            self.current_action[0] -= 1
            self.redraw_image()

    # Redraws the image after an undo/redo action
    def redraw_image(self):
        new_image = QtGui.QImage(self.original_image)
        index = -1
        stop_index = len(self.actions) - 1 - self.current_action[0]
        for action in self.actions:
            index += 1
            if index <= stop_index:
                action.tool.apply_effect(action, new_image)

        self.current_image[0] = new_image
        self.update_image()

    # Limits how far the user is able to undo to save memory
    def limit_action_list_size(self):
        if len(self.actions) > 5:
            action = self.actions.popleft()
            action.tool.apply_effect(action, self.original_image)


app = QtWidgets.QApplication(sys.argv)

# Make sure virtual keyboard window isn't opaque when it is triggered
# QtGui.QGuiApplication.inputMethod().visibleChanged.connect(handleVisibleChanged)

window = Ui()
app.exec_()
