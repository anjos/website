#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 11 Abr 2008 14:39:42 CEST

if [ $# = 0 ]; then
  echo "usage: $0 python-executable-name"
  exit 1
fi

function replace () {
  #1. what, 
  #2. newvalue, 
  #3. file
  echo "Changing file $3...";
  sed -e "s%^$1\(\s*\)=\(\s*\).*%$1\1=\2$2%" -i '~' $3
}

for f in bootstrap.sh Makefile stuff/Makefile; do
  replace PYTHON $1 $f
done

for f in stuff/Makefile; do
  replace BASEDIR $PWD $f
done

for f in stuff/settings.py; do
  replace BASEDIR "'$PWD/stuff'" $f
done

