import settings
from django.conf.urls.defaults import *
subdir = 'andre/'

urlpatterns = patterns('',
    (r'^%sadmin/' % subdir, include('django.contrib.admin.urls')),
    (r'^%spublication/' % subdir, include('stuff.publications.urls')),
    (r'^%sfile/' % subdir, include('stuff.files.urls')),
    (r'^%sphoto/' % subdir, include('stuff.picasaweb.urls')),
    (r'^%s$' % subdir, 'stuff.views.index'),

    # Media serving
    #(r'^archive/(?P<path>.*)$',
    # 'django.views.static.serve',
    # {'document_root': settings.MEDIA_ROOT,
    # 'show_indexes': True}
    # ), 
    )
