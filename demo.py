import os
import shutil
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QListWidget, QStatusBar,
                             QMessageBox, QInputDialog, QMenu, QListWidgetItem)


class FileManager(QWidget):
    def __init__(self):
        super().__init__()
        self.current_path = os.getcwd()  # 当前工作目录
        self.initUI()

    def initUI(self):
        # 创建布局
        top_Layout = QHBoxLayout()
        # 顶部布局：路径输入框和前往按钮
        self.path_edit = QLineEdit(self.current_path)
        self.go_button = QPushButton("前往")
        self.go_button.clicked.connect(self.go_to_path)
        top_Layout.addWidget(self.path_edit)
        top_Layout.addWidget(self.go_button)

        # 中间文件列表布局
        self.file_list = QListWidget()
        self.file_list.itemDoubleClicked.connect(self.open_file_or_folder)
        self.file_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.file_list.customContextMenuRequested.connect(self.show_context_menu)

        # 底部状态栏
        self.status_bar = QStatusBar()
        self.status_bar.showMessage(f'当前目录: {self.current_path}')

        # 整体布局
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_Layout)
        main_layout.addWidget(self.file_list)
        main_layout.addWidget(self.status_bar)
        self.setLayout(main_layout)
        self.setWindowTitle('简易文件管理器')
        self.setGeometry(300, 300, 600, 400)

        self.update_file_list()
        self.show()

    def update_file_list(self):
        self.file_list.clear()
        self.path_edit.setText(self.current_path)

        try:
            # 添加返回上一级的选项
            if self.current_path != os.path.dirname(self.current_path):
                self.file_list.addItem("..")

            for item in os.listdir(self.current_path):
                item_path = os.path.join(self.current_path, item)
                if os.path.isdir(item_path):
                    # 文件夹
                    list_item = QListWidgetItem(QIcon.fromTheme('folder'), item)
                else:
                    # 文件
                    list_item = QListWidgetItem(QIcon.fromTheme('text-x-generic'), item)
                self.file_list.addItem(list_item)
        except Exception as e:
            QMessageBox.warning(self, '错误', f'无法读取目录: {str(e)}')

    def go_to_path(self):
        path = self.path_edit.text()
        if os.path.exists(path) and os.path.isdir(path):
            self.current_path = path
            self.update_file_list()
            self.status_bar.showMessage(f'当前目录: {self.current_path}')
        else:
            QMessageBox.warning(self, '错误', '路径不存在或不是一个目录')

    def open_file_or_folder(self, item):
        item_name = item.text()

        # 处理返回上一级目录
        if item_name == "..":
            self.current_path = os.path.dirname(self.current_path)
            self.update_file_list()
            self.status_bar.showMessage(f'当前目录: {self.current_path}')
            return

        item_path = os.path.join(self.current_path, item_name)

        if os.path.isdir(item_path):
            self.current_path = item_path
            self.update_file_list()
            self.status_bar.showMessage(f'当前目录: {self.current_path}')
        else:
            try:
                # 跨平台打开文件
                if sys.platform == "win32":
                    os.startfile(item_path)
                elif sys.platform == "darwin":
                    os.system(f"open '{item_path}'")
                else:
                    os.system(f"xdg-open '{item_path}'")
            except Exception as e:
                QMessageBox.warning(self, '错误', f'无法打开文件: {str(e)}')

    def show_context_menu(self, pos):
        item = self.file_list.itemAt(pos)
        menu = QMenu(self)

        if item:
            item_path = os.path.join(self.current_path, item.text())

            if item.text() != "..":  # 不能对".."进行操作
                delete_action = menu.addAction('删除')
                delete_action.triggered.connect(lambda: self.delete_item(item_path))

                if os.path.isdir(item_path):
                    new_folder_action = menu.addAction('在此新建文件夹')
                    new_folder_action.triggered.connect(lambda: self.create_folder(item_path))

        # 总是在当前目录添加新建文件夹选项
        new_folder_action = menu.addAction('新建文件夹')
        new_folder_action.triggered.connect(lambda: self.create_folder(self.current_path))

        menu.exec_(self.file_list.mapToGlobal(pos))

    def create_folder(self, parent_path):
        folder_name, ok = QInputDialog.getText(self, '新建文件夹', '请输入文件夹名称:')
        if ok and folder_name:
            new_folder_path = os.path.join(parent_path, folder_name)
            try:
                os.mkdir(new_folder_path)
                self.update_file_list()
            except Exception as e:
                QMessageBox.warning(self, '错误', f'无法创建文件夹: {str(e)}')

    def delete_item(self, item_path):
        reply = QMessageBox.question(self, '确认删除', f'确定要删除 {os.path.basename(item_path)} 吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                else:
                    shutil.rmtree(item_path)  # 删除非空文件夹
                self.update_file_list()
            except Exception as e:
                QMessageBox.warning(self, '错误', f'无法删除: {str(e)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileManager()
    sys.exit(app.exec_())