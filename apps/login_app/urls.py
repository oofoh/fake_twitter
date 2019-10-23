from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^register/new$', views.register_new),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout)
]