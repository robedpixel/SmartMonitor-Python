import os

from PySide2.QtCore import Qt, QSize, QLocale, QPoint
from PySide2.QtGui import QPixmap, QIcon, QFontMetrics, QPen, QBrush
from PySide2.QtWidgets import QStyledItemDelegate, QFileSystemModel, QStyleOptionViewItem, QStyle


def getThumbnail(filename):
    icon = QIcon(filename)
    return icon


class QThumbnailDelegate(QStyledItemDelegate):
    def __init__(self, *args, **kwargs):
        QStyledItemDelegate.__init__(self, *args, **kwargs)
        self.thumbnail = None
        self.filemodel = QFileSystemModel(self)
        self.cache = {}

    def resetCache(self):
        self.cache.clear()

    def paint(self, painter, option, index):

        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight());
            painter.setPen(Qt.white)
            painter.setBrush(option.palette.highlightedText());
        else:
            painter.setPen(QPen(option.palette.foreground(), 0));
            painter.setBrush(QBrush(index.data(Qt.ForegroundRole)))

        fontMetrics = painter.fontMetrics()
        sFile = self.getFilenameFromModelIndex(index)
        if sFile in self.cache:
            pixmap = self.cache[sFile]
        else:
            if os.path.isdir(sFile):
                self.thumbnail = getThumbnail("resources/folder.png")
            else:
                self.thumbnail = getThumbnail(sFile)
            pixmap = self.thumbnail.pixmap(self.thumbnail.actualSize(QSize(256, 256)))
            self.cache[sFile] = pixmap
        printrect = option.rect
        printrect.setTopLeft(QPoint(printrect.topLeft().x()+option.rect.height(), printrect.topLeft().y()))
        painter.drawText(printrect, fontMetrics.elidedText(self.displayText(index.data(), QLocale.system()),
                                                             Qt.TextElideMode.ElideMiddle, printrect.width()),
                         option.displayAlignment)
        #if option.state & QStyle.State_Selected:
        #    painter.setPen(Qt.white)
        #    painter.setBrush(option.palette.highlightedText())
        #    style.drawControl(QStyle::CE_ItemViewItem, & opt, painter, widget)
        #else:
        #    painter.setPen(QPen(option.palette.foreground(), 0))
        #    painter.setBrush(qvariant_cast < QBrush > (index.data(Qt::ForegroundRole)))

        auxOption = QStyleOptionViewItem(option)
        if not pixmap.isNull() and index.column() == 0:
            auxOption.displayAlignment = Qt.AlignLeft | Qt.AlignVCenter
            auxOption.rect.setWidth(option.rect.height())
            auxOption.rect.moveTopLeft(QPoint(auxOption.rect.topLeft().x()-option.rect.height(), auxOption.rect.topLeft().y()))
            painter.drawPixmap(auxOption.rect, pixmap)

    def getFilenameFromModelIndex(self, index):
        filename = self.filemodel.filePath(index)
        return filename
