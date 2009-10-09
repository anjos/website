#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Qui 01 Out 2009 15:42:10 CEST

function install () {
  local package=$1; shift 1;
  echo "### Installing ${package}..."
  easy_install-${python_version} ${UPGRADE} --install-dir=${INSTALLDIR} $*;
  echo "### Installation of ${package} is done!"
}

function pilinstall () {
  local start=`pwd`
  echo "### Installing PIL..."
  cd ${INSTALLDIR};
  wget $1;
  local project=`basename $1 .tar.gz`;
  tar xvfz ${project}.tar.gz;
  cd ${project}
  ${PYTHON} setup.py build;
  ${PYTHON} setup.py install --home=${INSTALLDIR}/PIL
  cd ${INSTALLDIR};
  rm -rf ${project} `basename $1`;
  cd ${start}
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

function hg_install () {
  echo "### Cloning $1..."
  wdir=`basename $2`
  hg clone $2
  install $1 $wdir
  echo "### Removing $wdir..."
  rm -rf $wdir
  [ $# = 3 ] && ln -s $1 $3 #optional
  echo "### Mercurial based installation of $1 is done!"
}

function svndl () {
  if [ -d ${INSTALLDIR}/$1 ]; then
    echo "### Updating SVN checkout for package $1..."
    cd ${INSTALLDIR}/$1 && svn update .
  else
    cd ${INSTALLDIR}
    echo "### Checking-out for package $1..."
    svn co $2 $1
    [ $# = 3 ] && ln -s $1 $3 #optional
  fi
  cd -
}

