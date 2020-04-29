# -*- coding: utf-8 -*-
"""
marker , color , line style , label

"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('ggplot')

# data 생성
data1 = 0.5 + 0.1 * np.random.randn(100) # mean = 0 std =1
data2 = 0.7 + 0.1 * np.random.randn(100)
data3 = 0.9 + 0.1 * np.random.randn(100)
data4 = 0.3 + 0.1 * np.random.randn(100)

fig = plt.figure(figsize = (12,5))
chart = fig.add_subplot()

chart.plot(data1 , marker = 'o' , color = 'blue', linestyle = '-', label='data1')
chart.plot(data2 , marker = '+' , color = 'red', linestyle = '--', label='data2')
chart.plot(data3 , marker = '*' , color = 'green', linestyle = '-.', label='data3')
chart.plot(data4 , marker = 's' , color = 'yellow', linestyle = ':', label='data4')

chart.set_title("MultiLine Chart")
chart.set_xlabel('index')
chart.set_ylabel('random_number')
plt.legend(loc = 'best') #범례 추가


plt.show()
