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


class LabelListLayout(QVBoxLayout):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.tag_button_list_widget = QListWidget()
        self.tag_button_list_widget.setFocusPolicy(Qt.NoFocus)
        self.tag_button_list_widget.setStyleSheet("border: 5px solid rgb(230, 224, 209);")
        tag_button_list_widget_text = QLabel('Labels')
        tag_button_list_widget_text.setAlignment(Qt.AlignCenter)
        tag_button_list_widget_text.setFont(QtGui.QFont("Helvetica", 15, QtGui.QFont.Bold))
        self.addWidget(tag_button_list_widget_text)
        self.addWidget(self.tag_button_list_widget)
        self.setStretch(0, 1)
        self.setStretch(1, 270)
        self.refresh_tag_buttons({})

    def refresh_tag_buttons(self, items):
        self.tag_button_list_widget.clear()
        button_adder = QPushButton()
        button_adder.setStyleSheet("QPushButton{border-image: url(../img/labelbutton_new.png)}"
                                 "QPushButton:hover{border-image: url(../img/labelbutton_new_hover.png)}"
                                 "QPushButton:pressed{border-image: url(../img/labelbutton_new_press.png)}")
        button_adder.setObjectName('adder')
        button_adder.clicked.connect(self.parent.action_new_setting_window)
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

    def action_label_buttons(self):
        sending_button = self.sender()
        label_name = str(sending_button.objectName())
        self.parent.img_framework_layout.update_label(label_name)
        self.parent.img_framework_layout.move_cursor()

