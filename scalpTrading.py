from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.trades as trades
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import time
import numpy as np

accountID = "101-001-26225033-001"
access_token = "a2af7f7015402d0c63479e5d47429ed2-31c9114e1b496f6ea24b877452c1e20d"
api = API(access_token=access_token)

# Define the instrument you want to trade
instrument = "EUR_USD"

# Scalping profits
take_profit = 10  # Take profit price
stop_loss = 5  # Stop loss pips
trade_size = 1000  # Trade size

# Getting historical data
training_params = {
    "count": 100,  # Number of candlesticks for training
    "granularity": "M1"  # Granularity (e.g., M1 for 1-minute candles)
}

# Infinite loop for continuous trading
while True:
    # Get historical data for training
    r = instruments.InstrumentsCandles(instrument=instrument, params=training_params)
    api.request(r)
    training_data = r.response["candles"]

    # Extract features and labels from historical market data
    features = []
    labels = []

    for i in range(len(training_data) - 1):
        current_candle = training_data[i]
        next_candle = training_data[i + 1]

        # Calculate the price difference
        price_difference = float(next_candle["mid"]["c"]) - float(current_candle["mid"]["c"])

        # Assign labels based on the price difference
        if price_difference > 0:
            labels.append(1)
        else:
            labels.append(0)

        feature = [
            float(current_candle["mid"]["o"]),
            float(current_candle["mid"]["h"]),
            float(current_candle["mid"]["l"]),
            float(current_candle["mid"]["c"])
        ]
        features.append(feature)

    # Preprocess the features by standardizing the data
    scaler = StandardScaler()
    features = scaler.fit_transform(features)

    # Train a Random Forest classifier
    classifier = RandomForestClassifier()
    classifier.fit(features, labels)

    # Get the latest candle for prediction
    prediction_params = {
        "count": 1,
        "granularity": "M1"
    }

    r = instruments.InstrumentsCandles(instrument=instrument, params=prediction_params)
    api.request(r)
    latest_candle = r.response["candles"][0]

    # Extract features from the latest candle for prediction
    latest_feature = [
        float(latest_candle["mid"]["o"]),
        float(latest_candle["mid"]["h"]),
        float(latest_candle["mid"]["l"]),
        float(latest_candle["mid"]["c"])
    ]

    # Preprocess the latest feature
    latest_feature = scaler.transform([latest_feature])

    # Make a prediction
    prediction = classifier.predict(latest_feature)[0]

    # Place a scalp trade based on the prediction
    if prediction == 1:
        take_profit_price = round(float(latest_candle["mid"]["c"]) + (take_profit * 0.0001), 5)
        stop_loss_price = round(float(latest_candle["mid"]["o"]) - (stop_loss * 0.0001), 5)
        side = "BUY"
    else:
        take_profit_price = round(float(latest_candle["mid"]["c"]) - (take_profit * 0.0001), 5)
        stop_loss_price = round(float(latest_candle["mid"]["c"]) + (stop_loss * 0.0001), 5)
        side = "SELL"

    # Check if there are any open trades
    r = trades.TradesList(accountID=accountID)
    api.request(r)
    open_trades = r.response["trades"]

    if open_trades:
        # Close the oldest open position first
        trade_to_close = open_trades[0]
        trade_id = trade_to_close["id"]

        data = {
            "tradeID": trade_id
        }

        r = trades.TradeClose(accountID=accountID, tradeID=trade_id, data=data)
        api.request(r)
        print("Closed trade:", r.response)

    if prediction == 1:
        data = {
            "order": {
                "instrument": instrument,
                "units": str(trade_size),
                "type": "MARKET",
                "positionFill": "DEFAULT",
                "stopLossOnFill": {
                    "price": str(stop_loss_price)
                },
                "takeProfitOnFill": {
                    "price": str(take_profit_price)
                },
                "side": side
            }
        }

        r = orders.OrderCreate(accountID=accountID, data=data)
        api.request(r)
        print(r.response)

        # Check if the order was filled immediately
        if 'orderFillTransaction' in r.response:
            # Evaluate trade performance and adjust the model
            trade_result = r.response['orderFillTransaction']['tradeOpened']['tradeID']

            r = trades.TradeDetails(accountID=accountID, tradeID=trade_result)
            api.request(r)

            trade_profit_loss = float(r.response['trade']['unrealizedPL'])
            if trade_profit_loss > 0:
                # Trade was profitable, consider it a correct prediction
                labels.append(prediction)
                features = features.tolist()
                features.append(latest_feature[0])
                print("Scalp trade successful!")
            else:
                # Trade was unprofitable, consider it a wrong prediction
                labels.append(1 - prediction)
                features = features.tolist()
                features.append(latest_feature[0])

            # Retrain the classifier with updated data
            classifier.fit(features, labels)
        else:
            print("Scalp trade order not filled immediately.")
    else:
        print("No scalp trade opportunity.")

    # Sleep for a certain duration (e.g., 60 seconds) before the next iteration
    time.sleep(60)
