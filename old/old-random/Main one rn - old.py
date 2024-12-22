import sys

import PyQt5
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit,QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from Resources import bigback_rc
from Resources import test_rc
from Resources import transparent_rc
from fetcher import main


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the .ui file from the root directory
        uic.loadUi("uitest.ui", self)

        # Define our widgets
        self.items = [self.findChild(QLineEdit, f"item_{i}") for i in range(1, 13)]  # User Inputs
        self.search_buttons = [self.findChild(QPushButton, f"search_{i}_btn") for i in range(1, 13)]  # Search Buttons
        self.names = [self.findChild(QLabel, f"name_{i}") for i in range(1, 70)]  # Item names
        self.prices = [self.findChild(QLabel, f"price_{i}") for i in range(1, 70)]  # Item Prices

        # Connect signals
        for i in range(1, 13):
            self.search_buttons[i - 1].clicked.connect(getattr(self, f"start_search_thread_{i}"))
            self.search_buttons[i - 1].clicked.connect(lambda _, x=i: getattr(self, f"save_item_{x}")())

        for i in range(1, 13):
            with open(f'item{i}.txt', 'r', encoding="utf-8") as file:
                content = file.read()
                getattr(self, f"item_{i}").setText(self._translate("MainWindow", content))
                getattr(self, f"search_{i}_btn").click()
        

    _translate = QtCore.QCoreApplication.translate
    def start_search_thread_1(self):                            #does the multi threading stuff(AI generated)
        self.thread_1 = QtCore.QThread()
        self.worker_1 = SearchWorker(self.item_1.text())
        
        self.worker_1.moveToThread(self.thread_1)

        self.thread_1.started.connect(self.worker_1.run)
        self.worker_1.finished.connect(self.thread_1.quit)
        self.worker_1.finished.connect(self.worker_1.deleteLater)
        self.thread_1.finished.connect(self.thread_1.deleteLater)
        self.worker_1.result.connect(self.search_1)

        self.thread_1.start()


    def start_search_thread_2(self):
        self.thread_2 = QtCore.QThread()
        self.worker_2 = SearchWorker(self.item_2.text())

        self.worker_2.moveToThread(self.thread_2)

        self.thread_2.started.connect(self.worker_2.run)
        self.worker_2.finished.connect(self.thread_2.quit)
        self.worker_2.finished.connect(self.worker_2.deleteLater)
        self.thread_2.finished.connect(self.thread_2.deleteLater)
        self.worker_2.result.connect(self.search_2)

        self.thread_2.start()

    def start_search_thread_3(self):
        self.thread_3 = QtCore.QThread()
        self.worker_3 = SearchWorker(self.item_3.text())

        self.worker_3.moveToThread(self.thread_3)

        self.thread_3.started.connect(self.worker_3.run)
        self.worker_3.finished.connect(self.thread_3.quit)
        self.worker_3.finished.connect(self.worker_3.deleteLater)
        self.thread_3.finished.connect(self.thread_3.deleteLater)
        self.worker_3.result.connect(self.search_3)

        self.thread_3.start()

    def start_search_thread_4(self):
        self.thread_4 = QtCore.QThread()
        self.worker_4 = SearchWorker(self.item_4.text())

        self.worker_4.moveToThread(self.thread_4)

        self.thread_4.started.connect(self.worker_4.run)
        self.worker_4.finished.connect(self.thread_4.quit)
        self.worker_4.finished.connect(self.worker_4.deleteLater)
        self.thread_4.finished.connect(self.thread_4.deleteLater)
        self.worker_4.result.connect(self.search_4)

        self.thread_4.start()

    def start_search_thread_5(self):
        self.thread_5 = QtCore.QThread()
        self.worker_5 = SearchWorker(self.item_5.text())

        self.worker_5.moveToThread(self.thread_5)

        self.thread_5.started.connect(self.worker_5.run)
        self.worker_5.finished.connect(self.thread_5.quit)
        self.worker_5.finished.connect(self.worker_5.deleteLater)
        self.thread_5.finished.connect(self.thread_5.deleteLater)
        self.worker_5.result.connect(self.search_5)

        self.thread_5.start()

    def start_search_thread_6(self):
        self.thread_6 = QtCore.QThread()
        self.worker_6 = SearchWorker(self.item_6.text())

        self.worker_6.moveToThread(self.thread_6)

        self.thread_6.started.connect(self.worker_6.run)
        self.worker_6.finished.connect(self.thread_6.quit)
        self.worker_6.finished.connect(self.worker_6.deleteLater)
        self.thread_6.finished.connect(self.thread_6.deleteLater)
        self.worker_6.result.connect(self.search_6)

        self.thread_6.start()

    def start_search_thread_7(self):
        self.thread_7 = QtCore.QThread()
        self.worker_7 = SearchWorker(self.item_7.text())

        self.worker_7.moveToThread(self.thread_7)

        self.thread_7.started.connect(self.worker_7.run)
        self.worker_7.finished.connect(self.thread_7.quit)
        self.worker_7.finished.connect(self.worker_7.deleteLater)
        self.thread_7.finished.connect(self.thread_7.deleteLater)
        self.worker_7.result.connect(self.search_7)

        self.thread_7.start()

    def start_search_thread_8(self):
        self.thread_8 = QtCore.QThread()
        self.worker_8 = SearchWorker(self.item_8.text())


        self.worker_8.moveToThread(self.thread_8)

        self.thread_8.started.connect(self.worker_8.run)
        self.worker_8.finished.connect(self.thread_8.quit)
        self.worker_8.finished.connect(self.worker_8.deleteLater)
        self.thread_8.finished.connect(self.thread_8.deleteLater)
        self.worker_8.result.connect(self.search_8)
        
        self.thread_8.start()


    def start_search_thread_9(self):
        self.thread_9 = QtCore.QThread()
        self.worker_9 = SearchWorker(self.item_9.text())

        self.worker_9.moveToThread(self.thread_9)

        self.thread_9.started.connect(self.worker_9.run)
        self.worker_9.finished.connect(self.thread_9.quit)
        self.worker_9.finished.connect(self.worker_9.deleteLater)
        self.thread_9.finished.connect(self.thread_9.deleteLater)
        self.worker_9.result.connect(self.search_9)

        self.thread_9.start()

    def start_search_thread_10(self):
        self.thread_10 = QtCore.QThread()
        self.worker_10 = SearchWorker(self.item_10.text())

        self.worker_10.moveToThread(self.thread_10)

        self.thread_10.started.connect(self.worker_10.run_2)
        self.worker_10.finished.connect(self.thread_10.quit)
        self.worker_10.finished.connect(self.worker_10.deleteLater)
        self.thread_10.finished.connect(self.thread_10.deleteLater)
        self.worker_10.result.connect(self.search_10)

        self.thread_10.start()

    def start_search_thread_11(self):
        self.thread_11 = QtCore.QThread()
        self.worker_11 = SearchWorker(self.item_11.text())

        self.worker_11.moveToThread(self.thread_11)

        self.thread_11.started.connect(self.worker_11.run_2)
        self.worker_11.finished.connect(self.thread_11.quit)
        self.worker_11.finished.connect(self.worker_11.deleteLater)
        self.thread_11.finished.connect(self.thread_11.deleteLater)
        self.worker_11.result.connect(self.search_11)

        self.thread_11.start()

    def start_search_thread_12(self):
        self.thread_12 = QtCore.QThread()
        self.worker_12 = SearchWorker(self.item_12.text())

        self.worker_12.moveToThread(self.thread_12)

        self.thread_12.started.connect(self.worker_12.run_2)
        self.worker_12.finished.connect(self.thread_12.quit)
        self.worker_12.finished.connect(self.worker_12.deleteLater)
        self.thread_12.finished.connect(self.thread_12.deleteLater)
        self.worker_12.result.connect(self.search_12)

        self.thread_12.start()


    def save_item_1(self):
        with open("item1.txt", "w", encoding="utf-8") as file:
            file.write(self.item_1.text())                             

    def save_item_2(self):
        with open("item2.txt", "w", encoding="utf-8") as file:
            file.write(self.item_2.text())

    def save_item_3(self):
        with open("item3.txt", "w", encoding="utf-8") as file:
            file.write(self.item_3.text())

    def save_item_4(self):
        with open("item4.txt", "w", encoding="utf-8") as file:
            file.write(self.item_4.text())

    def save_item_5(self):
        with open("item5.txt", "w", encoding="utf-8") as file:
            file.write(self.item_5.text())

    def save_item_6(self):
        with open("item6.txt", "w", encoding="utf-8") as file:
            file.write(self.item_6.text())

    def save_item_7(self):
        with open("item7.txt", "w", encoding="utf-8") as file:
            file.write(self.item_7.text())

    def save_item_8(self):
        with open("item8.txt", "w", encoding="utf-8") as file:
            file.write(self.item_8.text())

    def save_item_9(self):
        with open("item9.txt", "w", encoding="utf-8") as file:
            file.write(self.item_9.text())

    def save_item_10(self):
        with open("item10.txt", "w", encoding="utf-8") as file:
            file.write(self.item_10.text())

    def save_item_11(self):
        with open("item11.txt", "w", encoding="utf-8") as file:
            file.write(self.item_11.text())

    def save_item_12(self):
        with open("item12.txt", "w", encoding="utf-8") as file:
            file.write(self.item_12.text())


    def search(self, result, start_index, item):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(start_index, start_index + 6):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            getattr(self, item).setText(_translate("MainWindow", "Item does not exist"))


    def search_1(self, result):
        self.search(result, 0, "item_1")

    def search_2(self, result):
        self.search(result, 6, "item_2")

    def search_3(self, result):
        self.search(result, 12, "item_3")

    def search_4(self, result):
        self.search(result, 18, "item_4")

    def search_5(self, result):
        self.search(result, 24, "item_5")

    def search_6(self, result):
        self.search(result, 30, "item_6")

    def search_7(self, result):
        self.search(result, 36, "item_7")

    def search_8(self, result):
        self.search(result, 42, "item_8")

    def search_9(self, result):
        self.search(result, 48, "item_9")


    def search_s(self, result, start_index, item):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(start_index, start_index + 5):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            getattr(self, item).setText(_translate("MainWindow", "Item does not exist"))


    def search_10(self, result):
        self.search_s(result, 54, "item_10")

    def search_11(self, result):
        self.search_s(result, 59, "item_11")

    def search_12(self, result):
        self.search_s(result, 64, "item_12")

    
class SearchWorker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    result = QtCore.pyqtSignal(object)

    def __init__(self, search_text):
        super().__init__()
        self.search_text = search_text

    def run(self):
        try:
            result = main(self.search_text, arcane=False)  #initializes the item fetcher
            self.result.emit(result)
        except Exception:
            self.result.emit(None)
        finally:
            self.finished.emit()


    def run_2(self):
        try:
            result = main(self.search_text, arcane=True)  #initializes the item fetcher
            self.result.emit(result)
        except Exception:
            self.result.emit(None)
        finally:
            self.finished.emit()

def mainn():                              #sets up the PyQt5 application
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":     #start the PyQt5 application
    mainn()