from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.create),
    url(r'^result$', views.show)
]
