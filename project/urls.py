from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import djpro.urls
import audit.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^publication/', include('project.publications.urls', namespace='publications')),
    url(r'^google/', include('djangoogle.urls')),
    url(r'^project/', djpro.urls.namespaced),
    url(r'^audit/', audit.urls.namespaced),
    # url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', 
    #   {'sitemaps': sitemaps}),
    url(r'^robots.txt$', include('robots.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 
      'django.views.i18n.javascript_catalog'),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^$', 'project.views.index', name='project-index'),
    url(r'^login/$', 'project.views.login', name='login'), 
    url(r'^logout/$', 'project.views.logout', name='logout'),

    # Media serving
    url(r'^media/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT,
     'show_indexes': True},
     name='media',
     ), 
    )

