#!/usr/bin/env python
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

import sys

import RPi.GPIO as GPIO

from RPLCD import i2c, gpio
import lcdtests.show_charmap as show_charmap
import lcdtests.format_test_20x4 as format_test_20x4
import lcdtests.format_test_16x2 as format_test_16x2


def print_usage():
    print('Usage: %s i2c [test] <options>' % sys.argv[0])
    print('       %s gpio [test] <options>' % sys.argv[0])
    print('')
    print('[test] Which test to run:')
    print('')
    print('   show_charmap - Displays all characters in the charmap')
    print('   test_format  - Tests display formating')
    print('')
    # Options for i2c mode
    if ((len(sys.argv) > 1) and (sys.argv[1] == 'i2c')):
        print('<options> i2c options:')
        print('')
        print('   expander - Supported I²C port expanders are PCF8574, MCP23008 and MCP23017')
        print('   addr     - The I²C address (in hex format) can be found with')
        print('              `i2cdetect 1` from the i2c-tools package.')
        print('   cols     - The number of columns on your LCD, e.g. 16')
        print('   rows     - The number of rows on your LCD, e.g. 2')
        print('   charmap  - Charmap can be either A00 or A02. If your display contains Japanese')
        print('              characters, it probably uses the A00 charmap, otherwise A02.')
        print('              default=A00')
        print('')
        print('   Expander specific options:')
        print('')
        print('   MCP23017: gpio_bank - Either A or B')
        print('')
        print('Options format: name=value e.g. expander=MCP23008 (Example below)')

        print('%s i2c charmap expander=MCP23017 addr=0x20 cols=20 rows=4 gpio_bank=A' % sys.argv[0])
    # Options for GPIO mode
    elif ((len(sys.argv) > 1) and (sys.argv[1] == 'gpio')):

        print('<options> gpio options:')
        print('')
        print('   mode     - GPIO numbering mode, either BOARD or BCM, default=BOARD')
        print('   cols    - The number of columns on your LCD, e.g. 16')
        print('   rows    - The number of rows on your LCD, e.g. 2')
        print('   rs      - RS pin number')
        print('   rw      - RW pin number')
        print('   e       - E pin number')
        print('   bl      - Backlight pin number, default=None')
        print('   data    - Data (d0-d7) gpio pin numbers (4 or 8 numbers depending')
        print('                    on if you want 4 or 8 bit mode, separated by comma)')
        print('                    Example: data=1,2,3,4,5,6,7,8 (for 8-bit mode)')
        print('                             data=4,5,6,7,8 (for 4-bit mode)')
        print('   charmap - Charmap can be either A00 or A02. If your display contains Japanese')
        print('              characters, it probably uses the A00 charmap, otherwise A02.')
        print('              default=A00')
        print('')
        print('Options format: name=value e.g. expander=MCP23008 (Example below)')
        print('%s gpio charmap cols=20 numbering_mode=BCM rows=4 rs=15 rw=18 e=16 d4=21 d5=22 d6=23 d7=24 backlight=None' % sys.argv[0])
    else:
        print('<options> For info about options run:')
        print('')
        print('   %s i2c' % sys.argv[0])
        print('   %s gpio' % sys.argv[0])
        print('')

    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print_usage()

    lcdmode = sys.argv[1]
    test = sys.argv[2]

    # Parse options into a dictionary
    options = {}
    if sys.version_info > (3, 0):
            options = dict([arg.split(sep='=', maxsplit=1) for arg in sys.argv[3:]])
    else:
        options = dict([arg.split('=', 1) for arg in sys.argv[3:]])

    # Common options
    cols = int(options.pop('cols'))
    rows = int(options.pop('rows'))
    charmap = options.pop('charmap', 'A00')
    mode = GPIO.BCM if options.pop('mode', GPIO.BCM) == 'BCM' else GPIO.BOARD

    if lcdmode == 'i2c':
        if len(sys.argv) < 5:
            print_usage()

        # i2c options
        i2c_expander = options.pop('expander')
        address = int(options.pop('addr'), 16)
        port = int(options.pop('port', '1'))

        lcd = i2c.CharLCD(i2c_expander, address, cols=cols, port=port,
                          rows=rows, expander_params=options)
    elif lcdmode == 'gpio':
        if len(sys.argv) < 8:
            print_usage()
        # gpio options
        data = options.pop('data')
        rs = int(options.pop('rs'))
        e = int(options.pop('e'))
        rw = int(options.pop('rw'))
        bl = options.pop('bl', None)
        if bl is not None:
            bl = int(bl)
        # Parse data pins into a list
        pins_data = {}
        if sys.version_info > (3, 0):
            pins_data = data.split(sep=',')
            print(pins_data)
        else:
            pins_data = data.split(',')
        # Convert data pins to int
        for i in range(len(pins_data)):
            pins_data[i] = int(str(pins_data[i]))
        print(pins_data)
        lcd = gpio.CharLCD(pin_rs=rs, pin_rw=rw, pin_e=e, pins_data=pins_data,
                       pin_backlight=bl, numbering_mode=mode, cols=cols, rows=rows,
                       charmap=charmap)
        pass
    else:
        print_usage()

    # Run selected test
    if test == 'show_charmap':
        show_charmap.run(lcd, rows, cols)
    elif test == 'format_test':
        if ((cols == 20) and (rows == 4)):
            format_test_20x4.run(lcd)
        elif ((cols == 16) and (rows == 2)):
            format_test_16x2.run(lcd)
        else:
            print_usage()
    else:
        print_usage()
