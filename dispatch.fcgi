#!/usr/bin/python2.5
BASEDIR = '/home/unidosps/new.unidosdegeneve.com' 
import os, sys, site

BASEDIR = os.path.join('/home/unidosps', 'new.unidosdegeneve.com') 

py = 'python%d.%d' % (sys.version_info[0], sys.version_info[1])
extras = os.path.join(BASEDIR,'sw-%s' % py)
pil = os.path.join(extras, 'PIL/lib/python')
site.addpackage(extras, 'easy-install.pth', set(sys.path))
site.addpackage(pil, 'PIL.pth', set(sys.path))
sys.path.insert(0, pil) #or django complains...

# for my django apps and project
sys.path.insert(0, BASEDIR)
sys.path.insert(0, extras)
sys.path.insert(0, os.path.join(BASEDIR, 'project'))

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "project.settings"
os.environ['BASEDIR'] = BASEDIR

# Our time zone
os.environ['TZ'] = 'Europe/Zurich'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
