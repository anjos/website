import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

subdir = 'andre/'
urlpatterns = patterns('',
    (r'^%sadmin/(.*)' % subdir, admin.site.root),
    (r'^%spublication/' % subdir, include('stuff.publications.urls')),
    (r'^%sfile/' % subdir, include('stuff.files.urls')),
    (r'^%sphoto/' % subdir, include('stuff.picasaweb.urls')),
    (r'^%s$' % subdir, 'stuff.views.index'),

    # Media serving
    (r'^%smedia/(?P<path>.*)$' % subdir,
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT,
     'show_indexes': True}
     ), 
    )
