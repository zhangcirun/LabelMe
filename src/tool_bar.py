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


class ToolBar(QToolBar):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        bar_open = QAction(QIcon("../img/folder.png"), "select", self)
        self.addAction(bar_open)

        bar_dir = QAction(QIcon("../img/db.png"), "output setting", self)
        self.addAction(bar_dir)

        bar_save = QAction(QIcon("../img/save_hover.png"), "save", self)
        self.addAction(bar_save)

        bar_exit = QAction(QIcon("../img/exit.png"), "exit", self)
        self.addAction(bar_exit)
        self.actionTriggered[QAction].connect(self.action_toolbar)

    def action_toolbar(self, a):
        text = a.text()
        if text == 'exit':
            qApp.exit()
        elif text == 'select':
            self.action_browse()
        elif text == 'output setting':
            self.parent.action_new_setting_window()
        elif text == 'save':
            self.action_save()

    def action_browse(self):
        url = QFileDialog.getExistingDirectory(self, "select")
        if url == "":
            print("\n取消选择")
            return

        if not url.endswith('/'):
            url += '/'

        self.parent.img_framework_layout.delete_all()
        self.parent.list_layout.clear_all()
        self.parent.list_layout.todo_list_layout.update_working_dir(url)
        self.parent.img_framework_layout.load_next_four()

    def action_save(self):
        self.parent.list_layout.save_all()
        print('save')