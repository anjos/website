#!/usr/bin/env python
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Mon 13 Aug 2007 08:43:49 AM PDT 

from django.shortcuts import render_to_response
from settings import MEDIA_URL

from django.contrib.sites.models import Site
site = Site.objects.get_current()

def index(request):
  return render_to_response('home.html', {'site': site, 
                                          'media': MEDIA_URL})
