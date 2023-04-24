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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_TableRecognize(object):
    def setupUi(self, TableRecognize):
        if not TableRecognize.objectName():
            TableRecognize.setObjectName(u"TableRecognize")
        TableRecognize.resize(800, 600)
        self.actionimage = QAction(TableRecognize)
        self.actionimage.setObjectName(u"actionimage")
        self.actionurl = QAction(TableRecognize)
        self.actionurl.setObjectName(u"actionurl")
        self.actionpdf = QAction(TableRecognize)
        self.actionpdf.setObjectName(u"actionpdf")
        self.action_image = QAction(TableRecognize)
        self.action_image.setObjectName(u"action_image")
        self.action_image.setIconVisibleInMenu(True)
        self.action_url = QAction(TableRecognize)
        self.action_url.setObjectName(u"action_url")
        self.action_pdf = QAction(TableRecognize)
        self.action_pdf.setObjectName(u"action_pdf")
        self.centralwidget = QWidget(TableRecognize)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 130, 721, 401))
        self.image_file = QLineEdit(self.centralwidget)
        self.image_file.setObjectName(u"image_file")
        self.image_file.setGeometry(QRect(80, 30, 113, 21))
        self.image_file_button = QPushButton(self.centralwidget)
        self.image_file_button.setObjectName(u"image_file_button")
        self.image_file_button.setGeometry(QRect(210, 30, 75, 23))
        TableRecognize.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TableRecognize)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        TableRecognize.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TableRecognize)
        self.statusbar.setObjectName(u"statusbar")
        TableRecognize.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_image)
        self.menu.addAction(self.action_url)
        self.menu.addAction(self.action_pdf)

        self.retranslateUi(TableRecognize)

        QMetaObject.connectSlotsByName(TableRecognize)
    # setupUi

    def retranslateUi(self, TableRecognize):
        TableRecognize.setWindowTitle(QCoreApplication.translate("TableRecognize", u"MainWindow", None))
        self.actionimage.setText(QCoreApplication.translate("TableRecognize", u"image", None))
        self.actionurl.setText(QCoreApplication.translate("TableRecognize", u"url", None))
        self.actionpdf.setText(QCoreApplication.translate("TableRecognize", u"pdf", None))
        self.action_image.setText(QCoreApplication.translate("TableRecognize", u"\u56fe\u7247", None))
#if QT_CONFIG(statustip)
        self.action_image.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.action_url.setText(QCoreApplication.translate("TableRecognize", u"\u7f51\u5740", None))
        self.action_pdf.setText(QCoreApplication.translate("TableRecognize", u"pdf", None))
        self.image_file_button.setText(QCoreApplication.translate("TableRecognize", u"\u56fe\u7247\u5730\u5740", None))
        self.menu.setTitle(QCoreApplication.translate("TableRecognize", u"\u8bc6\u522b\u6a21\u5f0f", None))
    # retranslateUi

