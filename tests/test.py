#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
Description :

Author      : Cirun Zhang
Contact     : cirun.zhang@envision-digital.com
Time        : 2020/7/8 
Software    : PyCharm
"""
from PyQt5.QtWidgets import *
from src.item_window import ItemWindow


class Window(QMainWindow):
    item_list = []

    def __init__(self):
        super().__init__()

        self.buttonsWidget = QWidget()
        self.buttonsWidgetLayout = QHBoxLayout(self.buttonsWidget)
        self.button_new = QPushButton("NEW")
        self.button_new.clicked.connect(self.action_new)

        self.button_modify = QPushButton("MODIFY")

        self.button_delete = QPushButton("DELETE")
        self.button_delete.clicked.connect(self.delete_item)

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

    def new_item(self, name):
        item_new = QListWidgetItem(name)
        self.item_list.append({'name': name, 'item': item_new})
        self.listwidget.addItem(item_new)

    def delete_item(self):
        items = self.listwidget.selectedItems()
        if len(items) > 0:
            row = self.listwidget.row(items[0])
            self.listwidget.takeItem(row)


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())