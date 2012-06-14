#!/usr/bin/env python
"""
colors.py
=========
Convert colors between rgb, hsv, and hex, perform arithmetic, blend modes,
and generate random colors within boundaries.
"""
from setuptools import setup

setup(
    name='colors.py',
    version='0.1.0',
    author='Matt Robenolt',
    author_email='matt@ydekproductions.com',
    url='https://github.com/mattrobenolt/colors.py',
    description='Convert and manipulate color values',
    long_description=__doc__,
    license='BSD',
    py_modules=['colors'],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
