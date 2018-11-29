import pymysql as sql 

db = sql.connect(host='localhost',port=3306,user='student',password='student',database='student')

c = db.cursor()

c.execute('select * from student')

data = c.fetchall()

for each_row in data : 
    print(*each_row,sep='\t')


c.close()

db.close()
