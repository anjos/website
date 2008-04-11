from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^$', 'picasaweb.views.view_gallery'),
                       (r'^(?P<id>\d+)/$', 'picasaweb.views.view_gallery'),
                       )

