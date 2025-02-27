import sys
import json
import time
import webbrowser
import requests
from PyQt5.QtGui import QPalette, QColor, QFont, QMovie, QCursor
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QApplication, QGraphicsDropShadowEffect, QListView, \
    QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QSizeGrip
from PyQt5.QtWidgets import QMainWindow, QGraphicsBlurEffect, QFrame, QDialog, QCompleter
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QEvent, QTimer, QStringListModel
from Resources import NewUITest_rc
from make_search_thread import make_search_thread, SearchWorker
from Api_Orders import game_items_dict_func
from functools import partial


class CustomListView(QListView):  # This class removes the scroll bar from the QCompleter popup and also sets the width
    def __init__(self, parent=None):
        super(CustomListView, self).__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFixedWidth(300)
        self.setFixedHeight(int(self.height() / 3 + self.height() / 18))

# Stuff for resizing the window - Copied
class SideGrip(QtWidgets.QWidget):
    def __init__(self, parent, edge):
        QtWidgets.QWidget.__init__(self, parent)
        if edge == QtCore.Qt.LeftEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunc = self.resizeLeft
        elif edge == QtCore.Qt.TopEdge:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunc = self.resizeTop
        elif edge == QtCore.Qt.RightEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunc = self.resizeRight
        else:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunc = self.resizeBottom
        self.mousePos = None

    def resizeLeft(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() - delta.x())
        geo = window.geometry()
        geo.setLeft(geo.right() - width)
        window.setGeometry(geo)

    def resizeTop(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() - delta.y())
        geo = window.geometry()
        geo.setTop(geo.bottom() - height)
        window.setGeometry(geo)

    def resizeRight(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() + delta.x())
        window.resize(width, window.height())

    def resizeBottom(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() + delta.y())
        window.resize(window.width(), height)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mousePos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mousePos is not None:
            delta = event.pos() - self.mousePos
            self.resizeFunc(delta)

    def mouseReleaseEvent(self, event):
        self.mousePos = None


