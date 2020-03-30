# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd


def choose(x):
    temp =[]
    temp2 = []
    temp3 = []
    html = urlopen("https://www.weather.go.kr/weather/climate/past_cal.jsp?stn=108&yy=2018&mm="+ str(x) +"&obs=1&x=17&y=10")  
    print("https://www.weather.go.kr/weather/climate/past_cal.jsp?stn=108&yy=2018&mm="+ str(x) +"&obs=1&x=17&y=10")
    bsObject = BeautifulSoup(html, "html.parser") 
    ele = bsObject.find_all('tr')
    ele = str(ele)
    ele = ele.split("\n")
    count = 1
    p = re.compile('평균기온:[-]*\d+')
    p2 = re.compile('일강수량:[\d]*.\d+')
    for i in range(0, len(ele)):
        result = p.findall(ele[i])
        result2 = p2.findall(ele[i])
        datetime_str = "2018/"+str(x)+"/"+str(count)
        if result:
            #print(result)
            temp.append(result)
            temp2.append(datetime_str)
            temp3.append(result2)
            count = count+1
    #print(temp)
    df = pd.DataFrame({'date':temp2, 'temper':temp,'rain':temp3})
    return df

def choose2(x):
    temp =[]
    temp2 = []
    temp3 = []
    html = urlopen("https://www.weather.go.kr/weather/climate/past_cal.jsp?stn=108&yy=2019&mm="+ str(x) +"&obs=1&x=17&y=10")  
    print("https://www.weather.go.kr/weather/climate/past_cal.jsp?stn=108&yy=2019&mm="+ str(x) +"&obs=1&x=17&y=10")
    bsObject = BeautifulSoup(html, "html.parser") 
    ele = bsObject.find_all('tr')
    ele = str(ele)
    ele = ele.split("\n")
    count = 1
    p = re.compile('평균기온:[-]*\d+')
    p2 = re.compile('일강수량:[\d]*.\d+')
    for i in range(0, len(ele)):
        result = p.findall(ele[i])
        result2 = p2.findall(ele[i])
        datetime_str = "2019/"+str(x)+"/"+str(count)
        if result:
            #print(result)
            temp.append(result)
            temp2.append(datetime_str)
            temp3.append(result2)
            count = count+1
    #print(temp)
    df = pd.DataFrame({'date':temp2, 'temper':temp,'rain':temp3})
    return df

answer = choose(1)


for i in range(2, 13):
    answer = answer.append([choose(i)])

for i in range(1,8):
    answer= answer.append([choose2(i)])
    
#print(answer)
answer.to_csv("C:\\Users\\user\\Desktop\\csv\\weather.csv",encoding='utf-8-sig',header=False,index=False)
