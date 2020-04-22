'''
1. templates 파일 작성
    - 사용자 요청과 서버의 응답을 작성하는 html file
2. static 파일 작성
    - 정적 파일 : image file , javascript , css
'''

from flask import Flask , render_template

# flask application
app = Flask(__name__) #생성자 -> obejct(app)

# 함수 장식자 : 사용자 요청 url
@app.route('/')
def index(): # 호출 함수
    return render_template('/app01/index.html') #templates file은 자동 인식

@app.route('/info')
def info():
    return render_template('/app01/info.html') #templates file은 자동 인식


# 프로그램의 시작점
if __name__ == "__main__":
    app.run()
