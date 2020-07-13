#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
Description :

Author      : Cirun Zhang
Contact     : cirun.zhang@envision-digital.com
Time        : 2020/7/13 
Software    : PyCharm
"""
from PyQt5.Qt import *
from PyQt5 import QtGui
from src.img_label import ImgBox


class ImgFrameWorkLayout(QGridLayout):
    img_path1 = '../img/image.png'
    img_path2 = '../img/image.png'
    img_path3 = '../img/image.png'
    img_path4 = '../img/image.png'

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.box1 = ImgBox(self, self.img_path1, 'box1')
        self.box2 = ImgBox(self, self.img_path2, 'box2')
        self.box3 = ImgBox(self, self.img_path3, 'box3')
        self.box4 = ImgBox(self, self.img_path4, 'box4')
        self.boxes = [self.box1, self.box2, self.box3, self.box4]

        self.addLayout(self.box1, 0, 0)
        self.addLayout(self.box2, 0, 1)
        self.addLayout(self.box3, 1, 0)
        self.addLayout(self.box4, 1, 1)

    def set_focus(self, target):
        for box in self.boxes:
            if box == target:
                box.set_focused(True)
            else:
                box.set_focused(False)

    def update_label(self, label_name):
        for box in self.boxes:
            if box.is_focused:
                box.set_finished(True)
                box.update_label(label_name)
                break
