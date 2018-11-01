#!C:\\Anaconda3\\python.exe
import cgi,cgitb
cgitb.enable()
print("Content-type:text/html")
print("\n\n")
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')
check  = form.getvalue('check')

f = open('C:\\xampp\\htdocs\\mysite\\templates\\login.html')
page = f.read()
f.close()

page = page.format(username,password,check)

print(page)




