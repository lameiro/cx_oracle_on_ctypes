# -*- coding: utf-8 -*-
import codecs
import os
import sys
from setuptools import setup, find_packages


def read(filename):
    try:
        with codecs.open(filename, encoding='utf-8') as f:
            return unicode(f.read())
    except NameError:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()


version = '0.1.dev0'

long_description = (
    read('readme.rst')
    + '\n\n' +
    read('changes.rst')
    + '\n\n' +
    read('contributors.rst')
    )




setup(
    name='cx_oracle_on_ctypes',
    version=version,
    description="Ctypes-based Python interface to Oracle",
    long_description=long_description,

    classifiers=[
        # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: Python Software Foundation License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Database",
        ],

    keywords='Oracle ctypes cx_Oracle ',
    license='BSD',
    author='Leandro Lameiro ',
    author_email='lameiro@gmails.com',
    url='https://github.com/lameiro/cx_oracle_on_ctypes',
    packages=find_packages(exclude=['ez_setup', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    )