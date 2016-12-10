API
###

CharLCD (I²C)
==============

The main class for controlling I²C connected LCDs.

.. autoclass:: RPLCD.i2c.CharLCD

CharLCD (GPIO)
==============

The main class for controlling GPIO (parallel) connected LCDs.

.. autoclass:: RPLCD.gpio.CharLCD

Enums
=====

Alignment
---------

This enum controls the text align mode of the LCD.

.. autoclass:: RPLCD.common.Alignment

ShiftMode
---------

This enum controls the shift mode of the LCD.

.. autoclass:: RPLCD.common.ShiftMode

CursorMode
----------

The cursor can either be hidden, or shown as line or as blinking box.

.. autoclass:: RPLCD.common.CursorMode

BacklightMode
-------------

A LCD backlight circuit can be configured in active high or active low mode.

.. autoclass:: RPLCD.common.BacklightMode
