from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.ninjas),
    url(r'^ninjas/(?P<color>\w+)$', views.colors)
]