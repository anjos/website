#!/usr/bin/env python2.3
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Mon Sep 15 14:08:01 PDT 2008

import sys, os

try:
  INTERP = "/usr/bin/python2.4"
  if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

  base = '/home/andreanjos/andre.adois.org'

  for f in os.listdir(base + '/sw'):
    egg = os.sep.join([base + '/sw', f])
    if f[-4:] == '.egg': sys.path.insert(0, egg)

  # Two extras for Django
  sys.path.insert(0, base + '/stuff')
  sys.path.insert(0, base)

  os.environ['BASEDIR']=os.path.realpath(base)
  os.environ['DJANGO_SETTINGS_MODULE']='stuff.settings'

  import django.core.handlers.wsgi
  application = django.core.handlers.wsgi.WSGIHandler()

except Exception, e:
  
  def application(environ, start_response):
    write = start_response('200 OK', [('Content-type', 'text/plain')])
    return ["Exception caught!\n** Here is the output:\n%s\n** Your sys.path is:\n%s" % (e, '\n'.join(sys.path))]
