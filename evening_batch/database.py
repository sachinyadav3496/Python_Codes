import pymysql as sql

con = sql.connect("localhost","root","","mysite")

c = con.cursor()

try :
    if c.execute("Select * from user where name = 'hari mohan' ") :
        info = c.fetchone()
        print(info)
    else :
        print("There is an error no user name found in the database")
except Exception as e:
    print("Error!! ",e)


