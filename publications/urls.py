from django.conf.urls.defaults import *
from django.views.generic import list_detail
from publications.models import Publication
from publications.feeds import TenLastPublications

from settings import MEDIA_URL
from django.contrib.sites.models import Site

feeds = { 'latest': TenLastPublications, }

# the location of the site CSS
css = MEDIA_URL + 'themed.css'
banner = MEDIA_URL + 'banner.jpg'
site = Site.objects.filter(id=1)[0]

# urlpatterns = patterns('publications.views',
#                        (r'^$', 'index'),
#                        (r'^(?P<pub_id>\d+)/$', 'get'))

publication_list = { 'queryset': Publication.objects.order_by('-date'),
                     'template_name': 'list.html',
                     'extra_context': {'site': site, 'css': css, 'banner': banner },
                     }

publication_detail = { 'queryset': Publication.objects.filter(),
                       'template_name': 'detail.html',
                       'extra_context': {'site': site, 'css': css, 'banner': banner },
                       }

urlpatterns = patterns('',
                       (r'^$', list_detail.object_list, publication_list),
                       (r'^feeds/(?P<url>.*)/$', 
                        'django.contrib.syndication.views.feed', 
                        {'feed_dict': feeds}),
                       (r'^(?P<object_id>\d+)/$', list_detail.object_detail,
                        publication_detail),
                       )

