# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '主窗口.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider, QFontDialog, QColorDialog,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(520, 420)
        Form.setStyleSheet(u"background-color: rgb(209, 228, 235)")
        self.verticalLayout_8 = QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setStyleSheet(u"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n""")
        self.lyric = QWidget()
        self.lyric.setObjectName(u"lyric")
        self.verticalLayout_4 = QVBoxLayout(self.lyric)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_lytextset = QLabel(self.lyric)
        self.lb_lytextset.setObjectName(u"lb_lytextset")
        self.lb_lytextset.setMinimumSize(QSize(80, 40))
        self.lb_lytextset.setMaximumSize(QSize(80, 40))

        self.verticalLayout.addWidget(self.lb_lytextset)

        self.bt_lysetfont = QPushButton(self.lyric)
        self.bt_lysetfont.setObjectName(u"bt_lysetfont")
        self.bt_lysetfont.setMinimumSize(QSize(120, 30))
        self.bt_lysetfont.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout.addWidget(self.bt_lysetfont)

        self.bt_lysetcolor = QPushButton(self.lyric)
        self.bt_lysetcolor.setObjectName(u"bt_lysetcolor")
        self.bt_lysetcolor.setMinimumSize(QSize(120, 30))
        self.bt_lysetcolor.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout.addWidget(self.bt_lysetcolor)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lb_lybgset = QLabel(self.lyric)
        self.lb_lybgset.setObjectName(u"lb_lybgset")
        self.lb_lybgset.setMinimumSize(QSize(80, 30))
        self.lb_lybgset.setMaximumSize(QSize(80, 30))

        self.verticalLayout.addWidget(self.lb_lybgset)

        self.bt_lybgsetcolor = QPushButton(self.lyric)
        self.bt_lybgsetcolor.setObjectName(u"bt_lybgsetcolor")
        self.bt_lybgsetcolor.setMaximumSize(QSize(120, 30))

        self.verticalLayout.addWidget(self.bt_lybgsetcolor)

        # self.cb_lycheckbox = QCheckBox(self.lyric)
        # self.cb_lycheckbox.setObjectName(u"cb_lycheckbox")
        # self.cb_lycheckbox.setMinimumSize(QSize(0, 30))

        # self.verticalLayout.addWidget(self.cb_lycheckbox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.lb_lynamewidth = QLabel(self.lyric)
        self.lb_lynamewidth.setObjectName(u"lb_lynamewidth")
        self.lb_lynamewidth.setMinimumSize(QSize(80, 40))
        self.lb_lynamewidth.setMaximumSize(QSize(80, 40))

        self.verticalLayout_2.addWidget(self.lb_lynamewidth)

        self.sld_lynamewidth = QSlider(self.lyric)
        self.sld_lynamewidth.setObjectName(u"sld_lynamewidth")
        self.sld_lynamewidth.setMinimumSize(QSize(250, 30))
        self.sld_lynamewidth.setOrientation(Qt.Orientation.Horizontal)
        # 设置滑动条范围
        self.sld_lynamewidth.setMinimum(50)
        self.sld_lynamewidth.setMaximum(500)
        # 设置滑动条默认值
        self.sld_lynamewidth.setValue(120)

        self.verticalLayout_2.addWidget(self.sld_lynamewidth)

        self.lb_lywindowwidth = QLabel(self.lyric)
        self.lb_lywindowwidth.setObjectName(u"lb_lywindowwidth")
        self.lb_lywindowwidth.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.lb_lywindowwidth)

        self.sld_lywindowwidth = QSlider(self.lyric)
        self.sld_lywindowwidth.setObjectName(u"sld_lywindowwidth")
        self.sld_lywindowwidth.setMinimumSize(QSize(0, 30))
        self.sld_lywindowwidth.setOrientation(Qt.Orientation.Horizontal)
        # 设置滑动条范围
        self.sld_lywindowwidth.setMinimum(150)
        self.sld_lywindowwidth.setMaximum(2440)
        # 设置滑动条默认值
        self.sld_lywindowwidth.setValue(800)

        self.verticalLayout_2.addWidget(self.sld_lywindowwidth)

        self.lb_lysettransparency = QLabel(self.lyric)
        self.lb_lysettransparency.setObjectName(u"lb_lysettransparency")
        self.lb_lysettransparency.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.lb_lysettransparency)

        self.sld_lytransparency = QSlider(self.lyric)
        self.sld_lytransparency.setObjectName(u"sld_lytransparency")
        self.sld_lytransparency.setMinimumSize(QSize(0, 30))
        self.sld_lytransparency.setOrientation(Qt.Orientation.Horizontal)
        # 设置滑动条范围
        self.sld_lytransparency.setMinimum(0)
        self.sld_lytransparency.setMaximum(255)
        # 设置滑动条默认值
        self.sld_lytransparency.setValue(200)

        self.verticalLayout_2.addWidget(self.sld_lytransparency)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.bt_lyshow = QPushButton(self.lyric)
        self.bt_lyshow.setObjectName(u"bt_lyshow")
        self.bt_lyshow.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.bt_lyshow.setFont(font)
        self.bt_lyshow.setStyleSheet(u"background-color: rgb(204, 220, 235)")

        self.verticalLayout_3.addWidget(self.bt_lyshow)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.lyric, "")
        self.song = QWidget()
        self.song.setObjectName(u"song")
        self.verticalLayout_13 = QVBoxLayout(self.song)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lb_dgtextset = QLabel(self.song)
        self.lb_dgtextset.setObjectName(u"lb_dgtextset")
        self.lb_dgtextset.setMinimumSize(QSize(80, 40))
        self.lb_dgtextset.setMaximumSize(QSize(80, 40))

        self.verticalLayout_5.addWidget(self.lb_dgtextset)

        self.bt_dgsetfont = QPushButton(self.song)
        self.bt_dgsetfont.setObjectName(u"bt_dgsetfont")
        self.bt_dgsetfont.setMinimumSize(QSize(120, 30))
        self.bt_dgsetfont.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_5.addWidget(self.bt_dgsetfont)

        self.bt_dgsetcolor = QPushButton(self.song)
        self.bt_dgsetcolor.setObjectName(u"bt_dgsetcolor")
        self.bt_dgsetcolor.setMinimumSize(QSize(120, 30))
        self.bt_dgsetcolor.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_5.addWidget(self.bt_dgsetcolor)

        self.lb_dgbttextset = QLabel(self.song)
        self.lb_dgbttextset.setObjectName(u"lb_dgbttextset")
        self.lb_dgbttextset.setMinimumSize(QSize(80, 40))
        self.lb_dgbttextset.setMaximumSize(QSize(80, 40))

        self.verticalLayout_5.addWidget(self.lb_dgbttextset)

        self.bt_dgbtsetfont = QPushButton(self.song)
        self.bt_dgbtsetfont.setObjectName(u"bt_dgbtsetfont")
        self.bt_dgbtsetfont.setMinimumSize(QSize(120, 30))
        self.bt_dgbtsetfont.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_5.addWidget(self.bt_dgbtsetfont)

        self.bt_dgbtsetcolor = QPushButton(self.song)
        self.bt_dgbtsetcolor.setObjectName(u"bt_dgbtsetcolor")
        self.bt_dgbtsetcolor.setMinimumSize(QSize(120, 30))
        self.bt_dgbtsetcolor.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_5.addWidget(self.bt_dgbtsetcolor)

        self.verticalSpacer_9 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lb_dgbgset = QLabel(self.song)
        self.lb_dgbgset.setObjectName(u"lb_dgbgset")
        self.lb_dgbgset.setMinimumSize(QSize(80, 40))
        self.lb_dgbgset.setMaximumSize(QSize(80, 40))

        self.verticalLayout_6.addWidget(self.lb_dgbgset)

        self.bt_dgbgsetcolor = QPushButton(self.song)
        self.bt_dgbgsetcolor.setObjectName(u"bt_dgbgsetcolor")
        self.bt_dgbgsetcolor.setMinimumSize(QSize(120, 30))
        self.bt_dgbgsetcolor.setMaximumSize(QSize(120, 30))

        self.verticalLayout_6.addWidget(self.bt_dgbgsetcolor)

        self.verticalSpacer_8 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)

        self.lb_dgsettransparency = QLabel(self.song)
        self.lb_dgsettransparency.setObjectName(u"lb_dgsettransparency")
        self.lb_dgsettransparency.setMinimumSize(QSize(0, 40))

        self.verticalLayout_6.addWidget(self.lb_dgsettransparency)

        self.sld_dgtransparency = QSlider(self.song)
        self.sld_dgtransparency.setObjectName(u"sld_dgtransparency")
        self.sld_dgtransparency.setMinimumSize(QSize(250, 30))
        self.sld_dgtransparency.setOrientation(Qt.Orientation.Horizontal)
        # 设置滑动条范围
        self.sld_dgtransparency.setMinimum(0)
        self.sld_dgtransparency.setMaximum(255)
        # 设置滑动条默认值
        self.sld_dgtransparency.setValue(200)

        self.verticalLayout_6.addWidget(self.sld_dgtransparency)

        self.verticalSpacer_15 = QSpacerItem(20, 130, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_15)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.bt_dgshow = QPushButton(self.song)
        self.bt_dgshow.setObjectName(u"bt_dgshow")
        self.bt_dgshow.setMinimumSize(QSize(0, 60))
        self.bt_dgshow.setFont(font)
        self.bt_dgshow.setStyleSheet(u"background-color: rgb(204, 220, 235)")

        self.verticalLayout_7.addWidget(self.bt_dgshow)


        self.verticalLayout_13.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.song, "")
        self.queue = QWidget()
        self.queue.setObjectName(u"queue")
        self.verticalLayout_22 = QVBoxLayout(self.queue)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_16 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_16)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.lb_pdtextset = QLabel(self.queue)
        self.lb_pdtextset.setObjectName(u"lb_pdtextset")
        self.lb_pdtextset.setMinimumSize(QSize(80, 40))
        self.lb_pdtextset.setMaximumSize(QSize(80, 40))

        self.verticalLayout_20.addWidget(self.lb_pdtextset)

        self.bt_pdsetfont = QPushButton(self.queue)
        self.bt_pdsetfont.setObjectName(u"bt_pdsetfont")
        self.bt_pdsetfont.setMinimumSize(QSize(120, 30))
        self.bt_pdsetfont.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_20.addWidget(self.bt_pdsetfont)

        self.bt_pdsetcolor = QPushButton(self.queue)
        self.bt_pdsetcolor.setObjectName(u"bt_pdsetcolor")
        self.bt_pdsetcolor.setMinimumSize(QSize(120, 30))
        self.bt_pdsetcolor.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_20.addWidget(self.bt_pdsetcolor)

        self.lb_pdbttextset = QLabel(self.queue)
        self.lb_pdbttextset.setObjectName(u"lb_pdbttextset")
        self.lb_pdbttextset.setMinimumSize(QSize(80, 40))
        self.lb_pdbttextset.setMaximumSize(QSize(80, 40))

        self.verticalLayout_20.addWidget(self.lb_pdbttextset)

        self.bt_pdbtsetfont = QPushButton(self.queue)
        self.bt_pdbtsetfont.setObjectName(u"bt_pdbtsetfont")
        self.bt_pdbtsetfont.setMinimumSize(QSize(120, 30))
        self.bt_pdbtsetfont.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_20.addWidget(self.bt_pdbtsetfont)

        self.bt_pdbtsetcolor = QPushButton(self.queue)
        self.bt_pdbtsetcolor.setObjectName(u"bt_pdbtsetcolor")
        self.bt_pdbtsetcolor.setMinimumSize(QSize(120, 30))
        self.bt_pdbtsetcolor.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_20.addWidget(self.bt_pdbtsetcolor)

        self.verticalSpacer_18 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_18)


        self.horizontalLayout_7.addLayout(self.verticalLayout_20)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_17)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.lb_pdbgset = QLabel(self.queue)
        self.lb_pdbgset.setObjectName(u"lb_pdbgset")
        self.lb_pdbgset.setMinimumSize(QSize(80, 40))
        self.lb_pdbgset.setMaximumSize(QSize(80, 40))

        self.verticalLayout_21.addWidget(self.lb_pdbgset)

        self.bt_pdbgsetcolor = QPushButton(self.queue)
        self.bt_pdbgsetcolor.setObjectName(u"bt_pdbgsetcolor")
        self.bt_pdbgsetcolor.setMinimumSize(QSize(120, 30))
        self.bt_pdbgsetcolor.setMaximumSize(QSize(120, 30))

        self.verticalLayout_21.addWidget(self.bt_pdbgsetcolor)

        self.verticalSpacer_19 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_19)

        self.lb_pdsettransparency = QLabel(self.queue)
        self.lb_pdsettransparency.setObjectName(u"lb_pdsettransparency")
        self.lb_pdsettransparency.setMinimumSize(QSize(0, 40))

        self.verticalLayout_21.addWidget(self.lb_pdsettransparency)

        self.sld_pdtransparency = QSlider(self.queue)
        self.sld_pdtransparency.setObjectName(u"sld_pdtransparency")
        self.sld_pdtransparency.setMinimumSize(QSize(250, 30))
        self.sld_pdtransparency.setOrientation(Qt.Orientation.Horizontal)
        # 设置滑动条范围
        self.sld_pdtransparency.setMinimum(0)
        self.sld_pdtransparency.setMaximum(255)
        # 设置滑动条默认值
        self.sld_pdtransparency.setValue(200)

        self.verticalLayout_21.addWidget(self.sld_pdtransparency)

        self.verticalSpacer_20 = QSpacerItem(20, 130, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_20)


        self.horizontalLayout_7.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_18)


        self.verticalLayout_22.addLayout(self.horizontalLayout_7)

        self.bt_pause = QPushButton(self.queue)
        self.bt_pause.setObjectName(u"pause")
        self.bt_pause.setMinimumSize(QSize(0, 30))
        self.bt_pause.setFont(font)
        self.bt_pause.setStyleSheet(u"background-color: rgb(204, 220, 235)")

        self.verticalLayout_22.addWidget(self.bt_pause)

        self.bt_pdshow = QPushButton(self.queue)
        self.bt_pdshow.setObjectName(u"bt_pdshow_3")
        self.bt_pdshow.setMinimumSize(QSize(0, 60))
        self.bt_pdshow.setFont(font)
        self.bt_pdshow.setStyleSheet(u"background-color: rgb(204, 220, 235)")

        self.verticalLayout_22.addWidget(self.bt_pdshow)

        self.tabWidget.addTab(self.queue, "")





        self.verticalLayout_8.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lb_lytextset.setText(QCoreApplication.translate("Form", u"\u6587\u672c\u8bbe\u7f6e", None))
        self.bt_lysetfont.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u5b57\u4f53", None))
        self.bt_lysetcolor.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u989c\u8272", None))
        self.lb_lybgset.setText(QCoreApplication.translate("Form", u"\u80cc\u666f\u8bbe\u7f6e", None))
        self.bt_lybgsetcolor.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u989c\u8272", None))
        # self.cb_lycheckbox.setText(QCoreApplication.translate("Form", "无边框设置 \n （慎用）", None))
        self.lb_lynamewidth.setText(QCoreApplication.translate("Form", u"\u6b4c\u540d\u5bbd\u5ea6", None))
        self.lb_lywindowwidth.setText(QCoreApplication.translate("Form", u"\u7a97\u4f53\u5bbd\u5ea6", None))
        self.lb_lysettransparency.setText(QCoreApplication.translate("Form", u"\u900f\u660e\u5ea6\u8bbe\u7f6e", None))
        self.bt_lyshow.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u6b4c\u8bcd\u7a97\u53e3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lyric), QCoreApplication.translate("Form", u"\u6b4c\u8bcd\u7a97\u53e3", None))
        self.lb_dgtextset.setText(QCoreApplication.translate("Form", u"\u6587\u672c\u8bbe\u7f6e", None))
        self.bt_dgsetfont.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u5b57\u4f53", None))
        self.bt_dgsetcolor.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u989c\u8272", None))
        self.lb_dgbttextset.setText(QCoreApplication.translate("Form", u"\u8868\u5934\u8bbe\u7f6e", None))
        self.bt_dgbtsetfont.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u5b57\u4f53", None))
        self.bt_dgbtsetcolor.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u989c\u8272", None))
        self.lb_dgbgset.setText(QCoreApplication.translate("Form", u"\u80cc\u666f\u8bbe\u7f6e", None))
        self.bt_dgbgsetcolor.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u989c\u8272", None))
        self.lb_dgsettransparency.setText(QCoreApplication.translate("Form", u"\u900f\u660e\u5ea6\u8bbe\u7f6e", None))
        self.bt_dgshow.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u70b9\u6b4c\u5217\u8868\u7a97\u53e3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.song), QCoreApplication.translate("Form", u"\u70b9\u6b4c\u529f\u80fd", None))
        self.lb_pdtextset.setText(QCoreApplication.translate("Form", u"\u6587\u672c\u8bbe\u7f6e", None))
        self.bt_pdsetfont.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u5b57\u4f53", None))
        self.bt_pdsetcolor.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u989c\u8272", None))
        self.lb_pdbttextset.setText(QCoreApplication.translate("Form", u"\u8868\u5934\u8bbe\u7f6e", None))
        self.bt_pdbtsetfont.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u5b57\u4f53", None))
        self.bt_pdbtsetcolor.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u989c\u8272", None))
        self.lb_pdbgset.setText(QCoreApplication.translate("Form", u"\u80cc\u666f\u8bbe\u7f6e", None))
        self.bt_pdbgsetcolor.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u989c\u8272", None))
        self.lb_pdsettransparency.setText(QCoreApplication.translate("Form", u"\u900f\u660e\u5ea6\u8bbe\u7f6e", None))
        self.bt_pause.setText(QCoreApplication.translate("Form", u"暂停排队", None))
        self.bt_pdshow.setText(QCoreApplication.translate("Form", u"显示排队列表窗口", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.queue), QCoreApplication.translate("Form", u"\u6392\u961f\u529f\u80fd", None))
    # retranslateUi

