from django.shortcuts import render_to_response
from picasaweb.models import PicasawebAccount

import datetime

from settings import MEDIA_URL
from django.contrib.sites.models import Site

# the location of the site CSS
css = MEDIA_URL + 'themed.css'
banner = MEDIA_URL + 'banner.jpg'
site = Site.objects.filter(id=1)[0]

def gd_date(s):
  """Converts a google data date representation into a real date"""
  try:
    return datetime.datetime.strptime(s.split('.')[0], '%Y-%m-%dT%H:%M:%S')
  except:
    return s

def view_gallery(request):
  """Gives an overview of the whole available gallery"""
  account = PicasawebAccount.objects.all()
  entries = []
  for a in account:
    for entry in a.feed.entry: #retrieves all data for this user
      dt = gd_date(entry.published.text)
      pos = 0
      for k in range(len(entries)):
        if entries[k][0] > dt: pos = k + 1
      entries.insert(pos, (dt, entry))
  entries = [k[1] for k in entries]

  return render_to_response('picasaweb_gallery.html', 
      {'entries': entries, 'site': site, 'css': css, 'banner': banner })
