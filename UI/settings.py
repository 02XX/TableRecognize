# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(574, 479)
        self.verticalLayout = QVBoxLayout(settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(settings)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.baidu_api_key = QLineEdit(settings)
        self.baidu_api_key.setObjectName(u"baidu_api_key")

        self.gridLayout.addWidget(self.baidu_api_key, 0, 1, 1, 1)

        self.label_2 = QLabel(settings)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.baidu_secret_key = QLineEdit(settings)
        self.baidu_secret_key.setObjectName(u"baidu_secret_key")

        self.gridLayout.addWidget(self.baidu_secret_key, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.line = QFrame(settings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer = QSpacerItem(20, 362, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(348, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.confirm = QPushButton(settings)
        self.confirm.setObjectName(u"confirm")

        self.horizontalLayout.addWidget(self.confirm)

        self.apply = QPushButton(settings)
        self.apply.setObjectName(u"apply")

        self.horizontalLayout.addWidget(self.apply)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(settings)

        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"Form", None))
        self.label.setText(QCoreApplication.translate("settings", u"\u767e\u5ea6api key", None))
        self.label_2.setText(QCoreApplication.translate("settings", u"\u767e\u5ea6secret key", None))
        self.confirm.setText(QCoreApplication.translate("settings", u"\u786e\u5b9a", None))
        self.apply.setText(QCoreApplication.translate("settings", u"\u5e94\u7528", None))
    # retranslateUi

