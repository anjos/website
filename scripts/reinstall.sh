#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Qui 18 Mar 2010 07:45:12 PDT
cd `dirname $0`/..
sw/bin/pip install --upgrade --no-dependencies --find-links=http://sw.andreanjos.org/git/simple/ $1
