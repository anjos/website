# This script is meant to be sourced
# You should make sure the DJANGO installment
# is available on the path bellow or the
# script will abort

# Andre Anjos <andre.dos.anjos@gmail.com>
# Original from 24th of March 2007

DJANGO=${HOME}/tmp/django;

if [ ! -d ${DJANGO} ]; then
  echo "The directory ${DJANGO} is not available. Check your installation!";
else
  export PATH=${DJANGO}/django/bin:${PATH};
  export PYTHONPATH=${DJANGO}:${PYTHONPATH};
fi

