from PySide6.QtCore import (QPoint, Signal, Qt)
from PySide6.QtWidgets import (QApplication, QListWidget, QLabel, QSizePolicy, QListWidgetItem, QVBoxLayout, QWidget)
from UI.song_ui import Ui_Form
from PySide6.QtCore import Slot
import requests
import time
import webbrowser
from unit.lxmusic import lxmusic
from GUI_songlistwidget import SongCustomWidget
import configparser

class SongWindow(QWidget, Ui_Form):
    closed = Signal()
    save_singnal = Signal(dict)
    def __init__(self, parent=None):

        self.bg_color = ''
        self.danmaku_list = []
        self.font = ''
        self.container_stylesheet = ''
        self.now_playing = ''


        super().__init__()

        self.parent_widget = parent

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 实例化lx
        self.lxmusic = lxmusic()

        # 设置窗口属性
        self.setMinimumHeight(480)
        self.setMinimumWidth(280)
        self.setWindowTitle("点歌列表")
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # 顶部表单设置（排队人数）
        self.lb_headframe = QLabel('已点歌曲：0首')
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
        self.list_widget.setStyleSheet('background-color: rgba(209, 228, 235, 0.8);color: rgb(3, 32, 22); border: none;')

        # test

        self.createcontainers(self.danmaku_list)


    def closeEvent(self, event):
        self.hide()
        self.save_settings()
        self.closed.emit()
        event.accept()



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
        songwindow_setting_dist = {'lb_head_font': self.lb_headframe.font(),
                                    'lb_head_style': self.lb_headframe.styleSheet(),
                                    'list_widget_style': self.list_widget.styleSheet(),
                                    'window_position': f"{window_position.x()},{window_position.y()}",
                                    'window_size': f"{window_size.width()},{window_size.height()}",
                                    'container_font': self.font,
                                    'container_stylesheet': self.container_stylesheet}

        self.save_singnal.emit(songwindow_setting_dist)

    def load_settings(self):
        config = configparser.ConfigParser()
        with open('config.ini', encoding='utf-8') as f:
            config.read_file(f)

        lb_head_font = config.get('Song_window', 'lb_head_font')
        lb_head_style = config.get('Song_window', 'lb_head_style')
        list_widget_style = config.get('Song_window', 'list_widget_style')
        self.font = config.get('Song_window', 'container_font')
        self.container_stylesheet = config.get('Song_window', 'container_stylesheet')
        self.lb_headframe.setFont(lb_head_font)
        self.lb_headframe.setStyleSheet(lb_head_style)
        self.list_widget.setStyleSheet(list_widget_style)

        move_point_str = config.get('Song_window', 'window_position')
        x, y = map(int, move_point_str.split(','))  # 将字符串解析为整数坐标
        window_size_str = config.get('Song_window', 'window_size')
        w, h = map(int, window_size_str.split(','))  # 将字符串解析为整数尺寸
        self.setGeometry(x, y, w, h)  # 设置窗口位置和尺寸


    """
    处理抓取弹幕
    """

    def process_msg(self, danmaku):
        if danmaku['order'] == '切歌':
            self.cut_song()
        if danmaku['order'] == '点歌':
            # 判断列表是否为空
            if self.danmaku_list:
                # 判断列表中是否已经存在该歌曲
                if all(d['name'] != danmaku['name'] for d in self.danmaku_list):
                    self.danmaku_list.append(danmaku)
                    self.reload()
                    if danmaku['singer']:
                        Scheme_url = self.lxmusic.music_searchPlay(name=danmaku['name'], singer=danmaku['singer'],
                                                                   playLater=True)
                        webbrowser.open(url=Scheme_url)
                    else:
                        Scheme_url = self.lxmusic.music_searchPlay(name=danmaku['name'], playLater=True)
                        webbrowser.open(url=Scheme_url)
            else:
                self.danmaku_list.append(danmaku)
                self.reload()
                Scheme_url = self.lxmusic.music_searchPlay(name=danmaku['name'])
                webbrowser.open(url=Scheme_url)

    def cut_song(self):
        # 发送切歌url
        webbrowser.open(self.lxmusic.skipNext())
        # if 列表不为空，
        if self.danmaku_list and self.danmaku_list[0]['name'] == self.now_playing:
            # 删除列表第一个元素
            self.danmaku_list.pop(0)
            # 重新加载列表
            self.reload()

    def get_status(self):
        try:
            response = requests.get("http://127.0.0.1:23330/status")
            response.raise_for_status()  # 检查请求是否成功
            data = response.json()

            """
            响应数据例子：
            {
              "status": "playing",
              "name": "天使的翅膀",
              "singer": "徐誉滕",
              "albumName": "李雷和韩梅梅",
              "duration": 214.543673,
              "progress": 5.051338,
              "playbackRate": 1,
              "picUrl": "http://xxx",
              "lyricLineText": "徐誉滕 - 天使的翅膀"
            }
            """

            return data

        except (requests.RequestException, ValueError) as e:
            time.sleep(1)
            self.get_status()

    def process_event(self, event):
        if "playing" in event:
            lx_status = self.get_status()
            self.now_playing = lx_status['name']


    def reload(self):
        self.list_widget.clear()
        self.createcontainers(self.danmaku_list)
        self.update_song_quantity(len(self.danmaku_list))

    def update_song_quantity(self, int):
        self.lb_headframe.setText(f'当前已点歌曲：{int}首')

    def del_item(self, song_name):
        self.danmaku_list = [item for item in self.danmaku_list if item.get('name') != song_name]
        self.reload()
        self.update_song_quantity(len(self.danmaku_list))


    def createcontainers(self, danmaku_list):
        for danmaku in danmaku_list:
            container = SongCustomWidget(danmaku['name'], self.font, self.container_stylesheet)
            container.del_item.connect(self.del_item)
            # 列表item实例化
            item = QListWidgetItem()

            # item设置大小
            item.setSizeHint(container.sizeHint())

            # 添加item到列表
            self.list_widget.addItem(item)

            # 添加自定义部件到item
            self.list_widget.setItemWidget(item, container)

    @Slot(dict)
    def receive_danmaku(self, danmaku):
        self.process_msg(danmaku)

    @Slot(str)
    def receive_event(self, event):
        self.process_event(event)

    @Slot(str)
    def get_font(self, color):
        self.font = color
        self.reload()

    @Slot(str)
    def get_color(self, color):
        self.container_stylesheet = color
        self.reload()


if __name__ == "__main__":
    app = QApplication([])
    window = SongWindow()
    window.show()
    app.exec()
