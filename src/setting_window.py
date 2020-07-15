#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
Description :

Author      : Cirun Zhang
Contact     : cirun.zhang@envision-digital.com
Time        : 2020/7/8 
Software    : PyCharm
"""
from src.item_window import ItemWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *


class SettingWindow(QMainWindow):
    list_widget = None
    label_dict = {}

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.set_width_height()
        self.add_components()
        self.setWindowTitle('Output Setting')
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def set_width_height(self):
        self.setFixedWidth(400)
        self.setFixedHeight(300)

    def add_components(self):
        self.buttonsWidget = QWidget()
        self.buttonsWidgetLayout = QHBoxLayout(self.buttonsWidget)
        self.button_new = QPushButton("NEW")
        self.button_new.clicked.connect(self.action_new)

        self.button_modify = QPushButton("MODIFY")
        self.button_modify.clicked.connect(self.action_modify)

        self.button_delete = QPushButton("DELETE")
        self.button_delete.clicked.connect(self.action_delete)

        self.buttonsWidgetLayout.addWidget(self.button_new)
        self.buttonsWidgetLayout.addWidget(self.button_modify)
        self.buttonsWidgetLayout.addWidget(self.button_delete)

        self.listwidget = QListWidget(self)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.vLayout = QVBoxLayout(self.centralWidget)
        self.vLayout.addWidget(self.listwidget)
        self.vLayout.addWidget(self.buttonsWidget)

    def action_new(self):
        itemwindow = ItemWindow(self)
        itemwindow.show()

    def action_delete(self):
        items = self.listwidget.selectedItems()
        if len(items) > 0:
            name = items[0].text()
            row = self.listwidget.row(items[0])
            self.delete_item(name)
            self.listwidget.takeItem(row)

    def action_modify(self):
        items = self.listwidget.selectedItems()
        if len(items) > 0:
            name = items[0].text()
            url = self.label_dict[name]
            itemwindow = ItemWindow(parent=self, name_old=name, url_old=url)
            itemwindow.show()

    def new_item(self, name, url):
        if name not in self.label_dict:
            item_new = QListWidgetItem(name)
            item_new.setIcon(QIcon('../img/label.png'))
            self.label_dict[name] = url
            self.listwidget.addItem(item_new)
            self.parent().label_list_layout.refresh_tag_buttons(self.label_dict)
        print(self.label_dict)

    def delete_item(self, name):
        self.label_dict.pop(name)
        self.parent().label_list_layout.refresh_tag_buttons(self.label_dict)
        print(self.label_dict)

    def modify_item(self, name_old, name_new, url_new):
        if name_new not in self.label_dict:
            self.delete_item(name_old)
            self.label_dict[name_new] = url_new

            for item_row in range(0, self.listwidget.count()):
                if self.listwidget.item(item_row).text() == name_old:
                    self.listwidget.item(item_row).setText(name_new)
                    break
            self.parent().label_list_layout.refresh_tag_buttons(self.label_dict)
        else:
            self.label_dict[name_new] = url_new
        print(self.label_dict)
