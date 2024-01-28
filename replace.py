from PyQt6 import QtWidgets, QtCore
class Replace(QtWidgets.QDialog):
    def __init__(self):
        super().__init__() 
        self.setWindowFlags(QtCore.Qt.WindowType.Window | 
        QtCore.Qt.WindowType.CustomizeWindowHint | 
        QtCore.Qt.WindowType.WindowStaysOnTopHint |
        QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.setWindowTitle('Replace')
        self.setFixedSize(400,200)
        self.horizontal_layout = QtWidgets.QHBoxLayout(self)
        self.frame = QtWidgets.QFrame(self)
        self.vertical_layout = QtWidgets.QVBoxLayout(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.label = QtWidgets.QLabel("Find what", self.frame_3)
        self.line_edit = QtWidgets.QLineEdit("", self.frame_3)
        self.horizontal_layout_2.addWidget(self.label)
        self.horizontal_layout_2.addWidget(self.line_edit) 
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.label_2 = QtWidgets.QLabel("Replace with", self.frame_6)
        self.line_edit_2 = QtWidgets.QLineEdit("", self.frame_6)
        self.horizontal_layout_3.addWidget(self.label_2)
        self.horizontal_layout_3.addWidget(self.line_edit_2) 
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.horizontal_layout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setStyleSheet("padding: 0px")
        self.vertical_layout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.check_box = QtWidgets.QCheckBox("Match case", self.frame_5)
        self.check_box_2 = QtWidgets.QCheckBox("Wrap around", self.frame_5)
        self.vertical_layout_3.addWidget(self.check_box, alignment= QtCore.Qt.AlignmentFlag.AlignBottom)
        self.vertical_layout_3.addWidget(self.check_box_2, alignment= QtCore.Qt.AlignmentFlag.AlignBottom)
        self.horizontal_layout_4.addWidget(self.frame_5, alignment= QtCore.Qt.AlignmentFlag.AlignBottom)
        self.vertical_layout.addWidget(self.frame_3)       
        self.vertical_layout.addWidget(self.frame_6)    
        self.vertical_layout.addWidget(self.frame_4)    
        self.frame_2 = QtWidgets.QFrame(self)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.push_button = QtWidgets.QPushButton("Find Next", self.frame_2)
        self.push_button_2 = QtWidgets.QPushButton("Replace", self.frame_2)
        self.push_button_3 = QtWidgets.QPushButton("Replace All", self.frame_2)
        self.push_button_4 = QtWidgets.QPushButton("Cancel", self.frame_2)
        self.vertical_layout_2.addWidget(self.push_button)
        self.vertical_layout_2.addWidget(self.push_button_2)
        self.vertical_layout_2.addWidget(self.push_button_3)
        self.vertical_layout_2.addWidget(self.push_button_4)
        self.horizontal_layout.addWidget(self.frame)
        self.horizontal_layout.addWidget(self.frame_2, alignment= QtCore.Qt.AlignmentFlag.AlignTop)
        if not self.line_edit.text():
            self.push_button.setEnabled(False)
            self.push_button_2.setEnabled(False)
            self.push_button_3.setEnabled(False)
        if self.line_edit.text():
            self.push_button.setEnabled(True)
            self.push_button_2.setEnabled(True)
            self.push_button_3.setEnabled(True)  