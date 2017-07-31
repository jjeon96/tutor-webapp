from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from accounts.views import (login_view, register_view, logout_view)
from . import views

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    # url(r'^comments/', include("comments.urls", namespace='comments')),
    
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    # url(r'^', include("posts.urls", namespace='posts')),
    #url(r'^posts/$', "<appname>.views.<function_name>"),

    url(r'^$', views.post_list, name='post_list')
]