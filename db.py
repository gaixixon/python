import sqlite3
class DB():
    conn =''
    c = ''
    def __init__(self):
        DB.connect()

        return
    def connect(self):
        try:
            self.conn = sqlite3.connect('/home/gaixixon/student/student.db')
            self.c = conn.cursor()
            return
        except Exception as e:
            raise e