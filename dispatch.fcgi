#!/usr/bin/python2.5
import os, sys, site

BASEDIR = os.path.join('/home/andreps', 'andreanjos.org')
os.environ['BASEDIR'] = BASEDIR 
py = 'python%d.%d' % (sys.version_info[0], sys.version_info[1])
INSTALLDIR = os.path.join(BASEDIR,'sw-%s' % py)
os.environ['INSTALLDIR'] = INSTALLDIR
site.addpackage(INSTALLDIR, 'easy-install.pth', set(sys.path))

sys.path.insert(0, BASEDIR)
sys.path.insert(0, INSTALLDIR)
sys.path.insert(0, os.path.join(BASEDIR, 'project'))

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

# Our time zone
os.environ['TZ'] = 'Europe/Zurich'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
