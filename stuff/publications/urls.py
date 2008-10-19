from django.conf.urls.defaults import *
from django.views.generic import list_detail
from publications.models import Publication
from publications.feeds import * 

from settings import MEDIA_URL
from django.contrib.sites.models import Site

feeds = { LatestPublications.basename: LatestPublications, 
          LatestDocuments.basename   : LatestDocuments,
        }

site = Site.objects.get_current()

publication_list = { 'queryset': Publication.objects.order_by('-date'),
                     'template_name': 'publication_list.html',
                     'extra_context': {'site': site, 'media': MEDIA_URL,
                                       'feeds': feeds.values()},
                    }

publication_detail = { 'queryset': Publication.objects.filter(),
                       'template_name': 'publication_detail.html',
                       'extra_context': {'site': site, 'media': MEDIA_URL},
                       }

urlpatterns = patterns('',
                       (r'^$', list_detail.object_list, publication_list),
                       (r'^feeds/(?P<url>.*)/$', 
                        'django.contrib.syndication.views.feed', 
                        {'feed_dict': feeds}),
                       (r'^(?P<object_id>\d+)/$', list_detail.object_detail,
                        publication_detail),
                       )

