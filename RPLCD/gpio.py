# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2017 Danilo Bargen

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

import RPi.GPIO as GPIO

from . import common as c
from .lcd import BaseCharLCD
from .compat import range


PinConfig = namedtuple('PinConfig', 'rs rw e d0 d1 d2 d3 d4 d5 d6 d7 backlight mode')


class CharLCD(BaseCharLCD):
    def __init__(self, pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
                       pin_backlight=None, backlight_mode=c.BacklightMode.active_low,
                       backlight_enabled=True,
                       numbering_mode=GPIO.BOARD,
                       cols=20, rows=4, dotsize=8,
                       charmap='A02',
                       auto_linebreaks=True):
        """
        Character LCD controller.

        The default pin numbers are based on the BOARD numbering scheme (1-26).

        You can save 1 pin by not using RW. Set ``pin_rw`` to ``None`` if you
        want this.

        :param pin_rs: Pin for register select (RS). Default: ``15``.
        :type pin_rs: int
        :param pin_rw: Pin for selecting read or write mode (R/W). Set this to
            ``None`` for read only mode. Default: ``18``.
        :type pin_rw: int
        :param pin_e: Pin to start data read or write (E). Default: ``16``.
        :type pin_e: int
        :param pins_data: List of data bus pins in 8 bit mode (DB0-DB7) or in 4
            bit mode (DB4-DB7) in ascending order. Default: ``[21, 22, 23, 24]``.
        :type pins_data: list of int
        :param pin_backlight: Pin for controlling backlight on/off. Set this to
            ``None`` for no backlight control. Default: ``None``.
        :type pin_backlight: int
        :param backlight_mode: Set this to one of the BacklightMode enum values
            to configure the operating control for the backlight. Has no effect if
            pin_backlight is ``None``
        :type backlight_mode: BacklightMode
        :param backlight_enabled: Whether the backlight is enabled initially.
            Default: ``True``. Has no effect if pin_backlight is ``None``
        :type backlight_enabled: bool
        :param numbering_mode: Which scheme to use for numbering of the GPIO pins,
            either ``GPIO.BOARD`` or ``GPIO.BCM``. Default: ``GPIO.BOARD`` (1-26).
        :type numbering_mode: int
        :param rows: Number of display rows (usually 1, 2 or 4). Default: ``4``.
        :type rows: int
        :param cols: Number of columns per row (usually 16 or 20). Default ``20``.
        :type cols: int
        :param dotsize: Some 1 line displays allow a font height of 10px.
            Allowed: ``8`` or ``10``. Default: ``8``.
        :type dotsize: int
        :param charmap: The character map used. Depends on your LCD. This must
            be either ``A00`` or ``A02``. Default: ``A02``.
        :type charmap: str
        :param auto_linebreaks: Whether or not to automatically insert line
            breaks. Default: ``True``.
        :type auto_linebreaks: bool

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
                              backlight=pin_backlight,
                              mode=numbering_mode)
        self.backlight_mode = backlight_mode

        # Call superclass
        super(CharLCD, self).__init__(cols, rows, dotsize,
                                      charmap=charmap,
                                      auto_linebreaks=auto_linebreaks)

        # Set backlight status
        if pin_backlight is not None:
            self.backlight_enabled = backlight_enabled

    def _init_connection(self):
        # Setup GPIO
        GPIO.setmode(self.numbering_mode)
        for pin in list(filter(None, self.pins))[:-1]:
            GPIO.setup(pin, GPIO.OUT)
        if self.pins.backlight is not None:
            GPIO.setup(self.pins.backlight, GPIO.OUT)

        # Initialization
        c.msleep(50)
        GPIO.output(self.pins.rs, 0)
        GPIO.output(self.pins.e, 0)
        if self.pins.rw is not None:
            GPIO.output(self.pins.rw, 0)

    def _close_connection(self):
        GPIO.cleanup()

    # Properties

    def _get_backlight_enabled(self):
        # We could probably read the current GPIO output state via sysfs, but
        # for now let's just store the state in the class
        if self.pins.backlight is None:
            raise ValueError('You did not configure a GPIO pin for backlight control!')
        return bool(self._backlight_enabled)

    def _set_backlight_enabled(self, value):
        if self.pins.backlight is None:
            raise ValueError('You did not configure a GPIO pin for backlight control!')
        if not isinstance(value, bool):
            raise ValueError('backlight_enabled must be set to ``True`` or ``False``.')
        self._backlight_enabled = value
        GPIO.output(self.pins.backlight,
                    value ^ (self.backlight_mode is c.BacklightMode.active_low))

    backlight_enabled = property(_get_backlight_enabled, _set_backlight_enabled,
            doc='Whether or not to turn on the backlight.')

    # Low level commands

    def _send(self, value, mode):
        """Send the specified value to the display with automatic 4bit / 8bit
        selection. The rs_mode is either ``RS_DATA`` or ``RS_INSTRUCTION``."""

        # Choose instruction or data mode
        GPIO.output(self.pins.rs, mode)

        # If the RW pin is used, set it to low in order to write.
        if self.pins.rw is not None:
            GPIO.output(self.pins.rw, 0)

        # Write data out in chunks of 4 or 8 bit
        if self.data_bus_mode == c.LCD_8BITMODE:
            self._write8bits(value)
        else:
            self._write4bits(value >> 4)
            self._write4bits(value)

    def _send_data(self, value):
        """Send data to the display. """
        self._send(value, c.RS_DATA)

    def _send_instruction(self, value):
        """Send instruction to the display. """
        self._send(value, c.RS_INSTRUCTION)

    def _write4bits(self, value):
        """Write 4 bits of data into the data bus."""
        for i in range(4):
            bit = (value >> i) & 0x01
            GPIO.output(self.pins[i + 7], bit)
        self._pulse_enable()

    def _write8bits(self, value):
        """Write 8 bits of data into the data bus."""
        for i in range(8):
            bit = (value >> i) & 0x01
            GPIO.output(self.pins[i + 3], bit)
        self._pulse_enable()

    def _pulse_enable(self):
        """Pulse the `enable` flag to process data."""
        GPIO.output(self.pins.e, 0)
        c.usleep(1)
        GPIO.output(self.pins.e, 1)
        c.usleep(1)
        GPIO.output(self.pins.e, 0)
        c.usleep(100)  # commands need > 37us to settle
