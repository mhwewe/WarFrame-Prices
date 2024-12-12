import pywmapi as wm

def main(item_link, arcane):
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


# threading.Thread(target= main, args=("item1","trumna_prime_set", False)).start()
# threading.Thread(target= main, args=("ma2","quassus_prime_set", False)).start()
# threading.Thread(target= main, args=("ma2","quassus_prime_set", False)).start()
# threading.Thread(target= main, args=("ma2","quassus_prime_set", False)).start()
# threading.Thread(target= main, args=("ma2","quassus_prime_set", False)).start()
# threading.Thread(target= main, args=("ma2","quassus_prime_set", False)).start()
# threading.Thread(target= main, args=("ma2","quassus_prime_set", False)).start()
# threading.Thread(target= main, args=("ma2","quassus_prime_set", False)).start()
# threading.Thread(target= main, args=("ma2","quassus_prime_set", False)).start()
# threading.Thread(target= main, args=("ma2","quassus_prime_set", False)).start()
# threading.Thread(target= main, args=("ma2","quassus_prime_set", False)).start()
# threading.Thread(target= main, args=("ma2","quassus_prime_set", False)).start()
#

