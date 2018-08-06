from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import bank
def home(request):
    return render(request,'myapp/home.html')

def hello(request):
    return render(request,'myapp/hello.html')

def bye(request):
    return HttpResponse("This is Bye")

def info(request):

    p1 = bank.objects.get(name='sachin')
    name = p1.name
    acc = p1.acc_no
    password = p1.password
    bal = p1.bal
    data = { 'name':name,'password':password,'Balance':bal,'Acc':acc }
    return render(request,'info.html',{ 'data': data })

