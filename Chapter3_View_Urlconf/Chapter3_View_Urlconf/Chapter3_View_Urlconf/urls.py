from django.conf.urls import patterns, include, url
from views import hours_ahead
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Chapter3_View_Urlconf.views.home', name='home'),
    # url(r'^Chapter3_View_Urlconf/', include('Chapter3_View_Urlconf.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)
