#!C:\\Anaconda3\\python.exe
import pymysql as sql
import cgi,cgitb
cgitb.enable()

data = cgi.FieldStorage()

name = data.getvalue('username')
pas = data.getvalue('password')
fname = data.getvalue('fname')
lname = data.getvalue('lname')
email = data.getvalue('email')
print("Content-type:text/html")
print("\n\n")

try :
    db = sql.connect(host='localhost',port=3306,user='pythoncgi',password='pythoncgi',database='pythoncgi')
    c = db.cursor()
    cmd = "insert into user values('{}','{}','{}','{}','{}')".format(name,pas,fname,lname,email)
    c.execute(cmd)
    db.commit()
    c.close()
    db.close()
    print("<h1 style='color:red'>Your Account Sucessfully Created Please Login</h1>")
    print("<a href='/python1/login.html'>Login</a>")
except Exception as e :
    print("<h1 style='color:red'>Invalid Form Data <br />Error!! {}</h1>".format(e))
    print("<a href='/python1/signup.html>Signup</a>")
