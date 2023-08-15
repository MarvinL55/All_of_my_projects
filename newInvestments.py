import json

import oandapyV20
from oandapyV20 import API
import numpy as np
import oandapyV20.endpoints.instruments as instruments
from oandapyV20.endpoints.orders import OrderCreate
import time
import requests

# Configuration
access_token = "7f1245290cd345cade28c3d8e4e4461e-80bec9d21b72231d8efbe608129efc7f"
account_id = "101-001-26305659-001"
instrument = "EUR_USD"
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 1.0
exploration_decay = 0.9

# Initialize API
api = API(access_token=access_token)

# Fetch historic data
def fetch_historic_data(count, granularity):
    params = {
        "count": count,
        "granularity": granularity,
        "price": "M"
    }
    r = instruments.InstrumentsCandles(instrument, params=params)

    while True:
        try:
            data = api.request(r)['candles']
            break
        except requests.exceptions.ConnectionError as e:
            print("Connection error occurred:", e)
            time.sleep(5)  # Wait for 5 seconds before retrying
    return data

# Calculate Simple Moving Average (SMA)
def calculate_sma(data, period):
    if len(data) < period:
        return None
    sma_prices = [float(candle['mid']['c']) for candle in data[-period:]]
    sma = sum(sma_prices) / period
    return sma

# Calculate Relative Strength Index (RSI)
def calculate_rsi(data, period):
    if len(data) < period + 1:
        return None
    prices = [float(candle['mid']['c']) for candle in data]
    changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
    gains = [change for change in changes if change > 0]
    losses = [change for change in changes if change < 0]
    avg_gain = sum(gains[:period]) / period
    avg_loss = abs(sum(losses[:period])) / period
    for i in range(period, len(gains)):
        if i < len(losses):
            avg_gain = ((avg_gain * (period - 1)) + gains[i]) / period
            avg_loss = ((avg_loss * (period - 1)) + abs(losses[i])) / period
        else:
            break
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Calculate additional indicators or features
def calculate_additional_indicators(data):
    # Calculate additional indicators or features
    # Placeholder values for demonstration purposes

    # Volume indicator
    volume = [float(candle['volume']) for candle in data]
    average_volume = sum(volume) / len(volume)

    # Volatility indicator
    close_prices = [float(candle['mid']['c']) for candle in data]
    volatility = np.std(close_prices)

    # Trend indicator
    sma_50 = calculate_sma(data, 50)
    if sma_50 is None:
        trend_indicator = 0
    else:
        trend_indicator = 1 if close_prices[-1] > sma_50 else -1

    # Oscillator
    rsi_14 = calculate_rsi(data, 14)
    oscillator = 0
    if rsi_14 is not None:
        oscillator = 1 if rsi_14 > 70 else -1

    # Support and resistance levels
    support_level = 1.20
    resistance_level = 1.25

    # Candlestick patterns
    candlestick_patterns = {
        "engulfing": False,
        "doji": True,
        "hammer": False
    }

    additional_indicators = {
        "volume": average_volume,
        "volatility": volatility,
        "trend": trend_indicator,
        "oscillator": oscillator,
        "support_resistance": (support_level, resistance_level),
        "candlestick_patterns": tuple(candlestick_patterns.items())
    }

    return additional_indicators


def get_state(data, index):
    current_price = float(data[index]["mid"]["c"])
    if len(data) < 20:
        return (current_price, 0, 0, {})  # Convert to tuple
    else:
        sma_20 = calculate_sma(data[:index + 1], 20)
        rsi_14 = calculate_rsi(data[:index + 1], 14)
        additional_indicators = calculate_additional_indicators(data[:index + 1])
        state = (current_price, sma_20, rsi_14, additional_indicators)  # Convert to tuple
        return state


# Choose an action based on the current state
def choose_action(state, exploration_rate):
    state_tuple = tuple(state)  # Convert state to tuple

    if np.random.uniform(0, 1) < exploration_rate:
        action = np.random.randint(0, 2)  # 2 actions: 0 = buy, 1 = sell
    else:
        state_key = (state_tuple[:-1], tuple(state_tuple[-1].items()))
        if state_key in Q:
            max_q_value = max(Q[state_key].values())
            actions_with_max_q = [a for a, q_value in Q[state_key].items() if q_value == max_q_value]
            action = np.random.choice(actions_with_max_q)
        else:
            action = np.random.randint(0, 2)

    return action

