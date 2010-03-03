#!/usr/bin/env python

# The first thing to do is to replace this interpreter with a new one
import os, sys
base = os.path.realpath(os.path.dirname(__file__))
wanted = os.path.join(base, 'sw', 'bin', 'python')

if wanted != sys.executable:
  # replace the interpreter in this case, please note execle() will not return!
  os.execle(wanted, wanted, os.path.realpath(__file__), os.environ)

# Sets-up the environment
os.environ.setdefault('HOME', '/home/andreps')
home_bin = os.path.join(os.environ['HOME'], 'sw', 'bin')
os.environ['PATH'] = ':'.join([home_bin, os.environ.get('PATH', '')])
sys.path.insert(0, os.path.join(base, 'project'))

# Our time zone
os.environ['TZ'] = 'Europe/Zurich'

# Sets up django w/o setting more environment variables
from django.core.management import setup_environ
import settings
setup_environ(settings)

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
