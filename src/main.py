
# Import required packages
from datetime import date
import io
import os
import subprocess
import sys
import platform
from PySide2.QtCore import Qt
from PySide2.QtGui import QImageReader
from PySide2.QtWidgets import QMessageBox

from CameraFolderWatcher import CameraFolderWatcher
from ImageDisplay import ImageDisplay
from NoteModule import ExifNoteModule, AppendedDataNoteModule, TextNoteModule
from NoteWindow import NoteWindow
from gphotothread2 import GPhotoThread2
from Tool import *
from ui_mainwindow import Ui_MainWindow
from os import listdir
from os.path import isfile, join
from PIL import Image
from pathlib import Path
from DragDropLabel import *
import exifread
from QFileDialogPreview import QFileDialogPreview
import pickle
import base64
from wakepy import set_keepawake, unset_keepawake
import shutil
from sys import platform

if platform == "linux":
    import rawpy

USR_CMT_TAG_ID = 37510


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


def get_image_exif_tags(filename: str) -> str:
    """
    img = Image.open(filename)
    temp_list = []
    exif_data = img.getexif()
    if exif_data:
        for tag, value in exif_data.items():
            decoded = TAGS.get(tag, tag)
            temp_list.append(decoded)
            temp_list.append(" : ")
            temp_list.append(str(value))
            temp_list.append("\n")
        ifd_data = exif_data.get_ifd(0x8769)
        for tag, value in ifd_data.items():
            decoded = TAGS.get(tag, tag)
            temp_list.append(decoded)
            temp_list.append(" : ")
            temp_list.append(str(value))
            temp_list.append("\n")
        output = ''.join(temp_list)
        return output
    return ""
    """
    with open(filename, 'rb') as file:
        temp_list = []
        tags = exifread.process_file(file, details=False)
        for tag in tags.keys():
            temp_list.append(str(tag))
            temp_list.append(" : ")
            temp_list.append(str(tags[tag]))
            temp_list.append("\n")
        output = ''.join(temp_list)
        return output
    return ""


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


def clear_airnef_folder():
    [f.unlink() for f in Path(Ui.AIRNEF_PICTURE_DIRECTORY).glob("*") if f.is_file()]


class InfoWindow(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self, text_to_display):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        text_view = QtWidgets.QPlainTextEdit()
        text_view.setPlainText(text_to_display)
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidget(text_view)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)
        self.setLayout(layout)
        self.setWindowTitle('Image Info')
        self.resize(1000, 600)


