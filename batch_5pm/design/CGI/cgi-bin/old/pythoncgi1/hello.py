#!C:\\Anaconda3\\python.exe
print("Content-type:text/html")
print("\n")
#This is header to tell browser what type of data we are sending
page = """
<!Doctype>
<html>
<head>
<title>Hello Python</title>
<link rel='stylesheet' type='text/css' href='/python1/css/main.css'>
</head>
<body>
<h1>Hello Python CGi</h1>
<a href='/python1/'>Home</a>
<a href='/cgi-bin/pythoncgi1/index.py'>Python Home</a>
</body>
</html>
"""
print(page)
