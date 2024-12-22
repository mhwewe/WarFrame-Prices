import sys
import pywmapi as wm
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import pywmapi as wm
from PyQt5.QtWidgets import *
from PyQt5 import uic
import Resources
import Items
from Resources import bigback_rc
from Resources import test_rc
from Resources import transparent_rc
from pathlib import Path
import pickle
def main(vari,item_link, arcane):
    n = -1;prices = [];names = [];lis = [];rows = 100;c = 0

    l = wm.items.get_orders(item_link)
    w = len(l)

    while n >= -w:
        if ("OrderType.sell" in str(l[n])) and ("Status.ingame" in str(l[n])) and arcane is True and ("mod_rank=5" in str(l[n])):
            Name = str(l[n]).split("ingame_name='")
            Name = Name[1].split("', avatar")
            name = Name[0]
            names.append(name)

            Price = str(l[n]).split("platinum=")
            Price = Price[1].split(', quantit')
            price = int(Price[0])
            prices.append(price)
            c += 1
        if ("OrderType.sell" in str(l[n])) and ("Status.ingame" in str(l[n])) and arcane is False:
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
    i = 0;
    li = []
    for price_name in sorted(zip(prices, names)):
        name_price = (
        price_name[1], f"{price_name[0]} P")
        lis.append(name_price)
        i = i + 1
        if i == rows: break
    t = 0
    return lis

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        #Load the UI file
        uic.loadUi("uitest.ui", self)

        #show the app
        self.show

#Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()