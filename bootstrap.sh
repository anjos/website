#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 04 Abr 2008 14:36:05 CEST

# Automatically set!
BASEDIR=/home/rabello/website
PYTHON=python2.5

# This script will download and install all necessary software for us
[ ! -d sw/installed ] && mkdir -pv sw/installed;

# A few environment setups
python_version=`${PYTHON} -c 'import sys; print "python%d.%d" % sys.version_info[0:2]'`
export PYTHONPATH=`pwd`/sw/installed/lib/${python_version}/site-packages

# Versions
scons_version=0.98.0;
gdata_version=1.0.11.1;
etree_version=1.2.6-20050316;
feedparser_version=4.1;
pydelicious_version=0.5.0;
textile_version=2.0.11;

function target() {
  echo "Retrieving `basename $1`..."
  wget --quiet $1;
  tar xfz `basename $1`;
}
function zipget() {
  echo "Retrieving `basename $1`..."
  wget --quiet $1;
  unzip -qq `basename $1`;
}

function setup() {
  echo "Setting up $1..."
  cd $1;
  ${PYTHON} setup.py --quiet build;
  ${PYTHON} setup.py --quiet install --prefix=${BASEDIR}/sw/installed;
  cd -;
}

function svnup() {
  echo "Updating (svn) $1...";
  cd $1;
  svn --quiet update .;
  cd -;
}

# change to sw dir
pushd sw

# scons download and installation
if [ ! -d scons-${scons_version} ]; then
  target http://prdownloads.sourceforge.net/scons/scons-${scons_version}.tar.gz
fi
setup scons-${scons_version};

# django trunk
if [ ! -d django-trunk ]; then
  svn --quiet co http://code.djangoproject.com/svn/django/trunk django-trunk
else
  svnup django-trunk
fi
setup django-trunk
rm -f ../media/django;
ln -s ${BASEDIR}/sw/installed/lib/${python_version}/site-packages/django/contrib/admin/media ../media/django

# gdata
if [ ! -d gdata.py-${gdata_version} ]; then
  target http://gdata-python-client.googlecode.com/files/gdata.py-${gdata_version}.tar.gz
fi
setup gdata.py-${gdata_version} 

# element tree
if [ ! -d elementtree-${etree_version} ]; then
  target http://effbot.org/media/downloads/elementtree-${etree_version}.tar.gz
fi
setup elementtree-${etree_version}

# flup
if [ ! -d flup-trunk ]; then
  svn --quiet co http://svn.saddi.com/flup/trunk flup-trunk
else
  svnup flup-trunk
fi
setup flup-trunk 

# docutils trunk
if [ ! -d docutils-trunk ]; then
  svn --quiet co http://svn.berlios.de/svnroot/repos/docutils/trunk/docutils docutils-trunk
else
  svnup docutils-trunk;
fi
setup docutils-trunk

# feedparser (we need special code for this one)
if [ ! -d feedparser-${feedparser_version} ]; then
  wget --quiet http://feedparser.googlecode.com/files/feedparser-${feedparser_version}.zip
  mkdir feedparser-${feedparser_version};
  cd feedparser-${feedparser_version};
  unzip -qq ../feedparser-${feedparser_version}.zip;
  cd -;
fi
setup feedparser-${feedparser_version}

# pydelicious trunk
if [ ! -d pydelicious-${pydelicious_version} ]; then
  zipget http://pydelicious.googlecode.com/files/pydelicious-${pydelicious_version}.zip
fi
setup pydelicious-${pydelicious_version}

# textile 
if [ ! -d textile-${textile_version} ]; then
  target http://pytextile.googlecode.com/files/textile-${textile_version}.tar.gz
fi
setup textile-${textile_version}

popd
