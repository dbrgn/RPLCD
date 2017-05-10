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

from smbus import SMBus

from . import common as c
from .lcd import BaseCharLCD


class CharLCD(BaseCharLCD):
    def __init__(self, address, port=1,
                       cols=20, rows=4, dotsize=8,
                       charmap='A02',
                       auto_linebreaks=True,
                       backlight_enabled=True, i2c_expander="PCF8574"):
        """
        CharLCD via PCF8574 I2C port expander:

            Pin mapping::

            7  | 6  | 5  | 4  | 3  | 2  | 1  | 0
            D7 | D6 | D5 | D4 | BL | EN | RW | RS


       CharLCD via Adafruit i2c/SPI LCD Backback with MCP23008 I2C port expander:

            Warning: You will most likely need a level shifter (that supports i2c)
            between the SCL/SDA connections on the backpack and the Raspberry Pi.
            Or you might damage the Pi and possibly any other 3.3V i2c devices
            connected on the i2c bus. The SCL/SDA outputs are rated 0.7*VDD
            which means the MCP23008 outputs 3.5V when 5V is applied to drive the LCD.

            Will most likely work with only a MCP23008 as well, but not tested.
            The MCP23008 needs to be connected the exactly the same way as the backpack.

            For complete schematics see the adafruit page at:
            https://learn.adafruit.com/i2c-spi-lcd-backpack/

            4-bit operation only supported.

            Pin mapping::

            7    |  6  |  5  |  4  |  3  | 2 | 1  | 0
            LITE | DB7 | DB6 | DB5 | DB4 | E | RS | -

            Note: MCP23017 is NOT supported, but the code can easily be adapted for it.


        :param address: The I2C address of your LCD.
        :type address: int
        :param port: The I2C port number. Default: ``1``.
        :type port: int
        :param cols: Number of columns per row (usually 16 or 20). Default: ``20``.
        :type cols: int
        :param rows: Number of display rows (usually 1, 2 or 4). Default: ``4``.
        :type rows: int
        :param dotsize: Some 1 line displays allow a font height of 10px.
            Allowed: 8 or 10. Default: ``8``.
        :type dotsize: int
        :param charmap: The character map used. Depends on your LCD. This must
            be either ``A00`` or ``A02``. Default: ``A02``.
        :type charmap: str
        :param auto_linebreaks: Whether or not to automatically insert line breaks.
            Default: ``True``.
        :type auto_linebreaks: bool
        :param backlight_enabled: Whether the backlight is enabled initially. Default: ``True``.
        :type backlight_enabled: bool
        :param i2c_expander: Set your i2c chip type. "PCF8574" or "MCP23008" supported. Default: "PCF8574"
        """

        # Set own address and port.
        self.address = address
        self.port = port

        # Set i2c expander, "PCF8574" and "MCP23008" are supported.
        self.i2c_expander = i2c_expander

        # Currently the I2C mode only supports 4 bit communication
        self.data_bus_mode = c.LCD_4BITMODE

        # Set backlight status
        if(self.i2c_expander == "PCF8574"):
            self._backlight = c.LCD_BACKLIGHT if backlight_enabled else c.LCD_NOBACKLIGHT
        elif(self.i2c_expander == "MCP23008"):
            self._backlight = c.MCP23008_BACKLIGHT if backlight_enabled else c.MCP23008_NOBACKLIGHT
        else:
            raise NotImplementedError('I2C expander is not supported.')
        # Call superclass
        super(CharLCD, self).__init__(cols, rows, dotsize,
                                      charmap=charmap,
                                      auto_linebreaks=auto_linebreaks)

        # Refresh backlight status
        self.backlight_enabled = backlight_enabled

    def _init_connection(self):
        self.bus = SMBus(self.port)

        if(self.i2c_expander == "PCF8574"):
            c.msleep(50)
        elif(self.i2c_expander == "MCP23008"):
            # Set IO DIRection to output on all GPIOs (GP0-GP7)
            self.bus.write_byte_data(self.address, c.MCP23008_IODIR, 0x00)
            # Variable for storing data and applying bitmasks and shifting.
            self._mcp_data = 0
        else:
            raise NotImplementedError('I2C expander is not supported.')

    def _close_connection(self):
        # Nothing to do here?
        pass

    # Properties

    def _get_backlight_enabled(self):
        if(self.i2c_expander == "PCF8574"):
            return self._backlight == c.LCD_BACKLIGHT
        elif(self.i2c_expander == "MCP23008"):
            return self._backlight == c.MCP23008_BACKLIGHT
        else:
            raise NotImplementedError('I2C expander is not supported.')

    def _set_backlight_enabled(self, value):
        if(self.i2c_expander == "PCF8574"):
            self._backlight = c.LCD_BACKLIGHT if value else c.LCD_NOBACKLIGHT
            self.bus.write_byte(self.address, self._backlight)
        elif(self.i2c_expander == "MCP23008"):
            if(value):
                self._mcp_data |= c.MCP23008_BACKLIGHT
            else:
                self._mcp_data &= c.MCP23008_NOBACKLIGHT
            self.bus.write_byte_data(self.address, c.MCP23008_GPIO, self._mcp_data)
        else:
            raise NotImplementedError('I2C expander is not supported.')

    backlight_enabled = property(_get_backlight_enabled, _set_backlight_enabled,
            doc='Whether or not to enable the backlight. Either ``True`` or ``False``.')

    # Low level commands

    def _send(self, value, mode):
        """Send the specified value to the display with automatic 4bit / 8bit selection.
        The rs_mode is either ``common.RS_DATA`` or ``common.RS_INSTRUCTION``."""
        if(self.i2c_expander == "PCF8574"):
            self._write4bits(mode | (value & 0xF0))
            self._write4bits(mode | ((value << 4) & 0xF0))
        elif(self.i2c_expander == "MCP23008"):
            if(mode == c.RS_INSTRUCTION):
                self._mcp_data &= ~c.MCP23008_RS
                self._pulse_data(value >> 4)
                self._pulse_data(value & 0x0F)
            elif(mode == c.RS_DATA):
                self._mcp_data |= c.MCP23008_RS
                self._pulse_data(value >> 4)
                self._pulse_data(value & 0x0F)
        else:
            raise NotImplementedError('I2C expander is not supported.')

    def _write4bits(self, value):
        """Write 4 bits of data into the data bus."""
        self.bus.write_byte(self.address, value | self._backlight)
        self._pulse_data(value)

    def _write8bits(self, value):
        """Write 8 bits of data into the data bus."""
        raise NotImplementedError('I2C currently supports only 4bit.')

    def _pulse_data(self, value):
        """Pulse the `enable` flag to process value."""
        if(self.i2c_expander == "PCF8574"):
            self.bus.write_byte(self.address, ((value & ~c.PIN_ENABLE) | self._backlight))
            c.usleep(1)
            self.bus.write_byte(self.address, value | c.PIN_ENABLE | self._backlight)
            c.usleep(1)
            self.bus.write_byte(self.address, ((value & ~c.PIN_ENABLE) | self._backlight))
            c.usleep(100)
        elif(self.i2c_expander == "MCP23008"):
            self._mcp_data &= ~c.MCP23008_DATAMASK
            self._mcp_data |= value << c.MCP23008_DATASHIFT
            self._mcp_data &= ~c.MCP23008_E
            self.bus.write_byte_data(self.address, c.MCP23008_GPIO, self._mcp_data)
            c.usleep(1)
            self._mcp_data |= c.MCP23008_E
            self.bus.write_byte_data(self.address, c.MCP23008_GPIO, self._mcp_data)
            c.usleep(1)
            self._mcp_data &= ~c.MCP23008_E
            self.bus.write_byte_data(self.address, c.MCP23008_GPIO, self._mcp_data)
            c.usleep(100)
        else:
            raise NotImplementedError('I2C expander is not supported.')
