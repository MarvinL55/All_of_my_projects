from alpaca_trade_api import REST

# Replace '<your API key>' and '<your secret key>' with your own keys
api = REST('PK13JVVMCAC41ALYG1N3', '6yp2s2Zn7MlxH7NV6hkqA6TmH1PkNpWMc6WuPtme', api_version='v2')

# Call the `get_account` method to retrieve your account information
account = api.get_account()

# Check if the account is authorized for trading
if account.trading_blocked:
    print('Account is not authorized for trading')
else:
    print('Account is authorized for trading')
