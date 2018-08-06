from django.http import HttpResponse
from django.shortcuts import render 


page = """<!Doctype html>

<html lang='en-us'>

<body bg-color='#808080'>
<h1>Welcome to Django Home Page</h1>
<h2>Hello World!! </h2>
<h3>Django is Awesome</h3>

</body>
</html>
"""

def index(request):

    return HttpResponse(page)


