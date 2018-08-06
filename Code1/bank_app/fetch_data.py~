import sqlite3 as sql
db = sql.connect('student')
c = db.cursor()
print("1.Enter data\n2Show data\n")
ch = int(input("Your Choice = "))
if ch == 1 :
    c.execute("insert into student(name,id,addr,marks) values(%s,%i,%s,%i)"%(input("Enter name "),int(input("Enter id of Student ")),input("Enter Address - "),int(input("Enter marks - "))))
    
    db.commit()
elif ch == 2 :
    print("\n1.find entry\n2.show all data")
    ck = int(input("Your choice - "))
    if ck == 1 :
        name = input("Enter name - ")
        cmd = 'select * from student where name={}'.format(name)
        c.execute(cmd)
        data = c.fetchall()
        print("Name = ",data[0][0])
        print("Id = ",data[0][1])
        print("Address = ",data[0][2])
        print("Marks = ",data[0][3])
    elif ck == 2 :
        c.execute('select * from student')
        l = c.fetchall()
        print("\nName\tID\tAddress\tMarks")
        for t in l:
            for var in t :

                print(var,end='\t')
            print()

db.commit()
c.close()
db.close()
