#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Thu 20 Nov 11:41:27 2008 

"""Specialized views for google apps.
"""

from django.shortcuts import render_to_response
from django.template import RequestContext
from google.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage

import time
import datetime
import locale
import socket

def get_locale(s, enc=None):
  s.replace('-','_')

  fields = s.split('-', 1)
  if len(fields) == 1: return locale.normalize(s) #nothing after the first dash
  if enc: return locale.normalize('_'.join(fields) + '.' + enc)
  return locale.normalize('_'.join(fields))

def view_gallery(request, id=None):
  """Gives an overview of the whole available gallery"""
  try:
    # we try to set the current locale to something that is better
    newloc = locale.normalize(request.LANGUAGE_CODE.replace('-','_')+'.utf8')
    locale.setlocale(locale.LC_ALL, newloc)
  except locale.Error:
    # we simply ignore otherwise, and leave it be
    pass

  if not id:
    account = PicasawebAccount.objects.all()
    owner = None
  else:
    account = PicasawebAccount.objects.filter(id=id)
    owner = account[0].email
    
  entries = []
  usermap = {}

  try:
    for a in account:
      usermap[a.feed.user.text] = a.id
      for entry in a.feed.entry: #retrieves all data for this user
        dt = gd_date(entry.published.text)
        pos = 0
        for k in range(len(entries)):
          if entries[k][0] > dt: pos = k + 1
        entries.insert(pos, (dt, entry))
    entries = [k[1] for k in entries]
  except socket.gaierror:
    pass #working offline?

  paginator = Paginator(entries, 9)

  # Make sure page request is an int. If not, deliver first page.
  try: page = int(request.GET.get('page', '1'))
  except ValueError: page = 1

  # If page request (9999) is out of range, deliver last page of results.
  try: now = paginator.page(page)
  except (EmptyPage, InvalidPage): now = paginator.page(paginator.num_pages)

  return render_to_response('picasaweb_gallery.html', 
                            {'objects': now, 
                             'usermap': usermap, 
                             'owner': owner},
                            context_instance=RequestContext(request))

def view_videos(request):
  """Gives an overview of the whole available video gallery"""
  try:
    # we try to set the current locale to something that is better
    newloc = locale.normalize(request.LANGUAGE_CODE.replace('-','_')+'.utf8')
    locale.setlocale(locale.LC_ALL, newloc)
  except locale.Error:
    # we simply ignore otherwise, and leave it be
    pass

  playlists = YouTubePlayList.objects.all()
    
  entries = []

  try:
    for p in playlists: entries += p.sorted
  except socket.gaierror:
    pass #working offline?
  entries.sort(reverse=True)

  paginator = Paginator(entries, 4)

  # Make sure page request is an int. If not, deliver first page.
  try: page = int(request.GET.get('page', '1'))
  except ValueError: page = 1

  # If page request (9999) is out of range, deliver last page of results.
  try: now = paginator.page(page)
  except (EmptyPage, InvalidPage): now = paginator.page(paginator.num_pages)

  return render_to_response('youtube_gallery.html', 
                            {'objects': now,}, 
                            context_instance=RequestContext(request))

def view_video(request, id, index):
  """Shows a single video"""
    
  playlist = YouTubePlayList.objects.get(id=id)
  try:
    object = playlist.sorted[int(index)] 
  except socket.gaierror:
    pass #working offline?

  return render_to_response('youtube_video.html', 
                            {'object': object,}, 
                            context_instance=RequestContext(request))

def view_agenda(request):
  """Gives an overview of the whole agenda"""
  try:
    # we try to set the current locale to something that is better
    newloc = locale.normalize(request.LANGUAGE_CODE.replace('-','_')+'.utf8')
    locale.setlocale(locale.LC_ALL, newloc)
  except locale.Error:
    # we simply ignore otherwise, and leave it be
    pass

  account = Calendar.objects.get(id=1)
  entries = []
  feed = None
  try:
    entries = [CalendarEntry(k) for k in account.feed.entry]
    feed = account.feed
  except socket.gaierror:
    pass #working offline?

  return render_to_response('agenda_entries.html', 
                            {
                             'feed': feed, 
                             'entries': sorted(entries)
                            },
                            context_instance=RequestContext(request))
