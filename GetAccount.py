import requests

# Set your API token and account type
API_TOKEN = 'a2af7f7015402d0c63479e5d47429ed2-31c9114e1b496f6ea24b877452c1e20d'
ACCOUNT_TYPE = 'practice'

# Set the API endpoint URL
endpoint = f"https://api-fx{ACCOUNT_TYPE}.oanda.com/v3/accounts"

# Send the request with the API token
response = requests.get(endpoint, headers={"Authorization": f"Bearer {API_TOKEN}"})

# Retrieve the account ID from the response
account_id = response.json()['accounts'][0]['id']
print("Account ID:", account_id)
