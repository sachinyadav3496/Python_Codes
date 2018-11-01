import sqlite3 as sql

db = sql.connect('grras.db')

c = db.cursor()

name = input("Enter student name : ")

cmd = f'select student.name,fees.due from student,fees where student.name = "{name}" and student.id = fees.id'
c.execute(cmd)

data = c.fetchone()

if data :

    print("Data of Student Table : ")
    print()
    print(*data)
    print()
else :
    print(f"There is no such student with name {name} exists in database")

