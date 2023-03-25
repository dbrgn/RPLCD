#!/usr/bin/env python

from setuptools import setup

readme = open('README.rst').read()

setup(name='RPLCD',
      version='1.3.1',
      description='A Raspberry Pi LCD library for the widely used Hitachi HD44780 controller.',
      long_description=readme,
      author='Danilo Bargen',
      author_email='mail@dbrgn.ch',
      url='https://github.com/dbrgn/RPLCD',
      license='MIT',
      keywords='raspberry, raspberry pi, lcd, liquid crystal, hitachi, hd44780',
      packages=['RPLCD', 'RPLCD.codecs', 'RPLCD_Tests'],
      entry_points={
          'console_scripts': ['rplcd-tests=RPLCD_Tests.entrypoint:run'],
      },
      platforms=['any'],
      python_requires='>=3.4',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: System :: Hardware :: Hardware Drivers',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
    )
