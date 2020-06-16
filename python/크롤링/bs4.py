#Scraping 
#pip install beautifulsoup4
#pip list
from urllib.request import urlopen
from bs4 import BeautifulSoup

#영화 사이트에서 
url = "https://www.rottentomatoes.com/" #Scraping 할 site
html = urlopen(url)
source = html.read() # 바이트코드 type으로 소스를 읽는다.
html.close()
soup = BeautifulSoup(source, "html5lib")

table = soup.find(id="top-box-office") #대소문자를 구별 함으로 오타를 내면 type이 null로 나온다.
movies = table.find_all(class_="media-lists__table table")
#data를 확인 해보면 제대로 들어있는 것을 볼 수 있다.

#stackoverflow에서 
page = urlopen("http://stackoverflow.com/questions/tagged/python")
document = page.read()
page.close()

soup = BeautifulSoup(document, 'html5lib')

questions = soup.find(id="questions")

questions_list = questions.find_all("a", class_="question-hyperlink")
for question in questions_list:
    print(question.get_text())
    print('http://stackoverflow.com' + question.get('href'))

#cgv 사이트에서
page = urlopen("http://www.cgv.co.kr/movies/")
document = page.read()
page.close()

soup = BeautifulSoup(document, 'html5lib')

questions = soup.find(id="cgvwrap")
questions_list = questions.find_all("div", class_="sect-movie-chart")


