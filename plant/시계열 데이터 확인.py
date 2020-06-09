# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:46:46 2020

@author: user
"""


import pandas as pd
from datetime import datetime , timedelta
plant1_train = pd.read_csv('plant1_train.csv')
plant2_train = pd.read_csv("plant2_train.csv")


plant1_train = plant1_train.drop('Unnamed: 0' , axis=1)
cols = ['Date' , 'loc1_tem', 'loc1_hum', 'loc1_coil_temp','loc2_tem', 'loc2_hum', 'loc2_coil_temp' , 'loc3_tem', 'loc3_hum', 'loc3_coil_temp', 'out_tem', 'out_hum', 'loc1' , 'loc2' , 'loc3']
plant1_train.columns = cols

#'''

plant1_train_first = plant1_train[['Date','loc1_tem', 'out_tem' , 'loc1_coil_temp','loc1_hum' ,'out_hum','loc1']]

a = datetime.strptime(plant1_train_first['Date'][0]  , '%Y-%m-%d %H:%M')

date_trans = []
for i in range(0,len(plant1_train_first)):
    date_trans.append(datetime.strptime(plant1_train_first['Date'][i] , '%Y-%m-%d %H:%M'))

plant1_train_first['date_trans'] = date_trans
plant1_train_first

hour24 = []
for i in range(0,len(plant1_train_first)):
    tmp = datetime.strptime(plant1_train_first['Date'][i]  , '%Y-%m-%d %H:%M') + timedelta(days=1)
    tmp1 = datetime.strptime(plant1_train_first['Date'][i]  , '%Y-%m-%d %H:%M')
    if(len(plant1_train_first[plant1_train_first['date_trans']==tmp]) > 0 ):
        loc_24hour = plant1_train_first[plant1_train_first['date_trans']==tmp]
        print(plant1_train_first['Date'][i])
        print(loc_24hour['Date'])
        print("this", float(loc_24hour['loc1'].values))
        print("-"*10)
        hour24.append(float(loc_24hour['loc1'].values))
    else:
        hour24.append(float('NaN'))

plant1_train_first['24hourloc'] = hour24
plant1_train_first

plant1_train_first_24 = plant1_train_first.dropna(axis=0)
plant1_train_first_24[plant1_train_first_24['24hourloc']==1]
plant1_train_first_24.columns

# balanced sampling (downsampling)
plant1_train_first_24_true = plant1_train_first_24[plant1_train_first_24['24hourloc']==1]
plant1_train_first_24_false = plant1_train_first_24[plant1_train_first_24['24hourloc']==0]

plant1_train_first_24_true.shape # (267, 9)
plant1_train_first_24_false.shape # (57133, 9)

plant1_train_first_24_true = plant1_train_first_24_true.drop(['Date', 'loc1_tem', 'out_tem', 'out_hum','loc1', 'date_trans'], axis=1)
plant1_train_first_24_false = plant1_train_first_24_false.drop(['Date', 'loc1_tem', 'out_tem', 'out_hum','loc1', 'date_trans'], axis=1)

plant1_train_first_24_false_sample = plant1_train_first_24_false.sample(500)

plant1_train_first_24_false_sample

plant1_balancedsample = pd.concat([plant1_train_first_24_true, plant1_train_first_24_false_sample])
plant1_balancedsample

from matplotlib import pyplot as plt
temp = plant1_train_first
temp2 = temp.set_index('date_trans')
temp2.columns
temp2['loc1_tem'].plot(color = 'r' , label = 'loc1_tem')
temp2['out_tem'].plot(color ='blue' , label = 'out_tem')
temp2['loc1_coil_temp'].plot( color = 'green' , label = 'loc1_coil_temp')
plt.show()

'''
tmp=temp2.loc1_tem['2016-04-01 0:00' : '2016-12-22 6:00']
unsampled = tmp.resample('H').first()
# tmp.resample('10T').first()
unsampled

unsampled.interpolate(method='linear')
'''
hour3 = temp2.resample('3H').first()
hour3_temp = hour3['loc1_coil_temp']
hour3_temp = hour3_temp.interpolate(method='linear')
hour3_temp = pd.DataFrame(hour3_temp)
hour3_temp

hour3_temp['shitf1'] = hour3_temp['loc1_coil_temp'].shift(-1)

train = hour3_temp.iloc[0:7000]
train = train[:-1]
test = hour3_temp.iloc[7000:]
test = test[:-1]



