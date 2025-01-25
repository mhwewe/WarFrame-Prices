from PyQt5 import QtCore, QtGui, QtWidgets
from new_fetcher import main
import time


def make_search_thread(self, item, item_name, start_index):
    thread = QtCore.QThread()
    worker = SearchWorker(item.text())
    worker.moveToThread(thread)
    thread.started.connect(worker.run)
    worker.finished.connect(thread.quit)
    worker.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)
    worker.result.connect(lambda result: self.search(result, start_index, item_name))
    thread.start()
    return worker, thread


def make_search_thread_s(self, item, item_name, start_index):
    thread = QtCore.QThread()
    worker = SearchWorker(item.text())
    worker.moveToThread(thread)

    thread.started.connect(worker.run_2)
    worker.finished.connect(thread.quit)
    worker.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)
    worker.result.connect(lambda result: self.search(result, start_index, item_name))
    thread.start()
    return worker, thread


class SearchWorker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    result = QtCore.pyqtSignal(object)

    def __init__(self, search_text):
        super().__init__()
        self.search_text = search_text

    def run(self):
        try:
            result = main(self.search_text, arcane=False)  # initializes the item fetcher
            self.result.emit(result)

        except Exception:
            self.result.emit(None)
        finally:
            self.finished.emit()

    def run_2(self):
        try:
            result = main(self.search_text, arcane=True)  # initializes the item fetcher
            self.result.emit(result)
        except Exception:
            self.result.emit(None)
        finally:
            self.finished.emit()