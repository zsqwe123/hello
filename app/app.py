from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:/Users/zhaos/PycharmProjects/app/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    department = request.form['department']
    phone_number = request.form['phone_number']
    photo = request.files['photo']
    import os

    directory = "C:/Users/zhaos/PycharmProjects/app/uploads"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 将照片保存到临时文件
    temp_photo = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
    photo.save(temp_photo)

    # 连接到数据库并插入数据
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, department TEXT, phone_number TEXT, photo TEXT)")
    cursor.execute("INSERT INTO users (name, department, phone_number, photo) VALUES (?, ?, ?, ?)", (name, department, phone_number, temp_photo))
    conn.commit()
    conn.close()

    return "注册成功！"

if __name__ == '__main__':
    app.run(debug=True)
