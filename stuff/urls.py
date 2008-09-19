import settings
from django.conf.urls.defaults import *
from django.contrib import admin

# databrowse capabilities to our stuff
# from django.contrib import databrowse
# from stuff.publications.models import Publication
# databrowse.site.register(Publication)

# authentication required for databrowsing
# from django.contrib.auth.decorators import login_required

admin.autodiscover()

subdir = ''
urlpatterns = patterns('',
    (r'^%sadmin/(.*)' % subdir, admin.site.root),
    (r'^%spublication/' % subdir, include('stuff.publications.urls')),
    (r'^%sfile/' % subdir, include('stuff.files.urls')),
    (r'^%sphoto/' % subdir, include('stuff.picasaweb.urls')),
    (r'^%sbookmark/' % subdir, include('stuff.delicious.urls')),
    # (r'^%sdb/(.*)' % subdir, databrowse.site.root),
    (r'^%s$' % subdir, 'stuff.views.index'),

    # Media serving
    (r'^%smedia/(?P<path>.*)$' % subdir,
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT,
     'show_indexes': True}
     ), 
    )

