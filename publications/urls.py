from django.conf.urls.defaults import *
from django.views.generic import list_detail
from publications.models import Publication

from settings import MEDIA_URL
from django.contrib.sites.models import Site

# urlpatterns = patterns('stuff.publications.views',
#                        (r'^$', 'index'),
#                        (r'^(?P<pub_id>\d+)/$', 'get'))

publication_list = { 'queryset': Publication.objects.all().order_by('-date'),
                     'extra_context': {'site_name': Site.objects.filter(id=1)[0].name,
                                       }
                     }

publication_detail = { 'queryset': Publication.objects.filter(),
                       'extra_context': {'site_name': Site.objects.filter(id=1)[0].name,
                                         'media_url': MEDIA_URL,
                                         }
                       }

urlpatterns = patterns('',
                       (r'^$', list_detail.object_list, publication_list),
                       (r'^(?P<object_id>\d+)/$', list_detail.object_detail, publication_detail),
                       )
