#!/usr/bin/python

import os, sys
sw = os.path.realpath('.')
py = 'python%d.%d' % (sys.version_info[0], sys.version_info[1])
sys.path.insert(0, os.path.join(sw, 'sw/installed/lib/%s/site-packages' % py))
sys.path.insert(0, sw)
sys.path.insert(0, os.path.join(sw, 'stuff'))

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
