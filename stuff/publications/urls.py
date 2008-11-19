from django.conf.urls.defaults import *
from django.views.generic import list_detail
from publications.models import Publication
from publications.feeds import * 
from publications.views import * 

feeds = { LatestPublications.basename: LatestPublications, 
          LatestDocuments.basename   : LatestDocuments,
        }

publication_detail = { 'queryset': Publication.objects.filter(),
                       'template_name': 'publication_detail.html',
                     }

urlpatterns = patterns('',
                       (r'^$', publications_by_year),
                       (r'^feeds/(?P<url>.*)/$', 
                        'django.contrib.syndication.views.feed', 
                        {'feed_dict': feeds}),
                       (r'^(?P<object_id>\d+)/$', list_detail.object_detail,
                        publication_detail),
                      )

