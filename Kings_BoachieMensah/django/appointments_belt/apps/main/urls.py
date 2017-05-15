from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^appointments$', views.create_user),
    url(r'^appointments/login$', views.login_user),
    url(r'^appointments/(?P<id>\d+)', views.update_appt),
]
