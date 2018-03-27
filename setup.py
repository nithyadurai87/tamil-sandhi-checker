#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Setup file derived from open-tamil project.
# (C) 2018 Ezhil Language Foundation

from distutils.core import setup
from codecs import open

setup(name='tamil-sandhi-checker',
      version='0.1',
      description='Tamil word conjugation, sandhi rules checker',
      author='Nithya Duraisamy, and other contributors',
      author_email='nithyadurai87@gmail.com',
      url='https://github.com/nithyadurai87/tamil-sandhi-checker',
      packages=['tamilsandhi'],
      package_dir={'tamilsandhi': 'tamilsandhi'},
      package_data={'tamilsandhi': ['all-tamil-nouns.txt']},
      license='GPL',
      scripts=['sandhichecker.sh'],
      platforms='PC,Linux,Mac',
      classifiers=['Natural Language :: Tamil',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4'],
      long_description=open('README.md','r','UTF-8').read(),
      download_url='https://github.com/nithyadurai87/tamil-sandhi-checker/archive/master.zip',#pip
      )
