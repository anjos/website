#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 04 Abr 2008 14:36:05 CEST

# Automatically set!
BASEDIR=`pwd`
PYTHON=python
python_version=`${PYTHON} -c 'import sys;print "%d.%d" % sys.version_info[0:2]'`
INSTALLDIR=${BASEDIR}/sw

# Versions
setuptools_egg=setuptools-0.6c8-py${python_version}.egg
setuptools=http://pypi.python.org/packages/${python_version}/s/setuptools/${setuptools_egg};
docutils=http://docutils.sourceforge.net/docutils-snapshot.tgz
django=http://www.djangoproject.com/download/1.0/tarball/;
scons=http://prdownloads.sourceforge.net/scons/scons-1.0.1.tar.gz;
gdata=http://gdata-python-client.googlecode.com/files/gdata.py-1.1.1.tar.gz;
etree=http://effbot.org/media/downloads/elementtree-1.2.6-20050316.tar.gz
feedparser=http://feedparser.googlecode.com/files/feedparser-4.1.zip
textile=http://pypi.python.org/packages/source/t/textile/textile-2.0.11.tar.gz
pysqlite2=http://oss.itsystementwicklung.de/download/pysqlite/2.5/2.5.0/pysqlite-2.5.0.tar.gz

# This script will download and install all necessary software for us
if [ ! -d ${INSTALLDIR}-python${python_version} ]; then
  mkdir -pv ${INSTALLDIR}-python${python_version};
  cd `dirname ${INSTALLDIR}`;
  ln -s `basename ${INSTALLDIR}`-python${python_version} `basename ${INSTALLDIR}`;
fi

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
  easy_install-${python_version} --install-dir=${INSTALLDIR} $2;
  echo "### Installation of $1 is done!"
}

install docutils ${docutils}
install django ${django}
install scons ${scons}
install gdata ${gdata}
install elementTree ${etree}
install feedparser ${feedparser}
install textile ${textile}
install pysqlite2 ${pysqlite2}

