# -*- coding: utf-8 -*-
"""
Copyright (C) 2013 Danilo Bargen

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

from . import common as c
from .compat import range


LCDConfig = namedtuple('LCDConfig', 'rows cols dotsize')


### MAIN ###

class CharLCD(object):

    # Init, setup, teardown

    def __init__(self, cols=20, rows=4, dotsize=8):
        """
        Character LCD controller. Base class only, you should use a subclass.

        Args:
            rows:
                Number of display rows (usually 1, 2 or 4). Default: 4.
            cols:
                Number of columns per row (usually 16 or 20). Default 20.
            dotsize:
                Some 1 line displays allow a font height of 10px.
                Allowed: 8 or 10. Default: 8.

        Returns:
            A :class:`CharLCD` instance.

        """
        assert dotsize in [8, 10], 'The ``dotsize`` argument should be either 8 or 10.'

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

        # Initialize display
        self._init_connection()

        # Write configuration to display
        self.command(c.LCD_FUNCTIONSET | displayfunction)
        c.usleep(50)

        # Configure display mode
        self._display_mode = c.LCD_DISPLAYON
        self._cursor_mode = int(c.CursorMode.hide)
        self.command(c.LCD_DISPLAYCONTROL | self._display_mode | self._cursor_mode)
        c.usleep(50)

        # Clear display
        self.clear()

        # Configure entry mode
        self._text_align_mode = int(c.Alignment.left)
        self._display_shift_mode = int(c.ShiftMode.cursor)
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
        row_offsets = [0x00, 0x40, 0x14, 0x54]  # TODO handle smaller displays
        self._cursor_pos = value
        self.command(c.LCD_SETDDRAMADDR | row_offsets[value[0]] + value[1])
        c.usleep(50)

    cursor_pos = property(_get_cursor_pos, _set_cursor_pos,
            doc='The cursor position as a 2-tuple (row, col).')

    def _get_text_align_mode(self):
        try:
            return c.Alignment[self._text_align_mode]
        except ValueError:
            raise ValueError('Internal _text_align_mode has invalid value.')

    def _set_text_align_mode(self, value):
        if not value in c.Alignment:
            raise ValueError('Cursor move mode must be of ``common.Alignment`` type.')
        self._text_align_mode = int(value)
        self.command(c.LCD_ENTRYMODESET | self._text_align_mode | self._display_shift_mode)
        c.usleep(50)

    text_align_mode = property(_get_text_align_mode, _set_text_align_mode,
            doc='The text alignment (``common.Alignment.left`` or ``common.Alignment.right``).')

    def _get_write_shift_mode(self):
        try:
            return c.ShiftMode[self._display_shift_mode]
        except ValueError:
            raise ValueError('Internal _display_shift_mode has invalid value.')

    def _set_write_shift_mode(self, value):
        if not value in c.ShiftMode:
            raise ValueError('Write shift mode must be of ``common.ShiftMode`` type.')
        self._display_shift_mode = int(value)
        self.command(c.LCD_ENTRYMODESET | self._text_align_mode | self._display_shift_mode)
        c.usleep(50)

    write_shift_mode = property(_get_write_shift_mode, _set_write_shift_mode,
            doc='The shift mode when writing (``common.ShiftMode.cursor`` or ' +
                '``common.ShiftMode.display``).')

    def _get_display_enabled(self):
        return self._display_mode == c.LCD_DISPLAYON

    def _set_display_enabled(self, value):
        self._display_mode = c.LCD_DISPLAYON if value else c.LCD_DISPLAYOFF
        self.command(c.LCD_DISPLAYCONTROL | self._display_mode | self._cursor_mode)
        c.usleep(50)

    display_enabled = property(_get_display_enabled, _set_display_enabled,
            doc='Whether or not to display any characters.')

    def _get_cursor_mode(self):
        try:
            return c.CursorMode[self._cursor_mode]
        except ValueError:
            raise ValueError('Internal _cursor_mode has invalid value.')

    def _set_cursor_mode(self, value):
        if not value in c.CursorMode:
            raise ValueError('Cursor mode must be of ``common.CursorMode`` type.')
        self._cursor_mode = int(value)
        self.command(c.LCD_DISPLAYCONTROL | self._display_mode | self._cursor_mode)
        c.usleep(50)

    cursor_mode = property(_get_cursor_mode, _set_cursor_mode,
            doc='How the cursor should behave (``common.CursorMode.hide``, ' +
                '``common.CursorMode.line`` or ``common.CursorMode.blink``).')

    # High level commands

    def write_string(self, value):
        """Write the specified string to the display.

        To control multiline behavior, use newline (\n) and carriage return
        (\r) characters.

        Lines that are too long automatically continue on next line.

        """
        for char in value:
            # Write regular chars
            if char not in '\n\r':
                self.write(ord(char))
                continue
            # Handle newlines and carriage returns
            row, col = self.cursor_pos
            if char == '\n':
                if row < self.lcd.rows - 1:
                    self.cursor_pos = (row + 1, col)
                else:
                    self.cursor_pos = (0, col)
            elif char == '\r':
                if self.text_align_mode is c.Alignment.left:
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

    # Mid level commands

    def command(self, value):
        """Send a raw command to the LCD."""
        self._send(value, c.RS_INSTRUCTION)

    def write(self, value):
        """Write a raw byte to the LCD."""

        # Get current position
        row, col = self._cursor_pos

        # Write byte if changed
        if self._content[row][col] != value:
            self._send(value, c.RS_DATA)
            self._content[row][col] = value  # Update content cache
            unchanged = False
        else:
            unchanged = True

        # Update cursor position.
        if self.text_align_mode is c.Alignment.left:
            if col < self.lcd.cols - 1:
                # No newline, update internal pointer
                newpos = (row, col + 1)
                if unchanged:
                    self.cursor_pos = newpos
                else:
                    self._cursor_pos = newpos
            else:
                # Newline, reset pointer
                if row < self.lcd.rows - 1:
                    self.cursor_pos = (row + 1, 0)
                else:
                    self.cursor_pos = (0, 0)
        else:
            if col > 0:
                # No newline, update internal pointer
                newpos = (row, col - 1)
                if unchanged:
                    self.cursor_pos = newpos
                else:
                    self._cursor_pos = newpos
            else:
                # Newline, reset pointer
                if row < self.lcd.rows - 1:
                    self.cursor_pos = (row + 1, self.lcd.cols - 1)
                else:
                    self.cursor_pos = (0, self.lcd.cols - 1)
