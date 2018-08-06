from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
def index(request):

    return HttpResponse("welcome to Django Site")

def year_archive(request,year):

    a_list = Article.objects.filter(pub_date__year=year)

    context = { 'year': year, 'article_list':a_list}
    return render(request,'news/year_archive.html',context)

def month_archive(request,year,month):

    a_list = Article.objects.filter(pub_date__month=month)
    context = { 'year':year, 'article_list':a_list}
    return render(request,'news/year_archive.html',context)

def article_detail(request,year,month,pk):
    a_list = Article.objects.filter(pub_date__month=month)
    context = { 'year':year, 'article_list':a_list}
    return render(request,'news/year_archive.html',context)