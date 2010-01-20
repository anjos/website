from django.conf.urls.defaults import *
from django.views.generic import list_detail
from publications.models import Publication
from publications.feeds import * 
from publications.views import * 

feeds = { LatestPublications.basename: LatestPublications, 
          LatestFiles.basename   : LatestFiles,
        }

publication_detail = { 'queryset': Publication.objects.filter(),
                       'template_name': 'publications/detail.html',
                     }

urlpatterns = patterns('',
                       url(r'^$', short_list, name='short_list'),
                       url(r'^year/$', publications_by_year, name='list'),
                       url(r'^list/$', simple_list, name='simple_list'),
                       url(r'^feeds/(?P<url>.*)/$',
                        'django.contrib.syndication.views.feed', 
                        {'feed_dict': feeds}),
                       url(r'^(?P<object_id>\d+)/$', list_detail.object_detail,
                        publication_detail),
                      )

