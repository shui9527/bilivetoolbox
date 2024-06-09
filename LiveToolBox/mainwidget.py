import os
import sys
import json
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFontDialog,
                               QColorDialog, QSlider, QSizePolicy, QLineEdit)
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import Qt, Signal
import lyricwidget
import diangewidget


class MainWidget(QWidget):
    Sendcodetodiange = Signal(str)

    def __init__(self):
        super().__init__()

        self.font = None
        self.color = None
        self.font_size = None
        self.transparency = None
        self.background_color = None
        self.song_name_width = None

        # 主窗口ui
        self.setWindowTitle('LX播放器直播用插件')
        self.setGeometry(1000, 500, 300, 200)

        self.bt_lyric = QPushButton("显示歌词窗口")
        self.bt_lyric.clicked.connect(self.toggle_lyric_window)
        self.lyric_widget = lyricwidget.LyricWidget()  # 添加LyricWidget组件
        self.lyric_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.bt_font = QPushButton("设置字体")
        self.bt_font.clicked.connect(self.set_lyric_widget_font)

        self.lx_diange_label = QLabel("配合LX播放器点歌")
        self.lx_diange_label2 = QLabel("当前点歌功能未启用")
        self.room_code_label = QLabel('主播身份码')
        self.room_code_le = QLineEdit()
        self.diange_widget = diangewidget.DianGeWidget()
        self.Sendcodetodiange.connect(self.diange_widget.get_room_code)

        self.load_settings()
        self.init_ui()

    def init_ui(self):

        self.label = QLabel("歌词窗口设置")

        self.bt_font = QPushButton("设置字体")
        self.bt_font.clicked.connect(self.set_lyric_widget_font)

        self.bt_color = QPushButton("设置颜色")
        self.bt_color.clicked.connect(self.set_lyric_widget_color)

        self.bt_lyric = QPushButton("显示歌词窗口")
        self.bt_lyric.clicked.connect(self.toggle_lyric_window)

        self.transparency_slider_label = QLabel("设置窗口透明度")
        # 添加设置歌词窗口标签透明度的滑动条
        self.transparency_slider = QSlider(Qt.Horizontal)
        self.transparency_slider.setMinimum(0)
        self.transparency_slider.setMaximum(255)
        # 设置初始透明度
        self.transparency_slider.setValue(200)
        self.transparency_slider.valueChanged.connect(self.set_lyric_widget_transparency)

        self.song_name_width_label = QLabel("设置歌曲名宽度")
        # 添加设置歌曲名宽度标签的滑动条
        self.song_name_width_slider = QSlider(Qt.Horizontal)
        self.song_name_width_slider.setMinimum(50)
        self.song_name_width_slider.setMaximum(800)
        # 设置初始歌曲名宽度
        self.song_name_width_slider.setValue(300)
        self.song_name_width_slider.valueChanged.connect(self.set_song_name_width)

        # 添加设置歌词窗口背景色的按钮
        self.bt_background_color = QPushButton("设置背景色")
        self.bt_background_color.clicked.connect(self.set_lyric_widget_background_color)

        self.bt_diange = QPushButton("启用点歌功能")
        self.bt_diange.clicked.connect(self.toggle_diange)

        self.bt_paidui = QPushButton("排队功能待施工")
        # self.bt_paidui.clicked.connect()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.bt_font)
        layout.addWidget(self.bt_color)
        layout.addWidget(self.transparency_slider_label)
        layout.addWidget(self.transparency_slider)
        layout.addWidget(self.song_name_width_label)
        layout.addWidget(self.song_name_width_slider)
        layout.addWidget(self.bt_background_color)
        layout.addWidget(self.bt_lyric)
        layout.addWidget(self.lx_diange_label)
        layout.addWidget(self.room_code_label)
        layout.addWidget(self.room_code_le)
        layout.addWidget(self.lx_diange_label2)
        layout.addWidget(self.bt_diange)
        self.setLayout(layout)

    """
    关闭主窗口时同时关闭所有窗口
    """

    def closeEvent(self, event):
        if self.lyric_widget is not None:
            self.lyric_widget.close()
        if self.diange_widget is not None:
            self.diange_widget.close()
        event.accept()
        self.save_settings()

    """
    歌词窗口设置项
    """

    def set_lyric_widget_transparency(self, value):
        self.lyric_widget.setWindowOpacity(value / 255)
        self.transparency = value / 255

    def set_song_name_width(self, value):
        self.lyric_widget.song_name.setFixedWidth(value)
        self.song_name_width = value

    def set_lyric_widget_background_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.lyric_widget.setStyleSheet(f"background-color: {color.name()};")
            self.background_color = color

    def set_lyric_widget_font(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.font = font
            if self.lyric_widget:
                self.lyric_widget.song_name.setFont(self.font)
                self.lyric_widget.song_lyric.setFont(self.font)
                self.font_size = self.font.pointSize()

    def set_lyric_widget_color(self):
        self.color = QColorDialog.getColor()
        if self.color.isValid():
            # 更新歌词窗口文本的颜色
            self.lyric_widget.song_name.setStyleSheet(f"color: {self.color.name()};")
            self.lyric_widget.song_lyric.setStyleSheet(f"color: {self.color.name()};")

    """
    保存/读取设置
    """

    def load_settings(self):
        if os.path.exists('settings.json'):
            with open('settings.json', 'r') as f:
                settings = json.load(f)
                if 'font' in settings:
                    self.font = QFont(settings['font'])

                    self.lyric_widget.song_name.setFont(self.font)
                    self.lyric_widget.song_lyric.setFont(self.font)

                if 'color' in settings:
                    self.color = QColor(settings['color'])
                    self.lyric_widget.song_name.setStyleSheet(f"color: {self.color.name()};")
                    self.lyric_widget.song_lyric.setStyleSheet(f"color: {self.color.name()};")

                if 'font_size' in settings:
                    self.font_size = int(settings['font_size'])
                    if self.lyric_widget:
                        font = self.lyric_widget.song_name.font()
                        font.setPointSize(self.font_size)
                        self.lyric_widget.song_name.setFont(font)
                        self.lyric_widget.song_lyric.setFont(font)

                if 'transparency' in settings:
                    self.transparency = settings.get('transparency', 255)
                    self.lyric_widget.setWindowOpacity(self.transparency)

                if 'background_color' in settings:
                    self.background_color = QColor(settings['background_color'])
                    self.lyric_widget.setStyleSheet(f"background-color: {self.background_color.name()};")

                if 'song_name_width' in settings:
                    self.song_name_width = settings.get('song_name_width', 300)
                    self.lyric_widget.song_name.setFixedWidth(self.song_name_width)

                if 'room_code' in settings:
                    self.room_code_le.setText(settings['room_code'])

    def save_settings(self):
        settings = {}
        if self.font:
            settings['font'] = self.font.toString()
        if self.color:
            settings['color'] = self.color.name()
        if self.font_size:
            settings['font_size'] = str(self.font_size)
        if self.transparency:
            settings['transparency'] = float(self.transparency)
        if self.background_color:
            settings['background_color'] = self.background_color.name()
        if self.song_name_width:
            settings['song_name_width'] = int(self.song_name_width)
        if self.room_code_le:
            settings['room_code'] = self.room_code_le.text()

        with open('settings.json', 'w') as f:
            json.dump(settings, f)

    """
    歌词窗口功能开关
    """

    def toggle_lyric_window(self):
        if '显示' in self.bt_lyric.text():
            self.bt_lyric.setText("关闭歌词窗口")
            self.lyric_widget.show()
            self.lyric_widget.start_data_thread()
            self.load_settings()


        else:
            self.bt_lyric.setText("显示歌词窗口")
            self.lyric_widget.hide()
            self.save_settings()

    """
    点歌功能开关
    """

    def toggle_diange(self):

        if self.bt_diange.text() == "启用点歌功能":
            self.bt_diange.setText("关闭点歌列表")
            self.lx_diange_label2.setText("当前点歌功能已启用")
            self.send_code_to_diange_window()
            self.diange_widget.show()
            # 启动弹幕获取函数
            self.diange_widget.start_data_thread()
        else:
            self.bt_diange.setText("启用点歌功能")
            self.diange_widget.hide()

    """
    传递身份码到点歌窗口
    """

    def send_code_to_diange_window(self):
        velue = self.room_code_le.text()
        self.Sendcodetodiange.emit(velue)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.show()

    sys.exit(app.exec())
