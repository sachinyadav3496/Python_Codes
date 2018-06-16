from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"personal/home.html")
def my(request):
    return render(request,"personal/my.jpg")
def contact(request):
    return render(request,"personal/basic.html",{'info':['if you want to email me, please contace','sachinyadav3496@gmail.com']})
