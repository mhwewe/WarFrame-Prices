import pywmapi as wm

from PyQt5.QtCore import QThread, pyqtSignal



class WorkerThread(QThread):
    result = pyqtSignal(list)

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
            if ("OrderType.sell" in str(l[n])) and ("Status.ingame" in str(l[n])) and self.arcane is True and (
                    "mod_rank=5" in str(l[n])):
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
        i = 0;
        li = []
        for price_name in sorted(zip(prices, names)):
            name_price = (
                price_name[1], f"{price_name[0]} P")
            lis.append(name_price)
            i = i + 1
            if i == rows: break
        self.result.emit(lis)


def start_fetch(self):
    # Example parameters
    item_link = "some-item-link"
    arcane = True

    # Initialize WorkerThread
    self.thread = WorkerThread(item_link, arcane)
    self.thread.result.connect(item1)  # Connect signal to slot
    self.thread.start()  # Start the thread


WorkerThread("trumna_prime_handle", arcane=False)
print(item1)