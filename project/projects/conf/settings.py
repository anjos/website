#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Seg 12 Out 2009 11:32:00 CEST 

"""Settings for projects
"""
import os
from django.conf import settings

PROJECTS_GIT_BASE_DIRECTORY = getattr(settings, 'PROJECTS_GIT_BASE_DIRECTORY',
    os.path.join(os.environ['HOME'], 'git'))

