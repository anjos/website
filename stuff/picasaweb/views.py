from django.shortcuts import render_to_response
from picasaweb.models import PicasawebAccount

import time, datetime
import locale

from settings import MEDIA_URL
from django.contrib.sites.models import Site

site = Site.objects.get_current()

def gd_date(s):
  """Converts a google data date representation into a real date"""
  return datetime.datetime(*(time.strptime(s.split('.')[0], '%Y-%m-%dT%H:%M:%S')[0:6]))

def get_locale(s):
  fields = s.split('-', 1)
  if len(fields) == 1: return locale.normalize(s) #nothing after the first dash
  return fields[0] + '_' + fields[1].upper()

def view_gallery(request, id=None):
  """Gives an overview of the whole available gallery"""
  locale.setlocale(locale.LC_ALL, get_locale(request.LANGUAGE_CODE))

  if not id:
    account = PicasawebAccount.objects.all()
    owner = None
  else:
    account = PicasawebAccount.objects.filter(id=id)
    owner = account[0].email
    
  entries = []
  usermap = {}
  for a in account:
    usermap[a.feed.user.text] = a.id
    for entry in a.feed.entry: #retrieves all data for this user
      dt = gd_date(entry.published.text)
      pos = 0
      for k in range(len(entries)):
        if entries[k][0] > dt: pos = k + 1
      entries.insert(pos, (dt, entry))
  entries = [k[1] for k in entries]

  return render_to_response('picasaweb_gallery.html', 
      {'entries': entries, 'site': site, 'media': MEDIA_URL,  
      'usermap': usermap, 'owner': owner})
