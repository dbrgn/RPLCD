Troubleshooting
###############


Compatibility Mode
==================

Not all LCDs are made equal. It appears that some devices (especially those with
non-original HD44780 controllers) don't run at the reference clock, and as such,
are out of specification when it comes to timings.

If you’ve been experiencing `issues
<https://github.com/dbrgn/RPLCD/issues/70>`__ with garbled text occasionally on
initialization/use of the display, try enabling the compatibility mode by
passing ``compat_mode=True`` to the ``CharLCD`` constructor.


TypeError: this constructor takes no arguments
==============================================

If you're getting this error, you are probably importing the ``CharLCD`` class
the wrong way. If you use parallel (GPIO) mode, you should use ``from RPLCD.gpio
import CharLCD``. If you use I²C mode, you should use ``from RPLCD.i2c import
CharLCD``.


ValueError: Invalid GPIO numbering mode
=======================================

Since version 1.0.0, you need to explicitly specify the pin numbering mode. So
if you're getting this error:

::

   ValueError: Invalid GPIO numbering mode: numbering_mode=None, must be
   either GPIO.BOARD or GPIO.BCM

...then you need to pass in the ``numbering_mode`` explicitly:

.. sourcecode:: python

   import RPi.GPIO as GPIO

   # For BOARD numbering
   lcd = CharLCD(..., numbering_mode=GPIO.BOARD)

   # For BCM numbering
   lcd = CharLCD(..., numbering_mode=GPIO.BCM)

The numbering mode is important, if you're unsure which one to use, search on
Google/DuckDuckGo to learn about the differences between the two numbering
modes.
