from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', admin.site.urls),
    (r'^publication/', include('stuff.publications.urls')),
    (r'^google/', include('stuff.google.urls')),
    (r'^project/', include('stuff.projects.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    (r'^$', 'stuff.views.index'),

    # Media serving
    (r'^media/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT,
     'show_indexes': True}
     ), 
    )

