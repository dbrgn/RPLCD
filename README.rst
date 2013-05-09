RPLCD
#####

A Python 2/3 Raspberry PI Character LCD library for the Hitachi HD44780
controller.

Tested with the 20x4 LCD that is sold for example by `adafruit.com
<http://www.adafruit.com/products/198>`_ or `mikroshop.ch
<http://mikroshop.ch/LED_LCD.html?gruppe=7&artikel=84>`_.

.. image:: https://raw.github.com/dbrgn/RPLCD/master/photo.jpg
    :alt: Photo of 20x4 LCD in action

This library is inspired by Adafruit Industries' `CharLCD library
<https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCD>`_
as well as by Arduino's `LiquidCrystal library
<http://arduino.cc/en/Reference/LiquidCrystal>`_.

The GPIO access is provided by the `RPIO <https://github.com/metachris/RPIO>`_
library.


Goals
=====

- Simple to use API
- Support for both 4 bit and 8 bit modes
- Python 2/3 compatible


API
===

Init, Setup, Teardown
---------------------

.. sourcecode:: python

    import RPIO
    from RPLCD import CharLCD

    # Initialize LCD
    lcd = CharLCD(pin_rs=15, pin_e=16, pins_data=[21, 22, 23, 24],
                  numbering_mode=RPIO.BOARD)
    lcd.setup(cols=20, rows=4, dotsize=8)

    # (...)

    lcd.close(clear=True)

Properties
----------

- ``cursor_pos`` -> ``(row, col)``
- ``cursor_move_mode`` -> ``1`` / ``2``
- ``write_shift_mode`` -> ``1`` / ``2``
- ``display_enabled`` -> ``True`` / ``False``
- ``cursor_mode`` -> ``0`` / ``1`` / ``2``

High Level Functions
--------------------

- ``write_string(value)``: Write the specified string to the display.
- ``clear()``: Overwrite display with blank characters and reset cursor position.
- ``home()``: Set cursor to initial position and reset any shifting.
- ``shift_display(amount)``: Shift the display. Use negative amounts to shift
  left and positive amounts to shift right.

Mid Level Functions
-------------------

- ``write(value)``: Send a raw command to the LCD.
- ``command(value)``: Write a raw byte to the LCD.


Resources
=========

- TC2004A-01 Data Sheet: http://www.adafruit.com/datasheets/TC2004A-01.pdf
- HD44780U Data Sheet: http://www.adafruit.com/datasheets/HD44780.pdf


License
=======

This code is licensed under the MIT license, see the `LICENSE file
<https://github.com/dbrgn/RPLCD/blob/master/LICENSE>`_ or `tldrlegal
<http://www.tldrlegal.com/license/mit-license>`_ for more information. 
