#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 08 Ago 2008 15:35:48 CEST

export BASEDIR=`pwd`
export INSTALLDIR=${BASEDIR}/sw
export PATH=${INSTALLDIR}:${HOME}/sw/bin:${PATH}
export PYTHONPATH=${BASEDIR}:${INSTALLDIR}:${PYTHONPATH}
export PYTHON=`which python2.5`
export DJANGO_SETTINGS_MODULE='project.settings'

# Common maintenance functions
source ./functions.sh
