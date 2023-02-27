from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QFileDialog, QVBoxLayout, QLabel



class QFileDialogPreview(QFileDialog):
    def __init__(self, *args, **kwargs):
        QFileDialog.__init__(self, *args, **kwargs)
        self.setOption(QFileDialog.DontUseNativeDialog, True)
        #self.thumbnail_delegate = QThumbnailDelegate()
        box = QVBoxLayout()

        self.setFixedSize(self.width() + 250, self.height())

        self.mpPreview = QLabel("Preview", self)
        self.mpPreview.setFixedSize(250, 250)
        self.mpPreview.setAlignment(Qt.AlignCenter)
        self.mpPreview.setObjectName("labelPreview")
        box.addWidget(self.mpPreview)

        box.addStretch()

        self.layout().addLayout(box, 1, 3, 1, 1)
        self.currentChanged.connect(self.onChange)
        self.fileSelected.connect(self.onFileSelected)
        self.filesSelected.connect(self.onFilesSelected)
        #self.currentUrlChanged.connect(self.resetDelegateCache)

        self._fileSelected = None
        self._filesSelected = None

    #def resetDelegateCache(self):
        #self.thumbnail_delegate.resetCache()

    def onChange(self, path):
        #pixmap = QPixmap(path)
        thumbnail = QIcon(path)

        if thumbnail.isNull():
            self.mpPreview.setText("Preview")
        else:
            self.mpPreview.setPixmap(thumbnail.pixmap(thumbnail.actualSize(QSize(256, 256))).scaled(self.mpPreview.width(), self.mpPreview.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def onFileSelected(self, file):
        self._fileSelected = file

    def onFilesSelected(self, files):
        self._filesSelected = files

    def getFileSelected(self):
        return self._fileSelected

    def getFilesSelected(self):
        return self._filesSelected