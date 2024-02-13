import sys
import traceback
from PySide2 import QtCore
from PySide2.QtCore import Qt, QModelIndex

class Add_data_model(QtCore.QAbstractTableModel):
    def __init__(self, data, heads, isReset=False):
        super(Add_data_model, self).__init__()
        self._data = data
        # self._data1 = data
        self.heads = heads
        if (isReset):
            self.lastSerialNo = data.shape[0]
        else:
            self.lastSerialNo = 0