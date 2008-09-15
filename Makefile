# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

# This you must set correctly
PYTHON=python2.4
PROC=$(shell ps awux | grep fcgi | grep $(PYTHON) | grep -v ps | awk '{ print $$2 }')

all: clean restart

.PHONY: clean restart 

restart:
	@skill -9 $(PROC)
	
clean: 	
	@find . -name '*~' -print0 | xargs -0 rm -vf 
