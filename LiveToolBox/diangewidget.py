from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QListWidget)
from PySide6.QtGui import QFont
import requests
import time
import webbrowser
from blivedmclas import BiliClientThread
import monitevent
from lxmusic import lxmusic


class DianGeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.diange_listwidget = QListWidget()  # 点歌列表

        self.parent_widget = parent
        self.diange_list = []  # 示例歌曲列表
        self.room_code = ''

        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle('点歌列表')

        self.setGeometry(750, 500, 250, 450)

        self.diange_listwidget.setGeometry(0, 0, 250, 450)
        # 设置字体微软雅黑 16
        self.diange_listwidget.setFont(QFont('Microsoft YaHei', 16))

        self.diange_listwidget.setStyleSheet("QListWidget{background-color: rgb(255, 255, 255);}")

        layout = QVBoxLayout()

        layout.addWidget(self.diange_listwidget)

        self.setLayout(layout)

        self.BiliClient_thread = BiliClientThread(self, self.room_code, self.process_msg)

        self.monite_thread = monitevent.LxSSEThread()

        self.monite_thread.data_updated.connect(self.process_event)

        self.lxmusic = lxmusic()

    """
    接收身份码
    """

    def get_room_code(self, room_code):
        self.room_code = room_code
        self.BiliClient_thread.get_code(self.room_code)

    """
    弹幕监听功能开关
    """

    def start_data_thread(self):
        self.BiliClient_thread.start()
        self.monite_thread.start()

    def stop_data_thread(self):
        self.BiliClient_thread.stop()

    def closeEvent(self, event):
        self.hide()
        event.accept()

    """
    处理抓取弹幕
    """

    def process_msg(self, msg):
        print(msg)

        if msg['order'] == '切歌':
            self.cut_song()

        if msg['order'] == '点歌':
            if self.diange_list:
                if msg['name'] not in self.diange_list:
                    self.diange_listwidget.addItem(msg['name'])
                    self.diange_list.append(msg)
                    Scheme_url = self.lxmusic.music_searchPlay(name=msg['name'], playLater=True)
                    webbrowser.open(url=Scheme_url)

            else:
                self.diange_listwidget.addItem(msg['name'])
                self.diange_list.append(msg)
                Scheme_url = self.lxmusic.music_searchPlay(name=msg['name'])
                webbrowser.open(url=Scheme_url)

    def cut_song(self):
        # 发送切歌url
        webbrowser.open(self.lxmusic.skipNext())
        if self.diange_list:
            self.del_list_first()

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
            # print(f"Error in remain_time: {e}")
            # 等待1秒
            time.sleep(1)
            self.get_status()

    def check_diangelist(self, lx_status, diange_list):
        if len(diange_list) >= 1:
            if lx_status['name'] != diange_list[0]['name']:
                del diange_list[0]
                self.del_list_first()

    def process_event(self, event):
        if 'playing' in event:
            lx_status = self.get_status()
            self.check_diangelist(lx_status, self.diange_list)

    def del_list_first(self):
        del self.diange_list[0]
        if self.diange_listwidget.count() > 0:
            item = self.diange_listwidget.takeItem(0)
            if item is not None:
                self.diange_listwidget.removeItemWidget(item)


if __name__ == "__main__":
    app = QApplication([])
    window = DianGeWidget()
    window.show()
    app.exec()
