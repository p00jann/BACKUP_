from PySide2.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QComboBox
from PySide2.QtCore import Qt, QSortFilterProxyModel, QRegExp

class MyFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super(MyFilterProxyModel, self).__init__(parent)
        self.filterPattern = QRegExp()

    def setFilterPattern(self, pattern):
        self.filterPattern.setPattern(pattern)
        self.invalidateFilter()

    def filterAcceptsRow(self, sourceRow, sourceParent):
        if not self.filterPattern.isEmpty():
            index = self.sourceModel().index(sourceRow, 0, sourceParent)
            data = self.sourceModel().data(index, Qt.DisplayRole)
            return self.filterPattern.indexIn(data) != -1
        return True

class MyTableModel:
    # Replace this class with your actual table model class
    pass

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        self.setupUi()

    def setupUi(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.filter_layout = QVBoxLayout(self.central_widget)

        self.name_combobox = QComboBox(self)
        self.name_combobox.addItems(["All", "Name1", "Name2", "Name3"])  # Add your names
        self.name_combobox.currentIndexChanged.connect(self.filterByName)

        self.table_view = QTableView(self)
        self.table_model = MyTableModel()  # Replace with your actual table model
        self.proxy_model = MyFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.table_model)
        self.table_view.setModel(self.proxy_model)
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.setSortingEnabled(True)

        self.filter_layout.addWidget(self.name_combobox)
        self.filter_layout.addWidget(self.table_view)

        self.setGeometry(100, 100, 800, 600)

    def filterByName(self, index):
        if index == 0:
            self.proxy_model.setFilterPattern("")  # Show all data
        else:
            name = self.name_combobox.currentText()
            self.proxy_model.setFilterPattern(name)

if __name__ == "__main__":
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec_()