import sys, math
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
from PySide2.QtCore import Qt

from ui_imagechooser import Ui_Dialog


# ---------------------------------------------------------------------------------------------------------
class clsFilePreviewModel(QtWidgets.QFileSystemModel):
    def __init__(self, cacheWidth=100, cacheHeight=100):
        super().__init__()
        self.previews = {'None': None}
        self.cacheWidth = cacheWidth
        self.cacheHeight = cacheHeight
        self.ncols = 2

    # ----------------------------------------------------------------------------
    def getPreview(self, index):
        itemName = super().data(index, QtCore.Qt.DisplayRole)

        #TODO: add check to not show nef pictures
        if itemName not in self.previews:
            qpm = QtGui.QPixmap(self.rootPath() + "/" + itemName)

            if qpm is None or qpm.isNull():
                qpm = super().data(index, QtCore.Qt.DecorationRole)
                if qpm and not qpm.isNull():
                    qpm = qpm.pixmap(self.cacheWidth, self.cacheHeight)
            if qpm and not qpm.isNull():
                qpm = qpm.scaled(self.cacheWidth, self.cacheHeight, QtCore.Qt.KeepAspectRatio)

            self.previews[itemName] = qpm
        return self.previews[itemName]

    # ----------------------------------------------------------------------------
    def data(self, index, role):
        if role == QtCore.Qt.DecorationRole:
            return self.getPreview(index)
        else:
            return super().data(index, role)


# ---------------------------------------------------------------------------------------------------------
class ImageChooser(QtWidgets.QDialog):
    def __init__(self, dir_path):
        super(ImageChooser, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.selected_file = None
        self.index = None
        self.gridSize = QtCore.QSize(150, 150)
        self.setWindowTitle("Open File")
        self.path = dir_path
        self.files = clsFilePreviewModel()
        self.files.setRootPath(self.path)

        self.view = self.findChild(QtWidgets.QListView, "listView")
        self.view.setModel(self.files)
        self.view.setRootIndex(self.files.index(dir_path))
        self.view.setViewMode(QtWidgets.QListView.IconMode)
        self.view.setGridSize(self.gridSize)
        self.view.setMovement(QtWidgets.QListView.Static)
        self.view.clicked.connect(self.on_view_clicked)
        self.dialog_buttons = self.findChild(QtWidgets.QDialogButtonBox, "buttonBox")
        self.open_button = self.dialog_buttons.button(QtWidgets.QDialogButtonBox.Open)

    def accept(self):
        if self.index:
            self.selected_file = self.files.filePath(self.index)
            super().accept()

    def on_view_clicked(self, index):
        self.index = index
