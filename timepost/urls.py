from django.conf import settings
from django.conf.urls import include, url
# from django.contrib.auth import views
from . import views

urlpatterns = [
    url(r'^ajax/timepost_create/$', views.timepost_create, name='timepost_create'),

]