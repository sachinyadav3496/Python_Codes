from django.shortcuts import render
def index(request):
    return render(request,'student/index.html')
def data(request,name='DON'):
    return render(request,'student/data.html',{'name':name})