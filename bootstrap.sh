#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 04 Abr 2008 14:36:05 CEST

if [ $# = 0 ]; then
  echo "usage: $0 <python interpreter path>";
  exit 1;
fi

# Automatically set!
BASEDIR=`pwd`
PYTHON=$1
UPGRADE=''
python_version=`${PYTHON} -c 'import sys;print "%d.%d" % sys.version_info[0:2]'`
INSTALLDIR=${BASEDIR}/sw

# Versions
setuptools_egg=setuptools-0.6c9-py${python_version}.egg
setuptools=http://pypi.python.org/packages/${python_version}/s/setuptools/${setuptools_egg};
docutils=http://docutils.sourceforge.net/docutils-snapshot.tgz
django=django
gdata=gdata.py
etree=elementtree
feedparser=feedparser
textile=textile
uuid=uuid
imaging=http://effbot.org/media/downloads/Imaging-1.1.6.tar.gz
pysqlite2=http://oss.itsystementwicklung.de/download/pysqlite/2.5/2.5.5/pysqlite-2.5.5.tar.gz
pygments=pygments
gitpython=gitpython
pytz=pytz
flup=flup

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

export PYTHONPATH=${INSTALLDIR}

if [ -z `which easy_install-${python_version}` ]; then
  # We install the setuptools
  echo "### Installing ${setuptools_egg}..."
  wget ${setuptools} 
  sh ${setuptools_egg} --install-dir=${INSTALLDIR}
  rm -f ${setuptools_egg}
  export PATH=${INSTALLDIR}:${PATH}
  echo "### Installation of ${setuptools_egg} is done!"
fi

function install () {
  echo "### Installing $1..."
  easy_install-${python_version} ${UPGRADE} --install-dir=${INSTALLDIR} $2;
  echo "### Installation of $1 is done!"
}

function git_install () {
  echo "### Cloning $1..."
  git clone $2
  wdir=`basename $2 .git`
  install $1 $wdir
  echo "### Removing $wdir..."
  rm -rf $wdir
  echo "### Git based installation of $1 is done!"
}

install docutils ${docutils}
install django ${django}
install gdata ${gdata}
install elementTree ${etree}
install feedparser ${feedparser}
install textile ${textile}
install uuid ${uuid}
install pysqlite2 ${pysqlite2}
install pygments ${pygments}
install gitpython ${gitpython}
