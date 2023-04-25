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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_TableRecognize(object):
    def setupUi(self, TableRecognize):
        if not TableRecognize.objectName():
            TableRecognize.setObjectName(u"TableRecognize")
        TableRecognize.resize(800, 754)
        self.centralwidget = QWidget(TableRecognize)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addLayout(self.verticalLayout)

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
    # retranslateUi

