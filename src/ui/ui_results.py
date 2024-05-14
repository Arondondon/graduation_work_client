# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_results.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

from src.ui.custom_widgets import ScaledLabel

class Ui_resultsDialog(object):
    def setupUi(self, resultsDialog):
        if not resultsDialog.objectName():
            resultsDialog.setObjectName(u"resultsDialog")
        resultsDialog.resize(812, 682)
        resultsDialog.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(100, 15, 15, 255), stop:1 rgba(70, 90, 110, 255));\n"
"font: 600 12pt \"Yu Gothic UI\";\n"
"color: white;\n"
"\n"
"")
        self.frame = QFrame(resultsDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 0, 771, 261))
        self.frame.setStyleSheet(u"background: rgba(255, 255, 255, 0);\n"
"margin: 0;\n"
"border-radius: 7;")
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.resultsLabel = QLabel(self.frame)
        self.resultsLabel.setObjectName(u"resultsLabel")
        self.resultsLabel.setMinimumSize(QSize(0, 40))
        self.resultsLabel.setStyleSheet(u"background: rgba(255, 255, 255, 0);\n"
"margin: 0;\n"
"border-radius: 7;\n"
"font-size: 18pt;")
        self.resultsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.resultsLabel)

        self.resultsFrame = QFrame(self.frame)
        self.resultsFrame.setObjectName(u"resultsFrame")
        self.resultsFrame.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.resultsFrame)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.frame1 = QFrame(self.resultsFrame)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(300, 0))
        self.verticalLayout = QVBoxLayout(self.frame1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, -1, 1, -1)
        self.generalResultsLabel = QLabel(self.frame1)
        self.generalResultsLabel.setObjectName(u"generalResultsLabel")
        self.generalResultsLabel.setMinimumSize(QSize(0, 28))
        self.generalResultsLabel.setMaximumSize(QSize(16777215, 28))
        self.generalResultsLabel.setStyleSheet(u"qproperty-alignment: AlignCenter;\n"
"font-size: 14pt;")

        self.verticalLayout.addWidget(self.generalResultsLabel)

        self.firstStat = QHBoxLayout()
        self.firstStat.setObjectName(u"firstStat")
        self.firstStatName = QLabel(self.frame1)
        self.firstStatName.setObjectName(u"firstStatName")
        self.firstStatName.setStyleSheet(u"")
        self.firstStatName.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.firstStat.addWidget(self.firstStatName)

        self.firstStatValue = QLabel(self.frame1)
        self.firstStatValue.setObjectName(u"firstStatValue")
        self.firstStatValue.setStyleSheet(u"")
        self.firstStatValue.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.firstStat.addWidget(self.firstStatValue)


        self.verticalLayout.addLayout(self.firstStat)

        self.secondStat = QHBoxLayout()
        self.secondStat.setObjectName(u"secondStat")
        self.secondStatName = QLabel(self.frame1)
        self.secondStatName.setObjectName(u"secondStatName")
        self.secondStatName.setStyleSheet(u"")
        self.secondStatName.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.secondStat.addWidget(self.secondStatName)

        self.secondStatValue = QLabel(self.frame1)
        self.secondStatValue.setObjectName(u"secondStatValue")
        self.secondStatValue.setStyleSheet(u"")
        self.secondStatValue.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.secondStat.addWidget(self.secondStatValue)


        self.verticalLayout.addLayout(self.secondStat)

        self.thirdStat = QHBoxLayout()
        self.thirdStat.setObjectName(u"thirdStat")
        self.thirdStatName = QLabel(self.frame1)
        self.thirdStatName.setObjectName(u"thirdStatName")
        self.thirdStatName.setStyleSheet(u"")
        self.thirdStatName.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.thirdStat.addWidget(self.thirdStatName)

        self.thirdStatValue = QLabel(self.frame1)
        self.thirdStatValue.setObjectName(u"thirdStatValue")
        self.thirdStatValue.setStyleSheet(u"")
        self.thirdStatValue.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.thirdStat.addWidget(self.thirdStatValue)


        self.verticalLayout.addLayout(self.thirdStat)

        self.fourthStat = QHBoxLayout()
        self.fourthStat.setObjectName(u"fourthStat")
        self.fourthStatName = QLabel(self.frame1)
        self.fourthStatName.setObjectName(u"fourthStatName")
        self.fourthStatName.setStyleSheet(u"")
        self.fourthStatName.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.fourthStat.addWidget(self.fourthStatName)

        self.fourthStatValue = QLabel(self.frame1)
        self.fourthStatValue.setObjectName(u"fourthStatValue")
        self.fourthStatValue.setStyleSheet(u"")
        self.fourthStatValue.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.fourthStat.addWidget(self.fourthStatValue)


        self.verticalLayout.addLayout(self.fourthStat)

        self.fifthStat = QHBoxLayout()
        self.fifthStat.setObjectName(u"fifthStat")
        self.fifthStatName = QLabel(self.frame1)
        self.fifthStatName.setObjectName(u"fifthStatName")
        self.fifthStatName.setStyleSheet(u"")
        self.fifthStatName.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.fifthStat.addWidget(self.fifthStatName)

        self.fifthStatValue = QLabel(self.frame1)
        self.fifthStatValue.setObjectName(u"fifthStatValue")
        self.fifthStatValue.setStyleSheet(u"")
        self.fifthStatValue.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.fifthStat.addWidget(self.fifthStatValue)


        self.verticalLayout.addLayout(self.fifthStat)


        self.horizontalLayout.addWidget(self.frame1)

        self.frame2 = QFrame(self.resultsFrame)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setMinimumSize(QSize(350, 0))
        self.verticalLayout_2 = QVBoxLayout(self.frame2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sectionsLabel = QLabel(self.frame2)
        self.sectionsLabel.setObjectName(u"sectionsLabel")
        self.sectionsLabel.setMinimumSize(QSize(0, 28))
        self.sectionsLabel.setStyleSheet(u"qproperty-alignment: AlignCenter;\n"
"font-size: 14pt;")

        self.verticalLayout_2.addWidget(self.sectionsLabel)

        self.sectionsComboBox = QComboBox(self.frame2)
        self.sectionsComboBox.setObjectName(u"sectionsComboBox")
        self.sectionsComboBox.setStyleSheet(u"background: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);")

        self.verticalLayout_2.addWidget(self.sectionsComboBox)

        self.resultsTextEdit = QTextEdit(self.frame2)
        self.resultsTextEdit.setObjectName(u"resultsTextEdit")
        self.resultsTextEdit.setMinimumSize(QSize(0, 0))
        self.resultsTextEdit.setStyleSheet(u"background: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7;\n"
"font-size: 10pt;\n"
"")
        self.resultsTextEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.resultsTextEdit)


        self.horizontalLayout.addWidget(self.frame2)


        self.verticalLayout_3.addWidget(self.resultsFrame)

        self.failedTestsFrame = QFrame(resultsDialog)
        self.failedTestsFrame.setObjectName(u"failedTestsFrame")
        self.failedTestsFrame.setGeometry(QRect(20, 280, 771, 381))
        self.failedTestsFrame.setStyleSheet(u"background: rgba(255, 255, 255, 0);\n"
"margin: 0;\n"
"border-radius: 7;")
        self.verticalLayout_4 = QVBoxLayout(self.failedTestsFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.failedTestsLabel = QLabel(self.failedTestsFrame)
        self.failedTestsLabel.setObjectName(u"failedTestsLabel")
        self.failedTestsLabel.setMinimumSize(QSize(0, 28))
        self.failedTestsLabel.setMaximumSize(QSize(16777215, 28))
        self.failedTestsLabel.setStyleSheet(u"qproperty-alignment: AlignCenter;\n"
"font-size: 14pt;")

        self.verticalLayout_4.addWidget(self.failedTestsLabel)

        self.imagesLayout = QHBoxLayout()
        self.imagesLayout.setSpacing(10)
        self.imagesLayout.setObjectName(u"imagesLayout")
        self.imagesLayout.setContentsMargins(-1, 10, -1, -1)
        self.previousButton = QPushButton(self.failedTestsFrame)
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.setMinimumSize(QSize(0, 100))
        self.previousButton.setMaximumSize(QSize(31, 16777215))
        self.previousButton.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(100, 15, 15, 255), stop:1 rgba(70, 90, 110, 255));\n"
