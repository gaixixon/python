
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3
conn = sqlite3.connect('/home/gaixixon/student/student.db')
cur = conn.cursor()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/studentform')
def studentform():
    return render_template('studentform.html')

@app.route('/studentlist')
def studentlist():
    global conn, cur
    result = cur.execute(''' SELECT * FROM student ''')
    result = cur.fetchall()
    return render_template('studentlist.html',result=result)

@app.route('/addstudent', methods=['POST' , 'GET'])
def addstudent():
    if request.method == 'POST':
        result = request.form.to_dict()
        global conn,cur
        cur.execute(''' INSERT INTO student (name,tel,dob,address) VALUES (?,?,?,?)''', (result["Name"],result["Tel"],result["Address"],result["DOB"]))
        #cur.commit()
    return render_template('index.html')
conn.commit()