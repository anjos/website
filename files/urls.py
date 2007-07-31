from django.conf.urls.defaults import *
from files.feeds import TenLastFilesUploaded

feeds = { 'latest': TenLastFilesUploaded, }

urlpatterns = patterns('',
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
     {'feed_dict': feeds}),
    )

