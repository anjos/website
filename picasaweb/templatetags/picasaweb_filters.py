#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Ter 01 Abr 2008 17:44:41 CEST 

from django.template import Library
from django.template.defaultfilters import stringfilter
import datetime

register = Library()

@register.filter
@stringfilter
def gd_date(value, arg):
  """Formats a Google Data style date into the format you want"""
  try:
    dt = datetime.datetime.strptime(value.split('.')[0], '%Y-%m-%dT%H:%M:%S')
  except:
    return value
  return dt.strftime(str(arg))
