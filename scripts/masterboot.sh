#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Ter 02 Mar 2010 09:42:18 PST

# This will bootstrap the website in case it is not available for accepting
# package requests through its PyPI interface

function get_head() {
  wget "http://git.andreanjos.org/?p=$1/.git;a=snapshot;h=refs/heads/master;sf=tgz" -O $1-master.tar.gz
  tar xvfz $1-master.tar.gz
  cd $1 && tar cvfz ../$1-master.tar.gz * && cd -
  rm -rf $1
}

get_head djpro
get_head audit
get_head djangoogle
get_head nav
pip install ./djpro-master.tar.gz ./audit-master.tar.gz ./djangoogle-master.tar.gz ./nav-master.tar.gz PIL uuid flup django-robots
rm -rf *-master*
