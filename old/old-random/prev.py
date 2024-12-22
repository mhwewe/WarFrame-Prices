from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import pywmapi as wm
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QListWidget, QListWidgetItem
from isapi.threaded_extension import WorkerThread

import Resources
import Items
from Resources import bigback_rc
from Resources import test_rc
from Resources import transparent_rc
from pathlib import Path
import pickle
import os


class MainWorker(QThread):
        result_ready = pyqtSignal(list)

        def __init__(self, item_link, arcane, parent=None):
                super().__init__(parent)
                self.item_link = item_link
                self.arcane = arcane

        def run(self):
                n = -1;
                prices = [];
                names = [];
                lis = [];
                rows = 100;
                c = 0

                l = wm.items.get_orders(self.item_link)
                w = len(l)

                while n >= -w:
                        if ("OrderType.sell" in str(l[n])) and (
                                "Status.ingame" in str(l[n])) and self.arcane is True and ("mod_rank=5" in str(l[n])):
                                Name = str(l[n]).split("ingame_name='")
                                Name = Name[1].split("', avatar")
                                name = Name[0]
                                names.append(name)

                                Price = str(l[n]).split("platinum=")
                                Price = Price[1].split(', quantit')
                                price = int(Price[0])
                                prices.append(price)
                                c += 1
                        if ("OrderType.sell" in str(l[n])) and ("Status.ingame" in str(l[n])) and self.arcane is False:
                                Name = str(l[n]).split("ingame_name='")
                                Name = Name[1].split("', avatar")
                                name = Name[0]
                                names.append(name)

                                Price = str(l[n]).split("platinum=")
                                Price = Price[1].split(', quantit')
                                price = int(Price[0])
                                prices.append(price)
                                c += 1
                        n = n - 1
                if rows > c:
                        rows = c
                i = 0
                for price_name in sorted(zip(prices, names)):
                        name_price = (
                                price_name[1], f"{price_name[0]} P")
                        lis.append(name_price)
                        i = i + 1
                        if i == rows: break
                self.result_ready.emit(lis)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Threading Example")
        self.resize(500, 300)

        # Layout Components
        layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.start_button = QPushButton("Fetch Data")

        layout.addWidget(self.list_widget)
        layout.addWidget(self.start_button)

        # Main Widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Button click triggers worker thread
        self.start_button.clicked.connect(self.fetch_data)

    def fetch_data(self):
        # Instantiate the worker thread with parameters
        self.worker = MainWorker(item_link="trumna_prime_set", arcane=False)

        # Connect worker signal to a handler method
        self.worker.result_ready.connect(self.handle_results)

        # Start the worker thread
        self.worker.start()

    def handle_results(self, results):
        # Populate the ListWidget with worker results
        self.list_widget.clear()
        for name, price in results:
            item = QListWidgetItem(f"{name}: {price}")
            self.list_widget.addItem(item)


# Main Application Execution
app = QApplication([])

main_win = MainWindow()
main_win.show()

app.exec()