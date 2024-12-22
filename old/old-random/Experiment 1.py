from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(110,40,300,300)
    win.setWindowTitle("yo")

    label = QtWidgets.QLabel(win)
    label.setText(("yo yo"))
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())
window()