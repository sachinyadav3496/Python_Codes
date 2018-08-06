import sqlite3 as sql

db = sql.connect('pybank.db')
c = db.cursor()

cmd = "create table bank(name text,acc_no int(5) primary key,bal text,password text)"
c.execute(cmd)
db.commit()
c.close()
db.close()
