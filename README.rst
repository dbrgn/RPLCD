RPLCD
#####

.. image:: https://badges.gitter.im/RPLCD/Lobby.svg
   :alt: Join the chat at https://gitter.im/RPLCD/Lobby
   :target: https://gitter.im/RPLCD/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. image:: https://img.shields.io/travis/dbrgn/RPLCD/master.svg
    :target: https://travis-ci.org/dbrgn/RPLCD
    :alt: Build Status
.. image:: https://img.shields.io/pypi/v/RPLCD.svg
    :target: https://pypi.python.org/pypi/RPLCD/
    :alt: PyPI Version
.. image:: https://img.shields.io/pypi/wheel/RPLCD.svg
    :target: https://pypi.python.org/pypi/RPLCD/
    :alt: PyPI Wheel
.. image:: https://img.shields.io/pypi/pyversions/RPLCD.svg
    :target: https://pypi.python.org/pypi/RPLCD/
    :alt: PyPI Python Versions
.. image:: https://img.shields.io/badge/dependencies-0-blue.svg
    :target: https://pypi.python.org/pypi/RPLCD/
    :alt: Dependencies
.. image:: https://img.shields.io/pypi/l/RPLCD.svg
    :target: https://pypi.python.org/pypi/RPLCD/
    :alt: License

A Python 3/2 Raspberry PI Character LCD library for the Hitachi HD44780
controller. It supports both GPIO (parallel) mode as well as boards with an I²C
port expander (e.g. the PCF8574 or the MCP23008).

This library is inspired by Adafruit Industries' CharLCD_ library as well as by
Arduino's LiquidCrystal_ library.

For GPIO mode, no external dependencies (except the ``RPi.GPIO`` library, which
comes preinstalled on Raspbian) are needed to use this library. If you want to
control LCDs via I²C, then you also need the ``python-smbus`` or ``smbus2`` library. If you
want to control the LCD with ``pigpio``, you have to install the pigpio_ library.

If you're trying to get started with RPLCD, you should probably `read the docs
<#documentation>`__ :)

.. image:: https://raw.github.com/dbrgn/RPLCD/master/photo-i2c.jpg
    :alt: Photo of 20x4 LCD in action


Setup
=====

You can install RPLCD directly from `PyPI
<https://pypi.python.org/pypi/RPLCD/>`_ using pip::

    $ sudo pip install RPLCD

If you want to use I²C, you also need either the smbus or `smbus2 <https://pypi.org/project/smbus2/>`_ library::

    $ sudo apt install python-smbus
    or
    $ sudo pip install smbus2

RPLCD will first try to use smbus if available and if not, fall back to smbus2.

You can also install the library manually without pip. Either just copy the
scripts to your working directory and import them, or download the repository
and run ``python setup.py install`` to install it into your Python package
directory.


Features
========

Implemented
-----------

- Simple to use API
- Support for both 4 bit and 8 bit modes
- Support for both parallel (GPIO) and I²C connection
- Support for custom characters
- Support for backlight control circuits
- Built-in support for `A00` and `A02` character tables
- Python 2/3 compatible
- Caching: Only write characters if they changed
- No external dependencies (except `RPi.GPIO`, and `python-smbus` or `smbus2` if you need
  I²C support)

Wishlist
--------

These things may get implemented in the future, depending on my free time and
motivation:

- MicroPython port

Supported I²C Port Expanders
----------------------------

- PCF8574 (used by a lot of I²C LCD adapters on Ali Express)
- MCP23008 (used in Adafruit I²C LCD backpack)
- MCP23017


Documentation
=============

- Stable (released on PyPI): http://rplcd.readthedocs.io/en/stable/
- Latest (current master): http://rplcd.readthedocs.io/en/latest/

Testing
=======

Interactive Test Script
-----------------------

To test your LCD, please run the ``rplcd-tests`` script with the ``testsuite``
target.

Unit Tests
----------

There are also unit tests. First, install dependencies:

    pip install -U -r requirements-dev.txt

Then run the tests:

    py.test -v


Coding Guidelines
=================

`PEP8 <http://www.python.org/dev/peps/pep-0008/>`__ via `flake8
<https://pypi.python.org/pypi/flake8>`_ with ``max-line-width`` set to 99 and
``E126-E128,C901`` ignored::

    flake8 --max-line-length=99 --ignore=E126,E127,E128,C901 RPLCD/lcd.py


Resources
=========

- TC2004A-01 Data Sheet: http://www.adafruit.com/datasheets/TC2004A-01.pdf
- HD44780U Data Sheet: http://www.adafruit.com/datasheets/HD44780.pdf


License
=======

This code is licensed under the MIT license, see the `LICENSE file
<https://github.com/dbrgn/RPLCD/blob/master/LICENSE>`_ or `tldrlegal
<http://www.tldrlegal.com/license/mit-license>`_ for more information. 


.. _charlcd: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCD
.. _liquidcrystal: http://arduino.cc/en/Reference/LiquidCrystal
.. _pigpio: http://abyz.me.uk/rpi/pigpio/
