'''
db -> web

1. index page 작성 -> 동 입력
2. server dong 받기
3. db 연동
4. 주소 조회
5. 조회 결과 -> client
'''

from flask import Flask , render_template ,request # app 생성 , template(html) 호출

app = Flask(__name__)

@app.route("/")
def index():
    return  render_template("/app03/index.html")

@app.route("/search",methods=['POST'])
def search():
    dong = request.form['dong']
    import pymysql
    config = {
        'host': '127.0.0.1',
        'user': 'scott',
        'password': 'tiger',
        'database': 'work',
        'port': 3306,
        'charset': 'utf8',
        'use_unicode': True}
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    cursor.execute(f"select * from zipcode_tab where dong like '%{dong}%'")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    #print(data)
    return render_template("/app03/result.html" , dong = dong , data = data)


if __name__ == "__main__":
    app.run()