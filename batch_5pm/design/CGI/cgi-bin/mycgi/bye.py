#!C:\\Anaconda3\\python.exe
print("Content-type:text/html")
print("\n\n")

f = open('C:\\xampp\\htdocs\\mysite\\templates\\bye.html')
page = f.read()
f.close()
print(page)