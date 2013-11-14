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

import RPIO

from . import common as c
from .lcd import CharLCD as BaseCharLCD
from .compat import range


PinConfig = namedtuple('PinConfig', 'rs rw e d0 d1 d2 d3 d4 d5 d6 d7 mode')


class CharLCD(BaseCharLCD):
    def __init__(self, pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
                       numbering_mode=RPIO.BOARD,
                       cols=20, rows=4, dotsize=8):
        """
        Character LCD controller.

        The default pin numbers are based on the BOARD numbering scheme (1-26).

        You can save 1 pin by not using RW. Set ``pin_rw`` to ``None`` if you
        want this.

        Args:
            pin_rs:
                Pin for register select (RS). Default: 15.
            pin_rw:
                Pin for selecting read or write mode (R/W). Set this to
                ``None`` for read only mode. Default: 18.
            pin_e:
                Pin to start data read or write (E). Default: 16.
            pins_data:
                List of data bus pins in 8 bit mode (DB0-DB7) or in 8 bit mode
                (DB4-DB7) in ascending order. Default: [21, 22, 23, 24].
            numbering_mode:
                Which scheme to use for numbering the GPIO pins.
                Default: RPIO.BOARD (1-26).
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
        # Set attributes
        self.numbering_mode = numbering_mode
        if len(pins_data) == 4:  # 4 bit mode
            self.data_bus_mode = c.LCD_4BITMODE
            block1 = [None] * 4
        elif len(pins_data) == 8:  # 8 bit mode
            self.data_bus_mode = c.LCD_8BITMODE
            block1 = pins_data[:4]
        else:
            raise ValueError('There should be exactly 4 or 8 data pins.')
        block2 = pins_data[-4:]
        self.pins = PinConfig(rs=pin_rs, rw=pin_rw, e=pin_e,
                              d0=block1[0], d1=block1[1], d2=block1[2], d3=block1[3],
                              d4=block2[0], d5=block2[1], d6=block2[2], d7=block2[3],
                              mode=numbering_mode)

        # Call superclass
        super(CharLCD, self).__init__(cols, rows, dotsize)

    def _init_connection(self):
        # Setup GPIO
        RPIO.setmode(self.numbering_mode)
        for pin in list(filter(None, self.pins))[:-1]:
            RPIO.setup(pin, RPIO.OUT)

        # Initialization
        c.msleep(50)
        RPIO.output(self.pins.rs, 0)
        RPIO.output(self.pins.e, 0)
        if self.pins.rw is not None:
            RPIO.output(self.pins.rw, 0)

    def _close_connection(self):
        RPIO.cleanup()

    # Low level commands

    def _send(self, value, mode):
        """Send the specified value to the display with automatic 4bit / 8bit selection.
        The mode is either ``common.RS_DATA`` or ``common.RS_INSTRUCTION``."""

        # Choose instruction or data mode
        RPIO.output(self.pins.rs, mode)

        # If the RW pin is used, set it to low in order to write.
        if self.pins.rw is not None:
            RPIO.output(self.pins.rw, 0)

        # Write data out in chunks of 4 or 8 bit
        if self.data_bus_mode == c.LCD_8BITMODE:
            self._write8bits(value)
        else:
            self._write4bits(value >> 4)
            self._write4bits(value)

    def _write4bits(self, value):
        """Write 4 bits of data into the data bus."""
        for i in range(4):
            bit = (value >> i) & 0x01
            RPIO.output(self.pins[i + 7], bit)
        self._pulse_enable()

    def _write8bits(self, value):
        """Write 8 bits of data into the data bus."""
        for i in range(8):
            bit = (value >> i) & 0x01
            RPIO.output(self.pins[i + 3], bit)
        self._pulse_enable()

    def _pulse_enable(self):
        """Pulse the `enable` flag to process data."""
        RPIO.output(self.pins.e, 0)
        c.usleep(1)
        RPIO.output(self.pins.e, 1)
        c.usleep(1)
        RPIO.output(self.pins.e, 0)
        c.usleep(100)  # commands need > 37us to settle
