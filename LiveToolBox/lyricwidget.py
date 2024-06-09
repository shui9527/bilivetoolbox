from PySide6.QtWidgets import (QWidget, QLabel, QHBoxLayout, QSizePolicy)
from PySide6.QtCore import Qt, QTimer
import monitevent


class LyricWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.song_name = QLabel('歌曲名称')  # 设置初始值
        self.song_lyric = QLabel('歌曲歌词')  # 设置初始值

        self.song_name.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.song_lyric.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        # 设置widget大小策略

        self.parent_widget = parent  # 保存父窗口指针
        self.event_type = ''
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('歌词窗口')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 设置窗口置顶
        self.setGeometry(600, 30, 1400, 30)  # 设置窗口大小

        # 设置文本靠左
        self.song_name.setAlignment(Qt.AlignLeft)
        self.song_lyric.setAlignment(Qt.AlignLeft)

        layout = QHBoxLayout()
        layout.addWidget(self.song_name)
        layout.addWidget(self.song_lyric)
        self.setLayout(layout)

        if self.parent_widget and self.parent_widget.font:
            self.song_name.setFont(self.parent_widget.font)
            self.song_lyric.setFont(self.parent_widget.font)
        if self.parent_widget and self.parent_widget.color:
            self.song_name.setStyleSheet(f"color: {self.parent_widget.color.name()};")
            self.song_lyric.setStyleSheet(f"color: {self.parent_widget.color.name()};")

        self.monite_thread = monitevent.LxSSEThread()
        self.monite_thread.data_updated.connect(self.process_event)

    """
    接收event更新歌词显示
    """

    def start_data_thread(self):
        self.monite_thread.start()

    def stop_data_thread(self):
        self.monite_thread.quit()

    def process_event(self, event):

        if '无法连接' in event:
            name = event.split(':')[0].strip().replace('"', '')
            lyric = event.split(':')[1].strip().replace('"', '')
            QTimer.singleShot(0, lambda: self.update_name_label(name))
            QTimer.singleShot(0, lambda: self.update_lyric_label(lyric))

        elif 'name' in event:
            # print(event)
            self.event_type = 'name'

        elif 'lyricLineText' in event:
            # print(event)
            self.event_type = 'lyricLineText'

        elif 'data' in event:
            if 'name' in self.event_type:
                name = event.split(':')[1].strip().replace('"', '')
                QTimer.singleShot(0, lambda: self.update_name_label(name))
                self.event_type = ''

            elif 'lyricLineText' in self.event_type:
                lyric = event.split(':')[1].strip().replace('"', '')
                QTimer.singleShot(0, lambda: self.update_lyric_label(lyric))
                self.event_type = ''

    def update_name_label(self, name):
        self.song_name.setText(name)

    def update_lyric_label(self, lyric):
        self.song_lyric.setText(lyric)

    def closeEvent(self, event):
        self.hide()
        event.accept()
