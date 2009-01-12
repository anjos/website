#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Thu 20 Nov 11:41:27 2008 

"""Specialized views for publications.
"""

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat  as _cat
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponsePermanentRedirect
from django.core.exceptions import ObjectDoesNotExist

from multimedia.models import File, Embedded, Item

def multimedia_file_by_category(request, category=None):
  """A personalized listing of multimedia files, by category."""
  
  if category:
    object_list = list(File.objects.filter(category=category).order_by('-date')) + list(Embedded.objects.filter(category=category).order_by('-date'))
    title = [k[1] for k in Item.category_choices if k[0] == category]
    if title: title = title[0]
    else: title = _(u'Undefined category (%s)' % category)
  else:
    object_list = list(File.objects.order_by('-date')) + \
      list(Embedded.objects.order_by('-date'))
    title = u'Multimedia Files'

  object_list.sort(key=lambda obj: obj.date, reverse=True) 

  return render_to_response('media_list.html',
                            {'object_list': object_list, 
                             'feeds': [],
                             'show_category': not bool(category),
                             'title': title,
                            },
                            context_instance=RequestContext(request))

def multimedia_all(request):
  return multimedia_file_by_category(request) 

def multimedia_public(request):
  return multimedia_file_by_category(request, 'M') 

def multimedia_personal(request):
  return multimedia_file_by_category(request, 'P') 

def multimedia_other(request):
  return multimedia_file_by_category(request, 'V') 

def multimedia_detail(request, object_id):
  object = Item(id=object_id) 

  # we try to convert the generic Item into the specific type
  try: object = object.file
  except ObjectDoesNotExist: pass
  else: 
    return HttpResponsePermanentRedirect(object.data.url)

  try: object = object.embedded
  except ObjectDoesNotExist: raise
  else:
    # current object is an embedded item, show a nice page to display it.
    return render_to_response('media_embedded.html',
                              {'object': object,
                               'title': object.name,
                              },
                              context_instance=RequestContext(request))

