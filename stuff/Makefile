# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

# This you must set correctly
BASEDIR=/Users/andre/Sites/website
PYTHON=python2.5

# This is automatic
PYTHON_VERSION=$(shell $(PYTHON) -c 'import sys; print "python%d.%d" % sys.version_info[0:2]')
PYTHONPATH=$(BASEDIR)/sw/installed/lib/$(PYTHON_VERSION)/site-packages

# Find my django projects
PROJECT=template files publications picasaweb

# These are helpers
PY=PYTHONPATH=$(PYTHONPATH) $(PYTHON_VERSION)
MAKE_MESSAGE=$(PY) -m 'django.bin.make-messages'
COMPILE_MESSAGE=$(PY) -m 'django.bin.compile-messages'

.PHONY: clean 

all: clean build

msg: msg-en msg-pt_BR

build: build-en build-pt_BR

msg-%:
	@echo "Updating language files for '"$(@:msg-%=%)"'"
	@for p in $(PROJECT); do cd $$p; \
		echo "Updating subproject '"$$p"'..."; \
	  $(MAKE_MESSAGE) -l $(@:msg-%=%); \
		echo "Subproject '"$$p"' done."; \
		cd -; done

build-%:
	@echo "Compiling language files for '"$(@:msg-%=%)"'"
	@for p in $(PROJECT); do cd $$p; \
		echo "Compiling subproject '"$$p"'..."; \
	  $(COMPILE_MESSAGE); \
		echo "Subproject '"$$p"' done."; \
		cd -; done

validate:
	@echo "Validating django models..."
	$(PY) manage.py validate 

syncdb: validate
	@echo "Sychronizing database (initialize, if empty)..."
	$(PY) manage.py syncdb

help: 
	$(PY) manage.py help

shell:
	$(PY) manage.py shell

test: validate syncdb
	@echo "Running python test server..."
	$(PY) manage.py runserver 8080

clean: 	
	find . -name '*~' -print0 | xargs -0 rm -vf 
	find . -name '*.py?' -print0 | xargs -0 rm -vf 
