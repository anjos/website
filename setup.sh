#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sun 28 Feb 20:48:07 2010
source sw/bin/activate
export BASEDIR=`pwd`/
export PATH=$HOME/sw:${PATH}
export DJANGO_SETTINGS_MODULE='project.settings'
