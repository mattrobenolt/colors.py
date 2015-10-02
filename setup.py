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
    version='0.2.1',
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
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ]
)
