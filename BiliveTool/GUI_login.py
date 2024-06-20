from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Signal
from UI.login_ui import Ui_Frame



class LoginWindow(QWidget, Ui_Frame):
    # 定义信号
    send_code = Signal(str)

    def __init__(self):
        super().__init__()

        # 实例化 UI_Form 类
        self.ui = Ui_Frame()
        # 将 UI_Form 类中定义的控件添加到当前窗口中
        self.ui.setupUi(self)









if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec()
