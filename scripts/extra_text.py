#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sun 28 Feb 19:52:16 2010 

"""A bunch of methods that will be added to the boostrap script. Please refer
to the virtualenv homepage for the explanation on those.
"""

import os, sys, subprocess

SWURL = 'http://andreanjos.org/project/pypi/simple/'
PACKAGES = [
    'PIL', 
    'djpro', 
    'djangoogle',
    'nav', 
    'audit', 
    'uuid', 
    'flup', 
    'django-robots'
    ]

def after_install(options, home_dir):
  """After everything is installed, this function is called.
  
  At this point, we populate our environment with all our goods.
  """
  if sys.platform == 'win32': bin = 'Scripts'
  else: bin = 'bin'
  
  installer = [os.path.join(home_dir, bin, 'pip'), 'install']
  installer.append('--find-links=%s' % SWURL)
  if options.upgrade: installer.append('--upgrade')

  # a sequence of installs
  subprocess.call(installer + PACKAGES)

def extend_parser(parser):
  """Adds an upgrade option."""
  parser.add_option('-U', '--upgrade', action='store_true', dest='upgrade', 
    help='Use this if you want to upgrade instead of installing (default)')
