import sys
import json
import time
import webbrowser
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QApplication, QMainWindow, QGraphicsBlurEffect, QFrame
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import Qt, QPoint
from Resources import test_rc
from make_search_thread import make_search_thread, SearchWorker, make_search_thread_s


class MainApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Load the .ui file from the root directory
        uic.loadUi("responsive1.ui", self)
        self.oldPos = self.pos()

        # title bar removal
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Define our widgets
        self.items = [self.findChild(QLineEdit, f"item_{i}") for i in range(1, 13)]  # User Inputs
        self.search_buttons = [self.findChild(QPushButton, f"search_{i}_btn") for i in range(1, 13)]  # Search Buttons
        self.names = [self.findChild(QLabel, f"name_{i}") for i in range(1, 70)]  # Item names
        self.prices = [self.findChild(QLabel, f"price_{i}") for i in range(1, 70)]  # Item Prices
        self.gotolinks = [self.findChild(QPushButton, f"gotolink_{i}_btn") for i in range(1, 13)] # go to link buttons
        self.backs = [self.findChild(QFrame, f"back_{i}") for i in range(1, 13)] # large transparent box behind names and prices
        self.close_btn = self.findChild(QPushButton, "close_btn") # close button
        self.minimize_btn = self.findChild(QPushButton, "minimize_btn") # minimize button
        self.refresh_btn = self.findChild(QPushButton, "refresh_btn") # refresh button
        self.main_background = self.findChild(QLabel, "main_background") # background photo
        self.order_buttons = [self.findChild(QPushButton, f"order_{i}_btn") for i in range(1, 13)] # order buttons


        # Connect signals
        self.close_btn.clicked.connect(self.close) # close button
        self.minimize_btn.clicked.connect(self.showMinimized) # minimize button
        self.refresh_btn.clicked.connect(self.refresh) # refresh button
        for i in range(1, 13):
            self.search_buttons[i - 1].clicked.connect(getattr(self, f"start_search_thread_{i}")) # search button connected to result gatherer
            self.search_buttons[i - 1].clicked.connect(lambda _, x=i: getattr(self, f"save_item_{x}")()) # search button connected to item memory
            self.search_buttons[i - 1].clicked.connect(
                lambda state, x=i, btn=self.search_buttons[i - 1]: self.disabler(x, btn)) # search button connected to button disabler

            self.gotolinks[i - 1].clicked.connect(getattr(self, f"gotolink{i}")) # go to link button connected to browser
            with open(f'Items.json') as file:
                content = json.load(file)
                getattr(self, f"item_{i}").setText(self._translate("MainWindow", content[f"item{i}"]))
                getattr(self, f"search_{i}_btn").click()


    _translate = QtCore.QCoreApplication.translate # idk
    # Functions
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    # disables the button that was pressed
    def disabler(self, i, btn):
        btn.setEnabled(False)

    # refresh button
    def refresh(self):
        print("yo")
        self.refresh_btn.setEnabled(False)
        for i in range(1, 13):
            getattr(self, f"search_{i}_btn").click()

    # Function for saving last entered item name
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

    #search thread stuff
    for i in range(1, 13):
        if i <= 9:
            # Making a search thread for the emitted signal
            exec(
                f"def start_search_thread_{i}(self): self.worker_{i}, self.thread_{i} = make_search_thread(self, self.item_{i}, 'item_{i}', {(i - 1) * 6})")
            exec(f"def search_{i}(self, result): self.search(result, {(i - 1) * 6}, 'item_{i}')")
        else:
            # Making a search thread for the emitted signal
            exec(
                f"def start_search_thread_{i}(self): self.worker_{i}, self.thread_{i} = make_search_thread_s(self, self.item_{i}, 'item_{i}', {54 + (i - 10) * 5})")
            exec(f"def search_{i}(self, result): self.search(result, {(i - 1) * 5}, 'item_{i}')")

        content = get_content(None) # creating and opening the link to the item
        exec(f"def gotolink{i}(self):"
             f"webbrowser.open_new(f'https://warframe.market/items/{content[f'item{i}']}')")

        exec(f"def save_item_{i}(self): self.save_item(self.item_{i}, {i}, {Items_dict})")



    # Sets the names and prices in the gui and enables the buttons when the names and prices are set
    def search(self, result, start_index, item):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            if start_index <= 48:
                starto = int((start_index) / 6)
                self.search_buttons[starto].setEnabled(True) # enables the button
                for i in range(start_index, start_index + 6):
                    getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                    getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                    c += 1
            else:
                starto = int((start_index + 3) / 6)
                self.search_buttons[starto].setEnabled(True) # enables the button
                self.refresh_btn.setEnabled(True)
                for i in range(start_index, start_index + 5):
                    getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                    getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                    c += 1
        except Exception:
            if start_index <= 48:
                for i in range(start_index, start_index + 6):
                    getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", "Item does not exist"))
                    getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", "Price"))
                    backo = (start_index / 6) + 1;
                    backo = int(backo)
                    # getattr(self, f"back_{backo}").setGraphicsEffect(QGraphicsBlurEffect()) # for failed searches
                    # self.order_buttons[backo - 1].setGraphicsEffect(QGraphicsBlurEffect())
                    # self.gotolinks[backo - 1].setGraphicsEffect(QGraphicsBlurEffect())

                    c += 1
            else:
                for i in range(start_index, start_index + 5):
                    backo = (start_index / 6) + 1
                    backo = int(backo)
                    getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", "Item does not exist"))
                    getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", "Price"))
                    # getattr(self, f"back_{backo + 1}").setGraphicsEffect(QGraphicsBlurEffect()) # for failed searches
                    # self.order_buttons[backo].setGraphicsEffect(QGraphicsBlurEffect())
                    # self.gotolinks[backo].setGraphicsEffect(QGraphicsBlurEffect())
                    c += 1

    def mousePressEvent(self, event):
        self.oldPosition = event.globalpos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        print(delta)



def mainn():  # sets up the PyQt5 application
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":  # start the PyQt5 application
    mainn()