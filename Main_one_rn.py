import sys
import json
import webbrowser
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from Resources import test_rc
from make_search_thread import make_search_thread, SearchWorker, make_search_thread_s

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the .ui file from the root directory
        uic.loadUi("uitest.ui", self)

        #title bar removal
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Define our widgets
        self.items = [self.findChild(QLineEdit, f"item_{i}") for i in range(1, 13)]  # User Inputs
        self.search_buttons = [self.findChild(QPushButton, f"search_{i}_btn") for i in range(1, 13)]  # Search Buttons
        self.names = [self.findChild(QLabel, f"name_{i}") for i in range(1, 70)]  # Item names
        self.prices = [self.findChild(QLabel, f"price_{i}") for i in range(1, 70)]  # Item Prices
        self.gotolinks = [self.findChild(QPushButton, f"gotolink_{i}_btn") for i in range(1, 13)]
        self.close_btn = self.findChild(QPushButton, "close_btn")
        self.minimize_btn = self.findChild(QPushButton, "minimize_btn")

        self.old_pos = self.pos()
        self.mouse_pressed = False



        # Connect signals
        self.close_btn.clicked.connect(self.close)
        self.minimize_btn.clicked.connect(self.showMinimized)
        for i in range(1, 13):
            self.search_buttons[i - 1].clicked.connect(getattr(self, f"start_search_thread_{i}"))
            self.search_buttons[i - 1].clicked.connect(lambda _, x=i: getattr(self, f"save_item_{x}")())
            self.gotolinks[i - 1].clicked.connect(getattr(self, f"gotolink{i}"))
            with open(f'Items.json')as file:
                content = json.load(file)
                getattr(self, f"item_{i}").setText(self._translate("MainWindow", content[f"item{i}"]))
                getattr(self, f"search_{i}_btn").click()


    _translate = QtCore.QCoreApplication.translate
    #Function for saving last entered item name
    with open('Items.json') as yoo:
        Items_dict = json.load(yoo)
    def save_item(self, item_index, i, test):
        Items_dict = test
        Items_dict.update({f"item{i}": f"{item_index.text()}"})
        with open("Items.json", "w") as f:
            json.dump(Items_dict, f)

    def get_content(self):
        with open('Items.json') as file:
             content = json.load(file)
        return content

    for i in range(1, 13):
        if i <= 9:
            #Making a search thread for the emitted signal
            exec(f"def start_search_thread_{i}(self): self.worker_{i}, self.thread_{i} = make_search_thread(self, self.item_{i}, 'item_{i}', {(i - 1) * 6})")
            exec(f"def search_{i}(self, result): self.search(result, {(i - 1) * 6}, 'item_{i}')")
        else:
            #Making a search thread for the emitted signal
            exec(f"def start_search_thread_{i}(self): self.worker_{i}, self.thread_{i} = make_search_thread_s(self, self.item_{i}, 'item_{i}', {54 + (i - 10) * 5})")
            exec(f"def search_{i}(self, result): self.search(result, {(i - 1) * 5}, 'item_{i}')")

        content = get_content(None)
        exec(f"def gotolink{i}(self):"
             f"webbrowser.open_new(f'https://warframe.market/items/{content[f'item{i}']}')")

        exec(f"def save_item_{i}(self): self.save_item(self.item_{i}, {i}, {Items_dict})")


    #Sets the names and prices in the gui
    def search(self, result, start_index, item):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            if start_index<=48:
                for i in range(start_index, start_index + 6):
                    getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                    getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                    c += 1
            else:
                for i in range(start_index, start_index + 5):
                    getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                    getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                    c += 1
        except Exception:
            getattr(self, item).setText(_translate("MainWindow", "Item does not exist"))


def mainn():                              #sets up the PyQt5 application
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":     #start the PyQt5 application
    mainn()