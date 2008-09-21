#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Thu 24 Jul 16:05:17 2008 

from django.contrib import admin
from delicious.models import DeliciousAccount 

# make it admin'able
class DeliciousAccountAdmin(admin.ModelAdmin):
  list_display = ('account', 'num_posts')
  list_filter = ['account']
  search_fields = ('account',)
  list_per_page = 10
  ordering = ['account']

admin.site.register(DeliciousAccount, DeliciousAccountAdmin)
