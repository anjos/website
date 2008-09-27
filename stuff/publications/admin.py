#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Thu 24 Jul 15:36:10 2008 

from django.contrib import admin
from publications.models import Publication, Document
from django.utils.translation import ugettext_lazy as _

class PublicationAdmin(admin.ModelAdmin):
  list_display = ('title', 'date', 'pub_type', 'has_abstract', 
      'count_documents')
  list_filter = ['date']
  list_per_page = 10
  ordering = ['-date']
  search_fields = ['title', 'date', 'media']
  date_hierarchy = 'date'
  fieldsets = (
      (None, {'fields': ('title', 'date', 'author_list', 
                         ('pub_type', 'media'),
                         ('volume', 'number', 'pages'), 
                         'abstract')}),
  )
    
admin.site.register(Publication, PublicationAdmin)

class DocumentAdmin(admin.ModelAdmin):
  list_display = ('name', 'date', 'public', 'md5', 'publication')
  list_filter = ['date']
  search_fields = ['name', 'date']
  date_hierarchy = 'date'
  list_per_page = 10
  ordering = ['-date']

admin.site.register(Document, DocumentAdmin)
