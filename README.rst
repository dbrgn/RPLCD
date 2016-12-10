RPLCD
#####

.. image:: https://img.shields.io/travis/dbrgn/RPLCD/master.svg
    :target: https://travis-ci.org/dbrgn/RPLCD
    :alt: Build Status
.. image:: https://img.shields.io/pypi/v/RPLCD.svg
    :target: https://pypi.python.org/pypi/RPLCD/
    :alt: PyPI Version
.. image:: https://img.shields.io/pypi/dm/RPLCD.svg
    :target: https://pypi.python.org/pypi/RPLCD/
    :alt: PyPI Downloads
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

A Python 2/3 Raspberry PI Character LCD library for the Hitachi HD44780
controller. It supports both GPIO (parallel) mode as well as boards with an I2C
port expander (e.g. the PCF8574).

Tested with the 20x4 LCD that is sold for example by `adafruit.com
<http://www.adafruit.com/products/198>`_ or `mikroshop.ch
<http://mikroshop.ch/LED_LCD.html?gruppe=7&artikel=84>`__.

Also tested with a 16x2 LCD from `mikroshop.ch
<!-- <http://mikroshop.ch/LED_LCD.html?gruppe=7&artikel=15> -->`__ and
JHD162A.

This library is inspired by Adafruit Industries' CharLCD_ library as well as by
Arduino's LiquidCrystal_ library.

No external dependencies (except the RPi.GPIO library, which comes preinstalled
on Raspbian) are needed to use this library.

.. image:: https://raw.github.com/dbrgn/RPLCD/master/photo-i2c.jpg
    :alt: Photo of 20x4 LCD in action

Setup
=====

You can install RPLCD directly from `PyPI
<https://pypi.python.org/pypi/RPLCD/>`_ using pip::

    $ sudo pip install RPLCD

If you want to use I2C, you also need smbus::

    $ sudo apt install python-smbus

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
- Support for both parallel and I²C connection
- Support for custom characters
- Support for backlight control circuits
- Python 2/3 compatible
- Caching: Only write characters if they changed
- No external dependencies (except `RPi.GPIO`)

Wishlist
--------

These things may get implemented in the future, depending on my free time and
motivation:

- MicroPython port

Documentation
=============

You can find the documentation here: https://readthedocs.org/projects/rplcd/


API
===

Init, Setup, Teardown
---------------------

.. sourcecode:: python

    import RPi.GPIO as GPIO
    from RPLCD.gpio import CharLCD, BacklightMode

    # Initialize display. All values have default values and are therefore
    # optional.
    lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
                  numbering_mode=GPIO.BOARD,
                  cols=20, rows=4, dotsize=8,
                  auto_linebreaks=True,
                  pin_backlight=None, backlight_enabled=True,
                  backlight_mode=BacklightMode.active_low)

    ...

    # If desired, reset the GPIO configuration and optionally clear the screen.
    # Note that this can lead to undesired effects on the LCD, because the GPIO
    # pins are not configured as input or output anymore.
    lcd.close(clear=True)

Properties
----------

- ``display_enabled`` -> ``True`` / ``False``
- ``cursor_pos`` -> ``(row, col)``
- ``text_align_mode`` -> ``Alignment.left`` / ``Alignment.right``
- ``write_shift_mode`` -> ``ShiftMode.cursor`` / ``ShiftMode.display``
- ``cursor_mode`` -> ``CursorMode.hide`` / ``CursorMode.line`` / ``CursorMode.blink``
- ``backlight_enabled`` -> ``True`` / ``False``

High Level Functions
--------------------

- ``write_string(value)``: Write the specified unicode string to the display.
  You can use newline (``\n``) and carriage return (``\r``) characters to
  control line breaks.
- ``clear()``: Overwrite display with blank characters and reset cursor position.
- ``home()``: Set cursor to initial position and reset any shifting.
- ``shift_display(amount)``: Shift the display. Use negative amounts to shift
  left and positive amounts to shift right.
- ``create_char(location, bitmap)``: Write a new character into the CGRAM at
  the specified location (0-7). See the examples section for more information.

Mid Level Functions
-------------------

- ``command(value)``: Send a raw command to the LCD.
- ``write(value)``: Write a raw byte to the LCD.

Context Managers
----------------

- ``cursor(lcd, row, col)``: Control the cursor position before entering the block.
- ``cleared(lcd)``: Clear the display before entering the block.


Testing
=======

To test your 20x4 display, please run the ``test_20x4.py`` script and
confirm/verify each step with the enter key. If you don't use the standard
wiring, make sure to add your pin numbers to the ``CharLCD`` constructor in
``test_20x4.py``.

To test a 16x2 display, proceed as explained above, but use the ``test_16x2.py``
script instead.


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

The module ``RPLCD/enum.py`` is (c) 2004-2013 by Barry Warsaw. It was
distributed as part of the ``flufl.enum`` package under the LGPL License version
3 or later.


.. _charlcd: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCD
.. _liquidcrystal: http://arduino.cc/en/Reference/LiquidCrystal
