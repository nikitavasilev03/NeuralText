# -*- coding: utf-8 -*-
#pylint: disable=no-name-in-module

import sys
from PyQt5.QtWidgets import QApplication
from include.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
    pass