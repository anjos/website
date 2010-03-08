from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import djpro.urls
import audit.urls
import publications.urls
import djangoogle.urls
import djit.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^publication/', publications.urls.namespaced),
    url(r'^google/', djangoogle.urls.namespaced),
    url(r'^git/', djit.urls.namespaced),
    url(r'^project/', djpro.urls.namespaced),
    url(r'^audit/', audit.urls.namespaced),
    url(r'^openid/', include('django_openid_auth.urls')),
    # url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', 
    #   {'sitemaps': sitemaps}),
    url(r'^robots.txt$', include('robots.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/(?P<packages>\S+?)/$', 
      'django.views.i18n.javascript_catalog'),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^$', 'project.views.index', name='project-index'),
    url(r'^about/$', 'project.views.about', name='project-about'),
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

