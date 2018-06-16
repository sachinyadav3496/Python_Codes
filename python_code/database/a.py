import sqlite3
con = sqlite3.connect("test.db")
c = con.cursor()
c.execute("create table user(name text, id int not null, sal float)")
c.execute("insert into user(name,id,sal) values('sachin',1,15)")
c.execute("insert into user(name,id,sal) values('lokesh',2,20)")
c.execute("select * from user")
print(c.fetchall())
c.close()
con.close()


