# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

DJANGO=$$HOME/sw/django-trunk
ETREE=$$HOME/sw/elementtree-1.2.6-20050316
GDATA=$$HOME/sw/gdata.py-1.0.11.1/src
MAKE_MESSAGE=$(DJANGO)/django/bin/make-messages.py
COMPILE_MESSAGE=$(DJANGO)/django/bin/compile-messages.py
PYTHONPATH=$(DJANGO):$(ETREE):$(GDATA)
PROJECT=template files publications picasaweb
PYTHON=PYTHONPATH=$(PYTHONPATH) python2.4

.PHONY: clean 

all: clean msg-en build-en msg-pt_BR build-pt_BR

msg-%:
	@echo "Updating language files for '"$(@:msg-%=%)"'"
	@for p in $(PROJECT); do cd $$p; \
		echo "Updating subproject '"$$p"'..."; \
	  PYTHONPATH=$(PYTHONPATH) $(MAKE_MESSAGE) -l $(@:msg-%=%); \
		echo "Subproject '"$$p"' done."; \
		cd -; done

build-%:
	@echo "Compiling language files for '"$(@:msg-%=%)"'"
	@for p in $(PROJECT); do cd $$p; \
		echo "Compiling subproject '"$$p"'..."; \
	  PYTHONPATH=$(PYTHONPATH) $(COMPILE_MESSAGE); \
		echo "Subproject '"$$p"' done."; \
		cd -; done

validate:
	@echo "Validating django models..."
	$(PYTHON) manage.py validate 

syncdb: validate
	@echo "Sychronizing database (initialize, if empty)..."
	$(PYTHON) manage.py syncdb

help: 
	$(PYTHON) manage.py help

shell:
	$(PYTHON) manage.py shell

test: validate syncdb
	@echo "Running python test server..."
	$(PYTHON) manage.py runserver 8080

clean: 	
	find . -name '*~' -print0 | xargs -0 rm -vf 
	find . -name '*.py?' -print0 | xargs -0 rm -vf 
