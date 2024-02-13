
import sys
import traceback

import numpy as np
from PySide2 import QtCore
from PySide2.QtCore import *
import numbers
#logging
#pyqtSignal




class ModelPosition(QAbstractTableModel):

    # sgcalciv = pyqtSignal(int,str,str,str,str)

    def __init__(self, data,heads):
        super(ModelPosition, self).__init__()
        self._data = data
        self.dta1 = []
        self.updatedrow={}
        self.color = []
        self.heads=heads
        self.iop = 0
        self.lastSerialNo =0

    def data(self, index, role):
        try:
            if role == Qt.DisplayRole:

                value = self._data[index.row(), index.column()]

                if(index.column()<9):
                    return value

                # elif(isinstance(value, numbers.Number)):
                #     return '%.2f'%value
                else:
                    return value

            # if role == Qt.TextAlignmentRole:
            #
            #     if (index.column()>0):
            #         return Qt.AlignVCenter + Qt.AlignRight

            if role == Qt.EditRole:
                value = self._data[index.row(),index.column()]
                if (isinstance(value, numbers.Number)):
                    return '%.2f' % value



            # if role == Qt.BackgroundColorRole:
            #     # print(role)
            #     value = self._data[index.row(), index.column()]
            #     if(index.column() in [7,8,9]):
            #         if(len(self.dta1) != 0):
            #             # print(value,type(value), self.dta1[index.row()], type(self.dta1[index.row()]))
            #
            #
            #             if(value > self.dta1[index.row()][index.column()-7]):
            #                 self.color[index.row()][index.column()-7] = '#4FB7E0'
            #                 return QtGui.QColor('#4FB7E0')
            #
            #             elif (value < self.dta1[index.row()][index.column()-7]):
            #                 self.color[index.row()][index.column()-7] = '#c2364b'
            #
            #                 return QtGui.QColor('#c2364b')
            #             else:
            #                 return QtGui.QColor(self.color[index.row()][index.column()-7])

                # if(index.column() in [13,15]):
                #     return QtGui.QColor(48, 57, 63)

            # if role == Qt.TextColorRole:
            #     value = self._data[index.row(), 8]
            #     if (index.column() == 8):
            #         if value <= 0:
            #             return QBrush(QtGui.QColor('#ff1b1b'))
            #         elif value >= 0:
            #             return QBrush(QtGui.QColor('#1ed953'))


        except:
            print(traceback.print_exc())


    def rowCount(self, index=''):
        try:
            return self.lastSerialNo
        except:
            print(traceback.print_exc())


    def columnCount(self, index=''):
        try:
            return len(self.heads)
        except:
            pass


    def setData(self, index, value, role=None):
        try:
            if  role == Qt.EditRole:
                if value == self._data[index.row()][index.column()]:
                    return False
                else:

                    if(value == ''):
                        return False
                    else:
                        try:

                            if index.column() == 0:
                                fltr = self._data[(np.where(self._data[:, 0] == value))]
                                if fltr.size != 0:
                                    return False
                                else:
                                    self._data[index.row()][index.column()] = str(value)
                                    name = self._data[index.row()][0]
                                    Sno = self._data[index.row()][4]
                                    age = self._data[index.row()][1]
                                    add = self._data[index.row()][2]
                                    mobilenumber = self._data[index.row()][3]
                                    self.sgcalciv.emit(Sno, name, age, add, mobilenumber)
                                    return True
                            else:

                                self._data[index.row()][index.column()] = str(value)
                                name = self._data[index.row()][0]
                                Sno = self._data[index.row()][4]
                                age = self._data[index.row()][1]
                                add = self._data[index.row()][2]
                                mobilenumber = self._data[index.row()][3]
                                self.sgcalciv.emit(Sno,name,age,add,mobilenumber)
                                return True
                        except:
                            return False
        except:
            print(traceback.print_exc())


    def flags(self, index):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable


    def headerData(self, section, orientation, role):
        try:
            if role == Qt.DisplayRole:
                if orientation == Qt.Horizontal:
                    return str(self.heads[section])
        except:
            print(traceback.print_exc())


    def insertRows(self, position=0, rows=1, index=QModelIndex()):
        try:
            self.beginInsertRows(QModelIndex(), position, position + rows - 1)
            self.endInsertRows()
            return True
        except:
            print(traceback.print_exc())

    def setDta1(self):
        try:
            self.dta1 = self._data[:,7].tolist()

        except:
            print(traceback.print_exc())


    def setDta(self,a):
        try:
            self._data = a
        except:
            print(traceback.print_exc())

    # def DelRows(self, position=0, rows=1, index=QModelIndex()):
    #     try:
    #         self.beginRemoveRows(QModelIndex(), 0, 0)
    #         self.endRemoveRows()
    #         return  True
    #     except:
    #         print(traceback.print_exc())

    def DelRows(self, position=0, rows=0, index=QModelIndex()):

        self.beginRemoveRows(QModelIndex(), position, position - rows)
        del self._data[position:position + rows]
        self.endRemoveRows()
        return True

        return True