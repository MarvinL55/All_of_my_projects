from stockPerdiction import creat_model, load_data
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint, TensorBoard
import os
import pandas as pd
from parameters import *

if not os.path.isdir("result"):
    os.mkdir("results")


if not os.path.isdir("logs"):
    os.mkdir("data")

data = load_data(ticker, N_STEPS, scale=SCALE, split_by_date=SPLIT_BY_DATE,
                 shuffle=SHUFFLE, lookup_step=LOOKUP_STEP, test_size=TEST_SIZE,
                 feature_columns=FEATURE_COLUMNS)

data["df"].to_csv(ticker_data_filename)

model = creat_model(N_STEPS, len(FEATURE_COLUMNS), loss=LOSS, units=UNITS, cell=CELL, n_layers=N_LAYERS,
                    dropout=DROPOUT, optimizer=OPTIMIZER, bidrectional=BIDIRECTIONAL)

checkpointer = ModelCheckpoint(os.path.join("results", model_name + ".h5"), save_weights_only=True, verbose=1)
tensorboard =TensorBoard(log_dir=os.path.join("logs", model_name))

history = model.fit(data["X_train"], data["y_train"],
                    batch_size=BATCH_SIZE,
                    epochs=EPOCHS,
                    validation_data=(data["X_test"], data["y_test"]),
                    callbacks=[checkpointer, tensorboard],
                    verbose=1)