import flask
from flask import Flask
print(flask.__version__)

# flask application
app = Flask(__name__) #생성자 -> obejct(app)

# 함수 장식자 : 사용자 요청 url
@app.route('/')
def hello():
    return "HELLO FLASK"

@app.route('/temp01')
def temp01():
    return "This is index"


# 프로그램의 시작점
if __name__ == "__main__":
    app.run()
