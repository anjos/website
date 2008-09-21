from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^$', 'delicious.views.view_gallery'),
                       (r'^(?P<id>\d+)/$', 'delicious.views.view_gallery'),
                       )

