Welcome to RPLCD's documentation!
#################################


About
=====

RPLCD is a Python 2/3 Raspberry PI Character LCD library for the Hitachi HD44780
controller. It supports both GPIO (parallel) mode as well as boards with an I²C
port expander (e.g. the PCF8574 or the MCP23008).

This library is inspired by Adafruit Industries' CharLCD_ library as well as by
Arduino's LiquidCrystal_ library.

For GPIO mode, no external dependencies (except the ``RPi.GPIO`` library, which
comes preinstalled on Raspbian) are needed to use this library. If you want to
control LCDs via I²C, then you also need the ``python-smbus`` library.


Features
========

**Already implemented**

- Simple to use API
- Support for both 4 bit and 8 bit modes
- Support for both parallel (GPIO) and I²C connection
- Support for custom characters
- Support for backlight control circuits
- Built-in support for ``A00`` and ``A02`` character tables
- Python 2/3 compatible
- Caching: Only write characters if they changed
- No external dependencies (except ``RPi.GPIO``, and ``python-smbus`` if you need
  I²C support)

**Wishlist**

These things may get implemented in the future, depending on my free time and
motivation:

- MicroPython port

**Supported I²C Port Expanders**

- PCF8574 (used by a lot of I²C LCD adapters on Ali Express)
- MCP23008 (used in Adafruit I²C LCD backpack)
- MCP23017


Contents
========

.. toctree::
   :maxdepth: 2

   installation.rst
   getting_started.rst
   usage.rst
   api.rst


Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _charlcd: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCD
.. _liquidcrystal: http://arduino.cc/en/Reference/LiquidCrystal
