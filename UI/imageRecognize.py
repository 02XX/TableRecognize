# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imageRecognize.ui'
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

class Ui_imageRecognize(object):
    def setupUi(self, imageRecognize):
        if not imageRecognize.objectName():
            imageRecognize.setObjectName(u"imageRecognize")
        imageRecognize.resize(748, 657)
        self.verticalLayout = QVBoxLayout(imageRecognize)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_file = QLineEdit(imageRecognize)
        self.image_file.setObjectName(u"image_file")

        self.horizontalLayout.addWidget(self.image_file)

        self.image_file_button = QPushButton(imageRecognize)
        self.image_file_button.setObjectName(u"image_file_button")

        self.horizontalLayout.addWidget(self.image_file_button)

        self.startRecognize = QPushButton(imageRecognize)
        self.startRecognize.setObjectName(u"startRecognize")

        self.horizontalLayout.addWidget(self.startRecognize)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.image = QLabel(imageRecognize)
        self.image.setObjectName(u"image")

        self.verticalLayout.addWidget(self.image)

        self.tableWidget = QTableWidget(imageRecognize)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(imageRecognize)

        QMetaObject.connectSlotsByName(imageRecognize)
    # setupUi

    def retranslateUi(self, imageRecognize):
        imageRecognize.setWindowTitle(QCoreApplication.translate("imageRecognize", u"Form", None))
        self.image_file.setPlaceholderText(QCoreApplication.translate("imageRecognize", u"\u8f93\u5165\u56fe\u7247\u5730\u5740", None))
        self.image_file_button.setText(QCoreApplication.translate("imageRecognize", u"\u56fe\u7247\u5730\u5740", None))
        self.startRecognize.setText(QCoreApplication.translate("imageRecognize", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.image.setText("")
    # retranslateUi

