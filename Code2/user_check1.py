#!C:/Python36/python.exe

import sys
import cgi,cgitb
import pymysql

cgitb.enable()

form = cgi.FieldStorage()

error = """
print("Content-Type:text/html")
print()
print("Error!!!")
print("</br>")
"""

#if ( 'name' in form ) and ( 'password' in form ) :
 #   user_name = form.getvalue('name')
#else :
 #   print(error)
    print("Error!!!No user name given ")
    sys.exit(1)
user_name=sachin
user_password=redhat
con = pymysql.connect("localhost","root","","mysite")
c = con.cursor()
c.execute("select * from user where name=user_name and password=user_password ")
info = c.fetchone()
con.close()

print("Content-Type:text/html\r\n")
print("</br>")
if info:
    s = """
<!Doctype html>
<html lang="en-us">
<head>
<title>MY_Login_TEST</title>
<h1>Let's See What you have Got Here - </h1>
</head>
<body bgcolor="#505050" text="EEEEEE">
<h2>Here is Your Information - </h2>
<p>ID = {0}</p>
<p>Name = {1}</p>
<p>Age = {2}</p>
<p>DOB = {3}</p>
<p>Language = {4}</p>
<p>Country = {5} </p>
</br>
    """.format(info[0],info[1],info[3],info[4],info[5],info[6])
    print(s)
else :
    f = open("C:\\xampp\\htdocs\\dashboard\\user_check.html")
    d = f.read()
    f.close()
