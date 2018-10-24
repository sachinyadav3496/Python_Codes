import sqlite3 as sql


db = sql.connect('my.db')

c = db.cursor()


c.execute('select * from student')
d = c.fetchall()
print(d)

name = input("Enter your name : ")

cmd = f"select * from student where name='{name}'"
print(cmd)
c.execute(cmd)

data = c.fetchone()

if data : 
    print("here is your data : ")
    for d in data : 
        print(f"\n\t{d}")
else : 
    print("No such user exists")
