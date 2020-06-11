# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime , timedelta
plant1_train = pd.read_csv('plant1_train.csv')
plant2_train = pd.read_csv("plant2_train.csv")


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

# --------
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

# df -> np
y_data = hour3['nextdaytemp'].values[0:-8].reshape(-1, 1)
hour3 = hour3.drop(["Date" , "loc1", "nextdaytemp"] , axis = 1)
type(hour3) # dataframe

type(hour3.values[0:-8]) #numpy
x_data = hour3.values[0:-8]

x_data.shape
y_data.shape

# train / test split
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

hour3.isnull().sum()
# =============================================================================
# loc1_tem          0
# out_tem           0
# loc1_coil_temp    0
# loc1_hum          0
# out_hum           0
# dayofyear         0
# dayofhour         0
# =============================================================================

from sklearn.preprocessing import MinMaxScaler
x_scaler = MinMaxScaler()
x_train_scaled = x_scaler.fit_transform(x_train)

print("Min:", np.min(x_train_scaled))
print("Max:", np.max(x_train_scaled))

x_test_scaled = x_scaler.transform(x_test)

y_scaler = MinMaxScaler()
y_train_scaled = y_scaler.fit_transform(y_train)
y_test_scaled = y_scaler.transform(y_test)

print(x_train_scaled.shape)
print(y_train_scaled.shape)

print(y_test_scaled.shape)














