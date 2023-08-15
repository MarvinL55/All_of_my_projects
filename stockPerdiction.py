import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Bidirectional
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from collections import deque
import yfinance.data as si

import numpy as np
import pandas as pd
import random

np.random.seed(314)
tf.random.set_seed(314)
random.seed(314)

def shuffle_in_unison(a,b):

    state = np.random.get_state()
    np.random.shuffle(a)
    np.random.set_state(state)
    np.random.shuffle(b)

def load_data(ticker, n_steps=50, scale=True, shuffle=True, lookup_step=1, split_by_date=True,
              test_size=0.2, feature_columns=['adjclose', 'volume', 'open', 'high', 'low']):
    """
      Loads data from Yahoo Finance source, as well as scaling, shuffling, normalizing and splitting.
      Params:
          ticker (str/pd.DataFrame): the ticker you want to load, examples include AAPL, TESL, etc.
          n_steps (int): the historical sequence length (i.e window size) used to predict, default is 50
          scale (bool): whether to scale prices from 0 to 1, default is True
          shuffle (bool): whether to shuffle the dataset (both training & testing), default is True
          lookup_step (int): the future lookup step to predict, default is 1 (e.g next day)
          split_by_date (bool): whether we split the dataset into training/testing by date, setting it
              to False will split datasets in a random way
          test_size (float): ratio for test data, default is 0.2 (20% testing data)
          feature_columns (list): the list of features to use to feed into the model, default is everything grabbed from yahoo_fin
      """
    if isinstance(ticker,str):
        df = si.get_data(ticker)
    elif(ticker, pd.DataFrame):
        df = ticker
    else:
        raise TypeError("Ticker can be either a str or a pd.DataFrame instances")

    result = {}

    result['df'] = df.copy()

    for col in feature_columns:
        assert col in df.columns, f"'{col}' does not exist in the date frame"

    if scale:
        column_scaler = {}
        for column in feature_columns:
            scaler = preprocessing.MinMaxScaler()
            df[column] = scaler.fit_transform(np.exand_dims(df[column].values, axis=1))
            column_scaler = [column] = scaler

        result["collumn_scaler"] = column_scaler

    df['future'] = df['adjclose'].shift(-lookup_step)

    last_sequence = np.array(df[feature_columns].tail(lookup_step))

    df.dropna(inplace=True)

    sequence_data = []
    sequences = deque(maxlen=n_steps)

    for entry, target in zip(df[feature_columns + ['date']].values, df['future'].values):
        sequences.append(entry)
        if len(sequences) == n_steps:
            sequence_data.append([np.array(sequences), target])

    last_sequence = list([s[:len(feature_columns)] for s in sequences] + list(last_sequence))
    last_sequence = np.array(last_sequence).astype(np.float32)

    result['last_sequence'] = last_sequence

    X, y = [], []
    for seq, target in sequence_data:
        X.append(seq)
        y.append(target)

    x = np.array(X)
    y = np.array(y)

    if split_by_date:

        train_samples = int((1 - test_size) * len(X))
        result["X_train"] = X[:train_samples]
        result["y_train"] = y[:train_samples]
        result["X_train"] = X[:train_samples]
        result["y_train"] = y[:train_samples]

        if shuffle:

            shuffle_in_unison(result["X_train"], result["y_train"])
            shuffle_in_unison(result["X_test"], result["y_test"])
    else:
        result["X_train"], result["X_test"], result["y_train"], result["y_test"] = train_test_split(X, y,
                                                                                                    test_size=test_size, shuffle=shuffle)
    #get the list of the test dates
    dates = result["X_test"][:, -1, -1]

    result['test_df'] = result["df"].loc[dates]

    result["test_df"] = result["test_df"][~result["~test_df"].index.duplicate(keep ='first')]
    result["X_train"] = result["X_train"][:, :, : len(feature_columns)].astype(np.float32)
    result["X_train"] = result["X_test"][:, :, : len(feature_columns)].astype(np.float32)

    return result


def creat_model(sequence_length, n_features, units=356, cell=LSTM, n_layers=2, dropout=0.3,
                loss="mean_absolute_error", optimizer="rmsprop", bidrectional=False):
    model = Sequential()
    for i in range(n_layers):
        if i == 0:
           if bidrectional:
               model.add(Bidirectional(cell(units, return_sequences=True), batch_input_shape=(None, sequence_length, n_features)))
           else:
               model.add((cell(units, return_sequences=False)))
        elif i == n_layers - 1:

            if bidrectional:
                model.add(Bidirectional(cell(units, return_sequences=False)))
            else:
                model.add(cell(units,return_sequences=False))
        else:

            if bidrectional:
                model.add(Bidirectional(cell(units, return_sequences=True)))
            else:
                model.add(cell(units, return_sequences=True))

            model.add(Dropout(dropout))
        model.add(Dense(1, activation="linear"))
        model.compile(loss=loss, metrics=["mean_absolute_error"], optimizer=optimizer)
        return model