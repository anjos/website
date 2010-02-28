#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Mon 20 Oct 11:19:56 2008 

"""Context processors for standard things on every template rendering
"""

from django.contrib.sites.models import Site
from nav.models import Item

def site(request): 
  return {'site': Site.objects.get_current()}

def full_path(request):
  return {'full_path': request.get_full_path()}

def navigation(request):
  nav = Item.objects.filter(parent=None).exclude(name='Welcome').order_by('name')
  try:
    nav = [Item.objects.get(name='Welcome')] + list(nav)
  except:
    pass
  return {'navigation': nav} 
