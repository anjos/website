#!/usr/bin/env python
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Mon 13 Aug 2007 08:43:49 AM PDT 

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout as django_logout
from django.contrib.auth.views import login as django_login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
  return render_to_response('home.html',
                            context_instance=RequestContext(request))

def login(request):
  return django_login(request, template_name='admin/login.html')

def logout(request):
  django_logout(request)
  if request.GET.has_key('next'): 
    next = request.GET['next']
  else: 
    next = reverse('project-index')
  if not next.strip(): next = '/'
  return HttpResponseRedirect(next)