def execute_action(action, current_price):
    global entry_price
    if action == 0:
        # Buy order
        buy_order = {
            "order": {
                "units": "1000",
                "instrument": instrument,
                "type": "MARKET",
                "positionFill": "DEFAULT"
            }
        }
        buy_order_payload = json.dumps(buy_order)  # Convert to JSON payload
        print("Buy order payload:", buy_order_payload)
        r = OrderCreate(accountID=account_id, data=buy_order_payload)
        response = api.request(r)
        print("Buy order response:", response)
        if "errorMessage" in response:
            print("Buy order error message:", response["errorMessage"])
        print("Buy order executed.")
        entry_price = current_price
    elif action == 1:
        # Sell order
        sell_order = {
            "order": {
                "units": "-1000",
                "instrument": instrument,
                "type": "MARKET",
                "positionFill": "DEFAULT"
            }
        }
        sell_order_payload = json.dumps(sell_order)  # Convert to JSON payload
        print("Sell order payload:", sell_order_payload)
        r = OrderCreate(accountID=account_id, data=sell_order_payload)
        response = api.request(r)
        print("Sell order response:", response)
        if "errorMessage" in response:
            print("Sell order error message:", response["errorMessage"])
        print("Sell order executed.")
        entry_price = None



def update_q_value(previous_state, previous_action, state, immediate_reward):
    if previous_state is not None and previous_action is not None:
        previous_state_tuple = tuple(previous_state)  # Convert previous_state to tuple
        if previous_state_tuple not in Q:
            Q[previous_state_tuple] = {0: 0, 1: 0}
        max_q_value = max(Q[state].values()) if state is not None and state in Q else 0
        previous_q_value = Q[previous_state_tuple][previous_action]
        updated_q_value = (
            previous_q_value
            + learning_rate * (immediate_reward + discount_factor * max_q_value - previous_q_value)
        )
        Q[previous_state_tuple][previous_action] = updated_q_value


# Close a trade based on stop loss or take profit
def close_trade(stop_loss_price, take_profit_price, current_price):
    global entry_price
    if current_price <= stop_loss_price:
        # Close trade with stop loss
        sell_order = {
            "order": {
                "units": "-1000",
                "instrument": instrument,
                "type": "MARKET",
                "positionFill": "DEFAULT"
            }
        }
        r = OrderCreate(accountID=account_id, data=sell_order)
        api.request(r)
        print("Trade closed with stop loss.")
        # Update Q-value for the previous state and action
        previous_state = get_state(data, -2)
        update_q_value(previous_state, previous_action, None, -1)  # Immediate reward for stop loss
        reset_trade()

    elif current_price >= take_profit_price:
        # Close trade with take profit
        sell_order = {
            "order": {
                "units": "-1000",
                "instrument": instrument,
                "type": "MARKET",
                "positionFill": "DEFAULT"
            }
        }
        r = OrderCreate(accountID=account_id, data=sell_order)
        api.request(r)
        print("Trade closed with take profit.")
        # Update Q-value for the previous state and action
        previous_state = get_state(data, -2)
        update_q_value(previous_state, previous_action, None, 1)  # Immediate reward for take profit
        reset_trade()

# Reset trade-related variables
def reset_trade():
    global entry_price, stop_loss_price, take_profit_price
    entry_price = None
    stop_loss_price = None
    take_profit_price = None

# Initialize Q-table
Q = {}

# Trading parameters
risk_percentage = 10  # Increase the risk percentage for more aggressive trading
risk_reward_ratio = 5  # Increase the risk/reward ratio for larger returns

# Global variables
entry_price = None
stop_loss_price = None
take_profit_price = None
previous_action = None

# Start the trading algorithm
while True:
    try:
        # Fetch historic data
        data = fetch_historic_data(21, "M15")

        # Get the current state
        current_index = len(data) - 1
        current_state = get_state(data, current_index)

        # Choose an action
        current_exploration_rate = exploration_rate * exploration_decay ** current_index
        action = choose_action(current_state, current_exploration_rate)

        # Execute the action
        if entry_price is None:
            execute_action(action, current_state[0])
            previous_action = action
        else:
            current_price = current_state[0]
            if previous_action == 0:
                stop_loss_price = entry_price - (entry_price * risk_percentage / 100)
                take_profit_price = entry_price + (entry_price * risk_percentage / 100 * risk_reward_ratio)
                close_trade(stop_loss_price, take_profit_price, current_price)
            elif previous_action == 1:
                stop_loss_price = entry_price + (entry_price * risk_percentage / 100)
                take_profit_price = entry_price - (entry_price * risk_percentage / 100 * risk_reward_ratio)
                close_trade(stop_loss_price, take_profit_price, current_price)
            execute_action(action, current_price)
            previous_action = action

        # Update Q-values
        if entry_price is not None:
            previous_state = get_state(data, current_index - 1)
            immediate_reward = 0
            if previous_action == 0:
                immediate_reward = current_state[0] - entry_price
            elif previous_action == 1:
                immediate_reward = entry_price - current_state[0]
            update_q_value(previous_state, previous_action, current_state, immediate_reward)

        # Wait for the next candle
        time.sleep(180)  # Sleep for 3 minutes
    except Exception as e:
        # Handle other exceptions
        print("An error occurred:", e)
        time.sleep(5)  # Wait for 5 seconds before retrying