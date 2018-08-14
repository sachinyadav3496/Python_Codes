import sqlite3 as sql
try : 
    db = sql.connect('mydata.db')
    c = db.cursor()
    cmd = "create table user(id int(6) primary key,name varchar(30) not null,password varchar(20) not null)"
    c.execute(cmd)
    cmd  = "insert into user(id,name,password) values (1001,'sachin','redhat'), (1002,'abhisaar','hello@world'), (1003,'Jay','jay@123'), (1004,'divya','my@world'),(1005,'kritika','hey@bye')"
    c.execute(cmd)
    db.commit()
    print("Table created sucess fully")
except Exception as e : 
    print("Error!!",e)
    db.rollback()
