from django.conf.urls.defaults import *

urlpatterns = patterns('stuff.publications.views',
                       (r'^$', 'index'),
                       (r'^(?P<pub_id>\d+)/$', 'get'))
