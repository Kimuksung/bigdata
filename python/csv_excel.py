'''
csv , excel file read / write

how to install?
cmd -> pip install library

'''

import pandas as pd


bmi = pd.read_csv("../data/bmi.csv",encoding="utf-8")
#print(bmi.info())
print(bmi.head())

height=bmi['height']
weight = bmi['weight']
label = bmi.label

print(len(height))
print(len(weight))

print(height.mean())
print(weight.mean())

max_h = max(height)
max_w = max(weight)

print(max_h)
print(max_w)

height_nor = height / max_h
weight_nor = weight / max_w

print(height_nor.mean())
print(weight_nor.mean())

# 범주형 변수 : label
lab_cnt = label.value_counts() #빈도수
print(lab_cnt)

# 2. excel file read
'''
pip install xlrd
'''
import os
print(os.getcwd())
excel = pd.ExcelFile("../data/sam_kospi.xlsx")
print(excel)
kospi = excel.parse('sam_kospi')
print(kospi)
print(kospi.info())

# 3. csv file save
kospi['diff'] = kospi.High - kospi.Low
print(kospi.info())

#csv file 저장 : 행 번호 제외
kospi.to_csv("../data/kospi_df2.csv", encoding = "utf-8" ,index =None)

kospi_df = pd.read_csv("../data/kospi_df2.csv")
print(kospi_df.head())