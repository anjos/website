# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

# This you must set correctly
BASEDIR=$(shell pwd)
PYTHON=python

# This is automatic
PYTHON_VERSION=$(shell $(PYTHON) -c 'import sys; print "%d.%d" % sys.version_info[0:2]')
PYTHONPATH=$(BASEDIR)/sw/installed/lib/python$(PYTHON_VERSION)/site-packages
PY=PYTHONPATH=$(PYTHONPATH) $(PYTHON) 

PROC=$(shell ps awux | grep fcgi | grep python | grep -v ps | awk '{ print $$2 }')

all: deepclean compile restart

.PHONY: compile clean deepclean restart update

update:
	./bootstrap.sh

restart:
	@skill -9 $(PROC)
	
compile:
	$(PY) -c 'import compileall; compileall.compile_dir(".")'

clean: 	
	@find . -name '*~' -print0 | xargs -0 rm -vf 

deepclean: clean
	@find . -name '*.py?' -print0 | xargs -0 rm -vf

flup:
	$(PY) ./dispatch.fcgi
