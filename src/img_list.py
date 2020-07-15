#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
Description :

Author      : Cirun Zhang
Contact     : cirun.zhang@envision-digital.com
Time        : 2020/7/13 
Software    : PyCharm
"""
import os

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.Qt import *


class TodoListLayout(QVBoxLayout):
    working_directory = ''
    index = 0

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.todo_list_widget = ListWidget(parent=self)
        text = QLabel('Todo')
        text.setAlignment(Qt.AlignCenter)
        text.setFont(QtGui.QFont("Helvetica", 15, QtGui.QFont.Bold))
        self.addWidget(text)
        self.addWidget(self.todo_list_widget)

    def load(self, item: QListWidgetItem):
        self.parent.img_framework_layout.load_from_todo(item)

    def unload(self, item: QListWidgetItem):
        self.parent.img_framework_layout.unload_from_todo(item)

    def delete(self, item: QListWidgetItem):
        self.todo_list_widget.takeItem(self.todo_list_widget.row(item))

    def update_working_dir(self, working_directory):
        self.working_directory = working_directory
        self.iterate_files()

    def iterate_files(self):
        if os.path.exists(self.working_directory) and os.path.isdir(self.working_directory):
            tmp = os.listdir(self.working_directory)

            self.todo_list_widget.clear()

            for file_name in tmp:
                if file_name.endswith('.jpg') or file_name.endswith('.png'):
                    img_path = self.working_directory + file_name
                    self.todo_list_widget.new_item_shallow(img_path=img_path, img_name=file_name, label='None')

            self.todo_list_widget.update()


class DoneListLayout(QVBoxLayout):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.done_list_widget = ListWidget(parent=self)
        text = QLabel('Done')
        text.setAlignment(Qt.AlignCenter)
        text.setFont(QtGui.QFont("Helvetica", 15, QtGui.QFont.Bold))
        self.addWidget(text)
        self.addWidget(self.done_list_widget)

    def add_item(self, item):
        self.done_list_widget.new_item_deep(item)
        item.setText('[' + item.label + '] ' + item.img_name)
        self.sort()
        self.done_list_widget.update()

    def load(self, item: QListWidgetItem):
        self.parent.img_framework_layout.load_from_done(item)

    def unload(self, item: QListWidgetItem):
        self.parent.img_framework_layout.unload_from_done(item)

    def sort(self):
        self.done_list_widget.sortItems()


class ListWidget(QListWidget):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setStyleSheet("QListWidget:item:selected:!active {background: rgb(3, 73, 252);}"
                           "QListWidget:item:selected:!active {color: white;}")
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.MultiSelection)
       # self.itemPressed.connect(self.item_clicked)

    def new_item_shallow(self, img_path, img_name, label):
        self.addItem(ListItem(self.parent, img_path, img_name, label))

    def new_item_deep(self, item: QListWidgetItem):
        self.addItem(item)

    # def item_clicked(self, item: QListWidgetItem) -> None:
    #     item.setSelected(not item.isSelected())
    #     if len(self.selectedItems()) >= 4:
    #         if item.isSelected():
    #             self.unload(item)
    #     else:
    #         if item.isSelected():
    #             self.unload(item)
    #         else:
    #             self.load(item)

    def selectionCommand(self, index, event):
        if len(self.selectedItems()) >= 4:
            self.unload(self.item(index.row()))
            return QItemSelectionModel.Deselect
        else:
            self.load(self.item(index.row()))
            return super().selectionCommand(index, event)

    def load(self, item: QListWidgetItem):
        #item.setSelected(True)
        self.parent.load(item)

    def unload(self, item: QListWidgetItem):
        #item.setSelected(False)
        if item.isSelected():
            self.parent.unload(item)


class ListItem(QListWidgetItem):

    def __init__(self, parent, img_path, img_name, label):
        super().__init__()
        self.parent = parent
        self.setText(img_name)
        self.img_path = img_path
        self.img_name = img_name
        self.label = label

    def set_label(self, label):
        self.label = label

    # def setSelected(self, aselect: bool) -> None:
    #     super().setSelected(aselect)
    #     print(aselect)