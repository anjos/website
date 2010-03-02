#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 04 Abr 2008 14:36:05 CEST

if [ $# != 1 ]; then
  echo "usage: $0 <installdir>";
  exit 1;
fi

# Base environment definitions
export PYTHONPATH=$1
export PATH=$1:${PATH}

# Automatically set!
python_version=`python -c 'import sys;print "%d.%d" % sys.version_info[0:2]'`

# We only do a fresh install if the $1 directory is not there...
if [ ! -d $1 ]; then

  mkdir -p $1;

  setuptools_egg=setuptools-0.6c11-py${python_version}.egg
  setuptools=http://pypi.python.org/packages/${python_version}/s/setuptools/${setuptools_egg};

  # We install the setuptools
  echo "### Installing 'virtualenv'..."
  wget ${setuptools} 
  sh ${setuptools_egg} --install-dir=$1
  rm -f ${setuptools_egg}
  easy_install-${python_version} --install-dir=$1 --quiet virtualenv;

else

  # In this case we only try an upgrade
  echo "### Trying a 'virtualenv' upgrade..."
  easy_install-${python_version} --install-dir=$1 --upgrade --quiet virtualenv;

fi

# Now we generate the bootstrap script 
echo "### Generating bootstrap..."
python ./make_bootstrap.py bootstrap.py ./extra_text.py
chmod 755 ./bootstrap.py
echo "### Done!"

exit 0;
