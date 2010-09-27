#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Ter 23 Mar 2010 10:24:26 PDT
cd `dirname $0`/..
mysqldump -h mysql.andreanjos.org -u aadjadmin -pxzb77yhH --opt aa_professional_website > db.sql
/usr/sbin/logrotate --state=backup/logrotate.state cron/logrotate.conf
rm -f db.sql
