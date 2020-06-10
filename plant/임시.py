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
