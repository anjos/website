#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Mon 30 Jun 2014 14:37:53 CEST

"""Procedures to clean-up unused app information
"""

def main():

  import os
  import sys

  if len(sys.argv) <= 1:
    print "usage: %s [-d|--debug] <app> [<app>...]"
    sys.exit(1)
  elif sys.argv[1] in ('-h', '--help'):
    print "usage: %s [-d|--debug] <app> [<app>...]"
    sys.exit(0)

  os.environ['DJANGO_SETTINGS_MODULE'] = 'anjos.website.settings'

  from django.contrib.contenttypes.models import ContentType
  from nav.models import Item

  debug = False
  if sys.argv[1] in ('-d', '--debug'):
    debug = True
    del sys.argv[1]

  for app in sys.argv[1:]:

    print "\nDeleting obsolete django content types and permissions for `%s'...\n" % (app,)

    for k in ContentType.objects.filter(app_label=app):
      if debug:
        print '[debug] would delete: %s %s@%s (%s)' % (k.id, k.model, k.app_label, k.name)
      else:
        print 'deleting: %s %s@%s (%s)' % (k.id, k.model, k.app_label, k.name)
        k.delete()

    print "\nDeleting menu entries related to `%s'...\n" % (app,)
    for k in Item.objects.filter(url__contains=app):
      if debug:
        print '[debug] would delete: %s %s' % (k.id, k.url)
      else:
        print 'deleting: %s %s' % (k.id, k.url)
        k.delete()
