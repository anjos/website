#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Fri 17 Oct 09:36:48 2008 

"""Tags to help coding your templates.
"""

from django import template
register = template.Library()

from project.publications.models import Publication

# This will return the media necessary for publications
def publications_media(context): return context
register.inclusion_tag('publications/embed/media.html', takes_context=True)(publications_media)

@register.inclusion_tag('publications/embed/last_bubble.html')
def last_publications_bubble(n):
  """Puts out a bubble with the latest 'n' publications."""
  return {'objects': Publication.objects.order_by('-date')[:n]}

