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
from PyQt5.QtCore import *


class ItemWindow(QMainWindow):
    def __init__(self, parent, name_old=None, url_old=None):
        super().__init__(parent=parent)
        self.name_old = name_old
        self.url_old = url_old
        self.set_width_height()
        self.add_component()

    def set_width_height(self):
        self.setFixedWidth(550)
        self.setFixedHeight(240)

    def add_component(self):
        self.hwidget1 = QWidget()
        self.hbox1 = QHBoxLayout(self.hwidget1)
        self.text_line_edit = QLineEdit()
        self.text_line_edit.setFixedWidth(20)
        if self.name_old is not None:
            self.text_line_edit.setText(self.name_old)
        self.hbox1.addWidget(QLabel("Category Name:"))
        self.hbox1.addWidget(self.text_line_edit)

        self.hwidget2 = QWidget()
        self.hbox2 = QHBoxLayout(self.hwidget2)
        self.text_url_edit = QLineEdit()
        self.text_url_edit.setFixedWidth(300)
        if self.url_old is not None:
            self.text_url_edit.setText(self.url_old)

        self.hbox2.addWidget(QLabel("Output URL:"))

        self.browse = QPushButton("Select")
        self.browse.clicked.connect(self.action_browse)

        self.hbox2.addWidget(self.text_url_edit)
        self.hbox2.addWidget(self.browse)

        self.text_widget = QWidget()
        self.text_layout = QVBoxLayout(self.text_widget)
        self.text_layout.addWidget(self.hwidget1, alignment=Qt.AlignLeft)
        self.text_layout.addWidget(self.hwidget2, alignment=Qt.AlignLeft)

        """botton"""
        self.button_widget = QWidget()
        self.button_widget_layout = QHBoxLayout(self.button_widget)
        self.commit = QPushButton("Commit")
        self.commit.clicked.connect(self.action_commit)

        self.cancel = QPushButton("Cancel")
        self.cancel.clicked.connect(self.action_cancel)

        self.button_widget_layout.addWidget(self.commit)
        self.button_widget_layout.addWidget(self.cancel)

        """layout"""
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.vLayout = QVBoxLayout(self.centralWidget)
        self.vLayout.addWidget(self.text_widget)
        self.vLayout.addWidget(self.button_widget)

    def action_commit(self):
        name_new = self.text_line_edit.text()
        url_new = self.text_url_edit.text()

        if name_new != "" and url_new != "":
            if self.name_old is None:
                self.parent().new_item(name_new, url_new)
                self.close()
            else:
                self.parent().modify_item(name_old=self.name_old, name_new=name_new, url_new=url_new)
                self.close()

    def action_cancel(self):
        self.close()

    def action_browse(self):
        url = QFileDialog.getExistingDirectory(self, "select")
        if url == "":
            return

        if not url.endswith('/'):
            url += '/'

        self.text_url_edit.setText(url)

