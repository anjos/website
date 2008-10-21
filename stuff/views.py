#!/usr/bin/env python
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Mon 13 Aug 2007 08:43:49 AM PDT 

from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
  return render_to_response('home.html',
                            context_instance=RequestContext(request))
