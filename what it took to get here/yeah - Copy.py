# import sys
# from multiprocessing.pool import worker
#
# from PyQt5 import QtWidgets, uic
# import pywmapi as wm
# import Resources
# import Items
# from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
# from Resources import bigback_rc
# from Resources import test_rc
# from Resources import transparent_rc
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import *
# import pywmapi as wm
# import Resources
# import Items
# from Resources import bigback_rc
# from Resources import test_rc
# from Resources import transparent_rc
# from pathlib import Path
# import pickle
# from fetcher import main
#
#
# class MainApp(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # Load the .ui file from the root directory
#         uic.loadUi("uitest.ui", self)
#
#         # Define our widgets
#         self.item_1 = self.findChild(QLineEdit, "item_1")
#         self.item_2 = self.findChild(QLineEdit, "item_2")
#         self.item_3 = self.findChild(QLineEdit, "item_3")
#         self.item_4 = self.findChild(QLineEdit, "item_4")
#         self.item_5 = self.findChild(QLineEdit, "item_5")
#         self.item_6 = self.findChild(QLineEdit, "item_6")
#         self.item_7 = self.findChild(QLineEdit, "item_7")
#         self.item_8 = self.findChild(QLineEdit, "item_8")
#         self.item_9 = self.findChild(QLineEdit, "item_9")
#         self.item_10 = self.findChild(QLineEdit, "item_10")
#         self.item_11 = self.findChild(QLineEdit, "item_11")
#         self.item_12 = self.findChild(QLineEdit, "item_12")
#
#         self.search_1_btn = self.findChild(QPushButton, "search_1_btn")
#         self.search_2_btn = self.findChild(QPushButton, "search_2_btn")
#         self.search_3_btn = self.findChild(QPushButton, "search_3_btn")
#         self.search_4_btn = self.findChild(QPushButton, "search_4_btn")
#         self.search_5_btn = self.findChild(QPushButton, "search_5_btn")
#         self.search_6_btn = self.findChild(QPushButton, "search_6_btn")
#         self.search_7_btn = self.findChild(QPushButton, "search_7_btn")
#         self.search_8_btn = self.findChild(QPushButton, "search_8_btn")
#         self.search_9_btn = self.findChild(QPushButton, "search_9_btn")
#         self.search_10_btn = self.findChild(QPushButton, "search_10_btn")
#         self.search_11_btn = self.findChild(QPushButton, "search_11_btn")
#         self.search_12_btn = self.findChild(QPushButton, "search_12_btn")
#
#         self.name_1 = self.findChild(QLabel, "name_1")
#         self.name_2 = self.findChild(QLabel, "name_2")
#         self.name_3 = self.findChild(QLabel, "name_3")
#         self.name_4 = self.findChild(QLabel, "name_4")
#         self.name_5 = self.findChild(QLabel, "name_5")
#         self.name_6 = self.findChild(QLabel, "name_6")
#         self.name_7 = self.findChild(QLabel, "name_7")
#         self.name_8 = self.findChild(QLabel, "name_8")
#         self.name_9 = self.findChild(QLabel, "name_9")
#         self.name_10 = self.findChild(QLabel, "name_10")
#         self.name_11 = self.findChild(QLabel, "name_11")
#         self.name_12 = self.findChild(QLabel, "name_12")
#         self.name_13 = self.findChild(QLabel, "name_13")
#         self.name_14 = self.findChild(QLabel, "name_14")
#         self.name_15 = self.findChild(QLabel, "name_15")
#         self.name_16 = self.findChild(QLabel, "name_16")
#         self.name_17 = self.findChild(QLabel, "name_17")
#         self.name_18 = self.findChild(QLabel, "name_18")
#         self.name_19 = self.findChild(QLabel, "name_19")
#         self.name_20 = self.findChild(QLabel, "name_20")
#         self.name_21 = self.findChild(QLabel, "name_21")
#         self.name_22 = self.findChild(QLabel, "name_22")
#         self.name_23 = self.findChild(QLabel, "name_23")
#         self.name_24 = self.findChild(QLabel, "name_24")
#         self.name_25 = self.findChild(QLabel, "name_25")
#         self.name_26 = self.findChild(QLabel, "name_26")
#         self.name_27 = self.findChild(QLabel, "name_27")
#         self.name_28 = self.findChild(QLabel, "name_28")
#         self.name_29 = self.findChild(QLabel, "name_29")
#         self.name_30 = self.findChild(QLabel, "name_30")
#         self.name_31 = self.findChild(QLabel, "name_31")
#         self.name_32 = self.findChild(QLabel, "name_32")
#         self.name_33 = self.findChild(QLabel, "name_33")
#         self.name_34 = self.findChild(QLabel, "name_34")
#         self.name_35 = self.findChild(QLabel, "name_35")
#         self.name_36 = self.findChild(QLabel, "name_36")
#         self.name_37 = self.findChild(QLabel, "name_37")
#         self.name_38 = self.findChild(QLabel, "name_38")
#         self.name_39 = self.findChild(QLabel, "name_39")
#         self.name_40 = self.findChild(QLabel, "name_40")
#         self.name_41 = self.findChild(QLabel, "name_41")
#         self.name_42 = self.findChild(QLabel, "name_42")
#         self.name_43 = self.findChild(QLabel, "name_43")
#         self.name_44 = self.findChild(QLabel, "name_44")
#         self.name_45 = self.findChild(QLabel, "name_45")
#         self.name_46 = self.findChild(QLabel, "name_46")
#         self.name_47 = self.findChild(QLabel, "name_47")
#         self.name_48 = self.findChild(QLabel, "name_48")
#         self.name_49 = self.findChild(QLabel, "name_49")
#         self.name_50 = self.findChild(QLabel, "name_50")
#         self.name_51 = self.findChild(QLabel, "name_51")
#         self.name_52 = self.findChild(QLabel, "name_52")
#         self.name_53 = self.findChild(QLabel, "name_53")
#         self.name_54 = self.findChild(QLabel, "name_54")
#         self.name_55 = self.findChild(QLabel, "name_55")
#         self.name_56 = self.findChild(QLabel, "name_56")
#         self.name_57 = self.findChild(QLabel, "name_57")
#         self.name_58 = self.findChild(QLabel, "name_58")
#         self.name_59 = self.findChild(QLabel, "name_59")
#         self.name_60 = self.findChild(QLabel, "name_60")
#         self.name_61 = self.findChild(QLabel, "name_61")
#         self.name_62 = self.findChild(QLabel, "name_62")
#         self.name_63 = self.findChild(QLabel, "name_63")
#         self.name_64 = self.findChild(QLabel, "name_64")
#         self.name_65 = self.findChild(QLabel, "name_65")
#         self.name_66 = self.findChild(QLabel, "name_66")
#         self.name_67 = self.findChild(QLabel, "name_67")
#         self.name_68 = self.findChild(QLabel, "name_68")
#         self.name_69 = self.findChild(QLabel, "name_69")
#
#         self.price_1 = self.findChild(QLabel, "price_1")
#         self.price_2 = self.findChild(QLabel, "price_2")
#         self.price_3 = self.findChild(QLabel, "price_3")
#         self.price_4 = self.findChild(QLabel, "price_4")
#         self.price_5 = self.findChild(QLabel, "price_5")
#         self.price_6 = self.findChild(QLabel, "price_6")
#         self.price_7 = self.findChild(QLabel, "price_7")
#         self.price_8 = self.findChild(QLabel, "price_8")
#         self.price_9 = self.findChild(QLabel, "price_9")
#         self.price_10 = self.findChild(QLabel, "price_10")
#         self.price_11 = self.findChild(QLabel, "price_11")
#         self.price_12 = self.findChild(QLabel, "price_12")
#         self.price_13 = self.findChild(QLabel, "price_13")
#         self.price_14 = self.findChild(QLabel, "price_14")
#         self.price_15 = self.findChild(QLabel, "price_15")
#         self.price_16 = self.findChild(QLabel, "price_16")
#         self.price_17 = self.findChild(QLabel, "price_17")
#         self.price_18 = self.findChild(QLabel, "price_18")
#         self.price_19 = self.findChild(QLabel, "price_19")
#         self.price_20 = self.findChild(QLabel, "price_20")
#         self.price_21 = self.findChild(QLabel, "price_21")
#         self.price_22 = self.findChild(QLabel, "price_22")
#         self.price_23 = self.findChild(QLabel, "price_23")
#         self.price_24 = self.findChild(QLabel, "price_24")
#         self.price_25 = self.findChild(QLabel, "price_25")
#         self.price_26 = self.findChild(QLabel, "price_26")
#         self.price_27 = self.findChild(QLabel, "price_27")
#         self.price_28 = self.findChild(QLabel, "price_28")
#         self.price_29 = self.findChild(QLabel, "price_29")
#         self.price_30 = self.findChild(QLabel, "price_30")
#         self.price_31 = self.findChild(QLabel, "price_31")
#         self.price_32 = self.findChild(QLabel, "price_32")
#         self.price_33 = self.findChild(QLabel, "price_33")
#         self.price_34 = self.findChild(QLabel, "price_34")
#         self.price_35 = self.findChild(QLabel, "price_35")
#         self.price_36 = self.findChild(QLabel, "price_36")
#         self.price_37 = self.findChild(QLabel, "price_37")
#         self.price_38 = self.findChild(QLabel, "price_38")
#         self.price_39 = self.findChild(QLabel, "price_39")
#         self.price_40 = self.findChild(QLabel, "price_40")
#         self.price_41 = self.findChild(QLabel, "price_41")
#         self.price_42 = self.findChild(QLabel, "price_42")
#         self.price_43 = self.findChild(QLabel, "price_43")
#         self.price_44 = self.findChild(QLabel, "price_44")
#         self.price_45 = self.findChild(QLabel, "price_45")
#         self.price_46 = self.findChild(QLabel, "price_46")
#         self.price_47 = self.findChild(QLabel, "price_47")
#         self.price_48 = self.findChild(QLabel, "price_48")
#         self.price_49 = self.findChild(QLabel, "price_49")
#         self.price_50 = self.findChild(QLabel, "price_50")
#         self.price_51 = self.findChild(QLabel, "price_51")
#         self.price_52 = self.findChild(QLabel, "price_52")
#         self.price_53 = self.findChild(QLabel, "price_53")
#         self.price_54 = self.findChild(QLabel, "price_54")
#         self.price_55 = self.findChild(QLabel, "price_55")
#         self.price_56 = self.findChild(QLabel, "price_56")
#         self.price_57 = self.findChild(QLabel, "price_57")
#         self.price_58 = self.findChild(QLabel, "price_58")
#         self.price_59 = self.findChild(QLabel, "price_59")
#         self.price_60 = self.findChild(QLabel, "price_60")
#         self.price_61 = self.findChild(QLabel, "price_61")
#         self.price_62 = self.findChild(QLabel, "price_62")
#         self.price_63 = self.findChild(QLabel, "price_63")
#         self.price_64 = self.findChild(QLabel, "price_64")
#         self.price_65 = self.findChild(QLabel, "price_65")
#         self.price_66 = self.findChild(QLabel, "price_66")
#         self.price_67 = self.findChild(QLabel, "price_67")
#         self.price_68 = self.findChild(QLabel, "price_68")
#         self.price_69 = self.findChild(QLabel, "price_69")
#
#         # Do something
#         self.search_1_btn.clicked.connect(self.start_search_thread_1)
#         self.search_2_btn.clicked.connect(self.start_search_thread_2)
#         self.search_3_btn.clicked.connect(self.start_search_thread_3)
#         self.search_4_btn.clicked.connect(self.start_search_thread_4)
#         self.search_5_btn.clicked.connect(self.start_search_thread_5)
#         self.search_6_btn.clicked.connect(self.start_search_thread_6)
#         self.search_7_btn.clicked.connect(self.start_search_thread_7)
#         self.search_8_btn.clicked.connect(self.start_search_thread_8)
#         self.search_9_btn.clicked.connect(self.start_search_thread_9)
#         self.search_10_btn.clicked.connect(self.start_search_thread_10)
#         self.search_11_btn.clicked.connect(self.start_search_thread_11)
#         self.search_12_btn.clicked.connect(self.start_search_thread_12)
#
#     _translate = QtCore.QCoreApplication.translate
#
#     def start_search_thread_1(self):
#         self.thread_1 = QtCore.QThread()
#         self.worker_1 = SearchWorker(self.item_1.text())
#
#         self.worker_1.moveToThread(self.thread_1)
#
#         self.thread_1.started.connect(self.worker_1.run)
#         self.worker_1.finished.connect(self.thread_1.quit)
#         self.worker_1.finished.connect(self.worker_1.deleteLater)
#         self.thread_1.finished.connect(self.thread_1.deleteLater)
#         self.worker_1.result.connect(self.search_1)
#
#         self.thread_1.start()
#
#     def start_search_thread_2(self):
#         self.thread_2 = QtCore.QThread()
#         self.worker_2 = SearchWorker(self.item_2.text())
#
#         self.worker_2.moveToThread(self.thread_2)
#
#         self.thread_2.started.connect(self.worker_2.run)
#         self.worker_2.finished.connect(self.thread_2.quit)
#         self.worker_2.finished.connect(self.worker_2.deleteLater)
#         self.thread_2.finished.connect(self.thread_2.deleteLater)
#         self.worker_2.result.connect(self.search_2)
#
#         self.thread_2.start()
#
#     def start_search_thread_3(self):
#         self.thread_3 = QtCore.QThread()
#         self.worker_3 = SearchWorker(self.item_3.text())
#
#         self.worker_3.moveToThread(self.thread_3)
#
#         self.thread_3.started.connect(self.worker_3.run)
#         self.worker_3.finished.connect(self.thread_3.quit)
#         self.worker_3.finished.connect(self.worker_3.deleteLater)
#         self.thread_3.finished.connect(self.thread_3.deleteLater)
#         self.worker_3.result.connect(self.search_3)
#
#         self.thread_3.start()
#
#     def start_search_thread_4(self):
#         self.thread_4 = QtCore.QThread()
#         self.worker_4 = SearchWorker(self.item_4.text())
#
#         self.worker_4.moveToThread(self.thread_4)
#
#         self.thread_4.started.connect(self.worker_4.run)
#         self.worker_4.finished.connect(self.thread_4.quit)
#         self.worker_4.finished.connect(self.worker_4.deleteLater)
#         self.thread_4.finished.connect(self.thread_4.deleteLater)
#         self.worker_4.result.connect(self.search_4)
#
#         self.thread_4.start()
#
#     def start_search_thread_5(self):
#         self.thread_5 = QtCore.QThread()
#         self.worker_5 = SearchWorker(self.item_5.text())
#
#         self.worker_5.moveToThread(self.thread_5)
#
#         self.thread_5.started.connect(self.worker_5.run)
#         self.worker_5.finished.connect(self.thread_5.quit)
#         self.worker_5.finished.connect(self.worker_5.deleteLater)
#         self.thread_5.finished.connect(self.thread_5.deleteLater)
#         self.worker_5.result.connect(self.search_5)
#
#         self.thread_5.start()
#
#     def start_search_thread_6(self):
#         self.thread_6 = QtCore.QThread()
#         self.worker_6 = SearchWorker(self.item_6.text())
#
#         self.worker_6.moveToThread(self.thread_6)
#
#         self.thread_6.started.connect(self.worker_6.run)
#         self.worker_6.finished.connect(self.thread_6.quit)
#         self.worker_6.finished.connect(self.worker_6.deleteLater)
#         self.thread_6.finished.connect(self.thread_6.deleteLater)
#         self.worker_6.result.connect(self.search_6)
#
#         self.thread_6.start()
#
#     def start_search_thread_7(self):
#         self.thread_7 = QtCore.QThread()
#         self.worker_7 = SearchWorker(self.item_7.text())
#
#         self.worker_7.moveToThread(self.thread_7)
#
#         self.thread_7.started.connect(self.worker_7.run)
#         self.worker_7.finished.connect(self.thread_7.quit)
#         self.worker_7.finished.connect(self.worker_7.deleteLater)
#         self.thread_7.finished.connect(self.thread_7.deleteLater)
#         self.worker_7.result.connect(self.search_7)
#
#         self.thread_7.start()
#
#     def start_search_thread_8(self):
#         self.thread_8 = QtCore.QThread()
#         self.worker_8 = SearchWorker(self.item_8.text())
#
#         self.worker_8.moveToThread(self.thread_8)
#
#         self.thread_8.started.connect(self.worker_8.run)
#         self.worker_8.finished.connect(self.thread_8.quit)
#         self.worker_8.finished.connect(self.worker_8.deleteLater)
#         self.thread_8.finished.connect(self.thread_8.deleteLater)
#         self.worker_8.result.connect(self.search_8)
#
#         self.thread_8.start()
#
#     def start_search_thread_9(self):
#         self.thread_9 = QtCore.QThread()
#         self.worker_9 = SearchWorker(self.item_9.text())
#
#         self.worker_9.moveToThread(self.thread_9)
#
#         self.thread_9.started.connect(self.worker_9.run)
#         self.worker_9.finished.connect(self.thread_9.quit)
#         self.worker_9.finished.connect(self.worker_9.deleteLater)
#         self.thread_9.finished.connect(self.thread_9.deleteLater)
#         self.worker_9.result.connect(self.search_9)
#
#         self.thread_9.start()
#
#     def start_search_thread_10(self):
#         self.thread_10 = QtCore.QThread()
#         self.worker_10 = SearchWorker(self.item_10.text())
#
#         self.worker_10.moveToThread(self.thread_10)
#
#         self.thread_10.started.connect(self.worker_10.run)
#         self.worker_10.finished.connect(self.thread_10.quit)
#         self.worker_10.finished.connect(self.worker_10.deleteLater)
#         self.thread_10.finished.connect(self.thread_10.deleteLater)
#         self.worker_10.result.connect(self.search_10)
#
#         self.thread_10.start()
#
#     def start_search_thread_11(self):
#         self.thread_11 = QtCore.QThread()
#         self.worker_11 = SearchWorker(self.item_11.text())
#
#         self.worker_11.moveToThread(self.thread_11)
#
#         self.thread_11.started.connect(self.worker_11.run)
#         self.worker_11.finished.connect(self.thread_11.quit)
#         self.worker_11.finished.connect(self.worker_11.deleteLater)
#         self.thread_11.finished.connect(self.thread_11.deleteLater)
#         self.worker_11.result.connect(self.search_11)
#
#         self.thread_11.start()
#
#     def start_search_thread_12(self):
#         self.thread_12 = QtCore.QThread()
#         self.worker_12 = SearchWorker(self.item_12.text())
#
#         self.worker_12.moveToThread(self.thread_12)
#
#         self.thread_12.started.connect(self.worker_12.run)
#         self.worker_12.finished.connect(self.thread_12.quit)
#         self.worker_12.finished.connect(self.worker_12.deleteLater)
#         self.thread_12.finished.connect(self.thread_12.deleteLater)
#         self.worker_12.result.connect(self.search_12)
#
#         self.thread_12.start()
#
#     def search_1(self, result):
#         _translate = QtCore.QCoreApplication.translate
#         try:
#             c = 0
#             self.setWindowTitle(_translate("MainWindow", "Yo"))
#             for i in range(6):
#                 getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
#                 getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
#                 c += 1
#         except Exception:
#             self.item_1.setText(_translate("MainWindow", "This item does not exist"))
#
#     def search_2(self, result):
#         _translate = QtCore.QCoreApplication.translate
#         try:
#             c = 0
#             self.setWindowTitle(_translate("MainWindow", "Yo"))
#             for i in range(6, 12):
#                 getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
#                 getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
#                 c += 1
#         except Exception:
#             self.item_2.setText(_translate("MainWindow", "This item does not exist"))
#
#     def search_3(self, result):
#         _translate = QtCore.QCoreApplication.translate
#         try:
#             c = 0
#             self.setWindowTitle(_translate("MainWindow", "Yo"))
#             for i in range(12, 18):
#                 getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
#                 getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
#                 c += 1
#         except Exception:
#             self.item_3.setText(_translate("MainWindow", "This item does not exist"))
#
#     def search_4(self, result):
#         _translate = QtCore.QCoreApplication.translate
#         try:
#             c = 0
#             self.setWindowTitle(_translate("MainWindow", "Yo"))
#             for i in range(18, 24):
#                 getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
#                 getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
#                 c += 1
#         except Exception:
#             self.item_4.setText(_translate("MainWindow", "This item does not exist"))
#
#     def search_5(self, result):
#         _translate = QtCore.QCoreApplication.translate
#         try:
#             c = 0
#             self.setWindowTitle(_translate("MainWindow", "Yo"))
#             for i in range(24, 30):
#                 getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
#                 getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
#                 c += 1
#         except Exception:
#             self.item_5.setText(_translate("MainWindow", "This item does not exist"))
#
#     def search_6(self, result):
#         _translate = QtCore.QCoreApplication.translate
#         try:
#             c = 0
#             self.setWindowTitle(_translate("MainWindow", "Yo"))
#             for i in range(30, 36):
#                 getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
#                 getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
#                 c += 1
#         except Exception:
#             self.item_6.setText(_translate("MainWindow", "This item does not exist"))
#
#     def search_7(self, result):
#         _translate = QtCore.QCoreApplication.translate
#         try:
#             c = 0
#             self.setWindowTitle(_translate("MainWindow", "Yo"))
#             for i in range(36, 42):
#                 getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
#                 getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
#                 c += 1
#         except Exception:
#             self.item_7.setText(_translate("MainWindow", "This item does not exist"))
#
#     def search_8(self, result):
#         _translate = QtCore.QCoreApplication.translate
#         try:
#             c = 0
#             self.setWindowTitle(_translate("MainWindow", "Yo"))
#             for i in range(42, 48):
#                 getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
#                 getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
#                 c += 1
#         except Exception:
#             self.item_8.setText(_translate("MainWindow", "This item does not exist"))
#
#     def search_9(self, result):
#         _translate = QtCore.QCoreApplication.translate
#         try:
#             c = 0
#             self.setWindowTitle(_translate("MainWindow", "Yo"))
#             for i in range(48, 54):
#                 getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
#                 getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
#                 c += 1
#         except Exception:
#             self.item_9.setText(_translate("MainWindow", "This item does not exist"))
#
#     def search_10(self, result):
#         _translate = QtCore.QCoreApplication.translate
#         try:
#             c = 0
#             self.setWindowTitle(_translate("MainWindow", "Yo"))
#             for i in range(54, 59):
#                 getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
#                 getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
#                 c += 1
#         except Exception:
#             self.item_10.setText(_translate("MainWindow", "This item does not exist"))
#
#     def search_11(self, result):
#         _translate = QtCore.QCoreApplication.translate
#         try:
#             c = 0
#             self.setWindowTitle(_translate("MainWindow", "Yo"))
#             for i in range(59, 64):
#                 getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
#                 getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
#                 c += 1
#         except Exception:
#             self.item_11.setText(_translate("MainWindow", "This item does not exist"))
#
#     def search_12(self, result):
#         _translate = QtCore.QCoreApplication.translate
#         try:
#             c = 0
#             self.setWindowTitle(_translate("MainWindow", "Yo"))
#             for i in range(64, 69):  # Note: Adjust as needed based on the total result length.
#                 getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
#                 getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
#                 c += 1
#         except Exception:
#             self.item_12.setText(_translate("MainWindow", "This item does not exist"))
#
#
# class SearchWorker(QtCore.QObject):
#     finished = QtCore.pyqtSignal()
#     result = QtCore.pyqtSignal(object)
#
#     def __init__(self, search_text):
#         super().__init__()
#         self.search_text = search_text
#
#     def run(self):
#         try:
#             result = main(self.search_text, arcane=False)
#             self.result.emit(result)
#         except Exception:
#             self.result.emit(None)
#         finally:
#             self.finished.emit()
#
#
# def mainn():
#     app = QtWidgets.QApplication(sys.argv)
#     window = MainApp()
#     window.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     mainn()


