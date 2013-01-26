#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Ter 23 Mar 2010 10:24:26 PDT
cd `dirname $0`
mysqldump -h mysql.andreanjos.org -u aadjadmin -prr45TUxzb --opt aa_professional_website > db.sql
/usr/sbin/logrotate --state=logrotate.state logrotate.conf
