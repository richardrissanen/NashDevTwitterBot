#!/usr/bin/env python

import os
from setuptools import setup, find_packages

REQUIREMENTS = [
    'feedparser',
    'tweepy'
]

setup(
    name='nashDevTwitterBot',
    version='0.1.0',
    description='Bot that pulls events from cal.nashvl.org and tweets them',
    long_description='README',
    author='Richard Rissanen',
    author_email='email@richardrissanen.com',
    url='https://github.com/richardrissanen/nashDevTwitterBot',
    license="Public Domain",
    install_requires=REQUIREMENTS,
    keywords=['nashDevTwitterBot NashDev Nashville Twitter'],
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications',
    ],
    python_requires='~=3.6',
)
