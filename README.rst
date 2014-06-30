===================================
 Andre Anjos' Professional Website
===================================

This package contains the source and deployment instructions for my personal
website. The latest version is available from `my github website
<http://github.com/anjos/website>`.

Installation
------------

Clone this package using the following command::

  $ git clone git@github.com:anjos/website
  $ git submodule init
  $ git submodule update

After that, bootstrap the environment::

  $ python bootstrap.py
  $ ./bin/buildout

Create the PDF for your CV::

  $ cd anjos/website/static/cv
  $ make

By default, the settings on the project are setup to work with a local
``db.sql3`` that should be placed at the root of the package. You can also work
against a MySQL server. In such a case, you will need to get hold of the MySQL
connection string. You can copy the one on your private server, if you have the
right to do so::

  $ scp andreanjos@andreanjos.org:andreanjos.org/anjos.website/anjos/website/dbconfig.py anjos/website

Otherwise, here is a template (it should be placed on the same directory as
``settings.py`` is)::

  import os

  DATABASES = {
      'local': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'local.sql3')
        },
      'server': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<database-name>',
        'USER': '<database-user>',
        'PASSWORD': '*********',
        'HOST': 'mysql.andreanjos.org',
        'PORT': '3306',
        },
      }

  DATABASES['default'] = DATABASES['server']

.. warning::

  Make sure you don't make the above file public, or checks it into the git
  repository. It contains sensitive data (username, password and the database
  server address).

Next, you will need to copy media only available remotely, to the current
working directory and collect all apps static files::

  $ ./bin/dj collectstatic --noinput
  $ rsync -avz andreanjos@andreanjos.org:andreanjos.org/public/media media/

Maintenance
-----------

Here are some common tips for maintenance.

Running a Test Server
=====================

To start a test server::

  $ ./bin/dj runserver

Removing Obsolete ContentTypes
===============================

This happens when you remove applications from your website::

  $ ./bin/dj shell
  >>> from django.contrib.contenttypes.models import ContentType
  >>> for ct in ContentType.objects.filter(app_label='audit'):
  ...     ct.delete()
  ...
  >>>

Moving a MySQL database to SQLite3
==================================

To work locally, using an SQLite database for development, you can dump the
current data on your server and load it again on a local sqlite3 database::

  $ ./bin/dj dumpdata > data.json
  $ vim anjos/website/dbconfig.py # change to the local database configuration
  $ ./bin/dj syncdb --noinput
  $ ./bin/dj reset auth --noinput
  $ ./bin/dj reset contenttypes --noinput
  $ ./bin/dj loaddata data.json
  $ rm -f data.json

Installing on Dreamhost
=======================

Follow these steps:

1. Make sure that the database configuration is set right;
2. Make sure that the variable ``DREAMHOST`` is set to ``True`` at the top of
   the ``settings.py`` file. Do the same for ``DEBUG`` (setting it to
   ``False``);
3. Link ``passenger_wsgi.py``::
   $ cd <website-directory>
   $ ln -s anjos.website/bin/dj.wsgi passenger_wsgi.py
4. Set up the backup cronjob to execute daily (e.g.: ``backup/do_it.sh``). Here
   is an example::

     #!/bin/sh
     cd `dirname $0`
     mysqldump -h mysql.andreanjos.org -u aadjadmin -p******* --opt aa_professional_website > db.sql
     /usr/sbin/logrotate --state=logrotate.state logrotate.conf
