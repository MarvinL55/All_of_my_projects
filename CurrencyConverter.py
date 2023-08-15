import requests

class Currency_convertor:

    rates = { }
    def __init__(self, url):
        data = requests.get(url).json()

        self.rates = data["rates"]

    def convert(self, from_currency, to_currency, amount):
        intial_amount = amount
        if from_currency != "EUR":
            amount = amount/ self.rates[from_currency]

        amount = round(amount * self.rates[to_currency], 2)
        print("{} {} = {} {}".format(intial_amount, from_currency, amount,to_currency))

if __name__ == "__main__":

    url = str.__add__("https://www.coinbase.com/settings/api", YOUR_ACCESS_KEY="eOJN8AEfUpV9u2ot")
    c = Currency_convertor(url)
    from_country = input("From Country: ")
    to_country = input("To Country: ")
    amount = int(input("Amount: "))

    c.convert(from_country, to_country, amount)

