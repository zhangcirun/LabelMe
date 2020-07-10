#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
Description :

Author      : Cirun Zhang
Contact     : cirun.zhang@envision-digital.com
Time        : 2020/7/8 
Software    : PyCharm
"""
from PyQt5.Qt import *

from src.img_label import ImgBox
from src.setting_window import SettingWindow


class MainWindow(QMainWindow):
    box1 = None
    box2 = None
    box3 = None
    box4 = None
    img_dictionary = None
    tool_bar = None
    working_directory = None
    setting_window = None

    def __init__(self):
        super().__init__()
        self.set_width_height()
        self.add_menubar()
        self.add_components()
        self.show()

    def add_components(self):
        self.add_imgs('../img/01#箱变_A汇流箱01&1&2020-05-07.png',
                      '../img/01#箱变_A汇流箱01&1&2020-05-07.png',
                      '../img/01#箱变_A汇流箱01&1&2020-05-07.png',
                      '../img/01#箱变_A汇流箱01&1&2020-05-07.png')
        self.tag_button_list_widget = QListWidget()
        self.add_control_buttons()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.gridLayout)
        self.vbox.addWidget(QTextEdit())

        self.HLayout = QHBoxLayout(self.centralWidget)
        self.HLayout.addLayout(self.vbox)
        self.HLayout.addWidget(self.tag_button_list_widget)
        self.HLayout.addWidget(self.control_button_list_widget)

        self.HLayout.setStretch(0, 6)
        self.HLayout.setStretch(1, 2)
        self.HLayout.setStretch(2, 1)

    def refresh_components(self):
        self.HLayout.addLayout(self.vbox)
        self.HLayout.addWidget(self.tag_button_list_widget)
        self.HLayout.addWidget(self.control_button_list_widget)

    def add_control_buttons(self):
        self.control_button_list_widget = QListWidget()

        item_new = QListWidgetItem()
        button_new = QPushButton('OK')
        self.control_button_list_widget.addItem(item_new)
        self.control_button_list_widget.setItemWidget(item_new, button_new)

        item_new = QListWidgetItem()
        button_new = QPushButton('SKIP')
        self.control_button_list_widget.addItem(item_new)
        self.control_button_list_widget.setItemWidget(item_new, button_new)

    def add_imgs(self, img_path1, img_path2, img_path3, img_path4):
        self.gridLayout = QGridLayout()
        self.box1 = ImgBox(self, img_path1, 'box1')
        self.box2 = ImgBox(self, img_path2, 'box2')
        self.box3 = ImgBox(self, img_path3, 'box3')
        self.box4 = ImgBox(self, img_path4, 'box4')

        self.img_dictionary = {'box1': {'isFocused': False, 'isFinished': False, 'object': self.box1},
                               'box2': {'isFocused': False, 'isFinished': False, 'object': self.box2},
                               'box3': {'isFocused': False, 'isFinished': False, 'object': self.box3},
                               'box4': {'isFocused': False, 'isFinished': False, 'object': self.box4}}

        self.gridLayout.addLayout(self.box1, 0, 0)
        self.gridLayout.addLayout(self.box2, 0, 1)
        self.gridLayout.addLayout(self.box3, 1, 0)
        self.gridLayout.addLayout(self.box4, 1, 1)

    def select_img(self, img_name):
        for key in self.img_dictionary:
            if key != img_name:
                self.img_dictionary[key]['isFocused'] = False
                self.img_dictionary[key]['object'].defocus()

        self.img_dictionary[img_name]['isFocused'] = True
        self.img_dictionary[img_name]['object'].focus()

    def add_menubar(self):
        toolbar = self.addToolBar("File")

        bar_open = QAction(QIcon("../img/folder.png"), "select", self)
        toolbar.addAction(bar_open)

        bar_save = QAction(QIcon("../img/db.png"), "output setting", self)
        toolbar.addAction(bar_save)

        bar_exit = QAction(QIcon("../img/exit.png"), "exit", self)
        toolbar.addAction(bar_exit)

        toolbar.actionTriggered[QAction].connect(self.action_toolbar)

    def refresh_tag_buttons(self, items):
        self.tag_button_list_widget.clear()

        for key in items:
            item_new = QListWidgetItem()
            button_new = QPushButton(str(key))
            self.tag_button_list_widget.addItem(item_new)
            self.tag_button_list_widget.setItemWidget(item_new, button_new)

        self.tag_button_list_widget.update()

    def set_width_height(self):
        # self.setLayout()
        self.setFixedWidth(1200)
        self.setFixedHeight(800)

    def action_toolbar(self, a):
        text = a.text()
        if text == 'exit':
            qApp.exit()
        elif text == 'select':
            self.action_browse()
        elif text == 'output setting':
            if self.setting_window is None:
                self.setting_window = SettingWindow(parent=self)
            self.setting_window.show()
            print('save')

    def action_browse(self):
        url = QFileDialog.getExistingDirectory(self, "select")
        if url == "":
            print("\n取消选择")
            return

        if not url.endswith('/'):
            url += '/'

        self.working_directory = url
        print(url)


if __name__ == '__main__':
    app = QApplication([])
    mainwindow = MainWindow()
    app.exec_()
