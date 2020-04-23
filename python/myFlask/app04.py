'''
get vs post
    -parameter 전송 방식
    -get : url에 노출
    -post : body에 포함되어 전송(대량의 data)

<작업 순서>
1. index page : menu(radio or select) -> get
2. flask server parameter(메뉴 번호)
3. menu 번호에 따라 각 페이지 이동

'''

def db_conn():
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
    return conn , cursor

def select_function(): # 1. 레코드 조회
    conn , cursor = db_conn()
    sql = "select * from goods"
    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data

from flask import Flask , render_template ,request # app 생성 , template(html) 호출

app = Flask(__name__)

@app.route("/")
def index():
    return  render_template("/app04/index.html")

@app.route("/select",methods=['GET','POST'])
def select():
    if request.method=='GET':
        menu = request.args.get('menu')
        #dong = request.form['dong'] post
    if menu == "1": #전체 레코드 조회
        data = select_function()
        size = len(data)
        return render_template("/app04/select.html", data = data , size= size)

    if menu == "2":
        return render_template("/app04/insert_form.html")
    if menu == "3":
        return render_template("/app04/update_form.html")
    if menu == "4":
        return render_template("/app04/delete_form.html")

@app.route("/insert" , methods=['POST'])
def insert():
    try:
        if request.method == 'POST':
            code = int(request.form['code'])
            name = request.form['name']
            su = int(request.form['su'])
            dan = int(request.form['dan'])

        conn , cursor = db_conn()
        sql = f"insert into goods values ({code},'{name}',{su},{dan})"
        cursor.execute(sql)
        conn.commit()

        data = select_function()
        size = len(data)
        return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("/app04/error.html" , error_info = e)

@app.route("/update" , methods=['POST'])
def update():
    try:
        if request.method == 'POST':
            code = int(request.form['code'])
            su = int(request.form['su'])
            dan = int(request.form['dan'])

        conn , cursor = db_conn()
        sql = f"update goods set su ={su}, dan={dan} where code={code}"
        cursor.execute(sql)
        conn.commit()

        data = select_function()
        size = len(data)
        return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("/app04/error.html" , error_info = e)

@app.route("/delete", methods=['GET'])
def delete():
    try:
        if request.method == 'GET':
            code = request.args.get('code')

        conn, cursor = db_conn()
        sql = f"delete from goods where code={code}"
        cursor.execute(sql)
        conn.commit()

        data = select_function()
        size = len(data)
        return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("/app04/error.html", error_info=e)

if __name__ == "__main__":
    app.run()
