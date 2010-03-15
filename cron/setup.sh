#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 03 Jul 2009 16:58:58 CEST

base=`dirname $0`/..
source $base/sw/bin/activate
export PYTHONPATH=$base:$base/project
export PATH=$base/cron:$PATH
