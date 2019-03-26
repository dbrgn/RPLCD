# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2018 Danilo Bargen

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
from __future__ import print_function, division, absolute_import, unicode_literals

from collections import namedtuple

from . import codecs
from . import common as c
from .compat import range


LCDConfig = namedtuple('LCDConfig', 'rows cols dotsize')


# # # MAIN # # #

class BaseCharLCD(object):

    # Init, setup, teardown

    def __init__(self, cols=20, rows=4, dotsize=8, charmap='A02', auto_linebreaks=True):
        """
        Character LCD controller. Base class only, you should use a subclass.

        Args:
            cols:
                Number of columns per row (usually 16 or 20). Default 20.
            rows:
                Number of display rows (usually 1, 2 or 4). Default: 4.
            dotsize:
                Some 1 line displays allow a font height of 10px.
                Allowed: 8 or 10. Default: 8.
            charmap:
                The character map used. Depends on your LCD. This must be
                either ``A00`` or ``A02`` or ``ST0B``.  Default: ``A02``.
            auto_linebreaks:
                Whether or not to automatically insert line breaks.
                Default: True.

        """
        assert dotsize in [8, 10], 'The ``dotsize`` argument should be either 8 or 10.'

        # Initialize codec
        if charmap == 'A00':
            self.codec = codecs.A00Codec()
        elif charmap == 'A02':
            self.codec = codecs.A02Codec()
            pass
        elif charmap == 'ST0B':
            self.codec = codecs.ST0BCodec()
            pass
        else:
            raise ValueError(
                'The ``charmap`` argument must be either ``A00`` or ``A02`` or ``ST0B``')

        # LCD configuration
        self.lcd = LCDConfig(rows=rows, cols=cols, dotsize=dotsize)

        # Setup initial display configuration
        displayfunction = self.data_bus_mode | c.LCD_5x8DOTS
        if rows == 1:
            displayfunction |= c.LCD_1LINE
        elif rows in [2, 4]:
            # LCD only uses two lines on 4 row displays
            displayfunction |= c.LCD_2LINE
        if dotsize == 10:
            # For some 1 line displays you can select a 10px font.
            displayfunction |= c.LCD_5x10DOTS

        # Create content cache
        self._content = [[0x20] * cols for _ in range(rows)]

        # Set up auto linebreaks
        self.auto_linebreaks = auto_linebreaks
        self.recent_auto_linebreak = False

        # Initialize display
        self._init_connection()

        # Choose 4 or 8 bit mode
        if self.data_bus_mode == c.LCD_4BITMODE:
            # Hitachi manual page 46
            self.command(0x03)
            c.msleep(4.5)
            self.command(0x03)
            c.msleep(4.5)
            self.command(0x03)
            c.usleep(100)
            self.command(0x02)
        elif self.data_bus_mode == c.LCD_8BITMODE:
            # Hitachi manual page 45
            self.command(0x30)
            c.msleep(4.5)
            self.command(0x30)
            c.usleep(100)
            self.command(0x30)
        else:
            raise ValueError('Invalid data bus mode: {}'.format(self.data_bus_mode))

        # Write configuration to display
        self.command(c.LCD_FUNCTIONSET | displayfunction)
        c.usleep(50)

        # Configure display mode
        self._display_mode = c.LCD_DISPLAYON
        self._cursor_mode = c.CursorMode.hide
        self.command(c.LCD_DISPLAYCONTROL | self._display_mode | self._cursor_mode)
        c.usleep(50)

        # Clear display
        self.clear()

        # Configure entry mode
        self._text_align_mode = c.Alignment.left
        self._display_shift_mode = c.ShiftMode.cursor
        self._cursor_pos = (0, 0)
        self.command(c.LCD_ENTRYMODESET | self._text_align_mode | self._display_shift_mode)
        c.usleep(50)

    def close(self, clear=False):
        if clear:
            self.clear()
        self._close_connection()

    # Properties

    def _get_cursor_pos(self):
        return self._cursor_pos

    def _set_cursor_pos(self, value):
        if not hasattr(value, '__getitem__') or len(value) != 2:
            raise ValueError('Cursor position should be determined by a 2-tuple.')
        if value[0] not in range(self.lcd.rows) or value[1] not in range(self.lcd.cols):
            msg = 'Cursor position {pos!r} invalid on a {lcd.rows}x{lcd.cols} LCD.'
            raise ValueError(msg.format(pos=value, lcd=self.lcd))
        row_offsets = [0x00, 0x40, self.lcd.cols, 0x40 + self.lcd.cols]
        self._cursor_pos = value
        self.command(c.LCD_SETDDRAMADDR | row_offsets[value[0]] + value[1])
        c.usleep(50)

    cursor_pos = property(_get_cursor_pos, _set_cursor_pos,
            doc='The cursor position as a 2-tuple (row, col).')

    def _get_text_align_mode(self):
        if self._text_align_mode == c.Alignment.left:
            return 'left'
        elif self._text_align_mode == c.Alignment.right:
            return 'right'
        else:
            raise ValueError('Internal _text_align_mode has invalid value.')

    def _set_text_align_mode(self, value):
        if value == 'left':
            self._text_align_mode = c.Alignment.left
        elif value == 'right':
            self._text_align_mode = c.Alignment.right
        else:
            raise ValueError('Text align mode must be either `left` or `right`')
        self.command(c.LCD_ENTRYMODESET | self._text_align_mode | self._display_shift_mode)
        c.usleep(50)

    text_align_mode = property(_get_text_align_mode, _set_text_align_mode,
            doc='The text alignment (``left`` or ``right``).')

    def _get_write_shift_mode(self):
        if self._display_shift_mode == c.ShiftMode.cursor:
            return 'cursor'
        elif self._display_shift_mode == c.ShiftMode.display:
            return 'display'
        else:
            raise ValueError('Internal _display_shift_mode has invalid value.')

    def _set_write_shift_mode(self, value):
        if value == 'cursor':
            self._display_shift_mode = c.ShiftMode.cursor
        elif value == 'display':
            self._display_shift_mode = c.ShiftMode.display
        else:
            raise ValueError('Write shift mode must be either `cursor` or `display`.')
        self.command(c.LCD_ENTRYMODESET | self._text_align_mode | self._display_shift_mode)
        c.usleep(50)

    write_shift_mode = property(_get_write_shift_mode, _set_write_shift_mode,
            doc='The shift mode when writing (``cursor`` or ``display``).')

    def _get_display_enabled(self):
        return self._display_mode == c.LCD_DISPLAYON

    def _set_display_enabled(self, value):
        self._display_mode = c.LCD_DISPLAYON if value else c.LCD_DISPLAYOFF
        self.command(c.LCD_DISPLAYCONTROL | self._display_mode | self._cursor_mode)
        c.usleep(50)

    display_enabled = property(_get_display_enabled, _set_display_enabled,
            doc='Whether or not to display any characters.')

    def _get_cursor_mode(self):
        if self._cursor_mode == c.CursorMode.hide:
            return 'hide'
        elif self._cursor_mode == c.CursorMode.line:
            return 'line'
        elif self._cursor_mode == c.CursorMode.blink:
            return 'blink'
        else:
            raise ValueError('Internal _cursor_mode has invalid value.')

    def _set_cursor_mode(self, value):
        if value == 'hide':
            self._cursor_mode = c.CursorMode.hide
        elif value == 'line':
            self._cursor_mode = c.CursorMode.line
        elif value == 'blink':
            self._cursor_mode = c.CursorMode.blink
        else:
            raise ValueError('Cursor mode must be one of `hide`, `line` or `blink`.')
        self.command(c.LCD_DISPLAYCONTROL | self._display_mode | self._cursor_mode)
        c.usleep(50)

    cursor_mode = property(_get_cursor_mode, _set_cursor_mode,
            doc='How the cursor should behave (``hide``, ``line`` or ``blink``).')

    # High level commands

    def write_string(self, value):
        """
        Write the specified unicode string to the display.

        To control multiline behavior, use newline (``\\n``) and carriage
        return (``\\r``) characters.

        Lines that are too long automatically continue on next line, as long as
        ``auto_linebreaks`` has not been disabled.

        Make sure that you're only passing unicode objects to this function.
        The unicode string is then converted to the correct LCD encoding by
        using the charmap specified at instantiation time.

        If you're dealing with bytestrings (the default string type in Python
        2), convert it to a unicode object using the ``.decode(encoding)``
        method and the appropriate encoding. Example for UTF-8 encoded strings:

        .. code::

            >>> bstring = 'Temperature: 30°C'
            >>> bstring
            'Temperature: 30\xc2\xb0C'
            >>> bstring.decode('utf-8')
            u'Temperature: 30\xb0C'

        """
        encoded = self.codec.encode(value)  # type: List[int]
        ignored = False

        for [char, lookahead] in c.sliding_window(encoded, lookahead=1):

            # If the previous character has been ignored, skip this one too.
            if ignored is True:
                ignored = False
                continue

            # Write regular chars
            if char not in [codecs.CR, codecs.LF]:
                self.write(char)
                continue

            # We're now left with only CR and LF characters. If an auto
            # linebreak happened recently, and the lookahead matches too,
            # ignore this write.
            if self.recent_auto_linebreak is True:
                crlf = (char == codecs.CR and lookahead == codecs.LF)
                lfcr = (char == codecs.LF and lookahead == codecs.CR)
                if crlf or lfcr:
                    ignored = True
                    continue

            # Handle newlines and carriage returns
            row, col = self.cursor_pos
            if char == codecs.LF:
                if row < self.lcd.rows - 1:
                    self.cursor_pos = (row + 1, col)
                else:
                    self.cursor_pos = (0, col)
            elif char == codecs.CR:
                if self.text_align_mode == 'left':
                    self.cursor_pos = (row, 0)
                else:
                    self.cursor_pos = (row, self.lcd.cols - 1)

    def clear(self):
        """Overwrite display with blank characters and reset cursor position."""
        self.command(c.LCD_CLEARDISPLAY)
        self._cursor_pos = (0, 0)
        self._content = [[0x20] * self.lcd.cols for _ in range(self.lcd.rows)]
        c.msleep(2)

    def home(self):
        """Set cursor to initial position and reset any shifting."""
        self.command(c.LCD_RETURNHOME)
        self._cursor_pos = (0, 0)
        c.msleep(2)

    def shift_display(self, amount):
        """Shift the display. Use negative amounts to shift left and positive
        amounts to shift right."""
        if amount == 0:
            return
        direction = c.LCD_MOVERIGHT if amount > 0 else c.LCD_MOVELEFT
        for i in range(abs(amount)):
            self.command(c.LCD_CURSORSHIFT | c.LCD_DISPLAYMOVE | direction)
            c.usleep(50)

    def create_char(self, location, bitmap):
        """Create a new character.

        The HD44780 supports up to 8 custom characters (location 0-7).

        :param location: The place in memory where the character is stored.
            Values need to be integers between 0 and 7.
        :type location: int
        :param bitmap: The bitmap containing the character. This should be a
            tuple of 8 numbers, each representing a 5 pixel row.
        :type bitmap: tuple of int
        :raises AssertionError: Raised when an invalid location is passed in or
            when bitmap has an incorrect size.

        Example:

        .. sourcecode:: python

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

        """
        assert 0 <= location <= 7, 'Only locations 0-7 are valid.'
        assert len(bitmap) == 8, 'Bitmap should have exactly 8 rows.'

        # Store previous position
        pos = self.cursor_pos

        # Write character to CGRAM
        self.command(c.LCD_SETCGRAMADDR | location << 3)
        for row in bitmap:
            self._send_data(row)

        # Restore cursor pos
        self.cursor_pos = pos

    # Mid level commands

    def command(self, value):
        """Send a raw command to the LCD."""
        self._send_instruction(value)

    def write(self, value):  # type: (int) -> None
        """Write a raw byte to the LCD."""

        # Get current position
        row, col = self._cursor_pos

        # Write byte if changed
        try:
            if self._content[row][col] != value:
                self._send_data(value)
                self._content[row][col] = value  # Update content cache
                unchanged = False
            else:
                unchanged = True
        except IndexError as e:
            # Position out of range
            if self.auto_linebreaks is True:
                raise e
            self._send_data(value)
            unchanged = False

        # Update cursor position.
        if self.text_align_mode == 'left':
            if self.auto_linebreaks is False or col < self.lcd.cols - 1:
                # No newline, update internal pointer
                newpos = (row, col + 1)
                if unchanged:
                    self.cursor_pos = newpos
                else:
                    self._cursor_pos = newpos
                self.recent_auto_linebreak = False
            else:
                # Newline, reset pointer
                if row < self.lcd.rows - 1:
                    self.cursor_pos = (row + 1, 0)
                else:
                    self.cursor_pos = (0, 0)
                self.recent_auto_linebreak = True
        else:
            if self.auto_linebreaks is False or col > 0:
                # No newline, update internal pointer
                newpos = (row, col - 1)
                if unchanged:
                    self.cursor_pos = newpos
                else:
                    self._cursor_pos = newpos
                self.recent_auto_linebreak = False
            else:
                # Newline, reset pointer
                if row < self.lcd.rows - 1:
                    self.cursor_pos = (row + 1, self.lcd.cols - 1)
                else:
                    self.cursor_pos = (0, self.lcd.cols - 1)
                self.recent_auto_linebreak = True

    def cr(self):  # type: () -> None
        """Write a carriage return (``\\r``) character to the LCD."""
        self.write_string('\r')

    def lf(self):  # type: () -> None
        """Write a line feed (``\\n``) character to the LCD."""
        self.write_string('\n')

    def crlf(self):  # type: () -> None
        """Write a line feed and a carriage return (``\\r\\n``) character to the LCD."""
        self.write_string('\r\n')
