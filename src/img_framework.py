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

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.box1 = ImgBox(self, None)
        self.box2 = ImgBox(self, None)
        self.box3 = ImgBox(self, None)
        self.box4 = ImgBox(self, None)
        self.boxes = [self.box1, self.box2, self.box3, self.box4]

        self.addLayout(self.box1, 0, 0)
        self.addLayout(self.box2, 0, 1)
        self.addLayout(self.box3, 1, 0)
        self.addLayout(self.box4, 1, 1)

    def set_focus(self, target):
        if target.item is not None:
            for box in self.boxes:
                if box is target:
                    box.set_focused(True)
                else:
                    box.set_focused(False)

    def update_label(self, label_name):
        for box in self.boxes:
            if box.is_focused:
                box.set_finished(True)
                box.update_label(label_name)
                break

    def reset_all(self):
        for box in self.boxes:
            box.reset()

    def save(self):
        for box in self.boxes:
            if box.is_finished and box.item is not None:
                self.parent.todo_list_layout.delete(box.item)
                self.parent.done_list_layout.add_item(box.item)
                box.delete()

    def load_from_todo(self, item):
        for box in self.boxes:
            if box.item is None:
                box.load_from_todo(item)
                break

    def unload_from_todo(self, item):
        for box in self.boxes:
            if box.item is item:
                box.unload_from_todo()

    def load_from_done(self, item):
        for box in self.boxes:
            if box.item is None:
                box.load_from_done(item)
                break

    def unload_from_done(self, item):
        for box in self.boxes:
            if box.item is item:
                box.unload_from_done()

        self.parent.done_list_layout.sort()
