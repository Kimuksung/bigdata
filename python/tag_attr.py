'''
tag 속성과 내용 가져오기
- element : tag + 속성 + 내용
ex) href = attribute <a href="www.naver.com"> </a>
'''

from bs4 import BeautifulSoup
file = open("../data/html02.html",encoding="utf-8")
src = file.read()

html = BeautifulSoup(src,"html.parser")
#print(html)

links = html.find_all('a')
#print(links)

# a tag attribute(href , target)
urls =[]
for link in links:
    urls.append(link.attrs['href'])
    #print(link.attrs)
    #print(link.string)
    try:
        print(link.attrs['target'])
    except Exception as e:
        pass

print(urls)

import re #findall ,match , sub
#pattern = re.compile('[http://]+')
for i in urls:
    if re.match('[http://]+',i):
        print(i)
