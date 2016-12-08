# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2016 Danilo Bargen

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

from smbus import SMBus

from . import common as c
from .lcd import BaseCharLCD


class CharLCD(BaseCharLCD):
    """CharLCD via PCF8574 I2C port expander.

    Pin mapping::

        7  | 6  | 5  | 4  | 3  | 2  | 1  | 0
        D7 | D6 | D5 | D4 | BL | EN | RW | RS

    """
    def __init__(self, address, port=1, cols=20, rows=4, dotsize=8):
        self.address = address
        self.port = port
        self._backlight = c.LCD_BACKLIGHT

        # Currently the I2C mode only supports 4 bit communication
        self.data_bus_mode = c.LCD_4BITMODE

        # Call superclass
        super(CharLCD, self).__init__(cols, rows, dotsize)

    def _init_connection(self):
        print('init connection')
        self.bus = SMBus(self.port)
        c.msleep(50)

    def _close_connection(self):
        print('close connection')

    # High level commands

    def _get_backlight_enabled(self):
        return self._backlight == c.LCD_BACKLIGHT

    def _set_backlight_enabled(self, value):
        self._backlight = c.LCD_BACKLIGHT if value else c.LCD_NOBACKLIGHT
        self.bus.write_byte(self.address, self._backlight)

    backlight_enabled = property(_get_backlight_enabled, _set_backlight_enabled,
            doc='Whether or not to enable the backlight.')

    # Low level commands

    def _send(self, value, mode):
        """Send the specified value to the display with automatic 4bit / 8bit selection.
        The rs_mode is either ``common.RS_DATA`` or ``common.RS_INSTRUCTION``."""
        self._write4bits(mode | (value & 0xF0))
        self._write4bits(mode | ((value << 4) & 0xF0))

    def _write4bits(self, value):
        """Write 4 bits of data into the data bus."""
        self.bus.write_byte(self.address, value | self._backlight)
        self._pulse_data(value)

    def _write8bits(self, value):
        """Write 8 bits of data into the data bus."""
        raise NotImplementedError('I2C currently supports only 4bit.')

    def _pulse_data(self, value):
        """Pulse the `enable` flag to process value."""
        self.bus.write_byte(self.address, ((value & ~c.PIN_ENABLE) | self._backlight))
        c.usleep(1)
        self.bus.write_byte(self.address, value | c.PIN_ENABLE | self._backlight)
        c.usleep(1)
        self.bus.write_byte(self.address, ((value & ~c.PIN_ENABLE) | self._backlight))
        c.usleep(100)
