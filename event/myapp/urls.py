__author__ = 'sachin yadav'

from django.urls import path
from . import views

urlpatterns = [

    path('home/',views.main,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('adduser/',views.adduser,name='adduser'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('base/',views.base,name='base'),

]