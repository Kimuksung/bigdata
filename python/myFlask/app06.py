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

import pandas
monday=pandas.date_range(start='20180102', end='20181231',freq='W-MON')
print(monday)

from flask import Flask , render_template ,request # app 생성 , template(html) 호출

app = Flask(__name__)

@app.route("/")
def index():
    return  render_template("/app06/MultiLevelMenu-master/index.html" , monday = monday)

@app.route("/samsungid",methods =['GET'])
def samsungid():
    try:
        if request.method == 'GET':
            id = request.args.get('id')
        conn , cursor = db_conn()
        sql = f"select date , brand , menu , price , quantity from samsung where id={id}"
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        cursor.close()
        conn.close()

        return render_template("/app06/MultiLevelMenu-master/id_show.html", data = data , id=id )
    except Exception as e:
        return render_template("/app06/MultiLevelMenu-master/id_show.html", error = e)

@app.route("/samsungbr" , methods=['POST'])
def samsungbr():
    if request.method == 'POST':
        brand = request.form['brand']

    conn, cursor = db_conn()
    sql = f"select menu , price from samsung where brand='{brand}'"
    cursor.execute(sql)
    data = cursor.fetchall()
    data = set(data)
    cursor.close()
    conn.close()
    return render_template("/app06/MultiLevelMenu-master/brand.html", brand = brand , data= data )

@app.route("/graph",methods =['GET'])
def graph():
    if request.method == 'GET':
        day = request.args.get('day')

    import datetime
    day = datetime.datetime.strptime(day, '%Y-%m-%d %M:%S:%f')

    conn , cursur = db_conn()
    start_day = day.date()

    data = []

    sql = f"select sum(quantity) from samsung where date = '{start_day}' group by date"
    print(sql)
    cursur.execute(sql)
    temp = cursur.fetchone()
    print(temp)
    data.append(int(temp[0]))


    for i in range(4):
        start_day = start_day + datetime.timedelta(days=1)
        print(start_day)
        sql = f"select sum(quantity) from samsung where date = '{start_day}' group by date"
        print(sql)
        cursur.execute(sql)
        temp = cursur.fetchone()
        print(temp)
        if temp ==None:
            data.append(0)
        else:
            data.append(int(temp[0]))

    print(data)

    cursur.close()
    conn.close()

    labels = ['월','화','수','목','금']

    
    return render_template('/app06/MultiLevelMenu-master/graph.html', title='일주일 취식량', max=4000, labels=labels, values=data)

if __name__ == "__main__":
    app.run()
