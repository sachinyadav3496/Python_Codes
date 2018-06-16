__author__ = 'sachin yadav'
from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.mklogin,name='mklogin'),
]