class MainApp(QtWidgets.QWidget):
    _gripSize = 4

    def __init__(self):
        super().__init__()
        # Load the .ui file from the root directory
        uic.loadUi("NewUI.ui", self)
        #window move var
        self.oldPos = self.pos()

        # title bar removal
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Window resize - Copied
        self.sideGrips = [
            SideGrip(self, QtCore.Qt.LeftEdge),
            SideGrip(self, QtCore.Qt.TopEdge),
            SideGrip(self, QtCore.Qt.RightEdge),
            SideGrip(self, QtCore.Qt.BottomEdge),
        ]
        self.cornerGrips = [QtWidgets.QSizeGrip(self) for i in range(4)]

        # Defining the widgets
        self.search_frames = [self.findChild(QFrame, f"search_frame_{i}") for i in range(1, 13)]
        self.gotolink_frames = [self.findChild(QFrame, f"gotolink_frame_{i}") for i in range(1, 13)]
        self.order_frames = [self.findChild(QFrame, f"order_frame_{i}") for i in range(1, 13)]
        self.main_frame = self.findChild(QFrame, f"main_frame")
        self.inputs = [self.findChild(QLineEdit, f"input_{i}") for i in range(1, 13)]  # User Inputs
        self.search_buttons = [self.findChild(QPushButton, f"search_btn_{i}") for i in range(1, 13)]  # Search Buttons
        self.names = [self.findChild(QLabel, f"name_{i}") for i in range(1, 73)]  # Item names
        self.prices = [self.findChild(QLabel, f"price_{i}") for i in range(1, 73)]  # Item Prices
        self.plats = [self.findChild(QLabel, f"plat_icon_{i}") for i in range(1, 73)]
        self.gotolinks = [self.findChild(QPushButton, f"gotolink_btn_{i}") for i in range(1, 13)]  # go to link buttons
        self.close_btn = self.findChild(QPushButton, "close_btn")  # close button
        self.minimize_btn = self.findChild(QPushButton, "minimize_btn")  # minimize button
        self.refresh_btn = self.findChild(QPushButton, "refresh_btn")  # refresh button
        self.order_buttons = [self.findChild(QPushButton, f"order_btn_{i}") for i in range(1, 13)]  # order buttons
        self.detail_frames = [self.findChild(QFrame, f"details_frame_{i}") for i in range(1, 13)]  # Frames that the names and prices frames are in
        self.title_frame = self.findChild(QFrame, "title_frame")
        self.main_frame.setObjectName("main_frame")
        self.main_frame.setStyleSheet("border-bottom-left-radius: 10px;border-bottom-right-radius:10px;border:none;")
        names_css = "QLabel{color: rgba(60, 135, 156, 1);background:transparent;}"
        prices_css = "QLabel{color: rgba(203, 74, 158, 1);background:transparent;}"

        form_css = """
                    QFrame#main_frame {
                        background-image: url(:/newPrefix/background.png);
                        border: none;
                    }
                    """
        frame_background_css = """
                    QFrame {
                        background-color: rgba(7, 16, 19, 191);
                        border-top-left-radius: 5px;
                        border-top-right-radius: 5px;
                        border-bottom-left-radius: 5px;
                        border-bottom-right-radius: 5px;
                        transition: background-color 0.3s ease, box-shadow 0.3s ease;
                    }
                    QFrame:hover {
                        background-color: rgba(135, 135, 135, 1);
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    }
                    """
        input_background_css = """
                    QLineEdit {
                        background-color: rgba(7, 16, 19, 191);
                        border-top-left-radius: 10px;
                        border-top-right-radius: 10px;
                        border-bottom-left-radius: 10px;
                        border-bottom-right-radius: 10px;
                        border: none;
                        color: rgb(255, 255, 255);
                        font: 81 16pt "Lato ExtraBold";
                    }
                    """
        details_frames_css = """
                    QFrame {
                        background-color: rgba(7, 16, 19, 191);
                        border-radius: 10px;
                        font: 87 12pt "Lato Black";
                        color: rgb(255, 255, 255);
                    }
                    """
        disabled_btn_css = "background-color: #f23f43;"

        for i in range(0, 72):
            self.names[i].setStyleSheet(names_css)
            self.prices[i].setStyleSheet(prices_css)
            self.plats[i].setMinimumSize(20, 20)
            self.plats[i].setMaximumSize(30, 30)

        def make_shadow_effect():
            shadow_effect = QGraphicsDropShadowEffect()
            shadow_effect.setBlurRadius(10)  # Blur radius
            shadow_effect.setXOffset(3)  # Horizontal offset
            shadow_effect.setYOffset(3)  # Vertical offset
            shadow_effect.setColor(QColor(0, 0, 0, 120))
            return shadow_effect

        self.main_frame.setStyleSheet(form_css)
        for i in range(0, 12):
            self.search_frames[i].setStyleSheet(frame_background_css)
            self.inputs[i].setStyleSheet(input_background_css)
            self.detail_frames[i].setStyleSheet(details_frames_css)
            self.gotolink_frames[i].setStyleSheet(frame_background_css)
            self.order_frames[i].setStyleSheet(frame_background_css)

            self.detail_frames[i].setGraphicsEffect(make_shadow_effect())
            self.search_frames[i].setGraphicsEffect(make_shadow_effect())
            self.inputs[i].setGraphicsEffect(make_shadow_effect())
            self.gotolink_frames[i].setGraphicsEffect(make_shadow_effect())
            self.order_frames[i].setGraphicsEffect(make_shadow_effect())

        # Connect signals
        self.close_btn.clicked.connect(self.close)  # close button
        self.minimize_btn.clicked.connect(self.showMinimized)  # minimize button
        self.refresh_btn.clicked.connect(self.refresh)  # refresh button

        for i in range(1, 13):
            self.search_buttons[i - 1].clicked.connect(
                getattr(self, f"start_search_thread_{i}"))  # search button connected to result gatherer
            self.search_buttons[i - 1].clicked.connect(
                lambda _, x=i: getattr(self, f"save_item_{x}")())  # search button connected to item memory
            self.search_buttons[i - 1].clicked.connect(
                lambda state, x=i, btn=self.search_buttons[i - 1]: self.disabler(x,
                                                                                 btn))  # search button connected to button disabler

            self.gotolinks[i - 1].clicked.connect(
                getattr(self, f"gotolink{i}"))  # go to link button connected to browser
            with open(f'Items.json') as file:
                content = json.load(file)
                getattr(self, f"input_{i}").setText(self._translate("MainWindow", content[f"item{i}"]))
                getattr(self, f"search_btn_{i}").click()

        # Things for input QCompleter

        popup_style = """
                    QAbstractItemView {
                        background: transparent;
                        color: white;
                        border: 1px solid gray;
                        font: 12.8pt "Lato Medium";
                        padding-left: 5px;
                        padding-top: 11px;
                    }
                """

        with open(f'game_items.json') as file:  # load the names of every trade able game item
            game_items = json.load(file)

        popup = CustomListView()  # applies the effects of the class up the file to the popups
        self.completer_1 = QCompleter(game_items)  # gives QCompleter its completions
        self.completer_1.setPopup(popup)  # set the popup to the QCompleter
        self.completer_1.setMaxVisibleItems(6)  # sets max items...

        popup.setWindowFlags(
            Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)  # frameless nad no drop shadow for the popup box
        popup.setAttribute(Qt.WA_TranslucentBackground)  # translucency

        def blur(i):  # Blur stuff
            for ff in range(0, 12):
                self.detail_frames[ff].setGraphicsEffect(make_shadow_effect())
            self.detail_frames[i].setGraphicsEffect(QGraphicsBlurEffect())
            self.last_input = i  # saves the last input for the Enter key function to know which button to click

        def unblur(i):
            self.detail_frames[i].setGraphicsEffect(make_shadow_effect())

        # Blur behaviour
        for i in range(0, 12):
            self.inputs[i].selectionChanged.connect(partial(blur, i))
            self.inputs[i].editingFinished.connect(partial(unblur, i))

        popup.setStyleSheet(popup_style)  # obvius

        # applies the QCompleters to the QLineEdits
        for i in range(0, 12):
            self.inputs[i].setCompleter(self.completer_1)

    _translate = QtCore.QCoreApplication.translate  # idk

    # Functions

    # function for Enter key
    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.search_buttons[self.last_input].click()

    # disables the button that was pressed
    def disabler(self, i, btn):
        btn.setEnabled(False)
        btn.setStyleSheet("background-color: #f23f43; border-radius: 5;")

    # refresh button
    def refresh(self):
        self.refresh_btn.setEnabled(False)
        for i in range(1, 13):
            getattr(self, f"search_btn_{i}").click()

    # Function for saving last entered item name
    with open('Items.json') as yoo:
        Items_dict = json.load(yoo)

    def save_item(self, item_index, i, test):
        with open('Items.json') as yoo:
            Items_dict = json.load(yoo)
        Items_dict.update({f"item{i}": f"{item_index.text()}"})
        with open("Items.json", "w") as f:
            json.dump(Items_dict, f)

    def get_content(self):
        with open('Items.json') as file:
            content = json.load(file)
        return content

    # search thread stuff
    for i in range(1, 13):
        # Making a search thread for the emitted signal
        exec(
            f"def start_search_thread_{i}(self): self.worker_{i}, self.thread_{i} = make_search_thread(self, self.input_{i}, 'input_{i}', {(i - 1) * 6})")
        exec(f"def search_{i}(self, result): self.search(result, {(i - 1) * 6}, 'input_{i}')")

        content = get_content(None)  # creating and opening the link to the item
        exec(f"def gotolink{i}(self):"
             f"webbrowser.open_new(f'https://warframe.market/items/{content[f'item{i}'].replace(' ', '_')}')")

        exec(f"def save_item_{i}(self): self.save_item(self.input_{i}, {i}, {Items_dict})")

    # stuff for moving the frameless window - copied and modified to only work on the title bar
    def mousePressEvent(self, event):
        mouse_in_window = QCursor.pos().y() - self.y()
        if mouse_in_window < 40 and mouse_in_window > 5:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        mouse_in_window = QCursor.pos().y() - self.y()
        if mouse_in_window < 40 and mouse_in_window > 5:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    # Sets the names and prices in the gui and enables the buttons when the names and prices are set
    def search(self, result, start_index, kwargs):
        _translate = QtCore.QCoreApplication.translate
        try:
            c = 0
            starto = int((start_index) / 6)
            self.search_buttons[starto].setEnabled(True)
            self.search_buttons[starto].setStyleSheet(
                "image: url(:/newPrefix/New/search_gif.gif); border-image: url(:/newPrefix/New/blank.gif);")
            self.refresh_btn.setEnabled(True)  # enables the button
            for i in range(start_index, start_index + 6):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", result[c][0]))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", result[c][1]))
                c += 1
        except Exception:
            for i in range(start_index, start_index + 6):
                getattr(self, f"name_{i + 1}").setText(_translate("MainWindow", "Item does not exist"))
                getattr(self, f"price_{i + 1}").setText(_translate("MainWindow", "Price"))
                c += 1

    # Stuff for resizing the window - Copied
    @property
    def gripSize(self):
        return self._gripSize

    def setGripSize(self, size):
        if size == self._gripSize:
            return
        self._gripSize = max(2, size)
        self.updateGrips()

    def updateGrips(self):
        self.setContentsMargins(*[self.gripSize] * 4)

        outRect = self.rect()
        # an "inner" rect used for reference to set the geometries of size grips
        inRect = outRect.adjusted(self.gripSize, self.gripSize,
                                  -self.gripSize, -self.gripSize)

        # top left
        self.cornerGrips[0].setGeometry(
            QtCore.QRect(outRect.topLeft(), inRect.topLeft()))
        # top right
        self.cornerGrips[1].setGeometry(
            QtCore.QRect(outRect.topRight(), inRect.topRight()).normalized())
        # bottom right
        self.cornerGrips[2].setGeometry(
            QtCore.QRect(inRect.bottomRight(), outRect.bottomRight()))
        # bottom left
        self.cornerGrips[3].setGeometry(
            QtCore.QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())

        # left edge
        self.sideGrips[0].setGeometry(
            0, inRect.top(), self.gripSize, inRect.height())
        # top edge
        self.sideGrips[1].setGeometry(
            inRect.left(), 0, inRect.width(), self.gripSize)
        # right edge
        self.sideGrips[2].setGeometry(
            inRect.left() + inRect.width(),
            inRect.top(), self.gripSize, inRect.height())

            # bottom edge
        self.sideGrips[3].setGeometry(
        self.gripSize, inRect.top() + inRect.height(),
        inRect.width(), self.gripSize)

    def resizeEvent(self, event):
        QtWidgets.QWidget.resizeEvent(self, event)
        self.updateGrips()


def mainn():  # sets up the PyQt5 application
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":  # start the PyQt5 application
    mainn()