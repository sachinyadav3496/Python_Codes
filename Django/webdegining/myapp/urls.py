from django.conf.urls import url
from . import views 

urlpatterns = [
        url(r'^$',views.index,name='index'),
        url(r'^hello/',views.hello,name='hello'),
        url(r'^my/',views.image,name='image'),
        ]
