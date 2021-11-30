#!/usr/bin/env python

import io
import os
import re

from setuptools import setup


classifiers = [
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
]

install_requires = ['numpy', 'matplotlib', 'pandas', 'argparse', 'svgpath2mpl']

setup(
    name='svgpath2mpl',
    author='Brian McCall',
    author_email='',
    version='0.1',
    license='GPLv3',
    description='Sample pattern grader',
    long_description='Sample pattern grader',
    keywords=['svg', 'path', 'matplotlib', 'plotting', 'visualization'],
    url='https://github.com/brian-patrick-mccall/svg-grader',
    py_modules=['grade'],
    zip_safe=False,
    classifiers=classifiers,
    install_requires=install_requires,
    tests_require=None
)
