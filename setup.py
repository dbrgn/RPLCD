#!/usr/bin/env python

from setuptools import setup

readme = open('README.rst').read()

setup(name='RPLCD',
      version='0.2.0',
      description='A Raspberry Pi LCD library for the widely used Hitachi HD44780 controller.',
      long_description=readme,
      author='Danilo Bargen',
      author_email='mail@dbrgn.ch',
      url='https://github.com/dbrgn/RPLCD',
      license='MIT',
      keywords='raspberry, raspberry pi, lcd, liquid crystal, hitachi, hd44780',
      packages=['RPLCD'],
      platforms=['any'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: System :: Hardware :: Hardware Drivers',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
    )
