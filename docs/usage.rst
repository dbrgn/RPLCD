Usage
#####

Writing To Display
==================

Regular text can be written to the ``CharLCD`` instance using the
``write_string`` method. It accepts unicode strings.

The cursor position can be set by assigning a ``(row, col)`` tuple to
``cursor_pos``.

Newlines (``\n``) move down one line and carriage returns (``\r``) move to the
beginning of the current line.

.. sourcecode:: python

    >>> lcd.write_string(u'Raspberry Pi HD44780')
    >>> lcd.cursor_pos = (2, 0)
    >>> lcd.write_string(u'https://github.com/\n\rdbrgn/RPLCD')

.. image:: _static/photo.jpg
    :alt: Photo of 20x4 LCD in action


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
0-7). To actually show a stored character on the display, use ``unichr()``
function in combination with the location number you specified previously (e.g.
``write_string(unichr(2))``.

.. sourcecode:: python

    >>> from RPLCD.gpio import CharLCD, cleared, cursor
    >>> lcd = CharLCD()
    >>>
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
    >>> lcd.write_string(unichr(0))

The following tool can help you to create your custom characters:
https://omerk.github.io/lcdchargen/


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
