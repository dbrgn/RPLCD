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

from .lcd import CharLCD as BaseCharLCD
from .i2c_lib import I2CDevice


class CharLCD(BaseCharLCD):
    def __init__(self, cols=20, rows=4, dotsize=8):
	super(self, CharLCD).__init__(cols, rows, dotsize)

        # Currently the I2C mode only supports 4 bit communication 
    	self.data_bus_mode = LCD_4BITMODE
        
	# Call superclass
	super(CharLCD, self).__init__(cols, rows, dotsize)

    def _init_connection(self):
        print('init connection')

    def _close_connection(self):
        print('close connection')

    # Low level commands

    def _send(self, value, mode):
        """Send the specified value to the display with automatic 4bit / 8bit
        selection. The rs_mode is either ``RS_DATA`` or ``RS_INSTRUCTION``."""
        pass

    def _write4bits(self, value):
        """Write 4 bits of data into the data bus."""
        pass

    def _write8bits(self, value):
        """Write 8 bits of data into the data bus."""
        raise NotImplementedError('I2C currently supports only 4bit.')
