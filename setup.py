#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import django_currentorganization

from setuptools import setup

version = django_currentorganization.__version__

if sys.argv[-1] == 'publish':
    os.system('make release')
    sys.exit()

readme = open('README.rst').read()

description = "Conveniently store reference to request Organization on thread/db level."

setup(
    name='django-currentorganization',
    version=version,
    description=description,
    long_description=readme,
    author='Jack Linke, Paessler AG',
    author_email='support@omenapps.com',
    url='https://github.com/OmenApps/django-currentorganization',
    packages=[
        'django_currentorganization',
    ],
    include_package_data=True,
    license="BSD",
    zip_safe=False,
    keywords='django-currentorganization',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
    ],
)
