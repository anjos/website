# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

# Find my django projects and set some important variables
LANGUAGES=en pt_BR fr es
BIN=../sw/bin

# A few helpers -- don't modify!
python=$(BIN)/python
admin=PYTHONPATH=..:. $(BIN)/django-admin.py $(1) --settings=settings
admin_cd=cd $(1);\
	for l in $(LANGUAGES); do [ ! -d locale/$$l ] && mkdir -pv locale/$$l; done;\
  PYTHONPATH=../..:.. ../$(BIN)/django-admin.py $(2) --settings=settings;\
	cd -

# These are helpers

.PHONY: mrproper clean 

# ACTION: Executes a simple cleanup (remove '~' files and pyc files) and then
# will compile the PO locale files.
all: compile

# ACTION: Builds the PO locale files, by reading our source code and updating
# the existing message catalog. This will not compile the resulting PO source
# files.
strings:
	$(call admin_cd,templates,makemessages --all --extension=html,py,txt);

# ACTION: This will literally compile the PO files into MO files, that can be
# loaded by your web application
compile:
	$(call admin_cd,templates,compilemessages);

validate:
	$(call admin,validate)

syncdb: validate
	$(call admin,syncdb)

shell:
	$(call admin,shell)

dbshell:
	$(call admin,dbshell)

test: compile validate syncdb
	$(call admin,runserver 8080)

smtp:
	$(python) -m smtpd -n -c DebuggingServer localhost:1025

clean: mrproper
	$(python) -m compileall .

mrproper:
	find . -name '*~' -print0 | xargs -0 rm -vf 
	find . -name '*.py?' -print0 | xargs -0 rm -vf
