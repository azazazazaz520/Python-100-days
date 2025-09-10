import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 创建布局
        layout = QVBoxLayout()
        # 创建标签
        self.label = QLabel('Hello, PyQt5!')
        layout.addWidget(self.label)
        # 创建按钮
        button = QPushButton('Click me')
        button.clicked.connect(self.on_click) # 连接按钮点击事件
        layout.addWidget(button)
        # 设置布局
        self.setLayout(layout)
        # 设置窗口属性
        self.setWindowTitle('My PyQt5 Application')
        self.setGeometry(100, 100, 300, 200)
    def on_click(self):
        self.label.setText('Button clicked!')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show() # 显示主窗口
    sys.exit(app.exec_()) # 运行应用程序
