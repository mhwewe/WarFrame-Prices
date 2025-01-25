import time
from Api_Orders import Orders

def main(item_link, arcane):
    n = 0;c=0;prices = []; names = []; name_price = []; price_name = []; lis = []

    l = Orders(item_link)
    i = len(l) - 1

    while n <= len(l)-1:
        c = c + 1
        try:
            if ((l[len(l)-c]['order_type']) == 'sell') and (l[len(l)-c]['user']['status'] == 'ingame') and ((l[len(l)-c])['mod_rank'] == 5):
                names.append(l[len(l) - c]['user']['ingame_name'])
                prices.append(l[len(l) - c]['platinum'])
        except Exception:
            pass
        if ((l[len(l)-c]['order_type']) == 'sell') and (l[len(l)-c]['user']['status'] == 'ingame') and (len(l[len(l) - 1]) == 9):
            names.append(l[len(l) - c]['user']['ingame_name'])
            prices.append(l[len(l) - c]['platinum'])

        n = n + 1
        i = i - 1
    for price_name in sorted(zip(prices, names)):
        name_price = (
        price_name[1], f"{price_name[0]} P")
        lis.append(name_price)
    return lis