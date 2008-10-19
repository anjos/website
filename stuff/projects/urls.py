from django.conf.urls.defaults import *
from django.views.generic import list_detail
from projects.models import Project, Download
from projects.feeds import * 
from projects.views import *

from settings import MEDIA_URL
from django.contrib.sites.models import Site

# the location of the site CSS
site = Site.objects.filter(id=1)[0]

feeds = dict()
feeds[LatestDownloadsForProject.basename] = LatestDownloadsForProject
feeds[LatestDeveloperDownloadsForProject.basename] = \
    LatestDeveloperDownloadsForProject 

all_feeds = dict(feeds)
all_feeds[SparkleUpdatesForProject.basename] = SparkleUpdatesForProject

project_list = { 'queryset': Project.objects.order_by('-date'),
                 'template_name': 'project_list.html',
                 'extra_context': {'site': site, 'media': MEDIA_URL},
               }

project_detail = { 'queryset': Project.objects.filter(),
                   'template_name': 'project_detail.html',
                   'extra_context': {'site': site, 'media': MEDIA_URL, 
                                     'feeds': feeds.values()},
                 }

download_detail = { 'queryset': Download.objects.filter(),
                    'template_name': 'download_detail.html',
                    'extra_context': {'site': site, 'media': MEDIA_URL},
                  }

notes_detail = { 'queryset': Download.objects.filter(),
                 'template_name': 'notes_detail.html',
                 'extra_context': {'site': site, 'media': MEDIA_URL},
               }

urlpatterns = patterns('',
                       (r'^$', list_detail.object_list, project_list),
                       (r'^(?P<object_id>\w+)/$', list_detail.object_detail,
                        project_detail),
                       (r'^feeds/(?P<url>.*)/$', 
                        'django.contrib.syndication.views.feed', 
                        {'feed_dict': all_feeds}),
                       (r'^dsakey/(?P<object_id>\w+)/$', projects_dsa_pubkey),
                       (r'^download/(?P<object_id>\d+)/$',
                         list_detail.object_detail, download_detail),  
                       (r'^notes/(?P<object_id>\d+)/$',
                         list_detail.object_detail, notes_detail),  
                       )

