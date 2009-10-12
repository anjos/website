# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

# Find my django projects
PROJECT=publications projects templates

# These are helpers
MAKE_MESSAGE=django-admin.py makemessages
COMPILE_MESSAGE=django-admin.py compilemessages
LANGUAGES=en pt_BR fr es

.PHONY: simpleclean clean 

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
	@for p in $(PROJECT); do cd $$p; \
		echo "Compiling subproject '"$$p"'..."; \
	  $(COMPILE_MESSAGE); \
		echo "Subproject '"$$p"' done."; \
		cd -; done
	@echo "Compiling 'project'..."; $(COMPILE_MESSAGE); echo "Project done."; 

# ACTION: validates django models and nothing else
validate:
	@echo "Validating django models..."
	$(PYTHON) manage.py validate 

# ACTION: makes sure the existing DB schema is a reflection of what the current
# application models are
syncdb: validate
	@echo "Sychronizing database (initialize, if empty)..."
	$(PYTHON) manage.py syncdb

# ACTION: prints the django help message
help: 
	$(PYTHON) manage.py help

# ACTION: launches a python prompt with all our application and models
# available, excellent for prototyping filters
shell:
	$(PYTHON) manage.py shell

# ACTION: goes into the database shell so you can edit things manually 
dbshell:
	$(PYTHON) manage.py dbshell

# ACTION: this will actually validate, syncdb and start the development
# webserver, bound to port 8080 of your machine
test: build validate syncdb
	@echo "Running python test server..."
	$(PYTHON) manage.py runserver 8080

# ACTION: spawns a test SMTP server
smtp:
	@echo "Spawing test SMTP server at localhost:1025..."
	$(PYTHON) -m smtpd -n -c DebuggingServer localhost:1025

clean: simpleclean	
	$(PYTHON) -m compileall .

simpleclean:
	find . -name '*~' -print0 | xargs -0 rm -vf 
	find . -name '*.py?' -print0 | xargs -0 rm -vf
