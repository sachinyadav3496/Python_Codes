import sqlite3 as sql
db = sql.connect('bank.db')
c = db.cursor()

c.execute('create table  bank(user text,acc_no int(5) primary key,password text,bal int(15))')

c.execute("insert into bank(user,acc_no,password,bal) values('ram',1001,'redhat',1000)")
c.execute("insert into bank(user,acc_no,password,bal) values('shyam',1002,'Asimov',15000)")
c.execute("insert into bank(user,acc_no,password,bal) values('hari',1003,'python',10000)")
db.commit()
c.close()
db.close()
