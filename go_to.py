from PyQt6 import QtWidgets, QtCore
class GoTo(QtWidgets.QDialog):
    def __init__(self):
        super().__init__() 
        self.setWindowFlags(QtCore.Qt.WindowType.Window | 
        QtCore.Qt.WindowType.CustomizeWindowHint | 
        QtCore.Qt.WindowType.WindowStaysOnTopHint |
        QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.setWindowTitle('Find')
        self.setFixedSize(300,180)
        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel("Line number", self)
        self.line_edit = QtWidgets.QLineEdit(self)
        self.frame_2 = QtWidgets.QFrame(self)
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.frame_2)
        self.push_button = QtWidgets.QPushButton("Go to", self)
        self.push_button_2 = QtWidgets.QPushButton("Cancel", self)
        self.horizontal_layout.addWidget(self.push_button)
        self.horizontal_layout.addWidget(self.push_button_2)
        self.vertical_layout.addWidget(self.label)
        self.vertical_layout.addWidget(self.line_edit)
        self.vertical_layout.addWidget(self.frame_2, alignment= QtCore.Qt.AlignmentFlag.AlignRight)