
#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
Description :

Author      : Cirun Zhang
Contact     : cirun.zhang@envision-digital.com
Time        : 2020/7/10 
Software    : PyCharm
"""

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button = QPushButton('', self)
        self.button.clicked.connect(self.handleButton)
        self.button.setIcon(QIcon('../img/labelbutton.png'))
        self.button.setIconSize(QSize(24,24))
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        pass


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())