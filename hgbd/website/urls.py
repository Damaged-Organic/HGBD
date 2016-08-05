# hgbd_project/hgbd/website/urls.py
from django.conf.urls import include, url

from . import views

app_name = 'website'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^service/(?P<id>[0-9]+)/(?P<slug>\w+)', views.service, name='service'
    ),
    url(r'^cooperation$', views.cooperation, name='cooperation'),
]
