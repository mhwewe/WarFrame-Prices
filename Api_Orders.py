import requests
import json

def Orders(item_link):
    base_url = "https://api.warframe.market/v1/items/"
    if " " in item_link:
        item_link = item_link.replace(" ", "_")
        url = f"{base_url}{item_link}/orders"
    else:
        item_link = f"{item_link}_prime_set"
        url = f"{base_url}{item_link}/orders"

    response = requests.get(url)
    raw = response.json()
    orders = raw['payload']['orders']
    return orders

def get_item_names():
    response = requests.get("https://api.warframe.market/v1/items")
    raw = response.json()
    return raw

def game_items_dict_func():
    raw = get_item_names()
    length = len(raw['payload']['items'])
    list = []
    for i in range(0,length):
        item_name = raw['payload']['items'][i]['url_name']
        if "_prime_set" in item_name:
            item_name = item_name.split("_prime_set")
            item_name = item_name[0]
        elif "_" in item_name:
            item_name = item_name.replace("_", " ")
        list.append(item_name)
    with open("game_items.json", "w") as f:
        json.dump(list, f)

# with open('game_items.json') as um:
#     game_items_dictt = json.load(um)
# new = Orders('trumna_prime_set')
# print(new[len(new)-1]['user']['ingame_name'])
# print(orders[len(orders)-1]['user']['ingame_name'])