# -*- coding: utf-8 -*-
"""plant_RNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T8o5est9cCOs_xurw-j8FN6SuiY8RxZx
"""

from google.colab import drive
drive.mount('/gdrive', force_remount=True)

"""Data input"""

import pandas as pd
from datetime import datetime , timedelta

plant1_train = pd.read_csv("/gdrive/My Drive/Plain/plant1_train.csv")
plant2_train = pd.read_csv("/gdrive/My Drive/Plain/plant2_train.csv")

plant1_train = plant1_train.drop('Unnamed: 0' , axis=1)
cols = ['Date' , 'loc1_tem', 'loc1_hum', 'loc1_coil_temp','loc2_tem', 'loc2_hum', 'loc2_coil_temp' , 'loc3_tem', 'loc3_hum', 'loc3_coil_temp', 'out_tem', 'out_hum', 'loc1' , 'loc2' , 'loc3']
plant1_train.columns = cols

plant1_train_first = plant1_train[['Date','loc1_tem', 'out_tem' , 'loc1_coil_temp','loc1_hum' ,'out_hum','loc1']]

a = datetime.strptime(plant1_train_first['Date'][0]  , '%Y-%m-%d %H:%M')

date_trans = []
for i in range(0,len(plant1_train_first)):
    date_trans.append(datetime.strptime(plant1_train_first['Date'][i] , '%Y-%m-%d %H:%M'))

plant1_train_first['date_trans'] = date_trans
plant1_train_first

"""시계열 데이터 Check"""

from matplotlib import pyplot as plt
temp = plant1_train_first
temp2 = temp.set_index('date_trans')
hour3 = temp2.resample('3H').first()

hour3_temp = hour3['loc1_coil_temp']
hour3_temp = hour3_temp.interpolate(method='linear')

hour3_loc1_tem = hour3['loc1_tem']
hour3_loc1_tem = hour3_temp.interpolate(method='linear')

hour3_loc1_tem.plot(color = 'r' , label = 'loc1_tem')
hour3['out_tem'].plot(color ='blue' , label = 'out_tem')

hour3_temp.plot( color = 'green' , label = 'loc1_coil_temp')
plt.show()

"""Data Preprocessing"""

hour3
hour3.out_tem.values

hour3['dayofyear'] = hour3.index.dayofyear
hour3['dayofhour'] = hour3.index.hour
hour3['nextdaytemp'] = hour3.out_tem.shift(-8)
hour3
hour3.columns

# 선형 보간
hour3['loc1_tem'] = hour3['loc1_tem'].interpolate(method='linear')
hour3['out_tem'] = hour3['out_tem'].interpolate(method='linear')
hour3['loc1_coil_temp'] = hour3['loc1_coil_temp'].interpolate(method='linear')
hour3['loc1_hum'] = hour3['loc1_hum'].interpolate(method='linear')
hour3['out_hum'] = hour3['out_hum'].interpolate(method='linear')
hour3['nextdaytemp'] = hour3['nextdaytemp'].interpolate(method='linear')

print(hour3.isnull().sum())
# df -> np
y_data = hour3['nextdaytemp'].values[0:-8].reshape(-1, 1)
hour3 = hour3.drop(["Date" , "loc1", "nextdaytemp"] , axis = 1)
type(hour3) # dataframe

type(hour3.values[0:-8]) #numpy
x_data = hour3.values[0:-8]

x_data.shape
y_data.shape

"""Train test split / 0 ~ 1 normalize"""

num_data = len(x_data)
train_split = 0.8

num_train = int(train_split * num_data) # 7001
num_test = num_data - num_train # 1751

x_train = x_data[0:num_train]
x_test = x_data[num_train:]
len(x_train) + len(x_test)

y_train = y_data[0:num_train]
y_test = y_data[num_train:]

num_x_signals = x_data.shape[1]
num_y_signals = 1

import numpy as np
print("Min:", np.min(x_train))
print("Max:", np.max(x_train))

from sklearn.preprocessing import MinMaxScaler
x_scaler = MinMaxScaler()
x_train_scaled = x_scaler.fit_transform(x_train)

print("Min:", np.min(x_train_scaled))
print("Max:", np.max(x_train_scaled))

x_test_scaled = x_scaler.transform(x_test)

y_scaler = MinMaxScaler()
y_train_scaled = y_scaler.fit_transform(y_train)
y_test_scaled = y_scaler.transform(y_test)

print("x_train_scale_shape:" , x_train_scaled.shape)
print("y_train_scale_shape:" ,y_train_scaled.shape)

print("y_test_scale_shape:" ,y_test_scaled.shape)

"""Data generator

한번에 모든 data를 처리하지 말고 data를 분리하여 학습
"""

def batch_generator(batch_size, sequence_length):
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

batch_size = 256
sequence_length = 8 * 7 * 8

generator = batch_generator(batch_size=batch_size,sequence_length=sequence_length)
x_batch, y_batch = next(generator)

print("x_batch : ",x_batch.shape)
print("y_batch : ",y_batch.shape)

batch = 0 # First sequence in the batch.
signal = 0 # First signal from the 7 input-signals.
seq = x_batch[batch, :, signal]
plt.plot(seq)

seq2 = y_batch[batch, :, signal]
plt.plot(seq2)

validation_data = (np.expand_dims(x_test_scaled, axis=0), np.expand_dims(y_test_scaled, axis=0))    

print(np.expand_dims(x_test_scaled, axis=0).shape)
print(np.expand_dims(y_test_scaled, axis=0).shape)

"""RNN Modeling"""

import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Input, Dense, GRU, Embedding
from tensorflow.python.keras.optimizers import RMSprop
from tensorflow.python.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard, ReduceLROnPlateau

model = Sequential()
model.add(GRU(units=512, return_sequences=True, input_shape=(None, num_x_signals,)))
model.add(Dense(1, activation='sigmoid'))

warmup_steps = 50

def loss_mse_warmup(y_true, y_pred):
     y_true_slice = y_true[:, warmup_steps:, :]
     y_pred_slice = y_pred[:, warmup_steps:, :]
     # These sliced tensors both have this shape:
     # [batch_size, sequence_length - warmup_steps, num_y_signals]
     # Calculate the MSE loss for each value in these tensors.
     # This outputs a 3-rank tensor of the same shape.
     #loss = tf.losses.mean_squared_error(labels=y_true_slice, predictions=y_pred_slice)
     loss = tf.losses.mean_squared_error(y_true_slice, y_pred_slice)
     # Keras may reduce this across the first axis (the batch)
     # but the semantics are unclear, so to be sure we use
     # the loss across the entire tensor, we reduce it to a
     # single scalar with the mean function.
     loss_mean = tf.reduce_mean(loss)
     return loss_mean

#optimizer = RMSprop(lr=1e-3)
optimizer = tf.keras.optimizers.RMSprop(lr=1e-3)
model.compile(loss=loss_mse_warmup, optimizer=optimizer)
model.summary()

import os
checkpoint_path = "plant1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

callback_checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path, monitor='val_loss',verbose=1,save_weights_only=True,save_best_only=True)

callback_early_stopping = EarlyStopping(monitor='val_loss', patience=5, verbose=1)

callback_tensorboard = TensorBoard(log_dir='./23_logs/', histogram_freq=0, write_graph=False)

callback_reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, min_lr=1e-4,patience=0,verbose=1)

callbacks = [callback_early_stopping,callback_checkpoint,callback_tensorboard, callback_reduce_lr]

model.fit(x=generator,
 epochs=20,
 steps_per_epoch=100,
 validation_data=validation_data,
 callbacks=callbacks)

model.summary()