import requests
from Api_Orders import Orders

def main(item_link, arcane):
    n = 0;prices = [];names = [];lis = [];rows = 100;c = 0

    l = Orders(item_link)
    print(l[len(l)-1])

    while n <= len(l):
        print('y')
        if (("order_type" == 'sell') in l) and (("status" == 'ingame') in l) and (('mod_rank' == '5') in l):
            print("yo")
            Name = str(l[n]).split("ingame_name='")
            Name = Name[1].split("', avatar")
            name = Name[0]
            names.append(name)

            Price = str(l[n]).split("platinum=")
            Price = Price[1].split(', quantit')
            price = int(Price[0])
            prices.append(price)
            c += 1
        if (("order_type" == 'sell') in l) and (("status" == 'ingame') in l):
            Name = str(l[n]).split("ingame_name='")
            Name = Name[1].split("', avatar")
            name = Name[0]
            names.append(name)

            Price = str(l[n]).split("platinum=")
            Price = Price[1].split(', quantit')
            price = int(Price[0])
            prices.append(price)
            c += 1
        n = n + 1
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


test = main("arcane_energize", True)