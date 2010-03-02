#!/usr/bin/env python
import os, sys

# Sets-up the environment 
if not os.environ.has_key('HOME'): os.environ['HOME'] = '/home/andreps' 
BASEDIR = os.path.join(os.environ['HOME'], 'andreanjos.org')
os.environ['BASEDIR'] = BASEDIR 

# Load the virtualenv
activate_this = os.path.join(BASEDIR, 'sw', 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

# Our time zone
os.environ['TZ'] = 'Europe/Zurich'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
