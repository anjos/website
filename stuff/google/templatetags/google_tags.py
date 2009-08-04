#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Seg 16 Mar 2009 18:32:11 CET 

"""Introduces tags to facilitate the placement of "album views"
"""

from django import template
from django.conf import settings
register = template.Library()

from google.models import *
from google.views import gd_date
import socket

@register.inclusion_tag('picasaweb_last.html')
def last_album():
  account = PicasawebAccount.objects.all()
  obj = None
  dt = None
  try:
    for a in account:
      if not a.last: continue
      tmp = gd_date(a.last.published.text) 
      if not obj or (tmp > dt): 
        obj = a.last
        dt = tmp
  except socket.gaierror:
    pass #working offline?
  return {'lastalbum': obj, 'MEDIA_URL': settings.MEDIA_URL}

@register.inclusion_tag('agenda_next.html')
def next_agenda_item():
  agendas = Calendar.objects.all()
  obj = None
  try:
    for a in agendas:
      if not a.next: continue
      if obj:
        if a.next < obj: obj = a.next
      else:
        obj = a.next
  except socket.gaierror:
    pass #working offline?
  return {'object': obj}

