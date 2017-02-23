from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sessions$', views.login_user),
    url(r'^books_dashboard$', views.books_dashboard),
    url(r'^books/new$', views.books_new),
    url(r'^books$', views.create_book),
    url(r'^logout$', views.logout),
    url(r'^books/(?P<id>\d+)$', views.books_show),
    url(r'^reviews/(?P<id>\d+)$', views.create_review),
    url(r'^users/(?P<id>\d+)$', views.users_show),
]