class Ui(QtWidgets.QMainWindow):
    PICTURE_DIRECTORY = "pictures"
    AIRNEF_PICTURE_DIRECTORY = "airnefpictures"
    TEMP_DIRECTORY = "temp"
    GPHOTO_DIRECTORY = "gphotofs"
    MAX_UNDO_SIZE = 5
    MAX_PICTURE_STORAGE = 40
    MAX_IMAGE_VIEW_SIZE_BYTES = 1000000

    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        # Initialise window contents form ui python script

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_AcceptTouchEvents, False)
        default_font = QtGui.QFont()
        default_font.setFamily(default_font.defaultFamily())
        default_font.setPointSize(8)
        self.setFont(default_font)

        # Initialise variables
        self.scale_factor = [float(1)]
        self.file_notes = list()
        self.note_module = ExifNoteModule()
        self.selected_tool = None
        self.selected_button = None
        self.original_filename = None
        self.brush_sizes = {1: '5', 2: '7', 3: '10', 4: '14'}
        self.current_brush_size = [1]
        self.file_dialog = None
        self.selection = [QtCore.QRect()]
        self.note_window = None
        self.info_to_display = ""
        self.activated = False
        self.lastPoint = QtCore.QPoint()
        self.lastScale = self.scale_factor[0]
        self.image_tool = ImageTool()
        self.label_tool = LabelTool()

        self.actions = deque()
        self.current_action = [0]
        self.original_image = QtGui.QImage()
        self.current_image = [QtGui.QImage()]

        self.crop_tool = CropTool()
        self.crop_tool.set_selection(self.selection)
        self.crop_tool.set_image(self.current_image)
        self.crop_tool.set_scale(self.scale_factor)
        self.crop_tool.set_action_list(self.actions, self.current_action)

        self.note_window = None

        # Initialise buttons
        self.help_text = self.findChild(QtWidgets.QPlainTextEdit, "helpEdit")
        self.zoom_display_label = self.findChild(QtWidgets.QLabel, "zoomdisplaylabel")
        self.zoom_display_label.setVisible(False)

        # self.crop_button = self.findChild(QtWidgets.QPushButton, 'cropButton')
        # self.crop_button.setVisible(False)
        # self.crop_button.clicked.connect(self.on_crop_button_clicked)

        self.zoom_bar = self.findChild(QtWidgets.QScrollBar, 'zoomBar')
        self.zoom_bar.setVisible(False)
        self.zoom_bar.sliderMoved.connect(self.on_zoom_bar_modified)

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
        # self.display = ImageDisplay(self.on_image_display_clicked, self.on_image_display_move,
        #                            self.on_image_display_release, self.update_image,
        #                            self.scale_factor, self.scroll_area)
        self.display = ImageDisplay(self.on_image_display_clicked, self.on_image_display_move,
                                    self.on_image_display_release, self.on_image_drop)
        self.display.setMouseTracking(True)
        self.display.setAcceptDrops(True)
        self.scroll_area.setWidget(self.display)

        self.brush_button = self.findChild(QtWidgets.QPushButton, 'brushButton')
        self.brush_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.brush_button.clicked.connect(self.on_brush_button_clicked)
        self.brush_button.setFont(default_font)
        # self.brush_button.setVisible(False)

        # self.color_picker_button = self.findChild(QtWidgets.QPushButton, 'pickerButton')
        # self.color_picker_button.setStyleSheet(
        #    "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        # self.color_picker_button.clicked.connect(self.on_color_picker_button_clicked)

        # self.eraser_button = self.findChild(QtWidgets.QPushButton, 'eraserButton')
        # self.eraser_button.setStyleSheet(
        #    "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        # self.eraser_button.clicked.connect(self.on_eraser_button_clicked)

        # self.select_button = self.findChild(QtWidgets.QPushButton, 'selectButton')
        # self.select_button.setStyleSheet(
        #    "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        # self.select_button.clicked.connect(self.on_select_button_clicked)

        self.arrow_button = self.findChild(QtWidgets.QPushButton, 'arrowButton')
        self.arrow_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.arrow_button.clicked.connect(self.on_arrow_button_clicked)
        self.arrow_button.setFont(default_font)
        # self.arrow_button.setVisible(False)

        self.rect_button = self.findChild(QtWidgets.QPushButton, 'rectButton')
        self.rect_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.rect_button.clicked.connect(self.on_rect_button_clicked)
        self.rect_button.setFont(default_font)
        # self.rect_button.setVisible(False)

        self.circle_button = self.findChild(QtWidgets.QPushButton, 'cirButton')
        self.circle_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.circle_button.clicked.connect(self.on_circle_button_clicked)
        self.circle_button.setFont(default_font)

        self.label_button = self.findChild(QtWidgets.QPushButton, 'labelButton')
        self.label_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.label_button.clicked.connect(self.on_label_button_clicked)
        self.label_button.setFont(default_font)
        # self.circle_button.setVisible(False)

        # self.circle_label_button = self.findChild(QtWidgets.QPushButton, 'cirlabButton')
        # self.circle_label_button.setStyleSheet(
        #    "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        # self.circle_label_button.clicked.connect(self.on_circle_label_button_clicked)

        self.pan_button = self.findChild(QtWidgets.QPushButton, 'panButton')
        self.pan_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")

        self.pan_button.clicked.connect(self.on_pan_button_clicked)
        self.pan_button.setFont(default_font)

        self.zoom_button = self.findChild(QtWidgets.QWidget, 'zoomButton')
        self.zoom_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.zoom_button.clicked.connect(self.on_zoom_button_clicked)
        self.zoom_button.setFont(default_font)

        # self.burn_button = self.findChild(QtWidgets.QWidget, 'burnButton')
        # self.burn_button.setStyleSheet(
        #    "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        # self.burn_button.clicked.connect(self.on_burn_button_clicked)

        # self.dodge_button = self.findChild(QtWidgets.QWidget, 'dodgeButton')
        # self.dodge_button.setStyleSheet(
        #    "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        # self.dodge_button.clicked.connect(self.on_dodge_button_clicked)

        self.brush_color_button = self.findChild(QtWidgets.QWidget, 'brushcolorButton')
        self.brush_color_button.clicked.connect(self.on_brush_color_button_clicked)
        self.current_brush_color = [QtGui.QColor(QtCore.Qt.red)]
        set_button_color(self.current_brush_color[0], self.brush_color_button)
        self.brush_color_button.update()

        self.file_save_button = self.findChild(QtWidgets.QWidget, 'filesaveButton')
        self.file_save_button.clicked.connect(self.on_file_save_button_clicked)

        self.info_button = self.findChild(QtWidgets.QWidget, 'infoButton')
        self.info_button.clicked.connect(self.on_info_button_clicked)

        self.note_button = self.findChild(QtWidgets.QWidget, 'noteButton')
        self.note_button.clicked.connect(self.on_note_button_clicked)

        self.brush_size_button = self.findChild(QtWidgets.QWidget, 'brushSizeButton')
        self.brush_size_button.clicked.connect(self.on_brush_size_button_clicked)
        self.brush_size_pixmap = QtGui.QPixmap("resources/brush thickness " + str(self.current_brush_size[0]))
        self.brush_size_icon = QtGui.QIcon(self.brush_size_pixmap)
        self.brush_size_button.setIcon(self.brush_size_icon)
        self.brush_size_button.setIconSize(self.brush_size_pixmap.rect().size())

        self.burn_option_button = self.findChild(QtWidgets.QPushButton, 'burnButton')
        self.burn_option_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.burn_option_button.clicked.connect(self.on_burn_option_button_clicked)

        self.dodge_option_button = self.findChild(QtWidgets.QPushButton, 'dodgeButton')
        self.dodge_option_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.dodge_option_button.clicked.connect(self.on_dodge_option_button_clicked)

        self.remove_option_button = self.findChild(QtWidgets.QPushButton, 'removeButton')
        self.remove_option_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.remove_option_button.clicked.connect(self.on_remove_option_button_clicked)

        self.liquify_option_button = self.findChild(QtWidgets.QPushButton, 'liquifyButton')
        self.liquify_option_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.liquify_option_button.clicked.connect(self.on_liquify_option_button_clicked)

        self.blur_option_button = self.findChild(QtWidgets.QPushButton, 'blurButton')
        self.blur_option_button.setStyleSheet(
            "QPushButton{background-color:lightGray;}QPushButton:checked{background-color:cyan;}")
        self.blur_option_button.clicked.connect(self.on_blur_option_button_clicked)

        self.area_tab = self.findChild(QtWidgets.QTabWidget, 'AreaTab')
        self.label_tab = self.findChild(QtWidgets.QTabWidget, 'LabelTab')
        self.label_tab.setTabText(0, "Annotation Labels\n(Drag-and-Drop)")
        size_policy = self.label_tab.sizePolicy()
        size_policy.setRetainSizeWhenHidden(True)
        self.label_tab.setSizePolicy(size_policy)
        self.area_tab.setVisible(False)
        self.label_tab.setVisible(False)

        horizontal_layout = self.findChild(QtWidgets.QHBoxLayout, 'horizontalLayout')
        horizontal_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.icon_layout = self.findChild(QtWidgets.QGridLayout, 'iconLayout')

        self.selection_layout = self.findChild(QtWidgets.QGridLayout, 'selectionLayout')
        while self.selection_layout.count():
            child = self.selection_layout.takeAt(0)
            if child.widget():
                child.widget().setParent(self)
                child.widget().setVisible(False)

        self.button_list = list()
        self.button_list.append(self.brush_button)
        self.button_list.append(self.pan_button)
        self.button_list.append(self.zoom_button)
        # self.button_list.append(self.color_picker_button)
        # self.button_list.append(self.eraser_button)
        # self.button_list.append(self.select_button)
        self.button_list.append(self.arrow_button)
        self.button_list.append(self.rect_button)
        self.button_list.append(self.circle_button)
        self.button_list.append(self.label_button)
        # self.button_list.append(self.circle_label_button)
        self.button_list.append(self.file_save_button)
        self.button_list.append(self.info_button)
        self.button_list.append(self.burn_option_button)
        self.button_list.append(self.dodge_option_button)
        self.button_list.append(self.remove_option_button)
        self.button_list.append(self.liquify_option_button)
        self.button_list.append(self.blur_option_button)
        # self.button_list.append(self.burn_button)
        # self.button_list.append(self.dodge_button)

        self.tool_list = list()
        self.tool_list.append(self.zoom_button)
        self.tool_list.append(self.pan_button)
        self.tool_list.append(self.brush_button)
        # self.tool_list.append(self.color_picker_button)
        # self.tool_list.append(self.select_button)
        self.tool_list.append(self.arrow_button)
        self.tool_list.append(self.rect_button)
        self.tool_list.append(self.circle_button)
        self.tool_list.append(self.label_button)
        self.tool_list.append(self.burn_option_button)
        self.tool_list.append(self.dodge_option_button)
        self.tool_list.append(self.remove_option_button)
        self.tool_list.append(self.liquify_option_button)
        self.tool_list.append(self.blur_option_button)
        # self.tool_list.append(self.circle_label_button)
        # self.tool_list.append(self.eraser_button)
        # self.tool_list.append(self.burn_button)
        # self.tool_list.append(self.dodge_button)

        self.option_list = list()
        self.option_list.append(self.burn_option_button)
        self.option_list.append(self.dodge_option_button)
        self.option_list.append(self.remove_option_button)
        self.option_list.append(self.liquify_option_button)
        self.option_list.append(self.blur_option_button)

        self.selection_list = list()
        self.selection_list.append(self.brush_button)
        self.selection_list.append(self.arrow_button)
        self.selection_list.append(self.circle_button)
        self.selection_list.append(self.rect_button)
        self.selection_list.append(self.label_button)

        self.current_labels = list()

        self.burn_label_drag_list = list()
        self.burn_label_drag_list.append(("Here", QtCore.Qt.red))
        self.burn_label_drag_list.append(("+1/4", QtCore.Qt.red))
        self.burn_label_drag_list.append(("+2/4", QtCore.Qt.red))
        self.burn_label_drag_list.append(("+3/4", QtCore.Qt.red))
        self.burn_label_drag_list.append(("+1/3", QtCore.Qt.red))
        self.burn_label_drag_list.append(("+2/3", QtCore.Qt.red))
        self.burn_label_drag_list.append(("+1/2", QtCore.Qt.red))
        self.burn_label_drag_list.append(("+1", QtCore.Qt.red))
        self.burn_label_drag_list.append(("+2", QtCore.Qt.red))
        self.burn_label_drag_list.append(("+3", QtCore.Qt.red))

        self.dodge_label_drag_list = list()
        self.dodge_label_drag_list.append(("Here", QtCore.Qt.blue))
        self.dodge_label_drag_list.append(("-1/4", QtCore.Qt.blue))
        self.dodge_label_drag_list.append(("-2/4", QtCore.Qt.blue))
        self.dodge_label_drag_list.append(("-3/4", QtCore.Qt.blue))
        self.dodge_label_drag_list.append(("-1/3", QtCore.Qt.blue))
        self.dodge_label_drag_list.append(("-2/3", QtCore.Qt.blue))
        self.dodge_label_drag_list.append(("-1/2", QtCore.Qt.blue))
        self.dodge_label_drag_list.append(("-1", QtCore.Qt.blue))
        self.dodge_label_drag_list.append(("-2", QtCore.Qt.blue))
        self.dodge_label_drag_list.append(("-3", QtCore.Qt.blue))

        self.remove_label_drag_list = list()
        self.remove_label_drag_list.append(("Remove", QtGui.QColor("orange")))

        self.liquify_label_drag_list = list()
        self.liquify_label_drag_list.append(("Liquify", QtGui.QColor(QtCore.Qt.cyan)))

        self.blur_label_drag_list = list()
        self.blur_label_drag_list.append(("Blur", QtGui.QColor(QtCore.Qt.darkYellow)))

        """
        self.accept_label = DragDropImageLabel()
        self.accept_label.setMinimumSize(QtCore.QSize(0, 51))
        self.accept_label.setMaximumSize(QtCore.QSize(147, 51))
        self.accept_label.setAlignment(QtCore.Qt.AlignCenter)
        self.accept_label.setStyleSheet("border: 1px solid black;")
        self.accept_label.update_image(QtGui.QImage("resources/accept.png"))
        self.icon_layout.addWidget(self.accept_label)
        self.cross_label = DragDropImageLabel()
        self.cross_label.setMinimumSize(QtCore.QSize(0, 51))
        self.cross_label.setMaximumSize(QtCore.QSize(147, 51))
        self.cross_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cross_label.setStyleSheet("border: 1px solid black;")
        self.cross_label.update_image(QtGui.QImage("resources/cross.png"))
        self.icon_layout.addWidget(self.cross_label)
        """

        # TODO: set icon
        # for button in self.image_button_list:
        #    button[0].set_image(self.get_qimage_from_text(button[1]))

        # Click all the buttons for the tools so that they work with touch when an image is loaded
        # Don't ask me why, I don't know why either
        for button in self.tool_list:
            button.animateClick()

        # Make sure airnef picture folder and temp folder exists
        # os.makedirs(Ui.PICTURE_DIRECTORY, exist_ok=True)
        if platform == "linux":
            # set picture directory to folder under photos
            folder_date = date.today()
            Ui.PICTURE_DIRECTORY = "/home/pi/photos" + "/" + str(folder_date)
            os.makedirs("/home/pi/photos", exist_ok=True)
        self.picture_folder_missing = not os.path.exists(Ui.PICTURE_DIRECTORY)
        if platform == "linux":
            if self.picture_folder_missing:
                self.open_file_directory = "/home/pi/photos"
            else:
                self.open_file_directory = Ui.PICTURE_DIRECTORY
        else:
            self.open_file_directory = Ui.PICTURE_DIRECTORY

        # os.makedirs(Ui.PICTURE_DIRECTORY, exist_ok=True)
        os.makedirs(Ui.AIRNEF_PICTURE_DIRECTORY, exist_ok=True)
        os.makedirs(Ui.TEMP_DIRECTORY, exist_ok=True)
        os.makedirs(Ui.GPHOTO_DIRECTORY, exist_ok=True)
        clear_airnef_folder()

        # TODO:Start airnef
        self.camera_watcher_active = False
        self.gphoto_thread = GPhotoThread2()
        self.camera_watcher_active = self.gphoto_thread.initialize(os.path.abspath(Ui.GPHOTO_DIRECTORY),
                                                                   os.path.abspath(Ui.AIRNEF_PICTURE_DIRECTORY))
        if self.camera_watcher_active:
            self.gphoto_thread.start()
        # subprocess.run(["python", "airnef/airnefcmd.py","--outputdir", Ui.AIRNEF_PICTURE_DIRECTORY , "--realtimedownload",
        # "only"])

        # Setup filewatcher
        self.file_watcher = CameraFolderWatcher()
        self.file_watcher.monitor_directory(Ui.AIRNEF_PICTURE_DIRECTORY)
        self.file_watcher.register_callback(self.on_folder_changed_event)

        self.help_text.setPlainText("Open an image file to begin.")
        set_keepawake(keep_screen_awake=True)
        #self.start = time.time()
        #self.end = time.time()
        self.showMaximized()  # Show the GUI

    #def paintEvent(self, event):
    #    super(QtWidgets.QMainWindow, self).paintEvent(event)
    #    if self.camera_watcher_active:
    #        self.end = time.time()
    #        if (self.end - self.start) > 300:
    #            self.gphoto_thread.iterate()
    #            self.start = time.time()

    def closeEvent(self, *args, **kwargs):
        super(QtWidgets.QMainWindow, self).closeEvent(*args, **kwargs)
        unset_keepawake()
        if self.camera_watcher_active:
        #    self.gphoto_thread.shutdown()
            self.gphoto_thread.stop()
            self.gphoto_thread.join()
        self.file_watcher.shutdown()

    def show_open_dialog(self):
        # self.file_dialog = QtWidgets.QFileDialog(self, 'Open Image', self.PICTURE_DIRECTORY)
        self.file_dialog = QFileDialogPreview(self, 'Open File', self.open_file_directory)
        self.file_dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        # self.file_dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, False)
        self.file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        self.file_dialog.setNameFilter("Image Files (*.png *.jpg)")
        # self.file_dialog.setNameFilter("Image Files (*.png *.jpg *.nef)")
        # self.file_dialog.setIconProvider(icon_provider)
        # self.file_dialog = ImageChooser("pictures")
        # self.file_dialog.fileSelected.connect(self.load_image)
        # self.file_dialog.show()
        if self.file_dialog.exec():
            self.load_image(self.file_dialog.getFileSelected())

    def load_image(self, filename: str):
        if filename:
            self.load_image_from_file(filename)
            self.reset_buttons()

    def load_image_from_file(self, filename: str) -> bool:
        fileinfo = QtCore.QFileInfo(filename)
        new_image = QtGui.QImage()
        image_to_read = None
        if fileinfo.suffix() == "nef":
            # Sse rawpy to read nef file then load as QImage
            if fileinfo.size() > Ui.MAX_IMAGE_VIEW_SIZE_BYTES:
                # Clear temp file
                clear_temp_folder()
                with rawpy.imread(filename) as raw:
                    src = raw.postprocess()
                    img = Image.fromarray(src)  # Pillow image
                    # Make shrunken image
                    temp_filename = Ui.TEMP_DIRECTORY + "/tempimage.jpg"

                    if os.path.getsize(filename) > 5000000:
                        width, height = img.size
                        resized_img = img.resize((width // 8, height // 8))
                        resized_img.save(temp_filename)
                    else:
                        width, height = img.size
                        resized_img = img.resize((width // 2, height // 2))
                        resized_img.save(temp_filename)

                    while os.path.getsize(temp_filename) > Ui.MAX_IMAGE_VIEW_SIZE_BYTES:
                        img = Image.open(temp_filename)
                        width, height = img.size
                        resized_img = img.resize((width // 2, height // 2))
                        resized_img.save(temp_filename)

                    reader = QImageReader()
                    image_to_read = temp_filename
                    reader.setFileName(image_to_read)
                    reader.setAutoTransform(True)
                    new_image = reader.read()
            else:
                with rawpy.imread(filename) as raw:
                    src = raw.postprocess()
                    h, w, ch = src.shape
                    bytesPerLine = ch * w
                    buf = src.data.tobytes()  # or bytes(src.data)
                    new_image = QtGui.QImage(buf, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            self.note_module = AppendedDataNoteModule()
        else:
            if fileinfo.size() > Ui.MAX_IMAGE_VIEW_SIZE_BYTES:
                #    print("image too large! shrinking image for viewing and editing...")
                # Uncomment this line if SmartMonitor is set to read any kind of jpg file
                # image_to_read = shrink_file_size(filename)
                # Uncomment this line if SmartMonitor is going to be set to read nikon DSLR images only
                self.info_to_display = get_image_exif_tags(filename)
                # self.show_image_exif_info(text_to_display)
                image_to_read = extract_preview_image(filename)
            else:
                image_to_read = filename

            # Load in image
            reader = QImageReader()
            reader.setFileName(image_to_read)
            reader.setAutoTransform(True)
            new_image = reader.read()
            self.note_module = TextNoteModule()

        if new_image.isNull():
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle(QtGui.QGuiApplication.applicationDisplayName())
            msg_box.setText("Cannot load " + QtCore.QDir.fromNativeSeparators(filename) + ": " + reader.errorString())
            msg_box.exec()
            return False
        self.original_filename = filename
        self.original_image = new_image
        if self.original_image.colorSpace().isValid():
            self.original_image.convertToColorSpace(QtGui.QColorSpace(QtGui.QColorSpace.SRgb))
        self.set_image(new_image)
        json_struct = self.note_module.read_json_from_file(self.original_filename)
        try:
            if json_struct:
                self.file_notes = json_struct['notes']
        except KeyError:
            print("no json stored in UserComment tag")
        except ValueError:
            print("no json stored in UserComment tag")

        try:
            if json_struct:
                encoded_actions = json_struct['actions']
                self.actions = self.deserialize_actions(encoded_actions)
        except KeyError:
            print("no json stored in UserComment tag")
        except ValueError:
            print("no json stored in UserComment tag")

        self.current_action[0] = 0
        self.redraw_image()
        QtWidgets.QWidget.setWindowFilePath(self, filename)
        self.help_text.setPlainText("Select an annotation action and the area selection format on the left tab.")
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

    def on_image_drop(self, event):
        img = QtGui.QImage()
        mimedata = event.mimeData().data("PNG")
        color = pickle.loads(event.mimeData().data("color"))
        text = pickle.loads(event.mimeData().data("text"))
        if mimedata:
            current_effect = []
            img.loadFromData(mimedata)
            painter = QtGui.QPainter(self.current_image[0])
            new_pos = QtCore.QPoint(
                int((event.pos().x() - (img.width() / (2 / self.scale_factor[0]))) / self.scale_factor[0]),
                int((event.pos().y() - (img.height() / (2 / self.scale_factor[0]))) / self.scale_factor[0]))
            painter.drawImage(new_pos, img)

            current_effect.append(Effect(new_pos))

            # current_effect.append(img)
            current_effect.append(color)
            current_effect.append(text)
            stop_index = len(self.actions) - self.current_action[0]
            self.actions.insert(stop_index, Action(self.label_tool, current_effect, EffectType.LABEL))
            while len(self.actions) > stop_index + 1:
                self.actions.pop()
            self.current_action[0] = 0
            self.limit_action_list_size()

            self.update_image()

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
            self.note_module.save_notes_to_file(filename, self.file_notes)

    def on_file_save_button_clicked(self):
        self.save_actions_and_notes()
        # self.show_save_dialog()
        # self.save_image()

    # Method to do setup on buttons that are linked to selecting tools, tool_button is the button associated with the
    # tool, new_tool_setup_func is the function to call for extra tool setup code
    def select_tool(self, tool_button: QtWidgets.QPushButton, new_tool_setup_func):
        if self.label_button.isChecked():
            self.help_text.setPlainText("")
            self.label_tab.setVisible(False)
            self.label_button.setChecked(False)
        if tool_button.isEnabled():
            if self.selected_button == tool_button:
                self.selected_tool.on_deselect_tool()
                self.selected_tool = None
                self.selected_button = None
            else:
                if self.selected_tool:
                    self.selected_tool.on_deselect_tool()
                new_tool = new_tool_setup_func()
                new_tool.set_help_text(self.help_text)
                self.selected_tool = new_tool
                self.selected_tool.on_select_tool()
                self.selected_button = tool_button
                self.update_image()

    def deselect_current_tool(self):
        if self.selected_tool:
            if not (isinstance(self.selected_tool, ScaleTool) or isinstance(self.selected_tool, PanTool)):
                self.selected_tool.on_deselect_tool()
                self.selected_tool = None
                self.selected_button = None

    def on_brush_button_clicked(self):
        self.select_tool(self.brush_button, self.brush_tool_setup)

    def on_pan_button_clicked(self):
        self.select_tool(self.pan_button, self.pan_tool_setup)

    def on_brush_color_button_clicked(self):
        self.current_brush_color[0] = QtWidgets.QColorDialog.getColor()
        set_button_color(self.current_brush_color[0], self.brush_color_button)
        self.brush_color_button.update()
        self.restore_label_layout()
        # for label in self.label_text_drag_list:
        #    label[0].update_image(self.get_qimage_from_text(label[1]))

    def on_zoom_button_clicked(self):
        self.select_tool(self.zoom_button, self.zoom_tool_setup)

    def on_reset_zoom_button_clicked(self):
        self.scale_factor[0] = 1.0
        self.zoom_bar.setValue(int(100 * (self.scale_factor[0] - 0.25)))
        self.update_image()

    def on_note_button_clicked(self):
        self.note_window = NoteWindow(self.file_notes)
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

    def on_arrow_button_clicked(self):
        self.select_tool(self.arrow_button, self.arrow_tool_setup)

    def on_rect_button_clicked(self):
        self.select_tool(self.rect_button, self.rect_tool_setup)

    def on_circle_button_clicked(self):
        self.select_tool(self.circle_button, self.circle_tool_setup)

    def on_circle_label_button_clicked(self):
        self.select_tool(self.circle_label_button, self.circle_label_tool_setup)

    def on_burn_button_clicked(self):
        self.select_tool(self.burn_button, self.burn_tool_setup)

    def on_dodge_button_clicked(self):
        self.select_tool(self.dodge_button, self.dodge_tool_setup)

    def on_crop_button_clicked(self):
        self.crop_tool.crop()
        self.update_image()

    def on_redo_button_clicked(self):
        self.redo_action()

    def on_undo_button_clicked(self):
        self.undo_action()

    def on_info_button_clicked(self):
        self.show_image_exif_info(self.info_to_display)

    def on_burn_option_button_clicked(self):
        if self.label_button.isChecked():
            self.help_text.setPlainText("")
            self.label_tab.setVisible(False)
            self.label_button.setChecked(False)
        self.deselect_current_tool()
        while self.selection_layout.count():
            child = self.selection_layout.takeAt(0)
            if child.widget():
                child.widget().setParent(self)
                child.widget().setVisible(False)
        if self.burn_option_button.isChecked():
            for button in self.option_list:
                if button != self.burn_option_button:
                    button.setChecked(False)
            self.current_brush_color[0] = QtGui.QColor(QtCore.Qt.red)
            set_button_color(self.current_brush_color[0], self.brush_color_button)
            self.brush_color_button.update()
            self.current_labels = self.burn_label_drag_list
            self.restore_label_layout()
            self.selection_layout.addWidget(self.brush_button, 0, 0)
            self.brush_button.setVisible(True)
            self.selection_layout.addWidget(self.rect_button, 0, 1)
            self.rect_button.setVisible(True)
            self.selection_layout.addWidget(self.circle_button, 1, 0)
            self.circle_button.setVisible(True)
            self.selection_layout.addWidget(self.label_button, 1, 1)
            self.label_button.setVisible(True)
            self.area_tab.setVisible(True)
        else:
            self.current_labels = list()
            self.restore_label_layout()
            self.area_tab.setVisible(False)

    def on_dodge_option_button_clicked(self):
        if self.label_button.isChecked():
            self.help_text.setPlainText("")
            self.label_tab.setVisible(False)
            self.label_button.setChecked(False)
        self.deselect_current_tool()
        while self.selection_layout.count():
            child = self.selection_layout.takeAt(0)
            if child.widget():
                child.widget().setParent(self)
                child.widget().setVisible(False)
        if self.dodge_option_button.isChecked():
            for button in self.option_list:
                if button != self.dodge_option_button:
                    button.setChecked(False)
            self.current_brush_color[0] = QtGui.QColor(QtCore.Qt.blue)
            set_button_color(self.current_brush_color[0], self.brush_color_button)
            self.brush_color_button.update()
            self.current_labels = self.dodge_label_drag_list
            self.restore_label_layout()
            self.selection_layout.addWidget(self.brush_button, 0, 0)
            self.brush_button.setVisible(True)
            self.selection_layout.addWidget(self.rect_button, 0, 1)
            self.rect_button.setVisible(True)
            self.selection_layout.addWidget(self.circle_button, 1, 0)
            self.circle_button.setVisible(True)
            self.selection_layout.addWidget(self.label_button, 1, 1)
            self.label_button.setVisible(True)
            self.area_tab.setVisible(True)
        else:
            self.current_labels = list()
            self.restore_label_layout()
            self.area_tab.setVisible(False)

    def on_remove_option_button_clicked(self):
        if self.label_button.isChecked():
            self.help_text.setPlainText("")
            self.label_tab.setVisible(False)
            self.label_button.setChecked(False)
        self.deselect_current_tool()
        while self.selection_layout.count():
            child = self.selection_layout.takeAt(0)
            if child.widget():
                child.widget().setParent(self)
                child.widget().setVisible(False)
        if self.remove_option_button.isChecked():
            for button in self.option_list:
                if button != self.remove_option_button:
                    button.setChecked(False)
            self.current_brush_color[0] = QtGui.QColor("orange")
            set_button_color(self.current_brush_color[0], self.brush_color_button)
            self.brush_color_button.update()
            self.current_labels = self.remove_label_drag_list
            self.restore_label_layout()
            self.selection_layout.addWidget(self.brush_button, 0, 0)
            self.brush_button.setVisible(True)
            self.selection_layout.addWidget(self.rect_button, 0, 1)
            self.rect_button.setVisible(True)
            self.selection_layout.addWidget(self.circle_button, 1, 0)
            self.circle_button.setVisible(True)
            self.selection_layout.addWidget(self.label_button, 1, 1)
            self.label_button.setVisible(True)
            self.area_tab.setVisible(True)
        else:
            self.current_labels = list()
            self.restore_label_layout()
            self.area_tab.setVisible(False)

    def on_liquify_option_button_clicked(self):
        if self.label_button.isChecked():
            self.help_text.setPlainText("")
            self.label_tab.setVisible(False)
            self.label_button.setChecked(False)
        self.deselect_current_tool()
        while self.selection_layout.count():
            child = self.selection_layout.takeAt(0)
            if child.widget():
                child.widget().setParent(self)
                child.widget().setVisible(False)
        if self.liquify_option_button.isChecked():
            for button in self.option_list:
                if button != self.liquify_option_button:
                    button.setChecked(False)
            self.current_brush_color[0] = QtGui.QColor(QtCore.Qt.cyan)
            set_button_color(self.current_brush_color[0], self.brush_color_button)
            self.brush_color_button.update()
            self.current_labels = self.liquify_label_drag_list
            self.restore_label_layout()
            self.selection_layout.addWidget(self.brush_button, 0, 0)
            self.brush_button.setVisible(True)
            self.selection_layout.addWidget(self.arrow_button, 0, 1)
            self.arrow_button.setVisible(True)
            self.selection_layout.addWidget(self.label_button, 1, 0)
            self.label_button.setVisible(True)
            self.area_tab.setVisible(True)
        else:
            self.current_labels = list()
            self.restore_label_layout()
            self.area_tab.setVisible(False)

    def on_blur_option_button_clicked(self):
        if self.label_button.isChecked():
            self.help_text.setPlainText("")
            self.label_tab.setVisible(False)
            self.label_button.setChecked(False)
        self.deselect_current_tool()
        while self.selection_layout.count():
            child = self.selection_layout.takeAt(0)
            if child.widget():
                child.widget().setParent(self)
                child.widget().setVisible(False)
        if self.blur_option_button.isChecked():
            for button in self.option_list:
                if button != self.blur_option_button:
                    button.setChecked(False)
            self.current_brush_color[0] = QtGui.QColor(QtCore.Qt.darkYellow)
            set_button_color(self.current_brush_color[0], self.brush_color_button)
            self.brush_color_button.update()
            self.current_labels = self.blur_label_drag_list
            self.restore_label_layout()
            self.selection_layout.addWidget(self.arrow_button, 0, 0)
            self.arrow_button.setVisible(True)
            self.selection_layout.addWidget(self.rect_button, 0, 1)
            self.rect_button.setVisible(True)
            self.selection_layout.addWidget(self.circle_button, 1, 0)
            self.circle_button.setVisible(True)
            self.selection_layout.addWidget(self.label_button, 1, 1)
            self.label_button.setVisible(True)
            self.area_tab.setVisible(True)
        else:
            self.current_labels = list()
            self.restore_label_layout()
            self.area_tab.setVisible(False)

    def on_label_button_ints_clicked(self):
        self.current_labels = self.ints_label_drag_list
        if self.arrow_button.isChecked():
            self.arrow_button.animateClick()
        else:
            self.restore_label_layout()

    def on_label_button_halfs_clicked(self):
        self.current_labels = self.halfs_label_drag_list
        if self.arrow_button.isChecked():
            self.arrow_button.animateClick()
        else:
            self.restore_label_layout()

    def on_label_button_thirds_clicked(self):
        self.current_labels = self.thirds_label_drag_list
        if self.arrow_button.isChecked():
            self.arrow_button.animateClick()
        else:
            self.restore_label_layout()

    def on_label_button_fourths_clicked(self):
        self.current_labels = self.fourths_label_drag_list
        if self.arrow_button.isChecked():
            self.arrow_button.animateClick()
        else:
            self.restore_label_layout()

    def on_label_button_clicked(self):
        if self.label_button.isChecked():
            if self.selected_button:
                self.selected_tool.on_deselect_tool()
                self.selected_tool = None
                self.selected_button = None
            self.help_text.setPlainText("Labels:\nTap and hold to drag and drop the labels onto the canvas")
            self.label_tab.setVisible(True)
        else:
            self.help_text.setPlainText("")
            self.label_tab.setVisible(False)

    def on_camera_folder_button_clicked(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory", "/")
        if directory:
            self.file_watcher.monitor_directory(directory)
        # directory = QtWidgets.QFileDialog.getOpenFileName(self, "Select Directory", "/")
        # if directory:
        #    self.file_watcher.monitor_directory(QtCore.QFileInfo(directory[0]).dir().absolutePath())

    def on_zoom_bar_modified(self, position):
        self.scale_factor[0] = (position + 25) / 100
        self.zoom_display_label.setText("zoom: " + "{:.2f}".format(100 * self.scale_factor[0]) + "%")
        self.update_image()

    def brush_tool_setup(self) -> PaintTool:
        new_tool = PaintTool()
        new_tool.set_button(self.brush_button)
        new_tool.set_image(self.current_image)
        new_tool.set_color(self.current_brush_color)
        new_tool.set_scale(self.scale_factor)
        new_tool.set_paint_radius(self.brush_sizes, self.current_brush_size)
        new_tool.set_action_list(self.actions, self.current_action)
        return new_tool

    def pan_tool_setup(self) -> PanTool:
        new_tool = PanTool()
        new_tool.set_button(self.pan_button)
        new_tool.set_image(self.current_image)
        new_tool.set_scroll_area(self.scroll_area)
        return new_tool

    def zoom_tool_setup(self) -> ScaleTool:
        new_tool = ScaleTool(self.scale_factor, self.zoom_bar, self.zoom_display_label)
        new_tool.set_button(self.zoom_button)
        new_tool.set_image(self.current_image)
        return new_tool

    def color_picker_tool_setup(self):
        new_tool = ColourPickerTool()
        new_tool.set_button(self.color_picker_button)
        new_tool.set_color_button(self.brush_color_button)
        new_tool.set_image(self.current_image)
        new_tool.set_scale(self.scale_factor)
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

    def arrow_tool_setup(self) -> ArrowTool:
        new_tool = ArrowTool()
        new_tool.set_button(self.arrow_button)
        new_tool.set_image(self.current_image)
        new_tool.set_color(self.current_brush_color)
        new_tool.set_scale(self.scale_factor)
        new_tool.set_label_layout_restore_func(self.restore_label_layout)
        new_tool.set_paint_radius(self.brush_sizes, self.current_brush_size)
        new_tool.set_action_list(self.actions, self.current_action)
        return new_tool

    def rect_tool_setup(self) -> RectTool:
        new_tool = RectTool()
        new_tool.set_button(self.rect_button)
        new_tool.set_image(self.current_image)
        new_tool.set_color(self.current_brush_color)
        new_tool.set_scale(self.scale_factor)
        new_tool.set_paint_radius(self.brush_sizes, self.current_brush_size)
        new_tool.set_action_list(self.actions, self.current_action)
        return new_tool

    def circle_tool_setup(self) -> CircleTool:
        new_tool = CircleTool()
        new_tool.set_button(self.circle_button)
        new_tool.set_image(self.current_image)
        new_tool.set_color(self.current_brush_color)
        new_tool.set_scale(self.scale_factor)
        new_tool.set_paint_radius(self.brush_sizes, self.current_brush_size)
        new_tool.set_action_list(self.actions, self.current_action)
        return new_tool

    def circle_label_tool_setup(self) -> CircleWithLabelTool:
        new_tool = CircleWithLabelTool()
        new_tool.set_button(self.circle_label_button)
        new_tool.set_image(self.current_image)
        new_tool.set_color(self.current_brush_color)
        new_tool.set_scale(self.scale_factor)
        new_tool.set_paint_radius(self.brush_sizes, self.current_brush_size)
        new_tool.set_action_list(self.actions, self.current_action)
        return new_tool

    def burn_tool_setup(self) -> ImageTool:
        new_tool = ImageTool()
        new_tool.set_button(self.burn_button)
        new_tool.set_image(self.current_image)
        new_tool.set_scale(self.scale_factor)
        new_tool.set_insert_image(self.get_qimage_from_text("Burn +1"))
        new_tool.set_action_list(self.actions, self.current_action)
        return new_tool

    def dodge_tool_setup(self) -> ImageTool:
        new_tool = ImageTool()
        new_tool.set_button(self.dodge_button)
        new_tool.set_image(self.current_image)
        new_tool.set_scale(self.scale_factor)
        new_tool.set_insert_image(self.get_qimage_from_text("Dodge +1"))
        new_tool.set_action_list(self.actions, self.current_action)
        return new_tool

    def on_folder_changed_event(self, folder_changed_url: str):
        # Check and delete oldest image in picture folder if over limit
        if not self.picture_folder_missing:
            files = [f for f in os.listdir(self.PICTURE_DIRECTORY) if os.path.isfile(f)]

        # while len(files) > self.MAX_PICTURE_STORAGE:
        #    oldest_file = min(files, key=os.path.getctime)
        #    os.remove(os.path.abspath(oldest_file))

        changed_files = [join(folder_changed_url, f) for f in listdir(folder_changed_url) if
                         isfile(join(folder_changed_url, f)) and join(folder_changed_url, f).endswith('.JPG')]
        for image_file in changed_files:
            #time.sleep(1)

            # Copy the JPG and NEF to the picture folder with normalised file names
            if self.picture_folder_missing:
                os.makedirs(Ui.PICTURE_DIRECTORY, exist_ok=True)
                self.open_file_directory = Ui.PICTURE_DIRECTORY
                self.picture_folder_missing = False
            p = Path(image_file)
            destination_jpg_file = self.PICTURE_DIRECTORY + '/' + p.stem + '.jpg'
            destination_nef_file = self.PICTURE_DIRECTORY + '/' + p.stem + '.nef'
            nef_file = str(p.with_suffix('')) + '.NEF'
            try:
                shutil.move(image_file, os.path.abspath(destination_jpg_file), copy_function=shutil.copytree)
            except:
                print("copy jpg error")
            try:
                shutil.move(nef_file, os.path.abspath(destination_nef_file), copy_function=shutil.copytree)
            except:
                print("copy nef error")
            # self.load_image_from_file(os.path.abspath(destination_jpg_file))

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
        new_image = [QtGui.QImage(self.original_image)]
        index = -1
        stop_index = len(self.actions) - 1 - self.current_action[0]
        for action in self.actions:
            index += 1
            if index <= stop_index:
                action.tool.apply_effect(action, new_image)

        self.current_image[0] = new_image[0]
        self.update_image()

    # Limits how far the user is able to undo to save memory
    def limit_action_list_size(self):
        return
        # if len(self.actions) > 5:
        #    action = self.actions.popleft()
        #    action.tool.apply_effect(action, [self.original_image])

    def show_image_exif_info(self, info: str):
        self.note_window = InfoWindow(info)
        self.note_window.show()

    def reset_buttons(self):
        if self.label_button.isChecked():
            self.help_text.setPlainText("")
            self.label_tab.setVisible(False)
            self.label_button.setChecked(False)
        self.deselect_current_tool()
        while self.selection_layout.count():
            child = self.selection_layout.takeAt(0)
            if child.widget():
                child.widget().setParent(self)
                child.widget().setVisible(False)
        for button in self.option_list:
            button.setChecked(False)
        self.current_labels = list()
        self.restore_label_layout()
        self.area_tab.setVisible(False)

    """
    # TODO: touch gesture event handler
    def event(self, e):
        if e.type() == QtCore.QEvent.Gesture:
            print("gesture detected")
            return gesture_event(QtWidgets.QGestureEvent(e))
        return super(Ui, self).event(e)

    def gesture_event(self, e):
        pan = e.gesture(QtGui.QPanGesture)
        pinch = e.gesture(QtGui.QPinchGesture)
        if pan:
            print("pan gesture detected")
            #self.pan_triggered(e)
        elif pinch:
            print("pinch gesture detected")
            #self.pinch_triggered(e)
        else:
            pass
        e.accept()
        return True
    
    def pan_triggered(self, gesture):
        if gesture.state() == QtCore.Qt.GestureState.Qt.GestureStarted:
            self.activated = True
        elif gesture.state() == QtCore.Qt.GestureState.Qt.GestureUpdated:
            if self.activated:
                self.scroll_area.horizontalScrollBar().setValue(
                    self.horizontal_scroll_bar.value() + (gesture.delta().toPoint()))
                self.scroll_area.verticalScrollBar().setValue(
                    self.vertical_scroll_bar.value() + (gesture.delta().toPoint()))
        elif gesture.state() == QtCore.Qt.GestureState.Qt.GestureFinished:
            self.activated = False
        else:
            pass

    def pinch_triggered(self, gesture):
        if gesture.state() == QtCore.Qt.GestureState.Qt.GestureStarted:
            self.activated = True
            self.lastPoint = pos
            self.lastScale = self.scale_factor[0]
        elif gesture.state() == QtCore.Qt.GestureState.Qt.GestureUpdated:
            if self.activated:
                self.scale_factor[0] = self.lastScale + gesture.scaleFactor()
                if self.scale_factor[0] > 4.0:
                    self.scale_factor[0] = 4.0
                if self.scale_factor[0] < 0.25:
                    self.scale_factor[0] = 0.25
        elif gesture.state() == QtCore.Qt.GestureState.Qt.GestureFinished:
            self.activated = False
        else:
            pass
    """

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

    def display_labels_in_label_list(self, label_list: list):
        while self.icon_layout.count():
            child = self.icon_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for label in label_list:
            new_label = DragDropImageLabel()
            new_label.setMinimumSize(QtCore.QSize(0, 30))
            new_label.setMaximumSize(QtCore.QSize(147, 30))
            new_label.setAlignment(QtCore.Qt.AlignCenter)
            new_label.setStyleSheet("border: 1px solid black;")
            # new_label.update_image(self.get_qimage_from_text(label[1], label[0]))
            new_label.update_image(self.current_brush_color[0], label[0])
            self.icon_layout.addWidget(new_label)

    def restore_label_layout(self):
        self.display_labels_in_label_list(self.current_labels)

    def save_actions_and_notes(self):
        stop_index = len(self.actions) - self.current_action[0]
        while len(self.actions) > stop_index:
            self.actions.pop()
        self.current_action[0] = 0
        self.limit_action_list_size()
        encoded_actions = self.serialize_actions(self.actions)
        self.note_module.save_actions_and_notes(self.original_filename, encoded_actions, self.file_notes)
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Notification")
        msg_box.setText("Annotations Saved.")
        msg_box.exec_()

    def serialize_actions(self, actions):
        actionlist = []
        tooltype = 0
        for action in actions:
            tooltype = action.tool.get_tool_type()
            if tooltype in (
                    ToolType.PAINT, ToolType.ERASER, ToolType.ARROW, ToolType.LINE, ToolType.CIRCLE, ToolType.RECT):
                actionlist.append((tooltype, action.radius, action.color, action.effects, action.effect_type))
                continue
            actionlist.append((tooltype, action.effects, action.effect_type))
        encoded_actions = base64.b64encode(pickle.dumps(actionlist)).decode('ascii')
        return encoded_actions

    def deserialize_actions(self, action_list):
        decoded_action_list = pickle.loads(base64.b64decode(action_list.encode('ascii')))
        actions = []
        for action in decoded_action_list:
            if action[0] == ToolType.PAINT:
                tool = PaintTool()
                actions.append(PaintAction(tool, action[3], action[4], action[1], action[2]))
            elif action[0] == ToolType.ERASER:
                tool = EraserTool()
                actions.append(PaintAction(tool, action[3], action[4], action[1], action[2]))
            elif action[0] == ToolType.ARROW:
                tool = ArrowTool()
                actions.append(PaintAction(tool, action[3], action[4], action[1], action[2]))
            elif action[0] == ToolType.LINE:
                tool = LineTool()
                actions.append(PaintAction(tool, action[3], action[4], action[1], action[2]))
            elif action[0] == ToolType.RECT:
                tool = RectTool()
                actions.append(PaintAction(tool, action[3], action[4], action[1], action[2]))
            elif action[0] == ToolType.CIRCLE:
                tool = CircleTool()
                actions.append(PaintAction(tool, action[3], action[4], action[1], action[2]))
            elif action[0] == ToolType.IMAGE:
                tool = self.image_tool
                actions.append(Action(tool, action[1], action[2]))
            elif action[0] == ToolType.LABEL:
                tool = self.label_tool
                actions.append(Action(tool, action[1], action[2]))
        return deque(actions)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = Ui()
    app.exec_()
