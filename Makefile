# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.dos.anjos@gmail.com>
# Tue 22 Jan 2013 14:05:21 CET

# This you must set correctly
RSYNC_MASTER='andreps@andreanjos.org:andreanjos.org'
RSYNC=rsync --rsh=ssh --recursive --times --perms --owner --group --verbose --compress
PYTHON=python2.6

all: bootstrap test

.PHONY: clean restart mrproper

restart:
	@skill -15 python

clean: 	
	@find . -name '*~' -print0 | xargs -0 rm -vf 
	$(MAKE) --directory=project clean

pull:
	@echo 'Pulling Git sources'
	git pull
	@echo 'Synchronize Django database'
	$(RSYNC) $(RSYNC_MASTER)/db.sql3 ./
	@echo 'Synchronize media directory'
	$(RSYNC) $(RSYNC_MASTER)/media ./
	@echo 'Re-compiling language files'
	$(MAKE) --directory=project clean
	@echo 'Synchronization is done'

push:
	@echo 'Pushing Git sources into master repository'
	git push
	@echo 'Copying local database to master server'
	$(RSYNC) ./db.sql3 $(RSYNC_MASTER)/
	@echo 'Synchronizing local media with that of master server'
	$(RSYNC) ./media/ $(RSYNC_MASTER)/media/

test:
	$(MAKE) --directory=project BASEDIR=$(shell pwd) test
