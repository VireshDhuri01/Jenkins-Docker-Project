from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

# DB Config (will be replaced later with Docker env vars)
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "sqlcontainer"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_ROOT_PASSWORD", "root"),
    database=os.getenv("MYSQL_DB", "taskdb")
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    db.commit()
    return redirect('/')

@app.route('/update/<int:id>')
def update_task(id):
    cursor.execute("UPDATE tasks SET status='Done' WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_task(id):
    cursor.execute("DELETE FROM tasks WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)