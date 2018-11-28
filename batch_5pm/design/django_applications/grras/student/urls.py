from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.index),
    path('contact/',views.contact),
    #path('<str:name>/',views.data),
    path('signup/',views.Signup,name='student_signup'),
    path('login/',views.make_Login,name='student_login'),
    path('mksignup/',views.make_Signup,name='student_make_signup'),

]
