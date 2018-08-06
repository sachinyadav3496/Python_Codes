from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
s = """
Content-type:text/html

<html>
<head>
<title>first page</title>
<h1>Welcome to mysite</h1>
</head>
<body>
<h2>This is for test site </h2>
<h3>My name is sachin yadav </h3>
</body>
</html>"""
def index(request):
    return HttpResponse(s)
