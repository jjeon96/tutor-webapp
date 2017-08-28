from django.conf import settings
from django.conf.urls import include, url
# from django.conf.urls.static import static
# from django.conf.urls.static import static
# Add this import
from django.contrib.auth import views
from log.forms import UserLoginForm
from log.views import (login_view, register_view, logout_view, update_view)
from . import views

urlpatterns = [
    url(r'^ajax/timepost_create/$', views.timepost_create, name='timepost_create'),
]