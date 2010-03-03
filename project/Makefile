# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

# Find my django projects
PROJECT=publications templates
LANGUAGES=en pt_BR fr es

MAKE_MESSAGE=django-admin.py makemessages
COMPILE_MESSAGE=django-admin.py compilemessages

# These are helpers

.PHONY: mrproper clean 

# ACTION: Executes a simple cleanup (remove '~' files and pyc files) and then
# will compile the PO locale files.
all: build

# ACTION: Builds the PO locale files, by reading our source code and updating
# the existing message catalog. This will not compile the resulting PO source
# files.
msg:
	@for p in $(PROJECT); do cd $$p; \
		echo "Updating subproject '"$$p"'..."; \
		for l in $(LANGUAGES); do [ ! -d locale/$$l ] && mkdir -pv locale/$$l;done;\
	  $(MAKE_MESSAGE) --all --extension=html,py,txt; \
		echo "Subproject '"$$p"' done."; \
		cd -; \
	done

# ACTION: This will literally compile the PO files into MO files, that can be
# loaded by your web application
build:
	@echo "Compiling language files"
	@for p in $(PROJECT); do \
		[ ! -d $$p/locale ] && continue; \
		cd $$p; \
		echo "Compiling subproject '"$$p"'..."; \
		$(COMPILE_MESSAGE); \
		echo 'Subproject '$$p' done.'; \
		cd -; \
	done
	@if [ -d locale ]; then echo "Compiling 'project'..."; $(COMPILE_MESSAGE); echo "Project done."; fi

validate:
	./manage.py validate

syncdb: validate
	./manage.py syncdb

shell:
	./manage.py shell

dbshell:
	./manage.py dbshell

test: build validate syncdb
	./manage.py runserver 8080

smtp:
	python -m smtpd -n -c DebuggingServer localhost:1025

clean: mrproper
	python -m compileall .

mrproper:
	find . -name '*~' -print0 | xargs -0 rm -vf 
	find . -name '*.py?' -print0 | xargs -0 rm -vf
