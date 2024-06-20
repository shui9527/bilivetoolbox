import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Slot, QTimer, Signal
from UI.main_ui import Ui_Form
from GUI_login import LoginWindow
from GUI_queue import QueueWindow
from GUI_lyric import LyricWindow
from GUI_song import SongWindow
from blivedm.BiliClient import BiliClientThread
from unit.LXSSE import LXSSEThread
from unit.signalclass import Signal_To_Lyric, Signal_To_Song, Signal_To_Queue
import configparser

class MainWindow(QWidget, Ui_Form):
    # 定义信号
    signal_to_lyric = Signal(str)
    signal_to_song = Signal(str)
    signal_to_queue = Signal(str)
    update_danmaku_to_queue = Signal(dict)
    update_danmaku_to_song = Signal(dict)

    def __init__(self):
        self.ly_setting_dict = {}
        self.song_setting_dict = {}
        self.queue_setting_dict = {}


        super().__init__()

        # 实例化 UI_Form 类
        self.ui = Ui_Form()
        # 将 UI_Form 类中定义的控件添加到当前窗口中
        self.ui.setupUi(self)

        self.code = ''
        self.event_type: str = ''



        # 实例化子窗口
        self.LoginWindow = LoginWindow()
        self.LoginWindow.show()
        self.SongWindow = SongWindow()
        self.SongWindow.hide()
        self.QueueWindow = QueueWindow()
        self.QueueWindow.hide()
        self.LyricWindow = LyricWindow()
        self.LyricWindow.hide()



        self.lxsse = LXSSEThread(self)
        self.lxsse.data_updated.connect(self.LyricWindow.receive_event)
        self.lxsse.data_updated.connect(self.SongWindow.receive_event)

        # 调用 UI_Form 类中定义的方法

        # 登录按钮逻辑
        self.LoginWindow.ui.bt_connect.clicked.connect(self.login)
        self.ui.bt_lyshow.clicked.connect(self.lyric_toggle)
        self.ui.bt_dgshow.clicked.connect(self.song_toggle)
        self.ui.bt_pdshow.clicked.connect(self.queue_toggle)
        self.ui.bt_pause.clicked.connect(self.pause_toggle)

        # 实例化信号管理类
        self.signal_to_lyric = Signal_To_Lyric(self.LyricWindow)
        self.signal_to_song = Signal_To_Song(self.SongWindow)
        self.signal_to_queue = Signal_To_Queue(self.QueueWindow)

        # 绑定信号（歌词窗口）
        self.ui.sld_lynamewidth.valueChanged.connect(self.signal_to_lyric.on_name_width_slider_value_changed)
        self.ui.sld_lywindowwidth.valueChanged.connect(self.signal_to_lyric.on_window_width_slider_value_changed)
        self.ui.sld_lytransparency.valueChanged.connect(self.signal_to_lyric.on_transparency_slider_value_changed)
        # self.ui.cb_lycheckbox.stateChanged.connect(self.signal_to_lyric.on_checkbox_state_changed)
        self.ui.bt_lysetfont.clicked.connect(self.signal_to_lyric.on_set_font_button_clicked)
        self.ui.bt_lysetcolor.clicked.connect(self.signal_to_lyric.on_set_color_button_clicked)
        self.ui.bt_lybgsetcolor.clicked.connect(self.signal_to_lyric.on_bg_set_color_button_clicked)
        self.LyricWindow.closed.connect(self.lyricwindow_close)
        self.LyricWindow.save_singnal.connect(self.lyricwindow_save_setting)
        # 绑定信号（点歌窗口）
        self.ui.sld_dgtransparency.valueChanged.connect(self.signal_to_song.on_transparency_slider_value_changed)
        self.ui.bt_dgsetfont.clicked.connect(self.signal_to_song.on_set_font_button_clicked)
        self.ui.bt_dgsetcolor.clicked.connect(self.signal_to_song.on_set_color_button_clicked)
        self.ui.bt_dgbgsetcolor.clicked.connect(self.signal_to_song.on_bg_set_color_button_clicked)
        self.ui.bt_dgbtsetfont.clicked.connect(self.signal_to_song.on_bt_set_font_button_clicked)
        self.ui.bt_dgbtsetcolor.clicked.connect(self.signal_to_song.on_bt_set_color_button_clicked)
        self.update_danmaku_to_song.connect(self.SongWindow.receive_danmaku)
        self.SongWindow.closed.connect(self.songwindow_close)
        self.SongWindow.save_singnal.connect(self.songwindow_save_setting)

        # 绑定信号（排队窗口）
        self.ui.sld_pdtransparency.valueChanged.connect(self.signal_to_queue.on_transparency_slider_value_changed)
        self.ui.bt_pdsetfont.clicked.connect(self.signal_to_queue.on_set_font_button_clicked)
        self.ui.bt_pdsetcolor.clicked.connect(self.signal_to_queue.on_set_color_button_clicked)
        self.ui.bt_pdbgsetcolor.clicked.connect(self.signal_to_queue.on_bg_set_color_button_clicked)
        self.ui.bt_pdbtsetfont.clicked.connect(self.signal_to_queue.on_bt_set_font_button_clicked)
        self.ui.bt_pdbtsetcolor.clicked.connect(self.signal_to_queue.on_bt_set_color_button_clicked)
        self.update_danmaku_to_queue.connect(self.QueueWindow.receive_danmaku)
        self.QueueWindow.closed.connect(self.queuewindow_close)
        self.QueueWindow.save_singnal.connect(self.queuewindow_save_setting)

        # 绑定信号（登录窗口）
        self.LoginWindow.send_code.connect(self.receive_code)

        config = configparser.ConfigParser()
        with open('config.ini', encoding='utf-8') as f:
            config.read_file(f)

        self.code = config.get('Login_window', 'code')
        self.LoginWindow.ui.code.setText(self.code)

    """
    业务逻辑
    """

    # 登录
    def login(self):
        # 隐藏登录窗口
        self.LoginWindow.hide()
        self.show()
        # 发送验证码
        self.LoginWindow.send_code.emit(self.LoginWindow.ui.code.text())

    # 子窗口开关
    def lyric_toggle(self):
        if '显示' in self.ui.bt_lyshow.text():
            self.ui.bt_lyshow.setText("关闭歌词窗口")
            self.LyricWindow.load_settings()   # 加载窗口设置
            self.LyricWindow.show()

        else:
            self.ui.bt_lyshow.setText("显示歌词窗口")
            self.LyricWindow.hide()

    def song_toggle(self):
        if '显示' in self.ui.bt_dgshow.text():
            self.ui.bt_dgshow.setText("关闭点歌窗口")
            self.SongWindow.show()
            self.SongWindow.load_settings()   # 加载窗口设置
        else:
            self.ui.bt_dgshow.setText("显示点歌窗口")
            self.SongWindow.hide()

    def queue_toggle(self):
        if '显示' in self.ui.bt_pdshow.text():
            self.ui.bt_pdshow.setText("关闭排队窗口")
            self.QueueWindow.show()
            self.QueueWindow.load_settings()   # 加载窗口设置
        else:
            self.ui.bt_pdshow.setText("显示排队窗口")
            self.QueueWindow.hide()

    def pause_toggle(self):
        if '暂停' in self.ui.bt_pause.text():
            self.ui.bt_pause.setText("恢复排队")
            self.QueueWindow.pause = True
        else:
            self.ui.bt_pause.setText("暂停排队")
            self.QueueWindow.pause = False


    """
    关闭主窗口时同时关闭所有窗口
    """

    def closeEvent(self, event):
        if self.LyricWindow is not None:
            self.LyricWindow.close()
        if self.SongWindow is not None:
            self.SongWindow.close()
        if self.QueueWindow is not None:
            self.QueueWindow.close()
        self.save_settings()

    # 子窗口关闭修改按钮
    def lyricwindow_close(self):
        self.ui.bt_lyshow.setText("显示歌词窗口")

    def songwindow_close(self):
        self.ui.bt_dgshow.setText("显示点歌窗口")

    def queuewindow_close(self):
        self.ui.bt_pdshow.setText("显示排队窗口")

    # 更新弹幕
    def danmuku_callback(self, danmuku_data):

        # song逻辑
        if danmuku_data['order'] == '切歌' or '点歌':
            self.update_danmaku_to_song.emit(danmuku_data)

        # queue逻辑
        if danmuku_data['order'] == '排队' or '取消排队':
            self.update_danmaku_to_queue.emit(danmuku_data)




    """
    保存设置项
    """

    def save_settings(self):
        # 创建一个 ConfigParser 对象
        config = configparser.ConfigParser()

        # 设置配置项

        config['Login_window'] = {'code': self.code}


        print(self.ly_setting_dict)
        config['Lyric_window'] = self.ly_setting_dict

        print(self.song_setting_dict)
        config['Song_window'] = self.song_setting_dict

        print(self.queue_setting_dict)
        config['Queue_window'] = self.queue_setting_dict

        # 写入配置文件
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)

        print('保存成功')



    """
    槽函数
    """
    @Slot(dict)
    def lyricwindow_save_setting(self, setting):
        self.ly_setting_dict = setting


    @Slot(dict)
    def songwindow_save_setting(self, setting):
        self.song_setting_dict = setting

    @Slot(dict)
    def queuewindow_save_setting(self, setting):
        self.queue_setting_dict = setting


    # 接收身份码，启动client
    @Slot(str)
    def receive_code(self, code):
        if code == '':
            QMessageBox.warning(self, 'warning', '未输入身份码，无法连接直播间获取弹幕')
            return

        self.code = code
        self.biliclient = BiliClientThread(self, self.code, self.danmuku_callback)
        self.biliclient.start()

        self.lxsse.start()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.hide()
    sys.exit(app.exec())
