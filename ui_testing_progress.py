# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_testing_progress.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_testingProgressDialog(object):
    def setupUi(self, testingProgressDialog):
        if not testingProgressDialog.objectName():
            testingProgressDialog.setObjectName(u"testingProgressDialog")
        testingProgressDialog.resize(411, 352)
        testingProgressDialog.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(100, 15, 15, 255), stop:1 rgba(70, 90, 110, 255));\n"
"font: 600 12pt \"Yu Gothic UI\";\n"
"color: white;\n"
"\n"
"")
        self.cancelButton = QPushButton(testingProgressDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(90, 280, 231, 41))
        self.cancelButton.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(100, 20, 30, 253), stop:1 rgba(200, 60, 80, 255));\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"font-size: 14pt;")
        self.mainFrame = QFrame(testingProgressDialog)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(20, 20, 371, 251))
        self.mainFrame.setStyleSheet(u"background: rgba(255. 255. 255. 0);\n"
"margin: 5;\n"
"border-radius: 7;")
        self.verticalLayout = QVBoxLayout(self.mainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.firstStat = QHBoxLayout()
        self.firstStat.setObjectName(u"firstStat")
        self.firstStatName = QLabel(self.mainFrame)
        self.firstStatName.setObjectName(u"firstStatName")
        self.firstStatName.setStyleSheet(u"qproperty-alignment: AlignLeft;")

        self.firstStat.addWidget(self.firstStatName)

        self.vfirstStatValue = QLabel(self.mainFrame)
        self.vfirstStatValue.setObjectName(u"vfirstStatValue")
        self.vfirstStatValue.setStyleSheet(u"qproperty-alignment: AlignRight;")

        self.firstStat.addWidget(self.vfirstStatValue)


        self.verticalLayout.addLayout(self.firstStat)

        self.secondStat = QHBoxLayout()
        self.secondStat.setObjectName(u"secondStat")
        self.secondStatName = QLabel(self.mainFrame)
        self.secondStatName.setObjectName(u"secondStatName")
        self.secondStatName.setStyleSheet(u"qproperty-alignment: AlignLeft;")

        self.secondStat.addWidget(self.secondStatName)

        self.secondStatValue = QLabel(self.mainFrame)
        self.secondStatValue.setObjectName(u"secondStatValue")
        self.secondStatValue.setStyleSheet(u"qproperty-alignment: AlignRight;")

        self.secondStat.addWidget(self.secondStatValue)


        self.verticalLayout.addLayout(self.secondStat)

        self.thirdStat = QHBoxLayout()
        self.thirdStat.setObjectName(u"thirdStat")
        self.thirdStatName = QLabel(self.mainFrame)
        self.thirdStatName.setObjectName(u"thirdStatName")
        self.thirdStatName.setStyleSheet(u"qproperty-alignment: AlignLeft;")

        self.thirdStat.addWidget(self.thirdStatName)

        self.thirdStatValue = QLabel(self.mainFrame)
        self.thirdStatValue.setObjectName(u"thirdStatValue")
        self.thirdStatValue.setStyleSheet(u"qproperty-alignment: AlignRight;")

        self.thirdStat.addWidget(self.thirdStatValue)


        self.verticalLayout.addLayout(self.thirdStat)

        self.fourthStat = QHBoxLayout()
        self.fourthStat.setObjectName(u"fourthStat")
        self.fourthStatName = QLabel(self.mainFrame)
        self.fourthStatName.setObjectName(u"fourthStatName")
        self.fourthStatName.setStyleSheet(u"qproperty-alignment: AlignLeft;")

        self.fourthStat.addWidget(self.fourthStatName)

        self.fourthStatValue = QLabel(self.mainFrame)
        self.fourthStatValue.setObjectName(u"fourthStatValue")
        self.fourthStatValue.setStyleSheet(u"qproperty-alignment: AlignRight;")

        self.fourthStat.addWidget(self.fourthStatValue)


        self.verticalLayout.addLayout(self.fourthStat)

        self.progressBar = QProgressBar(self.mainFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(16)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(testingProgressDialog)

        QMetaObject.connectSlotsByName(testingProgressDialog)
    # setupUi

    def retranslateUi(self, testingProgressDialog):
        testingProgressDialog.setWindowTitle(QCoreApplication.translate("testingProgressDialog", u"Testing Progress", None))
        self.cancelButton.setText(QCoreApplication.translate("testingProgressDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.firstStatName.setText(QCoreApplication.translate("testingProgressDialog", u"\u0412\u0441\u0435\u0433\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u043e\u0432:", None))
        self.vfirstStatValue.setText(QCoreApplication.translate("testingProgressDialog", u"\u0427\u0438\u0441\u043b\u043e", None))
        self.secondStatName.setText(QCoreApplication.translate("testingProgressDialog", u"\u041d\u043e\u043c\u0435\u0440 \u0440\u0430\u0437\u0434\u0435\u043b\u0430:", None))
        self.secondStatValue.setText(QCoreApplication.translate("testingProgressDialog", u"\u0427\u0438\u0441\u043b\u043e", None))
        self.thirdStatName.setText(QCoreApplication.translate("testingProgressDialog", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u0442\u0435\u0441\u0442\u043e\u0432 \u0432 \u0440\u0430\u0437\u0434\u0435\u043b\u0435:", None))
        self.thirdStatValue.setText(QCoreApplication.translate("testingProgressDialog", u"\u0427\u0438\u0441\u043b\u043e", None))
        self.fourthStatName.setText(QCoreApplication.translate("testingProgressDialog", u"\u0412\u0441\u0435\u0433\u043e \u043f\u0440\u043e\u0439\u0434\u0435\u043d\u043e \u0442\u0435\u0441\u0442\u043e\u0432:", None))
        self.fourthStatValue.setText(QCoreApplication.translate("testingProgressDialog", u"\u0427\u0438\u0441\u043b\u043e", None))
    # retranslateUi

