from django.conf.urls.defaults import *
from django.views.generic import list_detail
from multimedia.views import *

urlpatterns = patterns('',
                       (r'^$', multimedia_public), 
                       (r'^press$', multimedia_public), 
                       (r'^personal$', multimedia_personal),
                       (r'^other$', multimedia_other),
                       #(r'^feeds/(?P<url>.*)/$', 
                       # 'django.contrib.syndication.views.feed', 
                       # {'feed_dict': feeds}),
                      )

