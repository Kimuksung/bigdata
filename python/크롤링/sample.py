import requests
from bs4 import BeautifulSoup
import openpyxl

#request는 정적 data들을 수집 할 때에 동적 data 수집에는 selinium을 사용
#치치의 분류
req = requests.get('http://www.samsunghospital.com/dept/main/index.do?DP_CODE=DEN&MENU_ID=002003007011')
raw = req.text

html = BeautifulSoup(raw, 'html.parser')
infos = html.select('div#leftMenu')

clip1 = infos[0] #무조건 indexing해주어야 한다. list로 되어있다.

clip1_title = clip1.select_one('ul.deptsection_3depth_menu ')
clip1_title = clip1.select('ul.deptsection_3depth_menu a')

print(clip1_title[0])
print(clip1_title[0].text)

#그냥 data를 수집하게 되면 프로그램으로 인식-> 해결법
raw = requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='+clip1_title[0].text, headers={'User-Agent': 'Mozilla/5.0'}).text
html = BeautifulSoup(raw, 'html.parser')
#infos = html.select('ul.type01')
infos = html.select('.answer')
print(infos[0].text)

#엑셀에 분류하여 저장 version차이 나서 그런가 한셀이라 그런가 sell 안에 적용이 되지 않는다.
'''
wb = openpyxl.load_workbook('crawling.xlsx')
sheet1 = wb.active

sheet1.title = "data"
sheet1['A1'] = '분류'
sheet1['A2'] = '값'
sheet1.append(clip1_title[0].text,infos[0].text)
wb.save('crawling.xlsx')
'''

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')