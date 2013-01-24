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

After that, bootstrap the environment::

  $ python bootstrap.py
  ...
  $ ./bin/buildout
  ...

By default, the settings on the project are setup to work with a local
``db.sql3`` that should be placed at the root of the package. You can also work
against a MySQL server. In such a case, you will need to get hold of the MySQL
connection string. You can copy the one on your private server, if you have the
right to do so::

  $ scp andreps@andreanjos.org:andreanjos.org/anjos/website/dbconfig.py anjos/website 

Otherwise, here is a template (it should be placed on the same directory as
``settings.py`` is)::

  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'db_name',
      'USER': '******',
      'PASSWORD': '******',
      'HOST': 'mysql.dbhost.com',
      'PORT': '3306',
    },
  }
  
.. warning::
  
  Make sure you don't make the above file public, or checks it into the git
  repository. It contains sensitive data (username, password and the database
  server address).

Next, you will need to copy media only available remotely, to the current
working directory and collect all apps static files::

  $ ./bin/dj collectstatic --noinput
  ...
  $ rsync -avz andreps@andreanjos.org:andreanjos.org/static/ static/
  ...

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

  $ ./manage.py shell
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
  $ vim anjos/website/settings.py # change to the local database configuration
  $ ./bin/dj syncdb --noinput
  $ ./bin/dj reset auth --noinput
  $ ./bin/dj reset contenttypes --noinput
  $ ./bin/dj loaddata data.json
  $ rm -f data.json

Installing on Dreamhost
=======================

Follow these steps:

1. Make sure that the database configuration is set right;
2. Make sure that the variable ``DREAMHOST`` is set to ``True`` at the top of the
   ``settings.py`` file.
