#!/home/andreps/andreanjos.org/sw/bin/python

import os, sys

# Sets-up the environment 
if not os.environ.has_key('HOME'): os.environ['HOME'] = '/home/andreps' 

# We add our basic software directory
os.environ['PATH'] = ':'.join([os.path.join(os.environ['HOME'], 'sw', 'bin'), os.environ['PATH']])

BASEDIR = os.path.join(os.environ['HOME'], 'andreanjos.org')
os.environ['BASEDIR'] = BASEDIR 

# This is the only missing path we need to add
sys.path += [BASEDIR, os.path.join(BASEDIR, 'project')]

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

# Our time zone
os.environ['TZ'] = 'Europe/Zurich'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
