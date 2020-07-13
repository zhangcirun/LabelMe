#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
Description :

Author      : Cirun Zhang
Contact     : cirun.zhang@envision-digital.com
Time        : 2020/7/13 
Software    : PyCharm
"""
import os
from PyQt5.Qt import *
from PyQt5 import QtGui


class ImgListLayout(QVBoxLayout):
    img_names = []
    working_directory = ''

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.file_list_widget = QListWidget()
        self.file_list_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        text = QLabel('Images')
        text.setAlignment(Qt.AlignCenter)
        text.setFont(QtGui.QFont("Helvetica", 15, QtGui.QFont.Bold))
        self.addWidget(text)
        self.addWidget(self.file_list_widget)

    # Todo this is a demo
    def select_next_batch_imgs(self):
        for i in range(0, 4):
            if i < self.file_list_widget.count():
                self.file_list_widget.item(i).setSelected(True)

    def update_working_dir(self, working_directory):
        self.working_directory = working_directory
        self.iterate_files()

    def iterate_files(self):
        if os.path.exists(self.working_directory) and os.path.isdir(self.working_directory):
            self.img_names = os.listdir(self.working_directory)
            self.file_list_widget.clear()
            for file_name in self.img_names:
                if file_name.endswith('.jpg') or file_name.endswith('.png'):
                    self.add_img_name_to_list(file_name)

            self.file_list_widget.update()
            self.select_next_batch_imgs()
            print(self.img_names)

    def add_img_name_to_list(self, img_name):
        item_new = QListWidgetItem(img_name)
        self.file_list_widget.addItem(item_new)
