import sqlite3 as sql 

db = sql.connect('grras.db')
c = db.cursor()


table1 = "CREATE TABLE student( id int(4) primary key, name varchar(30) not null, course varchar(30) not null, address varchar(100), email varchar(50) , ph_no varchar(15) not null ) "


table2 = "CREATE TABLE fees( id references student (id) on delete cascade on update cascade, fees float not null, due float )"

c.execute(table1)
c.execute(table2)

db.commit()

c.close()
db.close()
