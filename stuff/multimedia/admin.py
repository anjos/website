#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Thu 24 Jul 15:36:10 2008 

from django.contrib import admin
from multimedia.models import Item,Embedded,File

class ItemAdmin(admin.ModelAdmin):
  pass

class EmbeddedAdmin(admin.ModelAdmin):
  list_display = ('name', 'date', 'category')
  list_filter = ['date']
  search_fields = ['name', 'date']
  date_hierarchy = 'date'
  list_per_page = 10
  ordering = ['-date']

class FileAdmin(admin.ModelAdmin):
  list_display = ('name', 'date', 'public', 'category')
  list_filter = ['date']
  search_fields = ['name', 'date']
  date_hierarchy = 'date'
  list_per_page = 10
  ordering = ['-date']

admin.site.register(Item, ItemAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Embedded, EmbeddedAdmin)
