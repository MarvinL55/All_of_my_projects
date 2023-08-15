import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.orders as orders
import pandas as pd
import datetime
import time

# Define the maximum amount of capital to risk on each trade
from oandapyV20 import oandapyV20

max_risk_pct = 0.01  # Risk only 1% of capital each trade

# Set up the Oanda API client
client = oandapyV20.API(access_token="f20c1c004915fc395c77fd9ba7ea17b6-ab6a49d29a56625776c5d05a5077080b", environment="practice")

# Define the trading strategy
def trading_strategy():
    # Retrieve the last stock data
    params = {
        "instruments": "EUR_USD",
        "count": 100,
        "granularity": "M5"
    }
    r = pricing.PricingInfo(accountID="101-001-25450693-001", params=params)
    response = client.request(r)
    prices = response["prices"]

    stock_price = [float(price["bids"][0]["price"]) for price in prices]

    # Calculate the 20 period moving average
    moving_avg = pd.Series(stock_price).rolling(3).mean()

    # Check if the current price is above the moving average
    if stock_price[-1] > moving_avg.iloc[-1]:
        # Get the account summary
        r = accounts.AccountSummary(accountID="101-001-25450693-001")
        response = client.request(r)
        buying_power = float(response["account"]["balance"])

        # Calculate the maximum amount of capital to risk on each trade
        max_risk_capital = buying_power * max_risk_pct

        # Calculate the maximum number of shares to buy based on the maximum risk capital
        stock_price = float(prices[-1]["bids"][0]["price"])
        max_shares = int(max_risk_capital / stock_price)

        # Place a buy order for the maximum number of shares
        data = {
            "order": {
                "instrument": "EUR_USD",
                "units": max_shares,
                "type": "MARKET",
                "timeInForce": "FOK",
                "positionFill": "DEFAULT"
            }
        }
        r = orders.OrderCreate(accountID="101-001-25450693-001", data=data)
        response = client.request(r)
        if response["orderFillTransaction"]["id"]:
            print("Order placed successfully")
        else:
            print("Order placement failed")

# Run the trading strategy every minute
while True:
    # Get the current time
    now = datetime.datetime.now()

    # Run the trading strategy
    print("Running...")
    try:
        trading_strategy()
    except Exception as e:
        print("Error:", e)

    # Wait for 60 seconds before running the strategy again
    time.sleep(60)
