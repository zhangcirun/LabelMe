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
from src.img_list import ImgListLayout
from src.label_list import LabelListLayout
from src.img_framework import ImgFrameWorkLayout
from src.tool_bar import ToolBar
from src.setting_window import SettingWindow
from src.control_buttons import ControlButtonsLayout

class MainWindow(QMainWindow):
    tool_bar = None
    setting_window = None
    label_list_layout = None
    img_framework_layout = None
    file_list_layout = None
    control_buttons_layout = None

    def __init__(self):
        super().__init__()
        self.set_width_height()
        self.add_components()
        self.show()

    def add_components(self):
        self.tool_bar = ToolBar(self)
        self.img_framework_layout = ImgFrameWorkLayout(self)
        self.label_list_layout = LabelListLayout(self)
        self.file_list_layout = ImgListLayout(self)
        self.control_buttons_layout = ControlButtonsLayout(self)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.addToolBar(self.tool_bar)

        self.HLayout = QHBoxLayout(self.centralWidget)
        self.HLayout.addLayout(self.img_framework_layout)
        self.HLayout.addLayout(self.label_list_layout)
        self.HLayout.addLayout(self.file_list_layout)
        self.HLayout.addLayout(self.control_buttons_layout)

        self.HLayout.setStretch(0, 6)
        self.HLayout.setStretch(1, 3)
        self.HLayout.setStretch(2, 3)
        self.HLayout.setStretch(3, 1)

    def action_new_setting_window(self):
        if self.setting_window is None:
            self.setting_window = SettingWindow(parent=self)
        self.setting_window.show()

    def set_width_height(self):
        self.setFixedWidth(1350)
        self.setFixedHeight(800)


if __name__ == '__main__':
    app = QApplication([])
    mainwindow = MainWindow()
    app.exec_()
