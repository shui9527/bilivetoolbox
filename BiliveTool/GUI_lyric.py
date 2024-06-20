from UI.lyric_ui import Ui_lyricqwidget
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Signal, Qt, QPoint, Slot, QTimer
import configparser





class LyricWindow(QWidget, Ui_lyricqwidget):
    #定义信号
    closed = Signal()
    save_singnal = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.event_type = ''
        self.parent_widget = parent
        self.oldPos = None





        # self.style_sheet = ('background-color: rgba(235, 155, 55, 60);color: rgb(0, 0, 0);font: 14pt "微软雅黑"; label background-color: rgba(255, 255, 255, 0.1);color: rgb(133, 232, 122);font: 14pt "微软雅黑" )

        # 实例化 UI_Form 类
        self.ui = Ui_lyricqwidget()
        # 将 UI_Form 类中定义的控件添加到当前窗口中
        self.ui.setupUi(self)


        self.ui.name.setFixedWidth(120)

        # 默认样式
        self.ui.name.setStyleSheet('background-color: rgba(209, 228, 235, 0.8);color: rgb(3, 32, 22);')
        self.ui.lyric.setStyleSheet('background-color: rgba(209, 228, 235, 0.8);color: rgb(3, 32, 22);')



    # 更新歌词
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

        self.ui.name.setText(name)

    def update_lyric_label(self, lyric):

        self.ui.lyric.setText(lyric)




    """
    无边框拖放
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

    def closeEvent(self, event):
        self.hide()
        self.save_settings()

        event.accept()


    """
    保存和加载
    """
    def save_settings(self):
        window_position = self.pos()
        window_size = self.size()

        # 添加配置项
        lyricwindow_setting_dist = {'lywindow_name_style': self.ui.name.styleSheet(),
                                  'lywindow_lyric_style': self.ui.lyric.styleSheet(),
                                  'window_position': f"{window_position.x()},{window_position.y()}",
                                  'window_size': f"{window_size.width()},{window_size.height()}"}

        self.save_singnal.emit(lyricwindow_setting_dist)


    def load_settings(self):
        config = configparser.ConfigParser()
        with open('config.ini', encoding='utf-8') as f:
            config.read_file(f)

        lywindow_name_style = config.get('Lyric_window', 'lywindow_name_style')
        lywindow_lyric_style = config.get('Lyric_window', 'lywindow_lyric_style')
        self.ui.name.setStyleSheet(lywindow_name_style)
        self.ui.lyric.setStyleSheet(lywindow_lyric_style)

        move_point_str = config.get('Lyric_window', 'window_position')
        x, y = map(int, move_point_str.split(','))  # 将字符串解析为整数坐标
        window_size_str = config.get('Lyric_window', 'window_size')
        w, h = map(int, window_size_str.split(','))  # 将字符串解析为整数尺寸
        self.setGeometry(x, y, w, h)  # 设置窗口位置和尺寸



    """
    槽函数
    """
    # 接收处理lxsse
    @Slot(str)
    def receive_event(self, event):
        self.process_event(event)



if __name__ == "__main__":
    app = QApplication([])
    window = LyricWindow()
    window.show()
    app.exec()
