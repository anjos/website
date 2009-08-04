from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url(r'^photos/$', 'google.views.view_gallery',
                         name='picasaweb-view'),
                       url(r'^videos/$', 'google.views.view_videos',
                         name='youtube-view'),
                       url(r'^photos/(?P<id>\d+)/$',
                         'google.views.view_gallery',
                         name='picasaweb-user-view'),
                       url(r'^videos/(?P<id>\d+)/(?P<index>\d+)/$',
                         'google.views.view_video',
                         name='youtube-view-video'),
                       url(r'^agenda/$', 'google.views.view_agenda',
                         name='agenda-view'),
                       )

