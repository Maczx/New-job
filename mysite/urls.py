from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/$','blog.views.home'),
    url(r'^admin/', include(admin.site.urls)),
)
