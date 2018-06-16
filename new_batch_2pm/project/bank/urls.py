__author__ = 'sachin yadav'
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('signup/',views.signup),
    path('mysignup/',views.mysignup),
    path('login/',views.login)


]