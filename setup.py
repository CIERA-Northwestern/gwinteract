#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) Scott Coughlin (2018)
#
# This file is part of the gwinteract django webapp.

"""Setup the gwinteract package
"""

from __future__ import print_function

import sys
if sys.version < '2.6':
    raise ImportError("Python versions older than 2.6 are not supported.")

import glob
import os.path

from setuptools import (setup, find_packages)

# set basic metadata
PACKAGENAME = 'gwinteract'
DISTNAME = 'gwinteract'
AUTHOR = 'Scott Coughlin'
AUTHOR_EMAIL = 'scottcoughlin2014@u.northwestern.edu'
LICENSE = 'BSD 3 LICENSE'

cmdclass = {}

# -- versioning ---------------------------------------------------------------

import versioneer
__version__ = versioneer.get_version()
cmdclass.update(versioneer.get_cmdclass())

# -- dependencies -------------------------------------------------------------

setup_requires = [
    'setuptools',
    'pytest-runner',
]
install_requires = [
    'numpy >= 1.7.1',
    'scipy >= 0.12.1',
    'matplotlib >= 1.2.0, != 2.1.0, != 2.1.1',
    'configparser',
    'gwpy >= 0.12',
    'pandas >= 0.22 ; python_version >= \'3.5\'',
    'pandas < 0.21 ; python_version == \'3.4\'',
    'pandas >= 0.22 ; python_version == \'2.7\'',
    'django >= 1.11.3',
    'psycopg2-binary >= 2.7.5',
    'sqlalchemy >= 1.2.12',
    'seaborn >= 0.9.0',
    'ligo-gracedb >= 2.0.0',
]

# -- run setup ----------------------------------------------------------------

packagenames = find_packages()

setup(name=DISTNAME,
      provides=[PACKAGENAME],
      version=__version__,
      description='A Django webapp providing extra gravityspy tools.',
      url='https://gwinteract.ciera.northwestern.edu/',
      long_description=None,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      packages=packagenames,
      include_package_data=True,
      cmdclass=cmdclass,
      setup_requires=setup_requires,
      install_requires=install_requires,
      dependency_links = ['https://github.com/zooniverse/panoptes-python-client'],
      use_2to3=True,
      classifiers=[
          'Programming Language :: Python',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Astronomy',
          'Topic :: Scientific/Engineering :: Physics',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Operating System :: MacOS',
          'License :: OSI Approved :: BSD License v3 (BSDv3)',
      ],
)
