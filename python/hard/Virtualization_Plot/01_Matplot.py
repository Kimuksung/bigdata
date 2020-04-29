# -*- coding: utf-8 -*-
"""
matplotlib API

1. 기본 차트 그리기
2. 산점도 그리기
3. subplot 이용한 차트 그리기

"""

import matplotlib.pyplot as plt 

# 차트에서 한글 지원 
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False
import pandas as pd

import numpy as np

# 1. 기본 차트 그리기

data = np.arange(10)
#plt.plot(data,'r+')
#plt.show()

data2 = np.random.randn(10)
plt.plot(data , data2 ) #x, y
plt.show()

plt.plot(data , data2 , 'ro')
plt.show()

plt.plot(data2)
plt.show()

# 2. 산점도 그리기
# 단색
plt.scatter(data, data2 , c='r' , marker = 'o')
plt.show()

# 여러가지 색
cdata = np.random.randint(1,4,10) #1~3
cdata  
plt.scatter(data, data2 , c=cdata , marker = 'o')
plt.show()

# 3. subplot 이용 차트 그리기
fig = plt.figure(figsize = (5,3)) # 차트의 크기 지정
x1 = fig.add_subplot(2,2,1)
x2 = fig.add_subplot(2,2,2)
x3 = fig.add_subplot(2,2,3)
x4 = fig.add_subplot(2,2,4)

# data 생성
data3 = np.random.randint(1,100,100)
data4 = np.random.randint(10,110,100)
cdata = np.random.randint(1,4,100)

# 첫번쨰 격자 : histogram
x1.hist(data3)

# 산점도
x2.scatter(data3 , data4 ,c = cdata)

# 선그래프
x3.plot(data3)

# 점선 그래프
x4.plot(data4 ,  'g--')
plt.show()

# 차트 크기 지정 , 두 개 이상 차트 그리기
fig = plt.figure(figsize = (12,5))

chart = fig.add_subplot() # default = (1,1,1)
#계단형
chart.plot(data , color = 'r' , label = 'step' , drawstyle = 'steps-post')
#선스타일 차트
chart.plot(data2 , color = 'b', label ="line")

#차트 제목
plt.title('계단형 vs 선 스타일')
plt.xlabel('data')
plt.ylabel('난수 정수')
plt.legend(loc ='best')
plt.show()

# 막대차트
fig2 = plt.figure()

chart2 = fig2.add_subplot() # default = (1,1,1)
data = np.random.randint(80,250,5)
idx = range(len(data))
chart2.bar(idx , data , color = 'darkblue')

# x 축 눈금 레이블
x_label = ['seoul', 'daejun' , 'busan' , 'incheon' ,'bucheon']
plt.xticks(idx,x_label)
plt.xlabel('판매 지역')
plt.ylabel('매출 현황')
plt.title('2020년 1분기 전국 지역별 판매현황')
plt.show()






































