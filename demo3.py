import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui import window


class MainWindow(QMainWindow, window.Ui_MainWindow):  # 继承 Ui_MainWindow
    def __init__(self):
        super().__init__()  # 初始化 QMainWindow 和 Ui_MainWindow
        self.setupUi(self)  # 设置 UI 界面
        self.setupConnections()  # 设置按钮的槽函数

    def setupConnections(self):
        """在这里连接按钮的信号和槽，并确保信号只连接一次"""


    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()  # 创建 MainWindow 实例
    window.show()  # 显示窗口
    sys.exit(app.exec_())  # 运行应用
