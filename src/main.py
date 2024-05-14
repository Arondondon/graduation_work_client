import sys
#import time

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
#from PySide6.QtCore import QRunnable, QThreadPool, Slot

from src.actions.testing import Testing
from src.actions.server_requests import ServerConnection
from src.ui.ui_main import Ui_mainWindow
from src.ui.ui_image_adding import Ui_sendImageDialog
from src.ui.ui_results import Ui_resultsDialog
from src.ui.ui_testing_progress import Ui_testingProgressDialog


class TestingMainWindow(QMainWindow):
    def __init__(self):
        super(TestingMainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.conn = ServerConnection()

        self.ui_send_image_window = Ui_sendImageDialog()
        self.image_properties_items = []
        self.ui.uploadButton.clicked.connect(self.open_adding_image_window)

        self.ui.optionsComboBox.clear()
        self.ui_testing_progress_window = Ui_testingProgressDialog()
        self.ui.startButton.clicked.connect(self.open_testing_window)
        self.ui.addButton.clicked.connect(self.add_testing_option_to_list)

        self.ui_results_window = Ui_resultsDialog()

        self.testing = Testing(self.ui_testing_progress_window, self.ui_results_window)
        self.testing_options_items = []
        self.ui.optionsComboBox.addItems(self.testing.get_testing_options())

    def open_adding_image_window(self):
        self.new_adding_image_window = QtWidgets.QDialog()
        self.ui_send_image_window.setupUi(self.new_adding_image_window)
        self.conn.set_options_lists_for_image_adding(self.ui_send_image_window)
        self.ui_send_image_window.addButton.clicked.connect(self.add_image_property_to_list)
        self.ui_send_image_window.sendButton.clicked.connect(self.add_new_image_to_send)
        self.new_adding_image_window.show()

    def open_testing_window(self):
        self.new_testing_progress_window = QtWidgets.QDialog()
        self.ui_testing_progress_window.setupUi(self.new_testing_progress_window)

        self.ui_testing_progress_window.firstStatValue.setText('0')
        self.ui_testing_progress_window.secondStatValue.setText('0')
        self.ui_testing_progress_window.thirdStatValue.setText('0')
        self.ui_testing_progress_window.fourthStatValue.setText('0')
        self.ui_testing_progress_window.progressBar.setValue(0)

        self.ui_testing_progress_window.startButton.clicked.connect(self.start_testing)
        self.new_testing_progress_window.show()

    def open_results_window(self):
        self.new_testing_progress_window.close()

        self.new_results_window = QtWidgets.QDialog()
        self.ui_results_window.setupUi(self.new_results_window)
        self.new_results_window.show()

        self.testing.set_results()

    def start_testing(self):
        command = self.ui.cmdLineEdit.text()
        self.testing.start(command, self.testing_options_items)
        self.open_results_window()

    def add_image_property_to_list(self):
        text = self.ui_send_image_window.optionsComboBox.currentText()
        self.image_properties_items.append(text)
        self.ui_send_image_window.optionsListWidget.clear()
        for text in self.image_properties_items:
            item = QtWidgets.QListWidgetItem(text)
            self.ui_send_image_window.optionsListWidget.addItem(item)

    def add_testing_option_to_list(self):
        text = self.ui.optionsComboBox.currentText()
        if text not in self.testing_options_items:
            self.testing_options_items.append(text)
        self.ui.optionsListWidget.clear()
        for option in self.testing_options_items:
            item = QtWidgets.QListWidgetItem(option)
            self.ui.optionsListWidget.addItem(item)

    def add_new_image_to_send(self):
        path = self.ui_send_image_window.fileLineEdit.text()
        name = self.ui_send_image_window.nameComboBox.currentText()
        gender = self.ui_send_image_window.genderComboBox.currentText()
        race = self.ui_send_image_window.raceComboBox.currentText()
        properties = self.image_properties_items
        self.conn.send_image(path, name, properties)
        self.ui_send_image_window.optionsListWidget.clear()
        self.image_properties_items.clear()
        #self.new_adding_image_window.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestingMainWindow()
    window.show()
    sys.exit(app.exec())

