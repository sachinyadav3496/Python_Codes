from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.index),
    path('data/',views.data),
    path('data/<str:name>',views.data)
]