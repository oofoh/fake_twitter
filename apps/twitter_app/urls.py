from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home_page),
    url(r'^explore$', views.explore_page),
    url(r'^profile/(?P<profile_name>\w+)$', views.profile_page),
    url(r'^messages$', views.messages_page),
    url(r'^notifications$', views.notif_page),
    url(r'^settings$', views.settings_page)
]