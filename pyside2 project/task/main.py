import os
import sys
import traceback
import numpy as np
import Uic_2
from style_Sheet import Sty_Sheet

from PySide2.QtCore import QSortFilterProxyModel
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QMainWindow, QApplication, QTableView, QShortcut, QAbstractItemView
from Add_Data import Window2
from model import ModelPosition
import sqlite3



class main(QMainWindow):

    def __init__(self):
        try:
            super(main, self).__init__()
            path = os.getcwd()
            Ui_Path = os.path.join("Resource", "Ui", "Task_1.ui")
            # self.loadUi(Ui_Path)
            Uic_2.loadUi(Ui_Path,self)

            print("askjdha")
            ss = Sty_Sheet.load_stylesheet_pyside2()

            self.DB_path = os.path.join("DB", "mainDB.db")
            self.con = sqlite3.connect(self.DB_path)

            self.Disp_Data()
            self.create_Shortcut()

            self.createObject()
            self.connectSlots()

            self.getData()
        except:
            print(traceback.print_exc())

    def createObject(self):
        try:
            self.AddData = Window2()
            # self.DelData = Window3()
        except:
            print(traceback.print_exc())

    def connectSlots(self):
        try:
            self.btn_Add.clicked.connect(self.AddData.show)
            self.AddData.Add_btn.clicked.connect(self.addDataInTable)
            # self.model.sgcalciv.connect(self.editTable)
            # self.btn_Del.clicked.connect(self.DelData.show)
            # self.DelData.Btn_Del_Row.clicked.connect(self.delDatafromTable)
        except:
            print(traceback.print_exc())


    # def editTable(self, Sno, name, age, add, mobilenumber):
    #     try:
    #         editlist = [0, 1, 2, 3]
    #
    #         self.data[Sno, editlist] = [name, age, add, mobilenumber]
    #
    #         for j in editlist:
    #             ind = self.model.index(Sno, j)
    #             self.model.dataChanged.emit(ind, ind)
    #
    #         cur = self.con.cursor()
    #         cur.execute(
    #             "UPDATE emp SET name = ?, age = ?, \"add\" = ?, mobile_no = ? WHERE name = ? OR mobile_no = ?",
    #             (name, age, add, mobilenumber, name, mobilenumber)
    #         )
    #         self.con.commit()
    #     except:
    #         print(traceback.print_exc())


    def addDataInTable(self):
        try:
            post = self.AddData.lePost.text()
            name = self.AddData.leName.text()
            mobilenumber = self.AddData.leMobileNo.text()
            age = self.AddData.leAge.text()
            add = self.AddData.leAdd.text()

            fltr = self.data[(np.where(self.data[:, 0] == name))]


            if fltr.size != 0:
                srno = fltr[0][4]
                self.tableView.selectRow(srno)
                self.AddData.close()
            else:
                self.data[self.lastSerialNo, :] = [name, age, add, mobilenumber, self.lastSerialNo]
                self.lastSerialNo += 1
                self.model.lastSerialNo += 1
                self.model.insertRows()
                self.model.rowCount()
                ind = self.model.index(0, 0)
                ind1 = self.model.index(0, 1)
                self.model.dataChanged.emit(ind, ind1)
                self.AddData.close()
                self.setData(name, age, add, mobilenumber)
        except:
            print(traceback.print_exc())


    def Ref(self, name):
        try:
            fltr = self.data[(np.where(self.data[:, 0] == name))]

            if fltr.size != 0:
                srno = fltr[0][4]

                self.data[srno:self.lastSerialNo] = self.data[srno + 1:self.lastSerialNo + 1]

                self.model.DelRows()
                self.lastSerialNo -= 1
                self.model.lastSerialNo -= 1
                self.model.rowCount()
                ind = self.model.index(0, 0)
                ind1 = self.model.index(0, 1)
                self.model.dataChanged.emit(ind, ind1)
                self.lastSerialNo
                for i, j in enumerate(self.data[:self.lastSerialNo]):
                    j[4] = i
            else:
                pass
        except:
            print(traceback.print_exc())


    # def delDatafromTable(self):
    #     try:
    #         name = self.DelData.row_Name.text()
    #         self.Ref(name)
    #     except:
    #         print(traceback.print_exc())

    def getData(self):
        try:
            cur = self.con.cursor()
            cur.execute("select * from emp")
            result = cur.fetchall()

            for i in result:
                empdata = list(i)
                self.data[self.lastSerialNo, :] = [empdata[0], empdata[1], empdata[2], empdata[3], self.lastSerialNo]
                self.lastSerialNo += 1
                self.model.lastSerialNo += 1
                self.model.insertRows()
                self.model.rowCount()
                ind = self.model.index(0, 0)
                ind1 = self.model.index(0, 1)
                self.model.dataChanged.emit(ind, ind1)
        except:
            print(traceback.print_exc())

    def setData(self, name, age, add, mobileno):
        try:
            cur = self.con.cursor()
            cur.execute("INSERT INTO emp VALUES(?,?,?,?)", (name, age, add, mobileno))
            self.con.commit()
        except:
            print(traceback.print_exc())

    def Disp_Data(self):
        try:
            self.head = ["name", "age", "add", "mobile_no", "srno"]
            self.data = np.zeros((1000, len(self.head)), dtype=object)
            self.lastSerialNo = 0

            self.model = ModelPosition(self.data, self.head)

            self.smodel = QSortFilterProxyModel()
            # print(self.smodel)
            self.smodel.setSourceModel(self.model)
            self.smodel.setDynamicSortFilter(False)
            self.smodel.setFilterKeyColumn(3)
            # self.smodel.setFilterCaseSensitivity(False)

            self.tableView.setModel(self.smodel)
            self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

            self.tableView.setStyleSheet('color: rgb(255, 255, 255);\nbackground-color:#242424;')
        except:
            print(traceback.print_exc())

    def create_Shortcut(self):
        self.Esc = QShortcut(QKeySequence('Esc'), self)
        self.Esc.activated.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())

