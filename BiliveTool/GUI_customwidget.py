from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QSignalMapper,
                            QMetaObject, QObject, QPoint, QRect, Signal,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout, QFrame, QListWidget,
                               QLabel, QPushButton, QSizePolicy, QSlider, QScrollArea,
                               QSpacerItem, QTabWidget, QVBoxLayout, QWidget)


class CustomWidget(QWidget):

    del_item = Signal(str)

    def __init__(self, user, font, container_stylesheet, parent=None):
        self.font = font
        self.container_stylesheet = container_stylesheet + ';border-radius: 10px;'

        super().__init__(parent)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(6, 6, 6, 6)
        self.layout.setSpacing(10)
        # 设置圆角

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)


        self.setLayout(self.layout)

        self.lb_name = QLabel(user)
        self.lb_name.setObjectName("Name")
        self.lb_name.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.lb_name.setContentsMargins(10, 0, 0, 0)




        self.bt_del = QPushButton('Del')
        self.bt_del.setObjectName("Delete")
        self.bt_del.clicked.connect(self.on_click)
        self.bt_del.setMinimumHeight(20)
        self.bt_del.setMinimumWidth(35)
        self.bt_del.sizePolicy()
        self.bt_del.setContentsMargins(1, 1, 1, 1)
        self.bt_del.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)

        self.layout.addWidget(self.lb_name)
        self.layout.addWidget(self.bt_del)



        self.lb_name.setStyleSheet(self.container_stylesheet)
        self.bt_del.setStyleSheet(self.container_stylesheet)

        self.lb_name.setFont(self.font)
        self.bt_del.setFont(self.font)






    def on_click(self):
        del_name = self.lb_name.text()
        self.del_item.emit(del_name)


        # 设置样式表

        # # 窗体背景透明化
        #
        # palette = self.palette()
        # palette.setColor(QPalette.Window, QColor(255, 255, 255, 0))  # 设置窗口背景颜色为透明
        # self.setPalette(palette)
        #
        # delete_button_palette = self.bt_del.palette()
        # delete_button_palette.setColor(QPalette.Button, QColor(255, 2, 3, 0))  # 设置按钮颜色
        # self.bt_del.setAutoFillBackground(True)
        # self.bt_del.setPalette(delete_button_palette)
        #
        # # 设置标签的背景颜色
        # label_palette = self.lb_name.palette()
        # label_palette.setColor(QPalette.Window, QColor(0, 255, 0))  # 设置标签的背景颜色为绿色
        # self.lb_name.setAutoFillBackground(True)  # 确保标签背景可以被填充
        # self.lb_name.setPalette(label_palette)


        # 设置窗口背景色为透明
        # self.setAttribute(Qt.WA_TranslucentBackground)
        #
        # # 设置按钮文本颜色为黄色
        # self.bt_del.setStyleSheet("color: blue")
        #
        # # 设置标签背景色为红色，文本为蓝色
        # self.lb_name.setStyleSheet("background-color: red; color: blue")








if __name__ == "__main__":
    app = QApplication([])
    window = CustomWidget()
    window.show()
    app.exec()