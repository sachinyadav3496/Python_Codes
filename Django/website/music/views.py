from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='bg-color:#123456'>Welcome to my first Music Website</h1>")
