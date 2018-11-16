from django.shortcuts import render

# Create your views here.
def index(request,name=None,id=None):
    return render(request,'faculty/index.html',{'name':name,'id':id})