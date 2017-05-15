from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add),
    url(r'^delete/(?P<id>\d)$', views.delete),
    url(r'^destroy/(?P<id>\d)$', views.destroy),
]
