from django.conf.urls.defaults import *
from django.views.generic import list_detail
from projects.models import Project 

from settings import MEDIA_URL
from django.contrib.sites.models import Site

# the location of the site CSS
site = Site.objects.filter(id=1)[0]

project_list = { 'queryset': Project.objects.order_by('-date'),
                 'template_name': 'project_list.html',
                 'extra_context': {'site': site, 'media': MEDIA_URL},
               }

project_detail = { 'queryset': Project.objects.filter(),
                   'template_name': 'project_detail.html',
                   'extra_context': {'site': site, 'media': MEDIA_URL},
                 }

urlpatterns = patterns('',
                       (r'^$', list_detail.object_list, project_list),
                       (r'^(?P<object_id>\d+)/$', list_detail.object_detail,
                        project_detail),
                       )

