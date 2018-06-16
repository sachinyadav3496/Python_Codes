__author__ = 'sachin yadav'

from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    return render(request,'home/home.html')

