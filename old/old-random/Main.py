import pywmapi as wm
from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.console import ConsoleDimensions
from tkinter import *

def main(item_name, item_link, arcane):
    n = -1;prices = [];names = [];lis = [];rows = 6;c = 0

    item1 = item_name
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
        price_name[1], f"{price_name[0]} P", f"/w {price_name[1]} Yo I want the {item1} for {price_name[0]} Plat")
        lis.append(name_price)
        i = i + 1
        if i == rows: break
    t = 0

    table = Table(title=item1, show_header=True, header_style="bold blue")

    table.add_column("UserNames", justify="left", min_width=20, max_width=30)
    table.add_column("Platinum", justify="center", min_width=2, max_width=10)
    # table.add_column("Buy", min_width=5, max_width=70)

    while t < rows:
        table.add_row(lis[t][0],
                      lis[t][1],
                      # lis[t][2]
                      )
        t += 1
    return table


table1 = main("trumna_prime_set", "trumna_prime_set", arcane=False)
table2 = main("Quassus Prime Set", "quassus_prime_set", arcane=False)
table3 = main("Xaku Prime Set", "xaku_prime_set", arcane=False)
table4 = main("Sybaris Prime Set", "sybaris_prime_set", arcane=False)
table5 = main("Arcane Energize", "arcane_energize", arcane=True)
table6 = main("Khora Prime Set", "khora_prime_set", arcane=False)

layout = Layout(table1)
layout.split_column(
    Layout(name="upper"),
    Layout(name="lower"),
    Layout(name="lowerer"),
    Layout(name="lowererer")
)

layout["upper"].split_row(
    Layout(table1, name="lay1"),
    Layout(table2, name="lay2"),
)
layout["lower"].split_row(
    Layout(table3, name="lay3"),
    Layout(table4, name="lay4")
)
layout["lowerer"].split_row(
    Layout(table5, name="lay5"),
    Layout(table6, name="lay6")
)

console = Console()

console.size = ConsoleDimensions(width=console.size.width, height=45)

window = Tk() #make a window?

photo = PhotoImage(file="Warframe market logo crop.png")

window.geometry("800x800")
window.config(background="#101619")
window.title("WarFrame Market")

logo = PhotoImage(file="Warframe market logo crop.png")
window.iconphoto(True, logo)

label = Label(window,
              text=table1,
              font=('Arial', 20, 'bold'),
              image=photo,
              compound="bottom",
              fg='#3c879c',
              bg='#101619')

label.place(x=0,y=0)

window.mainloop() # place window on computer screen, listen for event
console.print(layout)