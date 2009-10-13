#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Fri 17 Oct 09:36:48 2008 

"""Specialized views for projects.
"""

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from projects.models import Project, Download

def projects_dsa_pubkey(request, slug):
  """View the DSA public key of project as a downloadable file"""
  try:
    p = Project.objects.get(slug=slug)
  except: 
    raise ObjectDoesNotExist

  return HttpResponse(p.dsa_pubkey, mimetype="text/plain")

