from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.create_user),
    url(r'^login$', views.login_user),
    url(r'^quotes$', views.main_page),
    url(r'^logout$', views.logout_user),
    url(r'^add_quote$', views.add_quote),
    url(r'^users/(?P<id>\d+)$', views.user_page),
    url(r'^add_favorite$', views.add_favorite),
    url(r'^destroy_favorite$', views.destroy_favorite),
]
