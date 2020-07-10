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
        self.parent.update_tag()


class ImgBox(QVBoxLayout):

    def __init__(self, parent, img_path, img_name):
        super().__init__()
        self.parent = parent
        self.img = ImgLabel(self, img_path)
        self.img_name = img_name
        self.hbox = QHBoxLayout()

        self.tag = QLabel('None')
        self.tag.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.tag.setAlignment(Qt.AlignCenter)

        self.icon = QLabel('None')
        icon_img = QPixmap('../img/label.png')
        self.icon.setPixmap(icon_img.scaled(20, 20, Qt.KeepAspectRatio))
        self.icon.setAlignment(Qt.AlignCenter)

        self.hbox.addStretch(6)
        self.hbox.addWidget(self.icon, 1)
        self.hbox.addWidget(self.tag, 1)
        self.hbox.addStretch(6)

        self.addLayout(self.hbox)
        self.addWidget(self.img)

    def notify(self):
        self.parent.select_img(self.img_name)

    def focus(self):
        self.img.setStyleSheet("border:10px solid rgb(0, 0, 150); ")
        self.img.update()

    def defocus(self):
        self.img.setStyleSheet("border:10px solid rgb(230, 224, 209); ")
        self.img.update()

    def update_tag(self):
        self.tag.setText("OK")
        self.tag.update()
