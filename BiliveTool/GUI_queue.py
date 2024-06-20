from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QSignalMapper,
                            QMetaObject, QObject, QPoint, QRect, Slot, Signal,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout, QFrame, QListWidget,
                               QLabel, QPushButton, QSizePolicy, QSlider, QScrollArea, QListWidgetItem,
                               QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

from unit.signalclass import Signal_To_Queue
from GUI_customwidget import CustomWidget
from GUI_songlistwidget import SongCustomWidget
import configparser

class QueueWindow(QWidget):
    closed = Signal()
    save_singnal = Signal(dict)

    def __init__(self, parent=None):

        self.user_list = []
        self.font = ''
        self.container_stylesheet = ''
        self.pause = False




        super().__init__(parent)

        self.parent_widget = parent

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)


        # 设置窗口属性
        self.setMinimumHeight(480)
        self.setMinimumWidth(280)
        self.setWindowTitle("排队列表")
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)



        # 顶部表单设置（排队人数）
        self.lb_headframe = QLabel('当前排队人数：0人')
        self.lb_headframe.setMinimumHeight(40)
        self.lb_headframe.setMaximumHeight(100)
        self.lb_headframe.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.lb_headframe.setAlignment(Qt.AlignCenter)

        # 设置顶部表单布局
        headlayout = QVBoxLayout()
        self.lb_headframe.setLayout(headlayout)
        headlayout.addWidget(self.lb_headframe)
        headlayout.setContentsMargins(0, 0, 0, 0)
        # 设置headframe背景色

        self.lb_headframe.setStyleSheet('background-color: rgba(209, 228, 235, 0.8);color: rgb(3, 32, 22); border: none;')
        self.layout.addWidget(self.lb_headframe)


        # 设置中间容器
        # 创建列表部件
        self.list_widget = QListWidget()
        self.list_widget.setObjectName('list_widget')
        self.list_widget.setStyleSheet("border: none;")
        self.layout.addWidget(self.list_widget)
        self.layout.setContentsMargins(4, 4, 4, 4)
        self.layout.setSpacing(0)

        # 设置初始化样式
        self.list_widget.setStyleSheet('background-color: rgba(209, 228, 235, 0.8);color: rgb(3, 32, 22);; border: none;')


        # test
        self.createcontainers(self.user_list)
        print(self.user_list)

    """
    GUI逻辑
    """




    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        if self.oldPos:
            delta = event.globalPosition() - self.oldPos  # Use QPointF for subtraction
            new_pos = self.pos() + QPoint(delta.x(), delta.y())  # Use QPoint for addition
            self.move(new_pos)
            self.oldPos = event.globalPosition()

    def mouseReleaseEvent(self, event):
        self.oldPos = None



    def save_settings(self):

        window_position = self.pos()
        window_size = self.size()

        # 添加配置项
        queuewindow_setting_dist = {'last_list': self.user_list,
                                    'lb_head_font': self.lb_headframe.font(),
                                    'lb_head_style': self.lb_headframe.styleSheet(),
                                    'list_widget_style': self.list_widget.styleSheet(),
                                    'window_position': f"{window_position.x()},{window_position.y()}",
                                    'window_size': f"{window_size.width()},{window_size.height()}",
                                    'container_font': self.font,
                                    'container_stylesheet': self.container_stylesheet}

        self.save_singnal.emit(queuewindow_setting_dist)

    def load_settings(self):
        config = configparser.ConfigParser()
        with open('config.ini', encoding='utf-8') as f:
            config.read_file(f)

        # 加载配置项
        # self.user_list = config.get('Queue_window', 'last_list')
        # print('load_setiing',self.user_list)
        lb_head_font = config.get('Queue_window', 'lb_head_font')
        lb_head_style = config.get('Queue_window', 'lb_head_style')
        list_widget_style = config.get('Queue_window', 'list_widget_style')
        self.font = config.get('Queue_window', 'container_font')
        self.container_stylesheet = config.get('Queue_window', 'container_stylesheet')
        self.lb_headframe.setFont(lb_head_font)
        self.lb_headframe.setStyleSheet(lb_head_style)
        self.list_widget.setStyleSheet(list_widget_style)





        move_point_str = config.get('Queue_window', 'window_position')
        x, y = map(int, move_point_str.split(','))  # 将字符串解析为整数坐标
        window_size_str = config.get('Queue_window', 'window_size')
        w, h = map(int, window_size_str.split(','))  # 将字符串解析为整数尺寸
        self.setGeometry(x, y, w, h)  # 设置窗口位置和尺寸



    """
    业务逻辑
    """

    def createcontainers(self, user_list):
        for user in user_list:
            container = CustomWidget(user, self.font, self.container_stylesheet)
            container.del_item.connect(self.del_item)
            # 列表item实例化
            item = QListWidgetItem()

            # item设置大小
            item.setSizeHint(container.sizeHint())

            # 添加item到列表
            self.list_widget.addItem(item)

            # 添加自定义部件到item
            self.list_widget.setItemWidget(item, container)


    def del_item(self, user_name):
        self.user_list.remove(user_name)
        self.reload()


    def reload(self):
        self.list_widget.clear()
        self.createcontainers(self.user_list)
        self.update_menber_quantity(len(self.user_list))


    def update_menber_quantity(self, int):
        self.lb_headframe.setText(f'当前排队人数：{int}人')


    def process_msg(self, msg_date):
        # 判断是否暂停排队
        if self.pause is False:
            if msg_date['order'] == '排队':
                if msg_date['username'] not in self.user_list:
                    self.user_list.append(msg_date['username'])
                    self.list_widget.clear()
                    self.reload()

            if msg_date['order'] == '取消排队':
                if msg_date['username'] in self.user_list:
                    self.del_item(msg_date['username'])


    def closeEvent(self, event):
        self.hide()
        self.save_settings()
        self.closed.emit()
        event.accept()





    @Slot(dict)
    def receive_danmaku(self, danmaku):
        self.process_msg(danmaku)

    @Slot(str)
    def receive_font(self, font):
        self.font = font
        self.reload()

    @Slot(str)
    def receive_color(self, color):
        self.container_stylesheet = color
        self.reload()

#


if __name__ == "__main__":
    app = QApplication([])
    window = QueueWindow()
    window.show()
    app.exec()
