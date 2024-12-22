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
        getattr(self, item).setText(_translate("MainWindow", "This item does not exist"))


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