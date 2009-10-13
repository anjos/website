#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Thu 24 Jul 15:36:10 2008 

from django.contrib import admin
from projects.models import Project, Download, Screenshot, Icon
from django.utils.translation import ugettext_lazy as _

def count_all_downloads(instance):
  return instance.download_set.count()
count_all_downloads.short_description = _(u'Downloads')

def count_downloads(instance):
  return instance.download_set.filter(development=True).count()
count_downloads.short_description = _(u'Public downloads')

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('name', 'updated_on', 'git_dir', 'wiki_page', count_downloads, count_all_downloads)
  list_filter = ['updated', 'name']
  list_per_page = 10
  ordering = ['-updated']
  search_fields = ['name', 'date', 'git_dir']
  date_hierarchy = 'date'
    
admin.site.register(Project, ProjectAdmin)

class DownloadAdmin(admin.ModelAdmin):
  list_display = ('name', 'date', 'development', 'project')
  list_filter = ['name', 'date', 'project']
  search_fields = ['name', 'date', 'project']
  date_hierarchy = 'date'
  list_per_page = 10
  ordering = ['-date']

class ScreenshotAdmin(admin.ModelAdmin):
  list_display = ('name', 'date', 'project')
  list_filter = ['name', 'date', 'project']
  search_fields = ['name', 'date', 'project']
  date_hierarchy = 'date'
  list_per_page = 10
  ordering = ['-date']

class IconAdmin(admin.ModelAdmin):
  list_display = ('name', 'date', 'project')
  list_filter = ['name', 'date', 'project']
  search_fields = ['name', 'date', 'project']
  date_hierarchy = 'date'
  list_per_page = 10
  ordering = ['-date']

admin.site.register(Download, DownloadAdmin)
admin.site.register(Screenshot, ScreenshotAdmin)
admin.site.register(Icon)