import sys
from multiprocessing.pool import worker

from PyQt5 import QtWidgets, uic
import pywmapi as wm
import Resources
import Items
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from Resources import bigback_rc
from Resources import test_rc
from Resources import transparent_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import pywmapi as wm
import Resources
import Items
from Resources import bigback_rc
from Resources import test_rc
from Resources import transparent_rc
from pathlib import Path
import pickle
from fetcher import main


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the .ui file from the root directory
        uic.loadUi("uitest.ui", self)

        # Define our widgets
        self.item_1 = self.findChild(QLineEdit, "item_1")
        self.item_2 = self.findChild(QLineEdit, "item_2")
        self.item_3 = self.findChild(QLineEdit, "item_3")
        self.item_4 = self.findChild(QLineEdit, "item_4")
        self.item_5 = self.findChild(QLineEdit, "item_5")
        self.item_6 = self.findChild(QLineEdit, "item_6")
        self.item_7 = self.findChild(QLineEdit, "item_7")
        self.item_8 = self.findChild(QLineEdit, "item_8")
        self.item_9 = self.findChild(QLineEdit, "item_9")
        self.item_10 = self.findChild(QLineEdit, "item_10")
        self.item_11 = self.findChild(QLineEdit, "item_11")
        self.item_12 = self.findChild(QLineEdit, "item_12")

        self.search_1_btn = self.findChild(QPushButton, "search_1_btn")
        self.search_2_btn = self.findChild(QPushButton, "search_2_btn")
        self.search_3_btn = self.findChild(QPushButton, "search_3_btn")
        self.search_4_btn = self.findChild(QPushButton, "search_4_btn")
        self.search_5_btn = self.findChild(QPushButton, "search_5_btn")
        self.search_6_btn = self.findChild(QPushButton, "search_6_btn")
        self.search_7_btn = self.findChild(QPushButton, "search_7_btn")
        self.search_8_btn = self.findChild(QPushButton, "search_8_btn")
        self.search_9_btn = self.findChild(QPushButton, "search_9_btn")
        self.search_10_btn = self.findChild(QPushButton, "search_10_btn")
        self.search_11_btn = self.findChild(QPushButton, "search_11_btn")
        self.search_12_btn = self.findChild(QPushButton, "search_12_btn")

        self.name_1 = self.findChild(QLabel, "name_1")
        self.name_2 = self.findChild(QLabel, "name_2")
        self.name_3 = self.findChild(QLabel, "name_3")
        self.name_4 = self.findChild(QLabel, "name_4")
        self.name_5 = self.findChild(QLabel, "name_5")
        self.name_6 = self.findChild(QLabel, "name_6")
        self.name_7 = self.findChild(QLabel, "name_7")
        self.name_8 = self.findChild(QLabel, "name_8")
        self.name_9 = self.findChild(QLabel, "name_9")
        self.name_10 = self.findChild(QLabel, "name_10")
        self.name_11 = self.findChild(QLabel, "name_11")
        self.name_12 = self.findChild(QLabel, "name_12")
        self.name_13 = self.findChild(QLabel, "name_13")
        self.name_14 = self.findChild(QLabel, "name_14")
        self.name_15 = self.findChild(QLabel, "name_15")
        self.name_16 = self.findChild(QLabel, "name_16")
        self.name_17 = self.findChild(QLabel, "name_17")
        self.name_18 = self.findChild(QLabel, "name_18")
        self.name_19 = self.findChild(QLabel, "name_19")
        self.name_20 = self.findChild(QLabel, "name_20")
        self.name_21 = self.findChild(QLabel, "name_21")
        self.name_22 = self.findChild(QLabel, "name_22")
        self.name_23 = self.findChild(QLabel, "name_23")
        self.name_24 = self.findChild(QLabel, "name_24")
        self.name_25 = self.findChild(QLabel, "name_25")
        self.name_26 = self.findChild(QLabel, "name_26")
        self.name_27 = self.findChild(QLabel, "name_27")
        self.name_28 = self.findChild(QLabel, "name_28")
        self.name_29 = self.findChild(QLabel, "name_29")
        self.name_30 = self.findChild(QLabel, "name_30")
        self.name_31 = self.findChild(QLabel, "name_31")
        self.name_32 = self.findChild(QLabel, "name_32")
        self.name_33 = self.findChild(QLabel, "name_33")
        self.name_34 = self.findChild(QLabel, "name_34")
        self.name_35 = self.findChild(QLabel, "name_35")
        self.name_36 = self.findChild(QLabel, "name_36")
        self.name_37 = self.findChild(QLabel, "name_37")
        self.name_38 = self.findChild(QLabel, "name_38")
        self.name_39 = self.findChild(QLabel, "name_39")
        self.name_40 = self.findChild(QLabel, "name_40")
        self.name_41 = self.findChild(QLabel, "name_41")
        self.name_42 = self.findChild(QLabel, "name_42")
        self.name_43 = self.findChild(QLabel, "name_43")
        self.name_44 = self.findChild(QLabel, "name_44")
        self.name_45 = self.findChild(QLabel, "name_45")
        self.name_46 = self.findChild(QLabel, "name_46")
        self.name_47 = self.findChild(QLabel, "name_47")
        self.name_48 = self.findChild(QLabel, "name_48")
        self.name_49 = self.findChild(QLabel, "name_49")
        self.name_50 = self.findChild(QLabel, "name_50")
        self.name_51 = self.findChild(QLabel, "name_51")
        self.name_52 = self.findChild(QLabel, "name_52")
        self.name_53 = self.findChild(QLabel, "name_53")
        self.name_54 = self.findChild(QLabel, "name_54")
        self.name_55 = self.findChild(QLabel, "name_55")
        self.name_56 = self.findChild(QLabel, "name_56")
        self.name_57 = self.findChild(QLabel, "name_57")
        self.name_58 = self.findChild(QLabel, "name_58")
        self.name_59 = self.findChild(QLabel, "name_59")
        self.name_60 = self.findChild(QLabel, "name_60")
        self.name_61 = self.findChild(QLabel, "name_61")
        self.name_62 = self.findChild(QLabel, "name_62")
        self.name_63 = self.findChild(QLabel, "name_63")
        self.name_64 = self.findChild(QLabel, "name_64")
        self.name_65 = self.findChild(QLabel, "name_65")
        self.name_66 = self.findChild(QLabel, "name_66")
        self.name_67 = self.findChild(QLabel, "name_67")
        self.name_68 = self.findChild(QLabel, "name_68")
        self.name_69 = self.findChild(QLabel, "name_69")

        self.price_1 = self.findChild(QLabel, "price_1")
        self.price_2 = self.findChild(QLabel, "price_2")
        self.price_3 = self.findChild(QLabel, "price_3")
        self.price_4 = self.findChild(QLabel, "price_4")
        self.price_5 = self.findChild(QLabel, "price_5")
        self.price_6 = self.findChild(QLabel, "price_6")
        self.price_7 = self.findChild(QLabel, "price_7")
        self.price_8 = self.findChild(QLabel, "price_8")
        self.price_9 = self.findChild(QLabel, "price_9")
        self.price_10 = self.findChild(QLabel, "price_10")
        self.price_11 = self.findChild(QLabel, "price_11")
        self.price_12 = self.findChild(QLabel, "price_12")
        self.price_13 = self.findChild(QLabel, "price_13")
        self.price_14 = self.findChild(QLabel, "price_14")
        self.price_15 = self.findChild(QLabel, "price_15")
        self.price_16 = self.findChild(QLabel, "price_16")
        self.price_17 = self.findChild(QLabel, "price_17")
        self.price_18 = self.findChild(QLabel, "price_18")
        self.price_19 = self.findChild(QLabel, "price_19")
        self.price_20 = self.findChild(QLabel, "price_20")
        self.price_21 = self.findChild(QLabel, "price_21")
        self.price_22 = self.findChild(QLabel, "price_22")
        self.price_23 = self.findChild(QLabel, "price_23")
        self.price_24 = self.findChild(QLabel, "price_24")
        self.price_25 = self.findChild(QLabel, "price_25")
        self.price_26 = self.findChild(QLabel, "price_26")
        self.price_27 = self.findChild(QLabel, "price_27")
        self.price_28 = self.findChild(QLabel, "price_28")
        self.price_29 = self.findChild(QLabel, "price_29")
        self.price_30 = self.findChild(QLabel, "price_30")
        self.price_31 = self.findChild(QLabel, "price_31")
        self.price_32 = self.findChild(QLabel, "price_32")
        self.price_33 = self.findChild(QLabel, "price_33")
        self.price_34 = self.findChild(QLabel, "price_34")
        self.price_35 = self.findChild(QLabel, "price_35")
        self.price_36 = self.findChild(QLabel, "price_36")
        self.price_37 = self.findChild(QLabel, "price_37")
        self.price_38 = self.findChild(QLabel, "price_38")
        self.price_39 = self.findChild(QLabel, "price_39")
        self.price_40 = self.findChild(QLabel, "price_40")
        self.price_41 = self.findChild(QLabel, "price_41")
        self.price_42 = self.findChild(QLabel, "price_42")
        self.price_43 = self.findChild(QLabel, "price_43")
        self.price_44 = self.findChild(QLabel, "price_44")
        self.price_45 = self.findChild(QLabel, "price_45")
        self.price_46 = self.findChild(QLabel, "price_46")
        self.price_47 = self.findChild(QLabel, "price_47")
        self.price_48 = self.findChild(QLabel, "price_48")
        self.price_49 = self.findChild(QLabel, "price_49")
        self.price_50 = self.findChild(QLabel, "price_50")
        self.price_51 = self.findChild(QLabel, "price_51")
        self.price_52 = self.findChild(QLabel, "price_52")
        self.price_53 = self.findChild(QLabel, "price_53")
        self.price_54 = self.findChild(QLabel, "price_54")
        self.price_55 = self.findChild(QLabel, "price_55")
        self.price_56 = self.findChild(QLabel, "price_56")
        self.price_57 = self.findChild(QLabel, "price_57")
        self.price_58 = self.findChild(QLabel, "price_58")
        self.price_59 = self.findChild(QLabel, "price_59")
        self.price_60 = self.findChild(QLabel, "price_60")
        self.price_61 = self.findChild(QLabel, "price_61")
        self.price_62 = self.findChild(QLabel, "price_62")
        self.price_63 = self.findChild(QLabel, "price_63")
        self.price_64 = self.findChild(QLabel, "price_64")
        self.price_65 = self.findChild(QLabel, "price_65")
        self.price_66 = self.findChild(QLabel, "price_66")
        self.price_67 = self.findChild(QLabel, "price_67")
        self.price_68 = self.findChild(QLabel, "price_68")
        self.price_69 = self.findChild(QLabel, "price_69")

        # Do something
        self.search_1_btn.clicked.connect(self.start_search_thread_1)
        self.search_1_btn.clicked.connect(lambda: self.save_item_1())
        self.search_2_btn.clicked.connect(self.start_search_thread_2)
        self.search_2_btn.clicked.connect(lambda: self.save_item_2())
        self.search_3_btn.clicked.connect(self.start_search_thread_3)
        self.search_3_btn.clicked.connect(lambda: self.save_item_3())
        self.search_4_btn.clicked.connect(self.start_search_thread_4)
        self.search_4_btn.clicked.connect(lambda: self.save_item_4())
        self.search_5_btn.clicked.connect(self.start_search_thread_5)
        self.search_5_btn.clicked.connect(lambda: self.save_item_5())
        self.search_6_btn.clicked.connect(self.start_search_thread_6)
        self.search_6_btn.clicked.connect(lambda: self.save_item_6())
        self.search_7_btn.clicked.connect(self.start_search_thread_7)
        self.search_7_btn.clicked.connect(lambda: self.save_item_7())
        self.search_8_btn.clicked.connect(self.start_search_thread_8)
        self.search_8_btn.clicked.connect(lambda: self.save_item_8())
        self.search_9_btn.clicked.connect(self.start_search_thread_9)
        self.search_9_btn.clicked.connect(lambda: self.save_item_9())
        self.search_10_btn.clicked.connect(self.start_search_thread_10)
        self.search_10_btn.clicked.connect(lambda: self.save_item_10())
        self.search_11_btn.clicked.connect(self.start_search_thread_11)
        self.search_11_btn.clicked.connect(lambda: self.save_item_11())
        self.search_12_btn.clicked.connect(self.start_search_thread_12)
        self.search_12_btn.clicked.connect(lambda: self.save_item_12())

    _translate = QtCore.QCoreApplication.translate

    def start_search_thread_1(self):  # does the multi threading stuff(AI generated)
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

        self.thread_10.started.connect(self.worker_10.run)
        self.worker_10.finished.connect(self.thread_10.quit)
        self.worker_10.finished.connect(self.worker_10.deleteLater)
        self.thread_10.finished.connect(self.thread_10.deleteLater)
        self.worker_10.result.connect(self.search_10)

        self.thread_10.start()

    def start_search_thread_11(self):
        self.thread_11 = QtCore.QThread()
        self.worker_11 = SearchWorker(self.item_11.text())

        self.worker_11.moveToThread(self.thread_11)

        self.thread_11.started.connect(self.worker_11.run)
        self.worker_11.finished.connect(self.thread_11.quit)
        self.worker_11.finished.connect(self.worker_11.deleteLater)
        self.thread_11.finished.connect(self.thread_11.deleteLater)
        self.worker_11.result.connect(self.search_11)

        self.thread_11.start()

    def start_search_thread_12(self):
        self.thread_12 = QtCore.QThread()
        self.worker_12 = SearchWorker(self.item_12.text())

        self.worker_12.moveToThread(self.thread_12)

        self.thread_12.started.connect(self.worker_12.run)
        self.worker_12.finished.connect(self.thread_12.quit)
        self.worker_12.finished.connect(self.worker_12.deleteLater)
        self.thread_12.finished.connect(self.thread_12.deleteLater)
        self.worker_12.result.connect(self.search_12)

        self.thread_12.start()

    def save_item_1(self):
        with open("Items/item1.txt", "w", encoding="utf-8") as file:  # Saves the item names from user input into
            file.write(self.item_1.text())  # item_x when search_x_btn is clicked

    def save_item_2(self):
        with open("Items/item2.txt", "w", encoding="utf-8") as file:
            file.write(self.item_2.text())

    def save_item_3(self):
        with open("Items/item3.txt", "w", encoding="utf-8") as file:
            file.write(self.item_3.text())

    def save_item_4(self):
        with open("Items/item4.txt", "w", encoding="utf-8") as file:
            file.write(self.item_4.text())

    def save_item_5(self):
        with open("Items/item5.txt", "w", encoding="utf-8") as file:
            file.write(self.item_5.text())

    def save_item_6(self):
        with open("Items/item6.txt", "w", encoding="utf-8") as file:
            file.write(self.item_6.text())

    def save_item_7(self):
        with open("Items/item7.txt", "w", encoding="utf-8") as file:
            file.write(self.item_7.text())

    def save_item_8(self):
        with open("Items/item8.txt", "w", encoding="utf-8") as file:
            file.write(self.item_8.text())

    def save_item_9(self):
        with open("Items/item9.txt", "w", encoding="utf-8") as file:
            file.write(self.item_9.text())

    def save_item_10(self):
        with open("Items/item10.txt", "w", encoding="utf-8") as file:
            file.write(self.item_10.text())

    def save_item_11(self):
        with open("Items/item11.txt", "w", encoding="utf-8") as file:
            file.write(self.item_11.text())

    def save_item_12(self):
        with open("Items/item12.txt", "w", encoding="utf-8") as file:
            file.write(self.item_12.text())

    def search_1(self, result):  # Displays the results taken from result
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(6):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            self.item_1.setText(_translate("MainWindow", "This item does not exist"))

    def search_2(self, result):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(6, 12):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            self.item_2.setText(_translate("MainWindow", "This item does not exist"))

    def search_3(self, result):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(12, 18):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            self.item_3.setText(_translate("MainWindow", "This item does not exist"))

    def search_4(self, result):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(18, 24):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            self.item_4.setText(_translate("MainWindow", "This item does not exist"))

    def search_5(self, result):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(24, 30):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            self.item_5.setText(_translate("MainWindow", "This item does not exist"))

    def search_6(self, result):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(30, 36):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            self.item_6.setText(_translate("MainWindow", "This item does not exist"))

    def search_7(self, result):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(36, 42):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            self.item_7.setText(_translate("MainWindow", "This item does not exist"))

    def search_8(self, result):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(42, 48):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            self.item_8.setText(_translate("MainWindow", "This item does not exist"))

    def search_9(self, result):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(48, 54):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            self.item_9.setText(_translate("MainWindow", "This item does not exist"))

    def search_10(self, result):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(54, 59):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            self.item_10.setText(_translate("MainWindow", "This item does not exist"))

    def search_11(self, result):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(59, 64):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            self.item_11.setText(_translate("MainWindow", "This item does not exist"))

    def search_12(self, result):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            self.setWindowTitle(_translate("MainWindow", "Yo"))
            for i in range(64, 69):  # Note: Adjust as needed based on the total result length.
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            self.item_12.setText(_translate("MainWindow", "This item does not exist"))


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


def mainn():  # sets up the PyQt5 application
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":  # start the PyQt5 application
    mainn()