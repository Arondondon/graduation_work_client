import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_main import Ui_mainWindow


class TestingMainWindow(QMainWindow):
    def __init__(self):
        super(TestingMainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestingMainWindow()
    window.show()
    sys.exit(app.exec())

