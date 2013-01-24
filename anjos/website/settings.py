# Django settings for my personal webpage

DEBUG = True
DREAMHOST = True
TEMPLATE_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = True
import os
#from .dbconfig import DATABASES

# These locations are calculated based on the settings.py location
D = os.path.dirname
BASEDIR = os.path.realpath(D(__file__))

DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.sqlite3', 
      'NAME': os.path.join(D(D(BASEDIR)), 'db.sql3')
      }
    }

ADMINS = (
    ('Andre Anjos', 'andre.dos.anjos@gmail.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en'
# Valid languages for this website
gettext = lambda s: s
LANGUAGES = (
  ('en', gettext('English')),
  ('pt-br', gettext('Brazilian Portuguese')),
  ('fr', gettext('French')),
  )
DEFAULT_LANGUAGE = 1
# Where to find MO compilations
LOCALE_PATHS = ( '%s/templates/locale' % BASEDIR, 
                )

SITE_ID = 1

# STATIC_ROOT: Absolute path to the directory that holds static media.
# Example: "/home/media/media.lawrence.com/"
# STATICFILES_DIRS: Add these extra paths when collecting static stuff
# STATIC_URL: Relative path to the files through the webserver

if DREAMHOST:
  STATIC_ROOT = os.path.join(D(D(D(BASEDIR))), 'public') + os.sep
  STATIC_URL = '/'

else:
  STATIC_ROOT = os.path.join(D(D(BASEDIR)), 'static') + os.sep
  STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASEDIR, 'static'),
    ]

# The default url for logging into the site
LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = '/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'wk&_+uqn)()=fz07y0qdl%@=m^gp^taf$&7ql&@-ffjk9aln_7'

# List of callables that know how to import templates from various sources.
if DEBUG:
  TEMPLATE_LOADERS = [
      'django.template.loaders.filesystem.Loader',
      'django.template.loaders.app_directories.Loader',      
      ]
else:
  TEMPLATE_LOADERS = [
      ('django.template.loaders.cached.Loader',(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'forum.modules.template_loader.module_templates_loader',
        'forum.skins.load_template_source',
        )),
      ]

# What we like to have in every page we render, as context
TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth', #for users and permissions
  'django.core.context_processors.static', #for STATIC_URL
  'django.core.context_processors.i18n', #for LANGUAGES  
  'django.core.context_processors.request', #for the request on all pages
  'anjos.website.context_processors.site', #for site
  'anjos.website.context_processors.full_path', #for the full_path
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'maintenancemode.middleware.MaintenanceModeMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'anjos.website.urls'

TEMPLATE_DIRS = (
  # Put strings here, like "/home/html/django_templates".
  # Always use forward slashes, even on Windows.
  '%s/templates' % BASEDIR,
)

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.admin',
  'django.contrib.markup',
  'django.contrib.staticfiles',
  # 'django.contrib.sitemaps',

  # External projects reused
  'djangoogle',
  'nav',
  'publications',
  'order',
  'flatties',

  # Other projects
  'robots',
  'django_openid_auth',
)

# Controls how many albums per page to see
DJANGOOGLE_ALBUMS_PER_PAGE = 8 

# Disables the sitemap functionality for robots
ROBOTS_USE_SITEMAP = False

# Enables filesystem caching
if DEBUG:
  cache_backend = 'django.core.cache.backends.dummy.DummyCache'
else:
  cache_backend = 'django.core.cache.backends.filebased.FileBasedCache'

CACHES = {
    'default': {
        'BACKEND': cache_backend,
        'LOCATION': os.path.join(D(D(BASEDIR)), 'cache'),
    }
}

# Edit this if you want to cache the whole site and use the cache middleware
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True # only for outsiders

# Which server do we authenticate against
OPENID_SSO_SERVER_URL = 'https://www.google.com/accounts/o8/id'
# Allow admins to login using this system
OPENID_USE_AS_ADMIN_LOGIN = True
# You may need this to establish your connection with Google for a start
# OPENID_CREATE_USERS = True

# For the maintenance mode middleware
#MAINTENANCE_MODE = True
