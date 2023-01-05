import sys
from PyQt5 import QtWidgets


class Windows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To Do List")

        self.text_label = QtWidgets.QTextEdit()
        self.text_label.setReadOnly(True)

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setPlaceholderText("Tache a ajouter")

        button1 = QtWidgets.QPushButton("Ajouter")
        button2 = QtWidgets.QPushButton("Tout supprimer")

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(self.text_label)
        vlayout.addWidget(self.line_edit)

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(button1)
        hlayout.addWidget(button2)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(vlayout)
        main_layout.addLayout(hlayout)

        button1.clicked.connect(self.add_to_do)
        button2.clicked.connect(self.clear_all)

    def add_to_do(self):
        self.text_label.append(self.line_edit.text())
        self.line_edit.clear()

    def clear_all(self):
        self.text_label.clear()
