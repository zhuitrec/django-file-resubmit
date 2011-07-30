#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2011 Ilya Shalyapin
#
#  django-file-resubmit is free software under terms of the MIT License.
#

import os
from setuptools import setup


readme = open(os.path.join(os.path.dirname(__file__), 'README.markdown')).read()

setup(
    name     = 'django-file-resubmit',
    version  = '0.1',
    packages = ['file_resubmit'],

    requires = ['python (>= 2.5)', 'django (>= 1.3)', 'sorl.thumbnail (>=11.0)'],

    description  = 'Keeps submited files when validation errors occure.',
    long_description = readme,
    author       = 'Ilya Shalyapin',
    author_email = 'ishalyapin@gmail.com',
    url          = 'http://coderiver.ru',
    download_url = 'https://un1t.github.com',
    license      = 'MIT License',
    keywords     = 'django form filefield resubmit',
    classifiers  = [
        'Development Status :: Development',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: General',
    ],
)