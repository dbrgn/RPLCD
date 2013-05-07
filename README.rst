RPLCD
=====

A Python 2/3 Raspberry PI Character LCD library for the Hitachi HD44780
controller.

Tested with the 20x4 LCD that is sold for example by `adafruit.com
<http://www.adafruit.com/products/198>`_ or `mikroshop.ch
<http://mikroshop.ch/LED_LCD.html?gruppe=7&artikel=84>`_.

This library is inspired by Adafruit Industries' `CharLCD library
<https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCD>`_
as well as by Arduino's `LiquidCrystal library
<http://arduino.cc/en/Reference/LiquidCrystal>`_.

The GPIO access is provided by the `RPIO <https://github.com/metachris/RPIO>`_
library.


Ideas / Goals
-------------

- Very simple to use API
- Python 2/3 compatible
- Idiomatic Python, e.g. using context managers
- Contrast support via PWM 
- Busy flag checking instead of sleeping


API Drafts
----------

.. sourcecode:: python

    import RPIO
    from RPLCD import CharLCD, cursor

    # Initialize LCD
    lcd = CharLCD(cols=20, rows=4,
                  pin_rs=15, pin_e=16, pins_data=[21, 22, 23, 24],
                  numbering_mode=RPIO.BOARD)

    # Write to display
    lcd.write('Hello world!')

    # Overwrite display
    lcd.write('This is simple!')

    # Set cursor using function
    lcd.set_cursor(1, 9)

    # Write or overwrite only the selected bytes
    # Display now shows ``This is awesome``
    lcd.write_raw('awesome')

    # Use context manager to set cursor
    with cursor(1, 9):
        lcd.write_raw('fan-tas-tic')

    # Turn LCD off and on
    lcd.turn_off()
    lcd.turn_on()

    # Clear LCD
    lcd.clear()

    # Clear LCD, cleanup GPIO
    lcd.close(clear=True)


Resources
---------

- TC2004A-01 Data Sheet: http://www.adafruit.com/datasheets/TC2004A-01.pdf
- HD44780U Data Sheet: http://www.adafruit.com/datasheets/HD44780.pdf


License
-------

This code is licensed under the MIT license, see the `LICENSE file
<https://github.com/dbrgn/RPLCD/blob/master/LICENSE>`_ or `tldrlegal
<http://www.tldrlegal.com/license/mit-license>`_ for more information. 
