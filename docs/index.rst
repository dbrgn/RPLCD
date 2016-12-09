Welcome to RPLCD's documentation!
#################################


About
=====

RPLCD is a Python 2/3 Raspberry PI Character LCD library for the Hitachi HD44780
controller. It supports both GPIO (parallel) mode as well as boards with an I2C
port expander (e.g. the PCF8574).

The library has been tested with the 20x4 LCD that is sold for example by
`adafruit.com <http://www.adafruit.com/products/198>`_ or `mikroshop.ch
<http://mikroshop.ch/LED_LCD.html?gruppe=7&artikel=84>`__. It has also been
tested with a 16x2 LCD from `mikroshop.ch
<http://mikroshop.ch/LED_LCD.html?gruppe=7&artikel=15>`__.

This library is inspired by Adafruit Industries' CharLCD_ library as well as by
Arduino's LiquidCrystal_ library.

No external dependencies (except the `RPi.GPIO` library, which comes
preinstalled on Raspbian) are needed to use this library.


Features
========

**Already implemented**

- Simple to use API
- Support for both 4 bit and 8 bit modes
- Support for both parallel (GPIO) and I²C connection
- Support for custom characters
- Support for backlight control circuits
- Python 2/3 compatible
- Caching: Only write characters if they changed
- No external dependencies

**Wishlist**

These things may get implemented in the future, depending on my free time and
motivation:

- MicroPython port


Contents
========

.. toctree::
   :maxdepth: 2

   installation.rst
   getting_started.rst


Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _charlcd: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCD
.. _liquidcrystal: http://arduino.cc/en/Reference/LiquidCrystal
