#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Fri 17 Oct 09:36:48 2008 

"""Tags to help coding your templates.
"""

from django import template
register = template.Library()
from django.conf import settings

from project.publications.models import Publication

# This will return the media necessary for publications
@register.inclusion_tag('publications/embed/media_widgets.html')
def publications_widgets_media(url=settings.MEDIA_URL):
  return {'MEDIA_URL': url}

@register.inclusion_tag('publications/embed/media.html')
def publications_media(url=settings.MEDIA_URL):
  return {'MEDIA_URL': url}

@register.inclusion_tag('publications/embed/last_bubble.html')
def last_publications_bubble(n, include_header):
  """Puts out a bubble with the latest 'n' publications."""
  return {'objects': Publication.objects.order_by('-date')[:n],
          'include_header': include_header}

