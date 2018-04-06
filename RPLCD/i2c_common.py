# -*- coding: utf-8 -*-
"""
Common functionality for I²C backends.

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

# PCF8574 backlight control
PCF8574_BACKLIGHT = 0x08
PCF8574_NOBACKLIGHT = 0x00

# PCF8574 Pin bitmasks
PCF8574_E = 0x4
PIN_READ_WRITE = 0x2  # TODO: Not used?
PIN_REGISTER_SELECT = 0x1  # TODO: Not used?

# MCP230XX backlight control
MCP230XX_BACKLIGHT = 0x80
MCP230XX_NOBACKLIGHT = 0x7f

# MCP230XX pin bitmasks and datamask
MCP230XX_RS = 0x02
MCP230XX_E = 0x4
MCP230XX_DATAMASK = 0x78
MCP230XX_DATASHIFT = 3

# MCP23008 Register addresses
MCP23008_IODIR = 0x00
MCP23008_GPIO = 0x09

# MCP23017 Register addresses
MCP23017_IODIRA = 0x00
MCP23017_IODIRB = 0x01
MCP23017_GPIOA = 0x12
MCP23017_GPIOB = 0x13
