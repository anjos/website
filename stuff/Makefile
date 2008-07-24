# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

# This you must set correctly
BASEDIR=$(shell dirname `pwd`)
PYTHON=python

# This is automatic
PYTHON_VERSION=$(shell $(PYTHON) -c 'import sys; print "%d.%d" % sys.version_info[0:2]')
PYTHONPATH=$(BASEDIR)/sw/installed/lib/python$(PYTHON_VERSION)/site-packages

# Find my django projects
PROJECT=template files publications picasaweb

# These are helpers
PY=PYTHONPATH=$(PYTHONPATH) $(PYTHON)
MAKE_MESSAGE=$(PY) -m 'django.bin.make-messages'
COMPILE_MESSAGE=$(PY) -m 'django.bin.compile-messages'

.PHONY: clean 

# ACTION: Executes a simple cleanup (remove '~' files and pyc files) and then
# will compile the PO locale files.
all: clean build

# ACTION: Builds the PO locale files, by reading our source code and updating
# the existing message catalog. This will not compile the resulting PO source
# files.
msg: msg-en msg-pt_BR

# ACTION: This will literally compile the PO files into MO files, that can be
# loaded by your web application
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

# ACTION: validates django models and nothing else
validate:
	@echo "Validating django models..."
	$(PY) manage.py validate 

# ACTION: makes sure the existing DB schema is a reflection of what the current
# application models are
syncdb: validate
	@echo "Sychronizing database (initialize, if empty)..."
	$(PY) manage.py syncdb

# ACTION: prints the django help message
help: 
	$(PY) manage.py help

# ACTION: launches a python prompt with all our application and models
# available, excellent for prototyping filters
shell:
	$(PY) manage.py shell

# ACTION: this will actually validate, syncdb and start the development
# webserver, bound to port 8080 of your machine
test: validate syncdb
	@echo "Running python test server..."
	$(PY) manage.py runserver 8080

clean: 	
	find . -name '*~' -print0 | xargs -0 rm -vf 
	find . -name '*.py?' -print0 | xargs -0 rm -vf 
