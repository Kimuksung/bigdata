'''
원격 서버 웹 수집
'''

from bs4 import BeautifulSoup #source -> html parsing
import urllib.request as res #원격 서버 파일 요청

url = "http://www.naver.com/index.html"

#1. 원격 서버 url 요청
req = res.urlopen(url)
print(req)
data = req.read()
print(data)

# 2. source -> html 형식 파싱
src = data.decode("utf-8")
html = BeautifulSoup(src , 'html.parser')
#print(html)

# 3. Tag 내용 가져오기
link = html.find('a')
print(link)
print(link.string)