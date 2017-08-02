from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.stub, name='stub'),
    url(r'^post_list$', views.post_list, name='post_list'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$',views.login,name='login'),
    url(r'^omfg$', views.omfg, name ='omfg'),
]
