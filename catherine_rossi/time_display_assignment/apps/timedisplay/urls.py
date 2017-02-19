from django.conf.urls import url

from . import views

#my routes!

urlpatterns = [
    url(r'^$', views.index), #my routes go here. Be sure to separate each route w/ a comma
    #followed by the controller (second argument)
    # This will call the index method of the views controller

]
