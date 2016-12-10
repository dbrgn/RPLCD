Usage
#####

Make sure to read the :ref:`getting-started` section if you haven't done so yet.

Writing To Display
==================

Regular text can be written to the :class:`~RPLCD.i2c.CharLCD` instance using
the :meth:`~RPLCD.i2c.CharLCD.write_string` method. It accepts unicode strings.

The cursor position can be set by assigning a ``(row, col)`` tuple to
:attr:`~RPLCD.i2c.CharLCD.cursor_pos`. It can be reset to the starting position
with :meth:`~RPLCD.i2c.CharLCD.home`.

Newline characters (``\n``) move down one line and carriage returns (``\r``)
move to the beginning of the current line.

.. sourcecode:: python

    lcd.write_string('Raspberry Pi HD44780')
    lcd.cursor_pos = (2, 0)
    lcd.write_string('https://github.com/\n\rdbrgn/RPLCD')

.. image:: _static/photo.jpg
    :alt: Photo of 20x4 LCD in action

After your script has finished, you may want to close the connection and
optionally clear the screen with the :meth:`~RPLCD.gpio.CharLCD.close` method.

.. sourcecode:: python

    lcd.close(clear=True)

When using a GPIO based LCD, this will reset the GPIO configuration. Note that
doing this without clearing can lead to undesired effects on the LCD, because
the GPIO pins are floating (not configured as input or output anymore).


Clearing the Display
====================

You can clear the display by using the :meth:`~RPLCD.i2c.CharLCD.clear` method. It
will overwrite the data with blank characters and reset the cursor position.

Alternatively, if you want to hide all characters but keep the data in the LCD
memory, set the :attr:`~RPLCD.i2c.CharLCD.display_enabled` property to ``False``.


Custom Wiring
=============

When using a LCD connected via GPIO pins, the wiring can be customized in the
:class:`~RPLCD.gpio.CharLCD` constructor. These are the standard values:

.. sourcecode:: python

    lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24])


Writing Special Characters
==========================

You might find that some characters like umlauts aren't written correctly to the
display. This is because the LCDs usually don't use `ASCII`, `ISO-8859-1` or any
other standard encoding. Furthermore, different LCDs from different vendors
actualls use different character maps.

There is a script in this project though that writes the entire character map
between 0 and 255 to the display. Simply run it as root (so you have permissions
to access `/dev/mem`) and pass it the number of rows and cols in your LCD::

    $ sudo python show_charmap.py 2 16

Confirm each page with the enter key. Try to find the position of your desired
character using the console output. On my display for example, the "ü" character
is at position 129 (in contrast to `ISO-8859-1` or `UTF-8`, which use 252).

Now you can simply create a unicode character from the bit value and write it
to the LCD. If you're using Python 3:

.. code:: python

    >>> 'Z%srich is a city in Switzerland.' % chr(129)
    'Z\x81rich is a city in Switzerland.'

And on Python 2, where you need to explicitly use unicode strings:

.. code:: python

    >>> u'Z%srich is a city in Switzerland.' % unichr(129)
    u'Z\x81rich is a city in Switzerland.'

In case you need a character that is not included in the default device
character map, there is a possibility to create custom characters and write them
into the HD44780 CGRAM. For more information, see the :ref:`custom-characters`
section.


.. _custom-characters:

Creating Custom Characters
==========================

The HD44780 supports up to 8 user created characters. A character is defined by
a 8x5 bitmap. The bitmap should be a tuple of 8 numbers, each representing a 5
pixel row. Each character is written to a specific location in CGRAM (numbers
0-7).

.. sourcecode:: python

    >>> lcd = CharLCD()
    >>> smiley = (
    ...     0b00000,
    ...     0b01010,
    ...     0b01010,
    ...     0b00000,
    ...     0b10001,
    ...     0b10001,
    ...     0b01110,
    ...     0b00000,
    ... )
    >>> lcd.create_char(0, smiley)

To actually show a stored character on the display, use :py:func:`chr()
<python:chr>` (Python 3) or :py:func:`unichr() <python2:unichr>` (if you're
still stuck on Python 2) function in combination with the location number you
specified previously (e.g. ``write_string(unichr(2))``).

.. sourcecode:: python

    >>> lcd.write_string(chr(0))

The following tool can help you to create your custom characters:
https://omerk.github.io/lcdchargen/


Changing the Cursor Appearance
==============================

The cursor appearance can be changed by setting the
:attr:`~RPLCD.i2c.CharLCD.cursor_mode` property to one of the following three
:class:`~RPLCD.common.CursorMode` values:

- :attr:`~RPLCD.common.CursorMode.hide` – No cursor will be displayed
- :attr:`~RPLCD.common.CursorMode.line` – The cursor will be indicated with an
  underline
- :attr:`~RPLCD.common.CursorMode.blink` – The cursor will be indicated with a
  blinking square


Backlight Control
=================

I²C
~~~

If you're using an LCD connected through the I²C bus, you can directly turn on
the backlight using the boolean :attr:`~RPLCD.i2c.CharLCD.backlight_enabled` property.

GPIO
~~~~

By setting the ``pin_backlight`` parameter in the :class:`~RPLCD.gpio.CharLCD`
constructor, you can control a backlight circuit.

First of all, you need to build an external circuit to control the backlight,
most LCD modules don't support it directly. You could do this for example by
using a transistor and a pull-up resistor. Then connect the transistor to a GPIO
pin and configure that pin using the ``pin_backlight`` parameter in the
constructor. If you use an active high circuit instead of active low, you can
change that behavior by setting the  ``backlight_mode`` to either
:attr:`BacklightMode.active_high <RPLCD.common.BacklightMode.active_high>` or
:attr:`BacklightMode.active_low <RPLCD.common.BacklightMode.active_low>`. Now
you can toggle the :attr:`~RPLCD.gpio.CharLCD.backlight_enabled` property to
turn the backlight on and off.


Scrolling Text
==============

I wrote a blogpost on how to implement scrolling text:
https://blog.dbrgn.ch/2014/4/20/scrolling-text-with-rplcd/

To see the result, go to https://www.youtube.com/watch?v=49RkQeiVTGU.


Raw Commands
============

You can send raw commands to the LCD with :meth:`~RPLCD.i2c.CharLCD.command` and
write a raw byte to the LCD with :meth:`~RPLCD.i2c.CharLCD.write`. For more
information, please refer to the Hitachi HD44780 datasheet.
