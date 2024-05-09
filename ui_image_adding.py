# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_image_adding.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_sendImageDialog(object):
    def setupUi(self, sendImageDialog):
        if not sendImageDialog.objectName():
            sendImageDialog.setObjectName(u"sendImageDialog")
        sendImageDialog.resize(492, 521)
        sendImageDialog.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(100, 15, 15, 255), stop:1 rgba(70, 90, 110, 255));\n"
"font: 600 12pt \"Yu Gothic UI\";\n"
"color: white;\n"
"\n"
"")
        self.sendButton = QPushButton(sendImageDialog)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(90, 460, 311, 41))
        self.sendButton.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(20, 100, 30, 253), stop:1 rgba(60, 200, 80, 255));\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"font-size: 16pt;\n"
"border-radius: 7;")
        self.mainFrame = QFrame(sendImageDialog)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(30, 20, 431, 421))
        self.mainFrame.setStyleSheet(u"background: rgba(255. 255. 255. 0);\n"
"margin: 0;\n"
"border-radius: 7;")
        self.verticalLayout_3 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.fileFrame = QFrame(self.mainFrame)
        self.fileFrame.setObjectName(u"fileFrame")
        self.fileFrame.setStyleSheet(u"background: rgba(255. 255. 255. 0);\n"
"margin: 0;\n"
"border-radius: 7;")
        self.verticalLayout = QVBoxLayout(self.fileFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fileLabel = QLabel(self.fileFrame)
        self.fileLabel.setObjectName(u"fileLabel")
        self.fileLabel.setStyleSheet(u"qproperty-alignment: AlignCenter;\n"
"font-size: 16pt;")

        self.verticalLayout.addWidget(self.fileLabel)

        self.fileLineEdit = QLineEdit(self.fileFrame)
        self.fileLineEdit.setObjectName(u"fileLineEdit")
        self.fileLineEdit.setStyleSheet(u"background: rgba(0, 0, 0, 200);\n"
"font: 12pt \"Courier New\";")

        self.verticalLayout.addWidget(self.fileLineEdit)


        self.verticalLayout_3.addWidget(self.fileFrame)

        self.nameComboBox = QComboBox(self.mainFrame)
        self.nameComboBox.addItem("")
        self.nameComboBox.setObjectName(u"nameComboBox")
        self.nameComboBox.setStyleSheet(u"background: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);")

        self.verticalLayout_3.addWidget(self.nameComboBox)

        self.genderComboBox = QComboBox(self.mainFrame)
        self.genderComboBox.addItem("")
        self.genderComboBox.setObjectName(u"genderComboBox")
        self.genderComboBox.setStyleSheet(u"background: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);")

        self.verticalLayout_3.addWidget(self.genderComboBox)

        self.raceComboBox = QComboBox(self.mainFrame)
        self.raceComboBox.addItem("")
        self.raceComboBox.setObjectName(u"raceComboBox")
        self.raceComboBox.setStyleSheet(u"background: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);")

        self.verticalLayout_3.addWidget(self.raceComboBox)

        self.optionsFrame = QFrame(self.mainFrame)
        self.optionsFrame.setObjectName(u"optionsFrame")
        self.optionsFrame.setStyleSheet(u"background: rgba(255. 255. 255. 0);\n"
"margin: 0;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.optionsFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.optionsLabel = QLabel(self.optionsFrame)
        self.optionsLabel.setObjectName(u"optionsLabel")
        self.optionsLabel.setStyleSheet(u"qproperty-alignment: AlignCenter;\n"
"font-size: 16pt;")

        self.verticalLayout_2.addWidget(self.optionsLabel)

        self.optionsLayout = QHBoxLayout()
        self.optionsLayout.setObjectName(u"optionsLayout")
        self.optionsComboBox = QComboBox(self.optionsFrame)
        self.optionsComboBox.addItem("")
        self.optionsComboBox.addItem("")
        self.optionsComboBox.setObjectName(u"optionsComboBox")
        self.optionsComboBox.setStyleSheet(u"background: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);")

        self.optionsLayout.addWidget(self.optionsComboBox)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.addButton = QPushButton(self.optionsFrame)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(20, 100, 30, 253), stop:1 rgba(60, 200, 80, 255));\n"
"border: 1px solid rgba(255, 255, 255, 40);")

        self.buttonsLayout.addWidget(self.addButton)

        self.deleteButton = QPushButton(self.optionsFrame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(100, 20, 30, 253), stop:1 rgba(200, 60, 80, 255));\n"
"border: 1px solid rgba(255, 255, 255, 40);")

        self.buttonsLayout.addWidget(self.deleteButton)


        self.optionsLayout.addLayout(self.buttonsLayout)


        self.verticalLayout_2.addLayout(self.optionsLayout)

        self.optionsListView = QListView(self.optionsFrame)
        self.optionsListView.setObjectName(u"optionsListView")
        self.optionsListView.setStyleSheet(u"background: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);")

        self.verticalLayout_2.addWidget(self.optionsListView)


        self.verticalLayout_3.addWidget(self.optionsFrame)


        self.retranslateUi(sendImageDialog)

        QMetaObject.connectSlotsByName(sendImageDialog)
    # setupUi

    def retranslateUi(self, sendImageDialog):
        sendImageDialog.setWindowTitle(QCoreApplication.translate("sendImageDialog", u"Dialog", None))
        self.sendButton.setText(QCoreApplication.translate("sendImageDialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.fileLabel.setText(QCoreApplication.translate("sendImageDialog", u"\u0424\u0430\u0439\u043b", None))
        self.fileLineEdit.setText("")
        self.nameComboBox.setItemText(0, QCoreApplication.translate("sendImageDialog", u"Anya Taylor-Joy", None))

        self.genderComboBox.setItemText(0, QCoreApplication.translate("sendImageDialog", u"female", None))

        self.raceComboBox.setItemText(0, QCoreApplication.translate("sendImageDialog", u"Europoid", None))

        self.optionsLabel.setText(QCoreApplication.translate("sendImageDialog", u"\u041e\u043f\u0446\u0438\u0438", None))
        self.optionsComboBox.setItemText(0, QCoreApplication.translate("sendImageDialog", u"first", None))
        self.optionsComboBox.setItemText(1, QCoreApplication.translate("sendImageDialog", u"second", None))

        self.addButton.setText(QCoreApplication.translate("sendImageDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.deleteButton.setText(QCoreApplication.translate("sendImageDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

