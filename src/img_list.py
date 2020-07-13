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


class ImgListLayout(QVBoxLayout):
    img_names = []

    def __init__(self):
        super().__init__()
        self.file_list_widget = QListWidget()
        self.file_list_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        text = QLabel('Images')
        text.setAlignment(Qt.AlignCenter)
        text.setFont(QtGui.QFont("Helvetica", 15, QtGui.QFont.Bold))
        self.addWidget(text)
        self.addWidget(self.file_list_widget)
