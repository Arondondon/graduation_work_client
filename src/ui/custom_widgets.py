from PySide6 import QtWidgets, QtCore


class ScaledLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        QtWidgets.QLabel.__init__(self)
        self._pixmap = self.pixmap()
        self._resized = False

    def setPixmap(self, pixmap):
        if not pixmap:
            return
        self._pixmap = pixmap
        return QtWidgets.QLabel.setPixmap(self, self._pixmap.scaled(self.frameSize(), QtCore.Qt.KeepAspectRatio))
