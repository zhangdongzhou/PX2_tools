# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:12:57 2020

@author: -
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from GridScan_main_logic import Logic_MainWindow as mainL
import sys

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainL(MainWindow)
#    ui.setupUi()
    ui.__init__()
#    MainWindow.show()
    ui.show()
    sys.exit(app.exec_())