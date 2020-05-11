# -*- coding: utf-8 -*-
"""
Time Series

1. 시계열 자료 생성
2. 날짜 type -> Kor
3. 시계열 시각화
4. 이동 평균 기능 : 5 , 10 ... -> trend smoothing


"""

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 1. data create
time_date = pd.date_range("2017-03-01" , "2020-03-30")
time_date

time_date_month = pd.date_range("2017-03-01" , "2020-03-30",freq = 'M')
time_date_month # month 단위

# 월 단위 매출 현황
x = pd.Series(np.random.uniform(10,100,36))
x

df = pd.DataFrame({'date' : time_date_month , 'price':x})
df

plt.plot(df['date'], df['price'])

# 2. 날짜 type -> Kor
cospi = pd.read_csv("cospi.csv")
cospi.info()
cospi.head()

'''
        Date     Open     High      Low    Close  Volume
0  26-Feb-16  1180000  1187000  1172000  1172000  176906
'''

date = cospi['Date']
date

# list + for : 26-Feb-16 -> 2016-02-16
kdate = [datetime.strptime(d,"%d-%b-%y") for d in date]
kdate
cospi['Date'] = kdate
cospi


# 3. 시계열 data 시각화
cospi.index

# 칼럼 -> index 적용
new_cospi = cospi.set_index('Date')
new_cospi['2016']
new_cospi['2016-03':'2016-01']

# subset
new_cospi_HL = new_cospi[['High' , 'Low']]
new_cospi_HL.index
new_cospi_HL.columns

# 2015년 기준
new_cospi_HL['2015'].plot(title="2015 Year")
plt.show()

# 2016년 기준
new_cospi_HL['2016'].plot(title="2016 Year")
plt.show()


# 2016년 기준
new_cospi_HL['2016-02'].plot(title="2016 Year")
plt.show()





















