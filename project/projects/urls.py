from django.conf.urls.defaults import *
from django.views.generic import list_detail
from projects.models import Project, Download
from projects.feeds import * 
from projects.views import *

feeds = dict()
feeds[LatestDownloadsForProject.basename] = LatestDownloadsForProject
feeds[LatestDeveloperDownloadsForProject.basename] = \
    LatestDeveloperDownloadsForProject 

all_feeds = dict(feeds)
all_feeds[SparkleUpdatesForProject.basename] = SparkleUpdatesForProject

project_list = { 'queryset': Project.objects.order_by('-date'),
                 'template_name': 'projects/list.html',
               }

project_detail = { 'queryset': Project.objects.filter(),
                   'template_name': 'projects/detail.html',
                   'extra_context': {'feeds': feeds.values()},
                 }

download_detail = { 'queryset': Download.objects.filter(),
                    'template_name': 'projects/download_detail.html',
                  }

notes_detail = { 'queryset': Download.objects.filter(),
                 'template_name': 'projects/notes_detail.html',
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

