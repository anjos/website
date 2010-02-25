# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

# This you must set correctly
RSYNC_MASTER='andreps@andreanjos.org:andreanjos.org'
RSYNC=rsync --rsh=ssh --recursive --times --perms --owner --group --verbose --compress
PROC=$(shell ps awux | grep fcgi | grep $(PYTHON) | grep -v ps | awk '{ print $$2 }')

all:

.PHONY: clean restart 

restart:
	@pkill -9 dispatch.fcgi 

reinstall:
	@rm -rf sw*
	@./bootstrap.sh $(PYTHON)
	
clean: 	
	@find . -name '*~' -print0 | xargs -0 rm -vf 
	make --directory=project clean

pull:
	@echo 'Pulling Git sources'
	git pull
	@echo 'Synchronize Django database'
	$(RSYNC) $(RSYNC_MASTER)/db.sql3 ./
	@echo 'Synchronize media directory'
	$(RSYNC) $(RSYNC_MASTER)/media ./
	@echo 'Re-compiling language files'
	$(MAKE) -C project clean
	@echo 'Synchronization is done'

push:
	@echo 'Pushing Git sources into master repository'
	git push
	@echo 'Copying local database to master server'
	$(RSYNC) ./db.sql3 $(RSYNC_MASTER)/
	@echo 'Synchronizing local media with that of master server'
	$(RSYNC) ./media/ $(RSYNC_MASTER)/media/

test:
	make --directory=project test
