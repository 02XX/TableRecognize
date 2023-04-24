# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_TableRecognize(object):
    def setupUi(self, TableRecognize):
        if not TableRecognize.objectName():
            TableRecognize.setObjectName(u"TableRecognize")
        TableRecognize.resize(800, 617)
        self.centralwidget = QWidget(TableRecognize)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_file = QLineEdit(self.centralwidget)
        self.image_file.setObjectName(u"image_file")

        self.horizontalLayout.addWidget(self.image_file)

        self.image_file_button = QPushButton(self.centralwidget)
        self.image_file_button.setObjectName(u"image_file_button")

        self.horizontalLayout.addWidget(self.image_file_button)

        self.startRecognize = QPushButton(self.centralwidget)
        self.startRecognize.setObjectName(u"startRecognize")

        self.horizontalLayout.addWidget(self.startRecognize)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        TableRecognize.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TableRecognize)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        TableRecognize.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TableRecognize)
        self.statusbar.setObjectName(u"statusbar")
        TableRecognize.setStatusBar(self.statusbar)

        self.retranslateUi(TableRecognize)

        QMetaObject.connectSlotsByName(TableRecognize)
    # setupUi

    def retranslateUi(self, TableRecognize):
        TableRecognize.setWindowTitle(QCoreApplication.translate("TableRecognize", u"MainWindow", None))
        self.image_file_button.setText(QCoreApplication.translate("TableRecognize", u"\u56fe\u7247\u5730\u5740", None))
        self.startRecognize.setText(QCoreApplication.translate("TableRecognize", u"\u5f00\u59cb\u8bc6\u522b", None))
    # retranslateUi

