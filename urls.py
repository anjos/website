import stuff.settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       # Uncomment this for admin:
                       (r'^admin/', include('django.contrib.admin.urls')),
                       
                       (r'^publication/', include('stuff.publications.urls')),
                       
                       # Media serving
                       (r'^archive/(?P<path>.*)$',
                        'django.views.static.serve',
                        {'document_root': stuff.settings.MEDIA_ROOT,
                        'show_indexes': True}
                        ), 
)
