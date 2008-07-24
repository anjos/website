#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Thu 24 Jul 16:02:03 2008 

from django.contrib import admin
from files.models import File 

class FileAdmin(admin.ModelAdmin):
  list_display = ('name', 'date', 'public')
  list_filter = ['date']
  search_fields = ['name', 'date']
  date_hierarchy = 'date'
  list_per_page = 10
  ordering = ['-date']

admin.site.register(File, FileAdmin)
