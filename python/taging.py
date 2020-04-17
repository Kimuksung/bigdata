'''
tag명으로 찾기
html.find('tag') : 최초 발견된 tag 수집
html.find_all('tag') : 해당 tag 전체 수집


'''

from bs4 import BeautifulSoup #html 파싱

# 1. local file 불러오기

file =open("../data/html01.html" , mode = 'r' ,encoding="utf-8")
src = file.read()

# 2. src-> html parsing
html = BeautifulSoup(src , 'html.parser')
# 3. tag 찾기 내용 추출
print(html)

h1 = html.html.body.h1
print(h1)
print(h1.string)

# find
h2 = html.find('h2')
print(h2)
print(h2.string)

# find_all
lis = html.find_all('li')
#print(lis ) #List

for li in lis:
    print(li.string)

li_cont = [li.string for li in lis]
print(li_cont)