"border: 1px solid rgba(255, 255, 255, 50);")

        self.imagesLayout.addWidget(self.previousButton)

        self.firstImage = ScaledLabel(self.failedTestsFrame)
        self.firstImage.setObjectName(u"firstImage")
        self.firstImage.setMinimumSize(QSize(0, 279))
        self.firstImage.setMaximumSize(QSize(337, 16777215))
        self.firstImage.setStyleSheet(u"background: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);")
        self.firstImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.imagesLayout.addWidget(self.firstImage)

        self.secondImage = ScaledLabel(self.failedTestsFrame)
        self.secondImage.setObjectName(u"secondImage")
        self.secondImage.setMinimumSize(QSize(0, 279))
        self.secondImage.setMaximumSize(QSize(337, 16777215))
        self.secondImage.setStyleSheet(u"background: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);")
        self.secondImage.setScaledContents(False)
        self.secondImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.imagesLayout.addWidget(self.secondImage)

        self.nextButton = QPushButton(self.failedTestsFrame)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMinimumSize(QSize(0, 100))
        self.nextButton.setMaximumSize(QSize(31, 16777215))
        self.nextButton.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(100, 15, 15, 255), stop:1 rgba(70, 90, 110, 255));\n"
"border: 1px solid rgba(255, 255, 255, 50);")

        self.imagesLayout.addWidget(self.nextButton)


        self.verticalLayout_4.addLayout(self.imagesLayout)

        self.expectedStat = QHBoxLayout()
        self.expectedStat.setObjectName(u"expectedStat")
        self.expectedStatName = QLabel(self.failedTestsFrame)
        self.expectedStatName.setObjectName(u"expectedStatName")
        self.expectedStatName.setStyleSheet(u"")
        self.expectedStatName.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.expectedStat.addWidget(self.expectedStatName)

        self.expectedStatValue = QLabel(self.failedTestsFrame)
        self.expectedStatValue.setObjectName(u"expectedStatValue")
        self.expectedStatValue.setMaximumSize(QSize(260, 16777215))
        self.expectedStatValue.setStyleSheet(u"")
        self.expectedStatValue.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.expectedStat.addWidget(self.expectedStatValue)


        self.verticalLayout_4.addLayout(self.expectedStat)

        self.actualStat = QHBoxLayout()
        self.actualStat.setObjectName(u"actualStat")
        self.actualStatName = QLabel(self.failedTestsFrame)
        self.actualStatName.setObjectName(u"actualStatName")
        self.actualStatName.setStyleSheet(u"")
        self.actualStatName.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.actualStat.addWidget(self.actualStatName)

        self.actualStatValue = QLabel(self.failedTestsFrame)
        self.actualStatValue.setObjectName(u"actualStatValue")
        self.actualStatValue.setMaximumSize(QSize(260, 16777215))
        self.actualStatValue.setStyleSheet(u"")
        self.actualStatValue.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.actualStat.addWidget(self.actualStatValue)


        self.verticalLayout_4.addLayout(self.actualStat)


        self.retranslateUi(resultsDialog)

        QMetaObject.connectSlotsByName(resultsDialog)
    # setupUi

    def retranslateUi(self, resultsDialog):
        resultsDialog.setWindowTitle(QCoreApplication.translate("resultsDialog", u"Dialog", None))
        self.resultsLabel.setText(QCoreApplication.translate("resultsDialog", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.generalResultsLabel.setText(QCoreApplication.translate("resultsDialog", u"\u041e\u0431\u0449\u0438\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.firstStatName.setText(QCoreApplication.translate("resultsDialog", u"\u0412\u0441\u0435\u0433\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u043e\u0432:", None))
        self.firstStatValue.setText(QCoreApplication.translate("resultsDialog", u"0", None))
        self.secondStatName.setText(QCoreApplication.translate("resultsDialog", u"\u0412\u0441\u0435\u0433\u043e \u0442\u0435\u0441\u0442\u043e\u0432:", None))
        self.secondStatValue.setText(QCoreApplication.translate("resultsDialog", u"0", None))
        self.thirdStatName.setText(QCoreApplication.translate("resultsDialog", u"\u041d\u0435 \u043f\u0440\u043e\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0442\u0435\u0441\u0442\u043e\u0432:", None))
        self.thirdStatValue.setText(QCoreApplication.translate("resultsDialog", u"0", None))
        self.fourthStatName.setText(QCoreApplication.translate("resultsDialog", u"\u041e\u0448\u0438\u0431\u043e\u043a \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u0440\u043e\u0434\u0430:", None))
        self.fourthStatValue.setText(QCoreApplication.translate("resultsDialog", u"0", None))
        self.fifthStatName.setText(QCoreApplication.translate("resultsDialog", u"\u041e\u043e\u0448\u0438\u0431\u043e\u043a \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u0440\u043e\u0434\u0430:", None))
        self.fifthStatValue.setText(QCoreApplication.translate("resultsDialog", u"0", None))
        self.sectionsLabel.setText(QCoreApplication.translate("resultsDialog", u"\u0420\u0430\u0437\u0434\u0435\u043b\u044b", None))
        self.resultsTextEdit.setHtml(QCoreApplication.translate("resultsDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.failedTestsLabel.setText(QCoreApplication.translate("resultsDialog", u"\u041d\u0435 \u043f\u0440\u043e\u0439\u0434\u0435\u043d\u043d\u044b\u0435 \u0442\u0435\u0441\u0442\u044b", None))
        self.previousButton.setText(QCoreApplication.translate("resultsDialog", u"L", None))
        self.firstImage.setText(QCoreApplication.translate("resultsDialog", u"first image", None))
        self.secondImage.setText(QCoreApplication.translate("resultsDialog", u"second image", None))
        self.nextButton.setText(QCoreApplication.translate("resultsDialog", u"R", None))
        self.expectedStatName.setText(QCoreApplication.translate("resultsDialog", u"\u041e\u0436\u0438\u0434\u0430\u0435\u043c\u044b\u0439 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442: \u0441\u043e\u0432\u043f\u0430\u0434\u0430\u044e\u0442 = ", None))
        self.expectedStatValue.setText(QCoreApplication.translate("resultsDialog", u"bool", None))
        self.actualStatName.setText(QCoreApplication.translate("resultsDialog", u"\u0424\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442: \u0441\u043e\u0432\u043f\u0430\u0434\u0430\u044e\u0442 = ", None))
        self.actualStatValue.setText(QCoreApplication.translate("resultsDialog", u"bool", None))
    # retranslateUi

