from django.conf.urls.defaults import * 
#from mysite.views import current_datetime,hours_ahead, display_meta
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#for admin use
urlpatterns = patterns('',
    (r'^admin/',include(admin.site.urls)),
)

#for views in root of mysite
urlpatterns += patterns('mysite.views',
    (r'^time/$', 'current_datetime'),
    (r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    (r'^who/$','display_meta'),
    (r'^getorpost/$', 'method_splitter',{'GET':'page_get','POST':'page_post'}),
    (r'^weibo/$','weibo'),
)

#for views in books
urlpatterns += patterns('mysite.books.views',
    (r'^search/$', 'search'),
)

#for views in contact
urlpatterns += patterns('mysite.contact.views',
    (r'^contact/$','contact'),
)
