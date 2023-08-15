import ccxt

# Initialize the Binance exchange object
exchange = ccxt.binance()

# Get the ticker for the BTC/USDT trading pair
ticker = exchange.fetch_ticker('BTC/USDT')

# Print the ticker data
print(ticker)
