#!C:\\Anaconda3\\python.exe
from random import randint,choice
print("Content-type:text/html")
print("\n\n")
start_page = """
<!Doctype html>
<html>
<head>
<link rel='stylesheet' type='text/css' href='/mysite/css/main.css'>
</head>
<body>
<h1>Hello World in Broser use CGI Script in Python</h1>
<p>See how easy it is</p>
<p>rest you know all python</p>

"""
l = [ 'hi','hello','bye','bye bye','good','bad']
print(f"<h2>{choice(l)}</h2>")
print(start_page)
print("<ol style='color:red'>")
for var in range(1,randint(8,15)):
        print("<li>")
        print("*"*var)
        print("</li>")
print("</ol>")

end_page = """
</body>
</html>
"""
print(end_page)