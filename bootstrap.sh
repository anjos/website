#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 04 Abr 2008 14:36:05 CEST

if [ $# -gt 0 ]; then
  echo "usage: $0";
  exit 1;
fi

# Load base definitions
source ./setup.sh

# Automatically set!
python_version=`${PYTHON} -c 'import sys;print "%d.%d" % sys.version_info[0:2]'`

# This script will download and install all necessary software for us
[ -r sw ] && rm -f sw;
if [ -d ${INSTALLDIR}-python${python_version} ]; then
  echo "Directory ${INSTALLDIR}-python${python_version} exists. Upgrade only."
  echo "If you need re-installing, remove the 'sw\*' directories manually."
  UPGRADE='--upgrade'
else
  mkdir -pv ${INSTALLDIR}-python${python_version};
fi
cd `dirname ${INSTALLDIR}`;
ln -s `basename ${INSTALLDIR}`-python${python_version} `basename ${INSTALLDIR}`;

setuptools_egg=setuptools-0.6c9-py${python_version}.egg
setuptools=http://pypi.python.org/packages/${python_version}/s/setuptools/${setuptools_egg};

if [ -z `which easy_install-${python_version}` ]; then
  # We install the setuptools
  echo "### Installing ${setuptools_egg}..."
  wget ${setuptools} 
  sh ${setuptools_egg} --install-dir=${INSTALLDIR}
  rm -f ${setuptools_egg}
  export PATH=${INSTALLDIR}:${PATH}
  echo "### Installation of ${setuptools_egg} is done!"
fi

install docutils docutils 
install django django
install gdata gdata
install textile textile
install uuid uuid
install pygments pygments
install gitpython gitpython
install pytz pytz
install flup flup

install pil --find-links http://www.pythonware.com/products/pil/ ${imaging}
# This fixes the PIL installation for Django
if [ ! -e ${INSTALLDIR}/PIL ]; then
  cd ${INSTALLDIR};
  ln -s PIL-* PIL;
  cd -;
fi

# some projects of mine
git_install djangoogle andreanjos@git.andreanjos.org:git/djangoogle.git
git_install audit andreanjos@git.andreanjos.org:git/audit.git
git_install nav andreanjos@git.andreanjos.org:git/nav.git
