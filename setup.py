#!/usr/bin/env python
"""
colors.py
=========
Convert colors between rgb, hsv, and hex, perform arithmetic, blend modes,
and generate random colors within boundaries.
"""
from setuptools import setup, find_packages
import colors

setup(
    name='colors.py',
    version=colors.__version__,
    author='Matt Robenolt',
    author_email='matt@ydekproductions.com',
    url='https://github.com/mattrobenolt/colors.py',
    description='Convert and manipulate color values',
    long_description=__doc__,
    license=colors.__license__,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ]
)
