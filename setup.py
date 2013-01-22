#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.dos.anjos@gmail.com>
# Tue 22 Jan 2013 13:37:39 CET

"""Professional website package management
"""

from setuptools import setup, find_packages

setup(

    name="anjos-website",
    version="1.0.0",
    description="My professional website",
    license="FreeBSD",
    author='Andre Anjos',
    author_email='andre.dos.anjos@gmail.com',
    long_description=open('README.rst').read(),
    url='https://github.com/anjos/website',

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
     
      # pretty generic
      'setuptools',
      'PIL',
      'flup',
      'uuid',
      'mysql-python',
      
      # others
      'django-robots',
      'django-openid-auth',
      'django-maintenancemode',
      
      # mine
      'django-publications',
      'djangoogle',
      'django-flatties',
      'django-nav',
      ],

    entry_points = {
      'console_scripts': [
        ],
      },

    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Environment :: Web Environment',
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Natural Language :: English',
      'Programming Language :: Python',
      ],
    
    )
