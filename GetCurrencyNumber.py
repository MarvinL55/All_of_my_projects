import json
import requests

key = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"

currencies = ["BITCOIN", "ETHEREUM", "MONERO"]

j = 0

price=["USD"]

for i in currencies:

    url = key+currencies[j]
    data = requests.get(url)
    data = data.json()
    j = j+1

    print(f"price is " + str(price))
