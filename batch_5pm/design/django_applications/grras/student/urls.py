from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.index),
    path('contact/',views.contact),
    #path('<str:name>/',views.data),
    path('login/',views.make_Login,name='student_login'),

]
