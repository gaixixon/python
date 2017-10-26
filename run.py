
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

class DBase(object):
    def connect(self):
        self.conn = sqlite3.connect('/home/gaixixon/student/student.db')
        self.cur = self.conn.cursor()
        return
    def list(self):
        self.connect()
        try:
            query = "SELECT * FROM student"
            self.cur.execute(query)
            return self.cur.fetchall()
        finally:
            self.conn.close()

    def Add(self,result):
        self.connect()
        try:
            query = """INSERT INTO student (name,dob,tel,address) VALUES (?,?,?,?)"""
            self.cur.execute(query,(result['Name'],result['Tel'],result['DOB'],result['Address']))
            self.conn.commit()
        finally:
            self.conn.close()

DB = DBase()
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/studentform')
def studentform():
    return render_template('studentform.html')

@app.route('/studentlist')
def studentlist():
    result = DB.list()
    return render_template('studentlist.html',result=result)

@app.route('/addstudent', methods=['POST' , 'GET'])
def addstudent():
    try:
        if request.method == 'POST':
            result = request.form.to_dict()
            DB.Add(result)
            return render_template('foo.html',result = result)
    except Exception as e:
        return render_template('foo.html',result = e)