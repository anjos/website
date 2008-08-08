#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 08 Ago 2008 15:35:48 CEST

export PATH=`pwd`/sw/installed/bin:${PATH}
export LD_LIBRARY_PATH=`pwd`/sw/installed/lib:${LD_LIBRARY_PATH}
export PYTHONPATH=`pwd`:`pwd`/sw/installed/lib/python2.5/site-packages:`pwd`/sw/installed/lib/scons-0.98.5:${PYTHONPATH}
export MANPATH=`pwd`/sw/installed/man:${MANPATH}
