#!C:\\Anaconda3\\python.exe
import cgi,cgitb
import pymysql as sql
cgitb.enable()
import os

print("Content-type:text/html")
print("\n")
data = os.environ['HTTP_COOKIE']
print(data)
print("Type of Cookes ",type(data))
print("Functions of data = ",dir(data))

form = cgi.FieldStorage()
name = form.getvalue('username')
password = form.getvalue('password')

try :
    db = sql.connect(host='localhost',port=3306,user='root',password='',database='pythoncgi')
    c = db.cursor()
    cmd = "select * from user where name='{}'".format(name)
    c.execute(cmd)
    data = c.fetchone()
    name = data[0]
    p = data[1]
    first_name = data[2]
    last_name = data[3]
    email = data[4]
    if p == password :
        print("Set-Cookie:username={};".format(name))
        print("Set-Cookie:password={};".format(password))
        print("Set-Cookie:Expires=Wednesday, 08-Aug-2018 10:30:00 GMT;")
        print("Content-type:text/html")
        print("\n\n")

        page = """
        <!Doctype html>
        <html>
        <head>
            <title>login</title>
            <link rel='stylesheet' type='text/css' href='/python1/css/main.css'>
        </head>
        <body>
            <h1 style='color:red'>Welcome mr. {0} </h1>
            <h1 style='color:blue'>Your Details is as follow</h1>
            <table>
            <th>Details</th>
            <tr>
                <td>Name</td>
                <td>First Name</td>
                <td>Last Name </td>
                <td>Email </td>
            </tr>

            <tr>
                <td>{0}</td>
                <td>{1}</td>
                <td>{2}</td>
                <td>{3}</td>
            </tr>
        </body>
        </html>
        """.format(name,first_name,last_name,email)

        print(page)
    else :
        print("Content-type:text/html")
        print("\n\n")
        print("<h1 style='color:red'>Invalid Entry </h1>")
        print("<a href='/python1/'>Home</a>")
except Exception as e :
    print("Content-type:text/html")
    print("\n\n")
    print("<h1 style='color:red'>No such user Exist</h1>")
    print("<a href='/python1/'>Home</a>")
