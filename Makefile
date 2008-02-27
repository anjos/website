# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

DJANGO=$$HOME/sw/django-trunk
MAKE_MESSAGE=$(DJANGO)/django/bin/make-messages.py
COMPILE_MESSAGE=$(DJANGO)/django/bin/compile-messages.py
PYTHONPATH=$(DJANGO)
PROJECT=template files publications

.PHONY: clean 

all: clean build-en build-pt_BR

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

clean: 	
	find . -name '*~' -print0 | xargs -0 rm -vf 
	find . -name '*.py?' -print0 | xargs -0 rm -vf 
