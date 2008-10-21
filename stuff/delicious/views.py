from django.shortcuts import render_to_response
from delicious.models import DeliciousAccount

import datetime
import locale

def gd_date(s):
  """Converts a delicious date representation into a real date"""
  return datetime.datetime(*s[0:6])

def get_locale(s):
  fields = s.split('-', 1)
  if len(fields) == 1: return locale.normalize(s) #nothing after the first dash
  return fields[0] + '_' + fields[1].upper()

def view_gallery(request, id=None):
  """Gives an overview of the whole available gallery"""
  locale.setlocale(locale.LC_ALL, get_locale(request.LANGUAGE_CODE))

  if not id:
    account = DeliciousAccount.objects.all()
    owner = None
  else:
    account = DeliciousAccount.objects.filter(id=id)
    owner = account[0].account
    
  entries = []
  for a in account:
    for entry in a.feed.entries: #retrieves all data for this user
      dt = gd_date(entry.updated_parsed)
      pos = 0
      for k in range(len(entries)):
        if entries[k][0] > dt: pos = k + 1
      entries.insert(pos, (dt, entry))
  entries = [k[1] for k in entries]

  return render_to_response('delicious_gallery.html', 
      {'entries': entries, 'owner': owner})
