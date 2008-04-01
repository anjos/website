from django.conf.urls.defaults import *
from django.views.generic import list_detail
from picasaweb.models import PicasawebAccount

from settings import MEDIA_URL
from django.contrib.sites.models import Site

# the location of the site CSS
css = MEDIA_URL + 'themed.css'
banner = MEDIA_URL + 'banner.jpg'
site = Site.objects.filter(id=1)[0]

user_list = { 'queryset': PicasawebAccount.objects.order_by('email'),
              'template_name': 'picasaweb_list.html',
              'extra_context': {'site': site, 'css': css, 'banner': banner },
            }

user_detail = { 'queryset': PicasawebAccount.objects.filter(),
                'template_name': 'picasaweb_detail.html',
                'extra_context': {'site': site, 'css': css, 'banner': banner },
              }

urlpatterns = patterns('',
                       (r'^$', 'picasaweb.views.view_gallery'),
                       (r'^list/$', list_detail.object_list, user_list),
                       (r'^(?P<object_id>\d+)/$', list_detail.object_detail,
                        user_detail),
                       )

