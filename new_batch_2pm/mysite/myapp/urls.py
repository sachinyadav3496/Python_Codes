__author__ = 'sachin yadav'
from django.urls import path
from django.http import HttpResponse
from . import views
urlpatterns = [
    path('',views.home),
    path('hello/',views.hello),
    path('bye/',views.bye),
    path('info/',views.info)
]