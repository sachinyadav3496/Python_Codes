from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.index),
    path('<str:name>/<int:id>',views.index),
]