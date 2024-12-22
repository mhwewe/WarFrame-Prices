import pywmapi as wm
from rich.console import Console
from rich.table import Table
from rich import print
from rich.layout import Layout
from rich.panel import Panel

n=-1; i=0; prices = []; list = []; names = []; lis = []; pri = []; rows = 6; c=0

item1= "Trumna Prime Set"
l = wm.items.get_orders("trumna_prime_set")

while n >= -400:
    if ("OrderType.sell" in str(l[n])) and ("Status.ingame" in str(l[n])):
        Name = str(l[n]).split("ingame_name='")
        Name = Name[1].split("', avatar"); name = Name[0]
        names.append(name)

        Price = str(l[n]).split("platinum=")
        Price = Price[1].split(', quantit'); price = int(Price[0])
        prices.append(price)
        c+=1
    n = n - 1
if rows>c:
    rows = c
i=0; li=[]
for price_name in sorted(zip(prices, names)):
    name_price = (price_name[1], f"{price_name[0]} P", f"/w {price_name[1]} Yo I want the {item1} for {price_name[0]} Plat")
    lis.append(name_price)
    i = i + 1
    if i == rows: break
t=0
console = Console()

table = Table(title=item1,show_header=True, header_style="bold blue")

table.add_column("UserNames",justify="left", min_width=20, max_width=30)
table.add_column("Platinum", justify="center", min_width=2, max_width=10)
#table.add_column("Buy", min_width=5, max_width=70)

while t<rows:
    table.add_row(lis[t][0],
                  lis[t][1],
                  #lis[t][2]
                  )
    t += 1
table1 = table

n=-1; i=0; prices = []; list = []; names = []; lis = []; pri = []; rows = 6; c=0

item1= "Quassus Prime Set"
l = wm.items.get_orders("quassus_prime_set")

while n >= -300:
    if ("OrderType.sell" in str(l[n])) and ("Status.ingame" in str(l[n])):
        Name = str(l[n]).split("ingame_name='")
        Name = Name[1].split("', avatar"); name = Name[0]
        names.append(name)

        Price = str(l[n]).split("platinum=")
        Price = Price[1].split(', quantit'); price = int(Price[0])
        prices.append(price)
        c += 1
    n = n - 1
if rows>c:
    rows = c
i=0; li=[]
for price_name in sorted(zip(prices, names)):
    name_price = (price_name[1], f"{price_name[0]} P", f"/w {price_name[1]} Yo I want the {item1} for {price_name[0]} Plat")
    lis.append(name_price)
    i = i + 1
    if i == rows: break
t=0
console = Console()

table = Table(title=item1,show_header=True, header_style="bold blue")

table.add_column("UserNames",justify="left", min_width=20, max_width=30)
table.add_column("Platinum", justify="center", min_width=2, max_width=10)
#table.add_column("Buy", min_width=5, max_width=70)

while t<rows:
    table.add_row(lis[t][0],
                  lis[t][1],
                  #lis[t][2]
                  )
    t += 1

table2= table


n=-1; i=0; prices = []; list = []; names = []; lis = []; pri = []; rows = 6; c=0

item1= "Sybaris Prime Set"
l = wm.items.get_orders("sybaris_prime_set")

while n >= -300:
    if ("OrderType.sell" in str(l[n])) and ("Status.ingame" in str(l[n])):
        Name = str(l[n]).split("ingame_name='")
        Name = Name[1].split("', avatar"); name = Name[0]
        names.append(name)

        Price = str(l[n]).split("platinum=")
        Price = Price[1].split(', quantit'); price = int(Price[0])
        prices.append(price)
        c += 1
    n = n - 1
if rows>c:
    rows = c
i=0; li=[]
for price_name in sorted(zip(prices, names)):
    name_price = (price_name[1], f"{price_name[0]} P", f"/w {price_name[1]} Yo I want the {item1} for {price_name[0]} Plat")
    lis.append(name_price)
    i = i + 1
    if i == rows: break
t=0
console = Console()

table = Table(title=item1,show_header=True, header_style="bold blue")

table.add_column("UserNames",justify="left", min_width=20, max_width=30)
table.add_column("Platinum", justify="center", min_width=2, max_width=10)
#table.add_column("Buy", min_width=5, max_width=70)

while t<rows:
    table.add_row(lis[t][0],
                  lis[t][1],
                  #lis[t][2]
                  )
    t += 1

table3= table


n=-1; i=0; prices = []; list = []; names = []; lis = []; pri = []; rows = 6; c=0

item1= "Xaku Prime Set"
l = wm.items.get_orders("xaku_prime_set")

while n >= -300:
    if ("OrderType.sell" in str(l[n])) and ("Status.ingame" in str(l[n])):
        Name = str(l[n]).split("ingame_name='")
        Name = Name[1].split("', avatar"); name = Name[0]
        names.append(name)

        Price = str(l[n]).split("platinum=")
        Price = Price[1].split(', quantit'); price = int(Price[0])
        prices.append(price)
        c += 1
    n = n - 1
if rows>c:
    rows = c
i=0; li=[]
for price_name in sorted(zip(prices, names)):
    name_price = (price_name[1], f"{price_name[0]} P", f"/w {price_name[1]} Yo I want the {item1} for {price_name[0]} Plat")
    lis.append(name_price)
    i = i + 1
    if i == rows: break
t=0
console = Console()

table = Table(title=item1,show_header=True, header_style="bold blue")

table.add_column("UserNames",justify="left", min_width=20, max_width=30)
table.add_column("Platinum", justify="center", min_width=2, max_width=10)
#table.add_column("Buy", min_width=5, max_width=70)

while t<rows:
    table.add_row(lis[t][0],
                  lis[t][1],
                  #lis[t][2]
                  )
    t += 1

table4= table

layout = Layout(table)
layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)

layout["upper"].split_row(
    Layout(table1, name="lay1"),
    Layout(table2, name="lay2"),
)
layout["lower"].split_row(
    Layout(table3, name="lay3"),
    Layout(table4, name="lay4")
)

console.print(layout)