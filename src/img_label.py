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


class ImgLabel(QLabel):
    def __init__(self, parent, img_path):
        super().__init__()
        self.parent = parent
        img = QPixmap(img_path)
        self.setPixmap(img.scaled(400, 400, Qt.KeepAspectRatio))
        self.setStyleSheet("border:10px solid rgb(230, 224, 209); ")

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.parent.notify()


class ImgBox(QVBoxLayout):
    is_focused = False
    is_finished = False
    label = None

    def __init__(self, parent, img_path, img_name):
        super().__init__()
        self.parent = parent
        self.img = ImgLabel(self, img_path)
        self.img_name = img_name

        self.container = QWidget()
        self.hbox = QHBoxLayout(self.container)
        self.container.setStyleSheet("background-color: rgb(189, 188, 185); ")

        self.tag = QLabel('None')
        self.tag.setFont(QtGui.QFont("Helvetica", 18, QtGui.QFont.Bold))
        self.tag.setAlignment(Qt.AlignVCenter)

        # self.icon = QLabel()
        # icon_img = QPixmap('../img/flag.png')
        # self.icon.setPixmap(icon_img.scaled(30, 30, Qt.KeepAspectRatio))
        # self.icon.setAlignment(Qt.AlignLeft)

        self.icon = QLabel()
        #self.icon.setStyleSheet("padding:{0px 0px 0px 0px;}")
        gif = QMovie('../img/91.gif')
        gif.setScaledSize(QSize(30, 30))
        gif.start()
        self.icon.setMovie(gif)

        self.hbox.addWidget(self.icon, 1)
        self.hbox.addStretch(6)
        self.hbox.addWidget(self.tag, 1)

        self.addWidget(self.container)
        self.addWidget(self.img)
        self.setSpacing(0)

    def notify(self):
        self.parent.select_img(self.img_name)

    def set_finished(self, is_finished):
        self.is_finished = is_finished
        self.update_border()

    def set_focused(self, is_focused):
        self.is_focused = is_focused
        self.update_border()

    def update_label(self, label):
        self.tag.setText(label)
        self.tag.update()

    def update_border(self):
        if self.is_focused:
            self.img.setStyleSheet("border:10px solid rgb(99, 142, 186); ")
        else:
            self.img.setStyleSheet("border:10px solid rgb(217, 216, 212); ")

        self.img.update()

        if self.is_finished:
            icon_img = QPixmap('../img/check.png')
            self.icon.setPixmap(icon_img.scaled(30, 30, Qt.KeepAspectRatio))
            self.icon.setAlignment(Qt.AlignLeft)
            # gif = QMovie('../img/gif1.gif')
            # gif.setScaledSize(QSize(30, 30))
            # self.icon.setMovie(gif)

            self.container.setStyleSheet("background-color: rgb(192, 217, 143); ")

            self.container.update()
            self.icon.update()
