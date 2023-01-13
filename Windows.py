import sys
from PyQt5 import QtWidgets


class Windows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To Do List")

        self.list_view = QtWidgets.QListWidget()

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setPlaceholderText("Tache a ajouter")

        button1 = QtWidgets.QPushButton("Ajouter")
        button2 = QtWidgets.QPushButton("Supprimer")
        button3 = QtWidgets.QPushButton("Tout supprimer")

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(self.list_view)
        vlayout.addWidget(self.line_edit)

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(button1)
        hlayout.addWidget(button2)
        hlayout.addWidget(button3)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(vlayout)
        main_layout.addLayout(hlayout)

        button1.clicked.connect(self.add_to_do)
        button2.clicked.connect(self.delete_view)
        button3.clicked.connect(self.clear_all)
        self.line_edit.returnPressed.connect(self.add_to_do)

    def add_to_do(self):
        text = self.line_edit.text()
        if text:
            self.list_view.addItem(text)
            self.line_edit.clear()

    def delete_view(self):
        items_selected = self.list_view.selectedItems()
        if items_selected:
            for item in items_selected:
                self.list_view.takeItem(self.list_view.row(item))

    def clear_all(self):
        self.list_view.clear()
