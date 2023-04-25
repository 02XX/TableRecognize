# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'urlRecognize.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_urlRecognize(object):
    def setupUi(self, urlRecognize):
        if not urlRecognize.objectName():
            urlRecognize.setObjectName(u"urlRecognize")
        urlRecognize.resize(727, 676)
        self.verticalLayout = QVBoxLayout(urlRecognize)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.urlPath = QLineEdit(urlRecognize)
        self.urlPath.setObjectName(u"urlPath")

        self.horizontalLayout.addWidget(self.urlPath)

        self.startRecognize = QPushButton(urlRecognize)
        self.startRecognize.setObjectName(u"startRecognize")

        self.horizontalLayout.addWidget(self.startRecognize)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.image = QLabel(urlRecognize)
        self.image.setObjectName(u"image")

        self.verticalLayout.addWidget(self.image)

        self.tableWidget = QTableWidget(urlRecognize)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(urlRecognize)

        QMetaObject.connectSlotsByName(urlRecognize)
    # setupUi

    def retranslateUi(self, urlRecognize):
        urlRecognize.setWindowTitle(QCoreApplication.translate("urlRecognize", u"Form", None))
        self.urlPath.setPlaceholderText(QCoreApplication.translate("urlRecognize", u"\u8f93\u5165URL\u5730\u5740", None))
        self.startRecognize.setText(QCoreApplication.translate("urlRecognize", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.image.setText("")
    # retranslateUi

