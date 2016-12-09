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


Custom Characters
=================

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

Scrolling Text
==============

I wrote a blogpost on how to implement scrolling text:
https://blog.dbrgn.ch/2014/4/20/scrolling-text-with-rplcd/

To see the result, go to https://www.youtube.com/watch?v=49RkQeiVTGU.
