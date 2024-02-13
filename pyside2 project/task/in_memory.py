import traceback

import numpy as np

import Uic_2
from PySide2.QtCore import Qt, QSortFilterProxyModel
from PySide2.QtWidgets import QPushButton, QMainWindow, QApplication, QAbstractItemView
from PySide2 import QtCore
import sys
import os
import DB.support as supp
from model import ModelPosition



class main(QMainWindow):
    print("asjhdgajshdg")
    def __init__(self):
        super(main,self).__init__()
        path = os.getcwd()
        Ui_Path = os.path.join("Resource", "Ui", "in_memory_CT.ui")
        Uic_2.loadUi(Ui_Path, self)
        self.connect_slot()
        self.db_creat_table_view()




    def connect_slot(self):
        self.pb_check_conn.clicked.connect(self.db_check_conn)
        self.pb_create_tbl.clicked.connect(self.db_create_conn)
        self.pb_disp_data.clicked.connect(self.db_disp_data)
        self.pb_insert_data.clicked.connect(self.db_insert_data)
        self.pb_backup.clicked.connect(self.db_backup)
        self.pb_check_conn.clicked.connect(self.combobox)
        self.cb_month.currentIndexChanged.connect(lambda :self.combobox2)

    def db_backup(self):
        try:
            supp.get_backup()
        except:
            print(traceback.print_exc())

    def db_creat_table_view(self):
        self.head = ["name", "age", "add", "mobile_no"]
        self.data = np.zeros((10, len(self.head)), dtype=object)
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


    def combobox(self):
        self.month=['jan','fab','march','april','may','jun','july','aug','sept','oct','nov','dec']
        self.cb_month.addItems(self.month)


    def combobox2(self):
        self.day=0
        for i in range(32):
            self.day=i
        print(self.day)
        self.cb_month.addItems(self.i)
        print("self.day______________________",self.day)
    def db_check_conn(self):
        self.db_conn = supp.check_conn()

    def db_create_conn(self):
        self.crt_tbl = supp.create_tab()

    def db_disp_data(self):
        self.disp_data = supp.display_data()
        print(self.disp_data)

        for i in self.disp_data:
            empdata = list(i)
            self.data[self.lastSerialNo, :] = [empdata[0], empdata[1], empdata[2], empdata[3],]
            self.lastSerialNo += 1
            self.model.lastSerialNo += 1
            self.model.insertRows()
            self.model.rowCount()
            ind = self.model.index(0, 0)
            ind1 = self.model.index(0, 1)
            self.model.dataChanged.emit(ind, ind1)



    def db_insert_data(self):
        name = self.le_name.text()
        age = self.le_age.text()
        add = self.le_add.text()
        mobile = self.le_mobile.text()
        self.insert_data = supp.insert_data(name,age,add,mobile)



if __name__=="__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())

