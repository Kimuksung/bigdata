'''
선택자(selector)
- 웹 문서 디자인(css)
- 선택자 : id(#) - 중복 불가 / class(.) - 중복 가능
- html.select('선택자') : 여러 개의 element 수집
- html.select_one('선택자') : 한 개 element 수집

'''

from bs4 import BeautifulSoup

file = open("../data/html03.html" , encoding="utf-8")
src = file.read()
#print(src)

html = BeautifulSoup(src , 'html.parser')

# tag & selector -> element 수집

# 1) id 선택자
table = html.select_one("#tab")
print(table)

ths = html.select("#tab > tr >th")
print(ths)

for th in ths:
    print(th.string)

# 2) class 선택자
trs = html.select("#tab > .odd")
for tr in trs :
    tds = tr.find_all('td')
    for td in tds:
        print(td.string)

# 3) tag[속성='값'] 찾기
trs = html.select("tr[class = 'odd']")
print(trs)
for tr in trs :
    tds = tr.find_all('td')
    for td in tds:
        print(td.string)

