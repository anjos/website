#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Thu 24 Jul 15:36:10 2008 

from django.contrib import admin
from projects.models import Project, Download
from django.utils.translation import ugettext_lazy as _

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('name', 'date', 'vc_url', 'wiki_page', 'count_downloads')
  list_filter = ['date']
  list_per_page = 10
  ordering = ['-date']
  search_fields = ['name', 'date', 'vc_url']
  date_hierarchy = 'date'
    
admin.site.register(Project, ProjectAdmin)

class DownloadAdmin(admin.ModelAdmin):
  list_display = ('name', 'date', 'public', 'size', 'md5', 'project')
  list_filter = ['date']
  search_fields = ['name', 'date']
  date_hierarchy = 'date'
  list_per_page = 10
  ordering = ['-date']

admin.site.register(Download, DownloadAdmin)
