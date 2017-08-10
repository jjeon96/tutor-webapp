from django.conf import settings
from django.conf.urls import include, url
# from django.conf.urls.static import static
from django.contrib import admin
# from django.conf.urls.static import static
# Add this import
from django.contrib.auth import views
from log.forms import UserLoginForm
from log.views import (login_view, register_view, logout_view)
from . import views
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'', include('log.urls')),
#     # url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
#     url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': UserLoginForm}, name='login'),
#     url(r'^logout/$', views.logout, {'next_page': '/login'},name='logout'),
# ]


urlpatterns = [

    # url(r'^comments/', include("comments.urls", namespace='comments')),

    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    # url(r'^', include("posts.urls", namespace='posts')),
    #url(r'^posts/$', "<appname>.views.<function_name>"),

    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^filter/$', views.post_filter, name='post_filter'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
