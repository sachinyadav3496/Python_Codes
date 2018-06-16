import sqlite3 as sql
db = sql.connect("test.db")
c = db.cursor()
c.execute("create table user(name text,id int not null,grade char)")
c.execute("insert into user(name,id,grade) values('sachin',1,'A')")
c.execute("insert into user(name,id,grade) values('yadav',1,'B')")
db.commit()
c.close()
db.close()

