# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(823, 573)
        mainWindow.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(100, 15, 15, 255), stop:1 rgba(70, 90, 110, 255));\n"
"font: 600 12pt \"Yu Gothic UI\";\n"
"color: white;\n"
"\n"
"")
        self.centralWidget = QWidget(mainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.startButton = QPushButton(self.centralWidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(180, 460, 471, 51))
        self.startButton.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(20, 100, 30, 253), stop:1 rgba(60, 200, 80, 255));\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"font-size: 16pt;\n"
"border-radius: 7;")
        self.cmdFrame = QFrame(self.centralWidget)
        self.cmdFrame.setObjectName(u"cmdFrame")
        self.cmdFrame.setGeometry(QRect(30, 50, 761, 81))
        self.cmdFrame.setStyleSheet(u"background: rgba(255. 255. 255. 0);\n"
"margin: 0;\n"
"border-radius: 7;")
        self.verticalLayout = QVBoxLayout(self.cmdFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cmdLabel = QLabel(self.cmdFrame)
        self.cmdLabel.setObjectName(u"cmdLabel")
        self.cmdLabel.setStyleSheet(u"qproperty-alignment: AlignCenter;\n"
"font-size: 16pt;")

        self.verticalLayout.addWidget(self.cmdLabel)

        self.cmdLineEdit = QLineEdit(self.cmdFrame)
        self.cmdLineEdit.setObjectName(u"cmdLineEdit")
        self.cmdLineEdit.setStyleSheet(u"background: rgba(0, 0, 0, 200);\n"
"font: 12pt \"Courier New\";")

        self.verticalLayout.addWidget(self.cmdLineEdit)

        self.optionsFrame = QFrame(self.centralWidget)
        self.optionsFrame.setObjectName(u"optionsFrame")
        self.optionsFrame.setGeometry(QRect(180, 160, 471, 265))
        self.optionsFrame.setStyleSheet(u"background: rgba(255. 255. 255. 0);\n"
"margin: 0;\n"
"border-radius: 7;")
        self.verticalLayout_2 = QVBoxLayout(self.optionsFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.optionsLabel = QLabel(self.optionsFrame)
        self.optionsLabel.setObjectName(u"optionsLabel")
        self.optionsLabel.setStyleSheet(u"qproperty-alignment: AlignCenter;\n"
"font-size: 16pt;")

        self.verticalLayout_2.addWidget(self.optionsLabel)

        self.optionsLayout = QHBoxLayout()
        self.optionsLayout.setSpacing(3)
        self.optionsLayout.setObjectName(u"optionsLayout")
        self.optionsComboBox = QComboBox(self.optionsFrame)
        self.optionsComboBox.addItem("")
        self.optionsComboBox.addItem("")
        self.optionsComboBox.setObjectName(u"optionsComboBox")
        self.optionsComboBox.setMinimumSize(QSize(300, 0))
        self.optionsComboBox.setStyleSheet(u"background: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);")

        self.optionsLayout.addWidget(self.optionsComboBox)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.addButton = QPushButton(self.optionsFrame)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(80, 0))
        self.addButton.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(20, 100, 30, 253), stop:1 rgba(60, 200, 80, 255));\n"
"border: 1px solid rgba(255, 255, 255, 40);")

        self.buttonsLayout.addWidget(self.addButton)

        self.deleteButton = QPushButton(self.optionsFrame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMinimumSize(QSize(80, 0))
        self.deleteButton.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(100, 20, 30, 253), stop:1 rgba(200, 60, 80, 255));\n"
"border: 1px solid rgba(255, 255, 255, 40);")

        self.buttonsLayout.addWidget(self.deleteButton)


        self.optionsLayout.addLayout(self.buttonsLayout)


        self.verticalLayout_2.addLayout(self.optionsLayout)

        self.optionsListWidget = QListWidget(self.optionsFrame)
        self.optionsListWidget.setObjectName(u"optionsListWidget")
        self.optionsListWidget.setStyleSheet(u"background: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);")
        self.optionsListWidget.setItemAlignment(Qt.AlignmentFlag.AlignLeading)

        self.verticalLayout_2.addWidget(self.optionsListWidget)

        self.uploadButton = QPushButton(self.centralWidget)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setGeometry(QRect(10, 540, 151, 21))
        self.uploadButton.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(117, 23, 23, 255), stop:1 rgba(119, 120, 146, 255));\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"font-size: 8pt;\n"
"border-radius: 7;")
        mainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Face Recognition Systems Testing", None))
        self.startButton.setText(QCoreApplication.translate("mainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.cmdLabel.setText(QCoreApplication.translate("mainWindow", u"\u041a\u043e\u043c\u0430\u043d\u0434\u0430 \u0434\u043b\u044f \u0437\u0430\u043f\u0443\u0441\u043a\u0430 \u0442\u0435\u0441\u0442\u0438\u0440\u0443\u0435\u043c\u043e\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u044b", None))
        self.cmdLineEdit.setText("")
        self.optionsLabel.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043f\u0446\u0438\u0438", None))
        self.optionsComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"Testing with tag PARTLY_COVERED_FACE", None))
        self.optionsComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"Simple Testing", None))

        self.addButton.setText(QCoreApplication.translate("mainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.deleteButton.setText(QCoreApplication.translate("mainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.uploadButton.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
    # retranslateUi

