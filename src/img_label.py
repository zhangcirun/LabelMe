#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
Description :

Author      : Cirun Zhang
Contact     : cirun.zhang@envision-digital.com
Time        : 2020/7/9 
Software    : PyCharm
"""
from PyQt5.Qt import *
from PyQt5 import QtGui
from src.img_list import ListItem


class ImgLabel(QLabel):
    def __init__(self, parent, img_path):
        super().__init__()
        self.parent = parent
        self.set_img(img_path)
        self.setStyleSheet("border:10px solid rgb(230, 224, 209); ")

    def set_img(self, img_path):
        img = QPixmap(img_path)
        self.setPixmap(img.scaled(400, 400, Qt.KeepAspectRatio))

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.parent.notify()


class ImgBox(QVBoxLayout):
    DEFAULT_PATH = '../img/image.png'
    is_focused = False
    is_finished = False
    item = None

    def __init__(self, parent, item: ListItem):
        super().__init__()
        self.parent = parent
        self.item = item

        if self.item is None:
            self.img = ImgLabel(self, self.DEFAULT_PATH)
        else:
            self.img = ImgLabel(self, item.img_path)

        self.container = QWidget()
        self.hbox = QHBoxLayout(self.container)
        self.container.setStyleSheet("background-color: rgb(189, 188, 185); ")

        self.tag = QLabel('')
        self.tag.setFont(QtGui.QFont("Helvetica", 22, QtGui.QFont.Bold))
        self.tag.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.icon = QLabel()
        self.icon.setAlignment(Qt.AlignLeft)
        self.icon_img_check = QPixmap('../img/check.png')
        self.icon_img_check = self.icon_img_check.scaled(40, 40, Qt.KeepAspectRatio)

        self.icon_img_pending = QPixmap('../img/pending.png')
        self.icon_img_pending = self.icon_img_pending.scaled(40, 40, Qt.KeepAspectRatio)

        # self.gif = QMovie('../img/91.gif')
        # self.gif.setScaledSize(QSize(30, 30))
        # self.gif.start()
        self.icon.setFixedSize(40, 40)
        #self.icon.setPixmap(self.icon_img_pending)

        self.hbox.addWidget(self.icon, 1)
        self.hbox.addStretch(6)
        self.hbox.addWidget(self.tag, 1)

        self.addWidget(self.container)
        self.addWidget(self.img)
        self.setSpacing(0)

    def notify(self):
        self.parent.set_focus(self)

    def set_finished(self, is_finished):
        self.is_finished = is_finished
        self.update_border()

    def set_focused(self, is_focused):
        self.is_focused = is_focused
        self.update_border()

    def update_label(self, label):
        self.item.set_label(label)
        self.tag.setText(label)
        self.tag.update()

    def update_border(self):
        if self.is_focused:
            self.img.setStyleSheet("border:10px solid rgb(99, 142, 186); ")
        else:
            self.img.setStyleSheet("border:10px solid rgb(217, 216, 212); ")

        if self.is_finished:
            #self.gif.stop()
            self.icon.setPixmap(self.icon_img_check)
            self.container.setStyleSheet("background-color: rgb(192, 217, 143); ")
        else:
            #self.gif.start()
            self.icon.setPixmap(self.icon_img_pending)
            self.container.setStyleSheet("background-color: rgb(189, 188, 185); ")

        self.container.update()
        self.icon.update()
        self.img.update()

    def load_from_todo(self, item):
        self.item = item
        self.img.set_img(self.item.img_path)
        self.item.set_label(self.item.label)
        self.tag.setText(self.item.label)
        self.is_finished = False
        self.is_focused = False
        self.update_border()

    def unload_from_todo(self):
        self.item.set_label('None')
        self.tag.setText('')
        self.item = None
        self.is_finished = False
        self.is_focused = False
        self.update_border()
        self.icon.setPixmap(QPixmap())
        self.img.set_img(self.DEFAULT_PATH)

    def load_from_done(self, item):
        self.item = item
        self.img.set_img(self.item.img_path)
        self.item.set_label(self.item.label)
        self.tag.setText(self.item.label)
        self.is_finished = True
        self.is_focused = False
        self.update_border()

    def unload_from_done(self):
        self.tag.setText('')
        self.item.setText('[' + self.item.label + '] ' + self.item.img_name)
        self.item = None
        self.is_finished = False
        self.is_focused = False
        self.update_border()
        self.icon.setPixmap(QPixmap())
        self.img.set_img(self.DEFAULT_PATH)

    def delete(self):
        self.img.set_img(self.DEFAULT_PATH)
        self.tag.setText('')

        if self.item is not None:
            self.item.setSelected(False)

        self.item = None
        self.is_finished = False
        self.is_focused = False
        print('delete')
        self.update_border()
        self.icon.setPixmap(QPixmap())

    def reset(self):
        self.item.set_label('None')
        self.tag.setText(self.item.label)
        self.is_finished = False
        self.update_border()