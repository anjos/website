#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 08 Ago 2008 15:35:48 CEST

export PATH=`pwd`/sw:${HOME}/sw/bin:${PATH}
export PYTHONPATH=`pwd`:`pwd`/sw:`pwd`/sw/PIL/lib/python:${PYTHONPATH}
export BASEDIR=`pwd`
export PYTHON=`which python2.5`
