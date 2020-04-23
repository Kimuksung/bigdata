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

from flask import Flask , render_template ,request # app 생성 , template(html) 호출

app = Flask(__name__)

@app.route("/")
def index():
    return  render_template("/app05/main.html")

@app.route("/docForm")
def doctor():
    return  render_template("/app05/docForm.html")

@app.route("/docPro", methods=['GET', 'POST'])
def docPro():
    if request.method=='POST':
        doc_id = int(request.form['id'])
        major = request.form['major']

        conn, cursor = db_conn()
        sql = f"select * from doctors where doc_id = {doc_id} and major_treat = '{major}'"
        cursor.execute(sql)
        row = cursor.fetchone()

        if row:
            #sql = f"select d.doc_id , t.pat_id , treat_contents , tread_date from doctors d inner join threatments t on d.doc_id == t.doc_id and d.doc_id == {doc_id}"
            sql = f"""SELECT doc_id, pat_id, treat_contents, tread_date
                               FROM doctors NATURAL JOIN treatments WHERE doc_id = {doc_id}"""
            cursor.execute(sql)
            data = cursor.fetchall()

            if data :
                size = len(data)
            else:
                size = 0

            cursor.close()
            conn.close()

            return render_template("/app05/docPro.html", dataset = data )
        else:
            return render_template("/app05/error.html" , info="id 또는 진료과목 확인")


@app.route("/nurseForm")
def nurseForm():
    return render_template("/app05/nurseForm.html")

@app.route("/nursePro" , methods=['POST'])
def nursePro():
    if request.method=='POST':
        nurse_id = int(request.form['id'])
        conn, cursor = db_conn()
        sql = f"select * from nurses where NUR_ID = {nurse_id}"
        cursor.execute(sql)
        row = cursor.fetchone()
        print("nurse_id:",nurse_id)
        print("fetch",row)
        if row :
            sql = f"""SELECT NUR_ID , DOC_ID, PAT_NAME , PAT_PHONE
                                           FROM nurses NATURAL JOIN patients WHERE NUR_ID = {nurse_id}"""
            cursor.execute(sql)
            data = cursor.fetchall()
            print("data:",data)
            cursor.close()
            conn.close()

            return render_template("/app05/docPro.html", dataset = data )
        else:
            return render_template("/app05/error.html", info="id 또는 진료과목 확인")



if __name__ == "__main__":
    app.run()
