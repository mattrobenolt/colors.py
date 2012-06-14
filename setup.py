#!/usr/bin/env python
"""
colors.py
=========
Convert colors between rgb, hsv, and hex, perform arithmetic, blend modes,
and generate random colors within boundaries.
"""
from setuptools import setup, find_packages

setup(
    name='colors.py',
    version='0.2.0',
    author='Matt Robenolt',
    author_email='matt@ydekproductions.com',
    url='https://github.com/mattrobenolt/colors.py',
    description='Convert and manipulate color values',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
