from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')
    #return HttpResponse("<h1 style='color:red'>Welcome first web page powered by django</h1>")