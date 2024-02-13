from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PySide2.QtGui import QDoubleValidator
import sys

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QLineEdit
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter a float value")

        # Set a double validator to allow only float values
        float_validator = QDoubleValidator(self)
        self.line_edit.setValidator(float_validator)

        # Set up the main layout
        central_widget = QWidget(self)
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(self.line_edit)

        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
