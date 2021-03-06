from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = "core"

urlpatterns = [
    url(r'^$', views.intro, name='intro'),

    url('^demo/', views.demo_login, name='demo_login'),
    url('^register/', views.register, name='register'),
    url('^logout/', auth_views.logout, name='logout', kwargs={'next_page': '/'}),

    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^account/$', views.account, name='account'),
    url(r'^search/$', views.search, name='search'),

    url(r'^series/start/$', views.watching_start, name='watching_start'),
    url(r'^series/(?P<watching_id>\d+)/$', views.watching, name='watching'),
    url(r'^series/(?P<watching_id>\d+)/seen/$', views.watching_seen, name='watching_seen'),
    url(r'^series/(?P<watching_id>\d+)/status/$', views.watching_status, name='watching_status'),
    url(r'^series/(?P<watching_id>\d+)/stop/$', views.watching_stop, name='watching_stop'),
]
