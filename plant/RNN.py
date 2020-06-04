# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime , timedelta
from sklearn.preprocessing import MinMaxScaler
import numpy as np

plant1_train = pd.read_csv('plant1_train.csv')
plant2_train = pd.read_csv("plant2_train.csv")


plant1_train = plant1_train.drop('Unnamed: 0' , axis=1)
cols = ['Date' , 'loc1_tem', 'loc1_hum', 'loc1_coil_temp','loc2_tem', 'loc2_hum', 'loc2_coil_temp' , 'loc3_tem', 'loc3_hum', 'loc3_coil_temp', 'out_tem', 'out_hum', 'loc1' , 'loc2' , 'loc3']
plant1_train.columns = cols

plant1_train_first = plant1_train[['Date','loc1_tem', 'out_tem' , 'loc1_coil_temp','loc1_hum' ,'out_hum','loc1']]


date_trans = []
for i in range(0,len(plant1_train)):
    date_trans.append(datetime.strptime(plant1_train_first['Date'][i] , '%Y-%m-%d %H:%M'))

plant1_train_first['date_trans'] = date_trans
plant1_train_first

hour24_temp = []
hour24_hum = []
for i in range(0,len(plant1_train_first)):
    tmp = datetime.strptime(plant1_train_first['Date'][i]  , '%Y-%m-%d %H:%M') + timedelta(days=1)
    tmp1 = datetime.strptime(plant1_train_first['Date'][i]  , '%Y-%m-%d %H:%M')
    if(len(plant1_train_first[plant1_train_first['date_trans']==tmp]) > 0 ):
        loc_24hour = plant1_train_first[plant1_train_first['date_trans']==tmp]
        print("this", float(loc_24hour['loc1_coil_temp'].values))
        print("-"*10)
        hour24_temp.append(float(loc_24hour['loc1_coil_temp'].values))
        hour24_hum.append(float(loc_24hour['loc1_hum'].values))
    else:
        hour24_temp.append(float('NaN'))
        hour24_hum.append(float('NaN'))

plant1_train_first['24hourtemp'] = hour24_temp
plant1_train_first['24hourhum'] = hour24_hum

plant1_train_first_24 = plant1_train_first.dropna(axis=0)

plant1_train_first_24["Hour"] = plant1_train_first_24["date_trans"].apply(lambda x: x.hour)

plant1_train_first_24["dayofyear"] = plant1_train_first_24["date_trans"].apply(lambda x: x.dayofyear)

plant1_train_first_24
plant1_train_first_24.columns
#Index(['loc1_coil_temp', 'loc1_hum', '24hourtemp', '24hourhum', 'Hour','dayofyear']
plant1_train_first_24.date_trans

plant1_train_first_24 = plant1_train_first_24.drop(['Date', 'loc1_tem', 'out_tem', 'out_hum','date_trans','loc1'], axis=1)
plant1_train_first_24

train_split = 0.8

num_train = int(len(plant1_train_first_24)* train_split)
num_test = int(len(plant1_train_first_24) - num_train)
num_train + num_test
len(plant1_train_first_24)

plant1_train_first_24_y = plant1_train_first_24.iloc[:,[2,3]]
plant1_train_first_24_x = plant1_train_first_24.drop(['24hourtemp', '24hourhum'] , axis=1)

x_train = plant1_train_first_24_x[0: num_train] 
x_test = plant1_train_first_24_x[num_test:]

y_train = plant1_train_first_24_y[0: num_train]
y_test = plant1_train_first_24_y[num_test:]

num_x_signals = plant1_train_first_24_x.shape[1]
num_y_signals = plant1_train_first_24_y.shape[1]


x_scaler = MinMaxScaler()
x_train_scaled = x_scaler.fit_transform(x_train)
x_test_scaled = x_scaler.transform(x_test)

y_scaler = MinMaxScaler()
y_train_scaled = y_scaler.fit_transform(y_train)
y_test_scaled = y_scaler.transform(y_test)

print(x_train_scaled.shape)
print(y_train_scaled.shape) 

batch_size = 256
sequence_length = 8 * 7 * 8

def batch_generator(batch_size, sequence_length):
 """
 Generator function for creating random batches of training-data.
 """
 # Infinite loop.
 while True:
     # Allocate a new array for the batch of input-signals.
     x_shape = (batch_size, sequence_length, num_x_signals)
     x_batch = np.zeros(shape=x_shape, dtype=np.float16)
     # Allocate a new array for the batch of output-signals.
     y_shape = (batch_size, sequence_length, num_y_signals)
     y_batch = np.zeros(shape=y_shape, dtype=np.float16)
     # Fill the batch with random sequences of data.
     for i in range(batch_size):
     # Get a random start-index.
     # This points somewhere into the training-data.
         idx = np.random.randint(num_train - sequence_length)
        
         # Copy the sequences of data starting at this index.
         x_batch[i] = x_train_scaled[idx:idx+sequence_length]
         y_batch[i] = y_train_scaled[idx:idx+sequence_length]

     yield (x_batch, y_batch)

generator = batch_generator(batch_size=batch_size,
 sequence_length=sequence_length)

x_batch, y_batch = next(generator)

print(x_batch.shape)
print(y_batch.shape)

import matplotlib.pyplot as plt
batch = 0 # First sequence in the batch.
signal = 0 # First signal from the 20 input-signals.
seq = x_batch[batch, :, signal]
plt.plot(seq)


validation_data = (np.expand_dims(x_test_scaled, axis=0), np.expand_dims(y_test_scaled, axis=0))

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Input, Dense, GRU, Embedding
from tensorflow.python.keras.optimizers import RMSprop
from tensorflow.python.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard, ReduceLROnPlateau

model = Sequential()

model.add(GRU(units=512, return_sequences=True, input_shape=(None, num_x_signals,)))
model.add(Dense(num_y_signals, activation='sigmoid'))

warmup_steps = 50

def loss_mse_warmup(y_true, y_pred):
 """
 Calculate the Mean Squared Error between y_true and y_pred,
 but ignore the beginning "warmup" part of the sequences.

 y_true is the desired output.
 y_pred is the model's output.
 """
 # The shape of both input tensors are:
 # [batch_size, sequence_length, num_y_signals].
 # Ignore the "warmup" parts of the sequences
 # by taking slices of the tensors.
 y_true_slice = y_true[:, warmup_steps:, :]
 y_pred_slice = y_pred[:, warmup_steps:, :]
 # These sliced tensors both have this shape:
 # [batch_size, sequence_length - warmup_steps, num_y_signals]
 # Calculate the MSE loss for each value in these tensors.
 # This outputs a 3-rank tensor of the same shape.
 loss = tf.losses.mean_squared_error(labels=y_true_slice,
 predictions=y_pred_slice)
 # Keras may reduce this across the first axis (the batch)
 # but the semantics are unclear, so to be sure we use
 # the loss across the entire tensor, we reduce it to a
 # single scalar with the mean function.
 loss_mean = tf.reduce_mean(loss)
 return loss_mean

optimizer = RMSprop(lr=1e-3)
model.compile(loss=loss_mse_warmup, optimizer=optimizer)
