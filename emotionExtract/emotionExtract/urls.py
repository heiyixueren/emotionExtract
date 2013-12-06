#-*-coding:utf-8-*-
from django.conf.urls import patterns, include, url
from emotionExtract import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'emotionExtract.views.home', name='home'),
    # url(r'^emotionExtract/', include('emotionExtract.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^getMsg/',views.getMsg),      #get wanted message,including keywords,emotion
    url(r'^',views.openIndexPage),      #open the index page if the url is null
)
