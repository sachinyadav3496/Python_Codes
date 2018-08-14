import sqlite3 as sql ; import os
db = sql.connect('mydata.db')
c = db.cursor()
cmd = "select * from user"
c.execute(cmd)
data = c.fetchall()
os.system('cls')
print("\n\n\n\n\n")
print("\t{:<15} {:<15} {:<15}".format('ID','NAME','PASSWORD'),end='\n\n')
for item in data : 
    print("\t{id:<15} {name:<15} {password:<15}\n".format(id=item[0],name=item[1],password=item[2]))
print("\n\n\n\n")
c.close()
db.close()
