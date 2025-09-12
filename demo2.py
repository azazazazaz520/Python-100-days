import sys
import ui
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QGridLayout)
class myApp(QWidget):
    def __init__(self):
        super().__init__()     #父类的构造函数
        self.initUI()

    def initUI(self):
        # 创建布局
        layout = QGridLayout()
        # 创建标签
        self.label1 = QLabel('Hello, PyQt5!')

        #创建另一个标签
        self.label2 = QLabel('This is a demo')

        self.label3 = QLabel('3')
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.label2, 0, 1)
        layout.addWidget(self.label3, 0, 2)
        # 创建按钮
        button = QPushButton('Click me')
        button.clicked.connect(self.on_click)  # 连接按钮点击事件
        layout.addWidget(button,4,9)
        #创建另一个按钮
        button2 = QPushButton('Click me')
        button2.clicked.connect(self.on_click_button2)
        layout.addWidget(button2,8,9)
        # 设置布局
        self.setLayout(layout)
        # 设置窗口属性
        self.setWindowTitle('My PyQt5 Application')
        self.setGeometry(100, 100, 800, 700)
    def on_click(self):
        self.label2.setText('Button clicked!')
    def on_click_button2(self):
        self.label3.setText('Button clicked!!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myApp()
    ex.show()  # 显示主窗口
    sys.exit(app.exec_())  # 运行应用程序


'''
QApplication：是 PyQt 应用程序的基础，每个 PyQt 应用程序都必须创建一个QApplication对象。
它管理着应用程序的控制流、事件处理、设置等。
例如，它负责处理用户的输入事件（鼠标点击、键盘输入等），并将这些事件分发给相应的控件进行处理。
没有QApplication对象，应用程序无法正常运行。

QWidget：是所有用户界面对象的基类，是最基本的窗口组件。
所有的 UI 组件（如按钮、标签、文本框等）都是直接或间接继承自QWidget。
它提供了基本的功能，如设置窗口的大小、位置、标题，处理鼠标和键盘事件等。
我们创建的主窗口类myApp继承自QWidget，从而获得了这些基本功能。



'''
