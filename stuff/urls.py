import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^publication/', include('stuff.publications.urls')),
    (r'^file/', include('stuff.files.urls')),
    (r'^photo/', include('stuff.picasaweb.urls')),
    (r'^bookmark/', include('stuff.delicious.urls')),
    (r'^project/', include('stuff.projects.urls')),
    (r'^multimedia/', include('stuff.multimedia.urls')),
    (r'^git/', include('stuff.dit.urls')),
    # (r'^db/(.*)', databrowse.site.root),
    (r'^$', 'stuff.views.index'),

    # Media serving
    (r'^%smedia/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT,
     'show_indexes': True}
     ), 
    )

