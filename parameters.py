import os
import time
from keras.layers import LSTM
#Window size of the sequence length
N_STEPS = 50
#Lookup step, 1 is the next day
LOOKUP_STEP = 15
#wheather to scale feature columns and output price as well
SCALE = True

scale_str = f"sc-{int(SCALE)}"
#weather toshuffle the dataset
SHUFFLE = True

shuffle_str = f"sh-{int(SHUFFLE)}"
#wheather to split the training/testing set by date
SPLIT_BY_DATE = False
split_by_date_str = f"sbd{int(SPLIT_BY_DATE)}"
#test ratio size, 0.2 is 20%
TEST_SIZE = 0.2
#features to use
FEATURE_COLUMNS = ['adjclose', 'volume', 'open', 'high', 'low']
#date now
date_now = time.strftime("%Y-%m-%d")

N_LAYERS = 2

CELL = LSTM
#256 LSTM neurons
UNITS = 256
#40% dropout
DROPOUT = 0.4

BIDIRECTIONAL = False

LOSS = "huber_loss"
OPTIMIZER = "adam"
BATCH_SIZE = 64
EPOCHS = 500


ticker = "AMZN"
ticker_data_filename = os.path.join("data", f"{ticker}_{date_now}.csv")

model_name = f"{date_now}_{ticker}-{shuffle_str}-{split_by_date_str} -\
{LOSS}-{OPTIMIZER}-{CELL._name_}-seq_{N_STEPS}-step-{LOOKUP_STEP}-layers-{N_LAYERS}-units-{UNITS}"
if BIDIRECTIONAL:
    model_name += "-b"