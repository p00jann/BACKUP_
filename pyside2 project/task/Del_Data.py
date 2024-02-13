import os
import sys
import traceback
import platform


import numpy as np
# from PyQt5 import uic
# from PyQt5.QtGui import QKeySequence
# from PyQt5.QtSql import QSqlDatabase
# from PyQt5.QtCore import QSortFilterProxyModel,Qt
# from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView, QShortcut

import Uic_2
from PySide2.QtGui import QKeySequence
from PySide2.QtSql import QSqlDatabase
from PySide2.QtCore import QSortFilterProxyModel,Qt
from PySide2.QtWidgets import QMainWindow, QApplication, QTableView, QShortcut



import sqlite3


class Window3(QMainWindow):
    def __init__(self):
        try:
            super(Window3, self).__init__()
            path = os.getcwd()
            Ui_Path_2 = os.path.join("Resource", "Ui", "Del_Data.ui")
            Uic_2.loadUi(Ui_Path_2, self)

            osType = platform.system()


            if (osType == 'Windows'):
                flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            else:
                flags = Qt.WindowFlags(Qt.SubWindow | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)

            # self.cancel.clicked.connect(self.hide)
            self.createShortcuts()


        except:
            print(traceback.print_exc())

    def createShortcuts(self):
        self.quitSc = QShortcut(QKeySequence('Esc'), self)
        self.quitSc.activated.connect(self.close)

    # def Add_Data(self):
    #     try:
    #         self.Win2 = QMainWindow()
    #         self.Ui = Window2()
    #         self.Ui.Add_Data(self.Win2)
    #         # self.btn_Add.clicked.connect(self.Add_Data)
    #
    #     except:
    #         print(traceback.print_exc())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win2 = Window3()
    win2.show()
    sys.exit(app.exec_())
    #
