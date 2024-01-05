from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# 配置数据库连接信息
db_config = {
    "host": "sheng",
    "user": "root",
    "password": "qwe123",
    "database": "face"
}

@app.route('/')
def index():
    return render_template('new_file.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # 连接到数据库并执行插入操作
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        values = (username, email, password)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
