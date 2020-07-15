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


class ControlButtonsLayout(QVBoxLayout):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.save_button = QPushButton()
        self.save_button.setObjectName('save')
        self.save_button.setStyleSheet("QPushButton{border-image: url(../img/save.png)}"
                                       "QPushButton:hover{border-image: url(../img/save_hover.png)}"
                                       "QPushButton:pressed{border-image: url(../img/save_press.png)}")
        self.save_button.setFixedSize(60, 60)
        self.save_button.clicked.connect(self.parent.img_framework_layout.save)

        self.next_button = QPushButton()
        self.next_button.setObjectName('next')
        self.next_button.setStyleSheet("QPushButton{border-image: url(../img/next.png)}"
                                       "QPushButton:hover{border-image: url(../img/next_hover.png)}"
                                       "QPushButton:pressed{border-image: url(../img/next_press.png)}")
        self.next_button.setFixedSize(60, 60)
        self.next_button.clicked.connect(self.parent.img_framework_layout.load_next_four)

        self.reset_button = QPushButton()
        self.reset_button.setObjectName('reset')
        self.reset_button.setStyleSheet("QPushButton{border-image: url(../img/reset.png)}"
                                        "QPushButton:hover{border-image: url(../img/reset_hover.png)}"
                                        "QPushButton:pressed{border-image: url(../img/reset_press.png)}")
        self.reset_button.setFixedSize(60, 60)
        self.reset_button.clicked.connect(self.parent.img_framework_layout.delete_all)

        self.addStretch(1)
        self.addWidget(self.save_button)
        self.addWidget(self.next_button)
        self.addWidget(self.reset_button)
        self.addStretch(2)
