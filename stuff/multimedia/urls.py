from django.conf.urls.defaults import *
from django.views.generic import list_detail
from multimedia.views import *

urlpatterns = patterns('',
                       (r'^$', multimedia_all), 
                       (r'^press$', multimedia_public), 
                       (r'^personal$', multimedia_personal),
                       (r'^other$', multimedia_other),
                       (r'^(?P<object_id>\d+)/$', multimedia_detail),
                       #(r'^feeds/(?P<url>.*)/$', 
                       # 'django.contrib.syndication.views.feed', 
                       # {'feed_dict': feeds}),
                      )

