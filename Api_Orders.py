import requests

def Orders(item_link):
    base_url = "https://api.warframe.market/v1/items/"
    url = f"{base_url}{item_link}/orders"

    response = requests.get(url)
    raw = response.json()
    orders = raw['payload']['orders']
    return orders

# new = Orders('trumna_prime_set')
# print(new[len(new)-1]['user']['ingame_name'])
# print(orders[len(orders)-1]['user']['ingame_name'])