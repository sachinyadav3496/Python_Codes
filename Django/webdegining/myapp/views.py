from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
s = """<!Doctype html>
<html>
<head>
<title>home_page</title>
</head>
<body>
<h1>Hey this is my first webpage by django</h1>
<h2>It is awesome</h2>
</body>
</html>
"""

def index(request):
    return HttpResponse(s)
def hello(request):
    return HttpResponse("hello world to django")


def image(request):
    return render(request,"image/home.html")

