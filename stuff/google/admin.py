#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Thu 24 Jul 16:05:17 2008 

from django.contrib import admin
from google.models import PicasawebAccount, Calendar, YouTubePlayList

# make it admin'able
class PicasawebAccountAdmin(admin.ModelAdmin):
  list_display = ('email', 'num_albums')
  list_filter = ['email']
  search_fields = ('date',)
  list_per_page = 10
  ordering = ['email']

admin.site.register(PicasawebAccount, PicasawebAccountAdmin)
admin.site.register(Calendar)
admin.site.register(YouTubePlayList)
