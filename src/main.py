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
from src.img_label import ImgBox
from src.pic_button import PicButton
from src.setting_window import SettingWindow
from src.img_list import ImgListLayout


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
        self.add_imgs('../img/image.png',
                      '../img/image.png',
                      '../img/image.png',
                      '../img/image.png')
        self.tag_button_list_widget_layout = QVBoxLayout()
        self.tag_button_list_widget = QListWidget()
        self.tag_button_list_widget.setFocusPolicy(Qt.NoFocus)
        self.tag_button_list_widget.setStyleSheet("border: 5px solid rgb(230, 224, 209);")
        tag_button_list_widget_text = QLabel('Labels')
        tag_button_list_widget_text.setAlignment(Qt.AlignCenter)
        tag_button_list_widget_text.setFont(QtGui.QFont("Helvetica", 15, QtGui.QFont.Bold))
        self.tag_button_list_widget_layout.addWidget(tag_button_list_widget_text)
        self.tag_button_list_widget_layout.addWidget(self.tag_button_list_widget)
        self.tag_button_list_widget_layout.setStretch(0, 1)
        self.tag_button_list_widget_layout.setStretch(1, 270)

        self.refresh_tag_buttons({})

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.gridLayout)
        #self.vbox.addWidget(QTextEdit())

        self.file_list_layout = ImgListLayout()

        self.HLayout = QHBoxLayout(self.centralWidget)
        self.HLayout.addLayout(self.vbox)
        self.HLayout.addLayout(self.tag_button_list_widget_layout)
        self.HLayout.addLayout(self.file_list_layout)

        self.HLayout.setStretch(0, 6)
        self.HLayout.setStretch(1, 3)
        self.HLayout.setStretch(2, 3)

    def add_img_name_to_list(self, img_name):
        item_new = QListWidgetItem(img_name)
        self.file_list_widget.addItem(item_new)

    def add_imgs(self, img_path1, img_path2, img_path3, img_path4):
        self.gridLayout = QGridLayout()
        self.box1 = ImgBox(self, img_path1, 'box1')
        self.box2 = ImgBox(self, img_path2, 'box2')
        self.box3 = ImgBox(self, img_path3, 'box3')
        self.box4 = ImgBox(self, img_path4, 'box4')

        self.img_dictionary = {'box1': {'label': 'None', 'object': self.box1},
                               'box2': {'label': 'None', 'object': self.box2},
                               'box3': {'label': 'None', 'object': self.box3},
                               'box4': {'label': 'None', 'object': self.box4}}

        self.gridLayout.addLayout(self.box1, 0, 0)
        self.gridLayout.addLayout(self.box2, 0, 1)
        self.gridLayout.addLayout(self.box3, 1, 0)
        self.gridLayout.addLayout(self.box4, 1, 1)

    def select_img(self, img_name):
        for key in self.img_dictionary:
            if key != img_name:
                self.img_dictionary[key]['object'].set_focused(False)

        self.img_dictionary[img_name]['object'].set_focused(True)

    def update_label(self, label_name):
        for key in self.img_dictionary:
            obj = self.img_dictionary[key]['object']
            if obj.is_focused:
                self.img_dictionary[key]['label'] = label_name
                obj.set_finished(True)
                obj.update_label(label_name)
                break

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
        button_adder = QPushButton()
        button_adder.setStyleSheet("QPushButton{border-image: url(../img/labelbutton_new.png)}"
                                 "QPushButton:hover{border-image: url(../img/labelbutton_new_hover.png)}"
                                 "QPushButton:pressed{border-image: url(../img/labelbutton_new_press.png)}")
        button_adder.setObjectName('adder')
        button_adder.clicked.connect(self.action_new_setting_window)
        item_adder = QListWidgetItem()
        item_adder.setSizeHint(QSize(0, 80))

        self.tag_button_list_widget.addItem(item_adder)
        self.tag_button_list_widget.setItemWidget(item_adder, button_adder)

        for key in items:
            item_new = QListWidgetItem()
            item_new.setSizeHint(QSize(0, 80))
            button_new = QPushButton()
            button_new.setStyleSheet("QPushButton{border-image: url(../img/labelbutton_default.png)}"
                                     "QPushButton:hover{border-image: url(../img/labelbutton_cover.png)}"
                                     "QPushButton:pressed{border-image: url(../img/labelbutton_pressed.png)}"
                                     "QPushButton{font:bold; font-size:30px;color:rgb(255,255,255)}")
            button_new.setText(str(key))
            button_new.setObjectName(str(key))
            button_new.clicked.connect(self.action_label_buttons)
            self.tag_button_list_widget.addItem(item_new)
            self.tag_button_list_widget.setItemWidget(item_new, button_new)

        self.tag_button_list_widget.update()

    def set_width_height(self):
        # self.setLayout()
        self.setFixedWidth(1300)
        self.setFixedHeight(800)

    def action_label_buttons(self):
        sending_button = self.sender()
        label_name = str(sending_button.objectName())
        self.update_label(label_name)

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
