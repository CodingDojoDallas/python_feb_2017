from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.create_user),
    url(r'^success$', views.success),
    url(r'^sessions$',views.login_user),

]
