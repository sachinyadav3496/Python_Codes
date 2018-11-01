import sqlite3 as sql 


db = sql.connect('grras.db')

c = db.cursor()

c.execute('insert into student values (1,"sachin","python","jaipur","sachin@grras.com","981232322"), (2,"rajat","linux","ganganagar","rajat.goyal@gmail.com","123442") ')
c.execute('insert into fees values (1,15000,5000) , (2,20000,8000)')

db.commit()
c.close()
db.close()
