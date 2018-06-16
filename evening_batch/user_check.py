#!C:/Python36/python.exe

import sys
import cgi,cgitb
import pymysql

"""#cgitb.enable()



#form = cgi.FieldStorage()


if 'name' in form :
    user_name = form.getvalue('name')
else :
    print("Content-Type:text/html")
    print()
    print("</br>")
    print("Error!!!No user name given ")
    sys.exit(1)


if 'password' in form :
    user_password = form.getvalue('password')
else :
    print("Content-Type:text/html")
    print()
    print("</br>")
    print("Error!!! No password is given ")
    sys.exit(1)
    """

con = pymysql.connect("localhost","root","","mysite")
c = con.cursor()
c.execute("select * from user ")
data = c.fetchall()
user_name=input("Enter user name - ")
user_password=input("Enter password - ")
f = 0

for var in data:
    if user_name in var :
        if user_password == var[2] :
            f = 1
            info = var



print("Content-Type:text/html\r\n")
print("</br>")
if f == 1 :

    s = """
<!Doctype html>
<html lang="en-us">
<head>
<title>MY_Login_TEST</title>
<h1>Let's See What you have Got Here - </h1>
</head>
<body bgcolor="#808080">
<h2>Here is Your Information - </h2>
<p>ID = {0}</p>
<p>Name = {1}</p>
<p>Age = {2}</p>
<p>DOB = {3}</p>
<p>Language = {4}</p>
<p>Country = {5} </p>
</br>
""".format(info[1],info[0],info[3],info[4],info[5],info[6])
    print(s)
else :
    print("Error!!! No such user Exist in Our System</br>Check your username and password and try again ")

