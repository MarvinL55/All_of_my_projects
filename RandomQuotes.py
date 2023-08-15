import random
import json

import requests
import responses

print("Here are some random quotes")

response = requests.get("https://quotes.toscrape.com/api/quotes")
quotes = response.json()

random_quote = random.choice(quotes["quotes"])
quotes_text = random_quote["text"]

print(quotes_text)