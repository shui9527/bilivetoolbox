# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '歌词窗口.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, Slot,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_lyricqwidget(object):
    def setupUi(self, lyricqwidget):
        if not lyricqwidget.objectName():
            lyricqwidget.setObjectName(u"lyricqwidget")

        lyricqwidget.setEnabled(True)
        lyricqwidget.resize(1080, 40)
        lyricqwidget.setMinimumSize(QSize(500, 40))
        # lyricqwidget.setAutoFillBackground(True)
        lyricqwidget.setStyleSheet(u"background-color: rgba(209, 228, 235, 0.01)")





        self.Layout = QHBoxLayout(lyricqwidget)
        self.Layout.setSpacing(0)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setObjectName(u"Layout")
        self.name = QLabel(lyricqwidget)
        self.name.setObjectName(u"name")

        # 设置拉伸
        self.name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        self.name.setStyleSheet(u"background-color: rgba(209, 228, 235, 0.9)")
        font = QFont()
        font.setFamilies([u"\u732b\u5543\u7f51\u7cd6\u5706\u4f53 (\u6d4b\u8bd5\u7248)"])
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setContentsMargins(9, 0, 0, 0)

        self.Layout.addWidget(self.name)

        self.lyric = QLabel(lyricqwidget)
        self.lyric.setObjectName(u"lyric")
        self.lyric.setFont(font)
        self.lyric.setContentsMargins(9, 0, 0, 0)
        self.lyric.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lyric.setStyleSheet(u"background-color: rgba(209, 228, 235, 0.9)")



        self.Layout.addWidget(self.lyric)

        lyricqwidget.setAttribute(Qt.WA_TranslucentBackground)
        #设置无边框
        lyricqwidget.setWindowFlags(Qt.FramelessWindowHint)






        self.retranslateUi(lyricqwidget)

        QMetaObject.connectSlotsByName(lyricqwidget)
    # setupUi

    def retranslateUi(self, lyricqwidget):
        lyricqwidget.setWindowTitle(QCoreApplication.translate("lyricqwidget", u"Lyric", None))
        self.name.setText(QCoreApplication.translate("lyricqwidget", u"TextLabel", None))
        self.lyric.setText(QCoreApplication.translate("lyricqwidget", u"TextLabel", None))
    # retranslateUi

    # @Slot()
    # def receive_bg_color(self, value):
    #     self.lyricqwidget.setPalette(value)
    #     self.lyricqwidget.setStyleSheet(f"background-color: {value}")