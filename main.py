import Windows
from PyQt5 import QtWidgets


app = QtWidgets.QApplication([])

win = Windows.Windows()
win.show()

app.exec()
