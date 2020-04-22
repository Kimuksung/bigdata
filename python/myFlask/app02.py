'''
python 객체(list, dict) -> template 으로 보내기
jinja2 템플릿 표현식

{{ object }} : 단일 객체 출력 시
{% for 변수 in 열거형 객체 %} : 열거형 객체 출력

'''

from flask import Flask , render_template # app 생성 , template(html) 호출

app = Flask(__name__)

@app.route("/")
def index():
    uname ="홍길동"
    goodsList= ["딸기", "포도","사과"]
    return  render_template("/app02/index.html")

@app.route("/temp01")
def temp():
    uname = "홍길동"
    goodsList = ["딸기", "포도", "사과"]

    return render_template("/app02/page.html" , name = uname , glist =goodsList)

@app.route("/temp02/<name>")
def temp02(name):
    return render_template("/app02/temp02_page.html" , name = name)

if __name__ == "__main__":
    app.run()