# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

PROC=$(shell ps awux | grep fcgi | grep python2.4 | grep -v ps | awk '{ print $$2 }')

all: deepclean compile restart

.PHONY: compile clean deepclean restart update

update:
	./bootstrap.sh
	cd stuff && svn update . && cd -

restart:
	@skill -9 $(PROC)
	
compile:
	@python2.4 -c 'import compileall; compileall.compile_dir(".")'

clean: 	
	@find . -name '*~' -print0 | xargs -0 rm -vf 

deepclean: clean
	@find . -name '*.py?' -print0 | xargs -0 rm -vf
