# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '登录窗口.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(317, 225)
        Frame.setStyleSheet(u"background-color: rgb(209, 228, 235)")
        self.verticalLayout_2 = QVBoxLayout(Frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tip = QLabel(Frame)
        self.tip.setObjectName(u"tip")
        self.tip.setMinimumSize(QSize(0, 80))
        self.tip.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamilies([u"\u732b\u5543\u7f51\u7cd6\u5706\u4f53 (\u6d4b\u8bd5\u7248)"])
        font.setPointSize(20)
        font.setBold(False)
        font.setKerning(True)
        self.tip.setFont(font)
        self.tip.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.tip)

        self.code = QLineEdit(Frame)
        self.code.setObjectName(u"code")
        self.code.setMinimumSize(QSize(0, 0))
        self.code.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"\u732b\u5543\u7f51\u7cd6\u5706\u4f53 (\u6d4b\u8bd5\u7248)"])
        font1.setPointSize(16)
        self.code.setFont(font1)
        self.code.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.code.setStyleSheet(u"background-color: rgb(228, 234, 216);")
        self.code.setMaxLength(20)
        self.code.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.code)

        self.bt_connect = QPushButton(Frame)
        self.bt_connect.setObjectName(u"connect")
        self.bt_connect.setMinimumSize(QSize(0, 80))
        font2 = QFont()
        font2.setFamilies([u"\u732b\u5543\u7f51\u7cd6\u5706\u4f53 (\u6d4b\u8bd5\u7248)"])
        font2.setPointSize(18)
        self.bt_connect.setFont(font2)

        self.verticalLayout.addWidget(self.bt_connect)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"\u0042\u0069\u006C\u0069\u0076\u0065\u0054\u006F\u006F\u006C", None))
        self.tip.setText(QCoreApplication.translate("Frame", u"\u8f93\u5165\u8eab\u4efd\u7801\u8fde\u63a5\u76f4\u64ad\u95f4", None))
        self.bt_connect.setText(QCoreApplication.translate("Frame", u"\u542f\u52a8\u8fde\u63a5", None))
    # retranslateUi

