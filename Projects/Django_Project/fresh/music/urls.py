from django.conf.urls import url
from . import views
app_name = 'music'

urlpatterns = [
        url(r'^$',views.index,name='index'),
        url(r'^(?P<album_id>[0-9]+)/$',views.details,name="detail"),
        url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favourite,name="favourite"),
        ]
