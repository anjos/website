from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^publication/', include('project.publications.urls')),
    #url(r'^google/', include('project.google.urls')),
    url(r'^project/', include('project.projects.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 
      'django.views.i18n.javascript_catalog'),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^$', 'project.views.index'),

    # Media serving
    url(r'^media/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT,
     'show_indexes': True},
     name='media',
     ), 
    )
