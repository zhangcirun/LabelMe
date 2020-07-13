#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
Description :

Author      : Cirun Zhang
Contact     : cirun.zhang@envision-digital.com
Time        : 2020/7/8 
Software    : PyCharm
"""
import os
from PyQt5.Qt import *
from PyQt5 import QtGui
from src.pic_button import PicButton
from src.setting_window import SettingWindow
from src.img_list import ImgListLayout
from src.label_list import LabelListLayout
from src.img_framework import ImgFrameWorkLayout


class MainWindow(QMainWindow):
    box1 = None
    box2 = None
    box3 = None
    box4 = None
    img_dictionary = None
    tool_bar = None
    working_directory = None
    setting_window = None
    label_list = None
    img_framework = None

    def __init__(self):
        super().__init__()
        self.set_width_height()
        self.add_menubar()
        self.add_components()
        self.show()

    def add_components(self):
        self.img_framework = ImgFrameWorkLayout(self)
        self.label_list = LabelListLayout(self)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.file_list_layout = ImgListLayout()

        self.HLayout = QHBoxLayout(self.centralWidget)
        self.HLayout.addLayout(self.img_framework)
        self.HLayout.addLayout(self.label_list)
        self.HLayout.addLayout(self.file_list_layout)

        self.HLayout.setStretch(0, 6)
        self.HLayout.setStretch(1, 3)
        self.HLayout.setStretch(2, 3)

    def add_img_name_to_list(self, img_name):
        item_new = QListWidgetItem(img_name)
        self.file_list_widget.addItem(item_new)

    def add_menubar(self):
        toolbar = self.addToolBar("File")

        bar_open = QAction(QIcon("../img/folder.png"), "select", self)
        toolbar.addAction(bar_open)

        bar_save = QAction(QIcon("../img/db.png"), "output setting", self)
        toolbar.addAction(bar_save)

        bar_exit = QAction(QIcon("../img/exit.png"), "exit", self)
        toolbar.addAction(bar_exit)

        toolbar.actionTriggered[QAction].connect(self.action_toolbar)

    def set_width_height(self):
        # self.setLayout()
        self.setFixedWidth(1300)
        self.setFixedHeight(800)

    def action_new_setting_window(self):
        if self.setting_window is None:
            self.setting_window = SettingWindow(parent=self)
        self.setting_window.show()

    def action_toolbar(self, a):
        text = a.text()
        if text == 'exit':
            qApp.exit()
        elif text == 'select':
            self.action_browse()
        elif text == 'output setting':
            self.action_new_setting_window()

    def action_browse(self):
        url = QFileDialog.getExistingDirectory(self, "select")
        if url == "":
            print("\n取消选择")
            return

        if not url.endswith('/'):
            url += '/'

        self.working_directory = url
        self.iterate_files()

    def iterate_files(self):
        if os.path.exists(self.working_directory) and os.path.isdir(self.working_directory):
            self.file_names = os.listdir(self.working_directory)
            self.file_list_widget.clear()
            for file_name in self.file_names:
                if file_name.endswith('.jpg') or file_name.endswith('.png'):
                    self.add_img_name_to_list(file_name)

            self.file_list_widget.update()
            self.select_next_batch_imgs()
            print(self.file_names)

    # Todo this is a demo
    def select_next_batch_imgs(self):
        for i in range(0, 4):
            if i < self.file_list_widget.count():
                self.file_list_widget.item(i).setSelected(True)


if __name__ == '__main__':
    app = QApplication([])
    mainwindow = MainWindow()
    app.exec_()
