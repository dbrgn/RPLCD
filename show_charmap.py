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

from RPLCD import i2c, gpio


try:
    range = xrange
except NameError:  # Python 3
    pass

try:
    safe_input = raw_input
except NameError:  # Python 3
    safe_input = input


def print_usage():
    print('Usage: %s i2c <expander> <addr> <rows> <cols>' % sys.argv[0])
    print('       %s gpio <rows> <cols>' % sys.argv[0])
    print('')
    print('<expander>  Supported I²C port expanders are PCF8574 and MCP23008')
    print('<addr>      The I²C address (in hex format) can be found with')
    print('            `i2cdetect 1` from the i2c-tools package.')
    print('<rows>      The number of rows on your LCD, e.g. 2')
    print('<cols>      The number of columns on your LCD, e.g. 16')
    print('')
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
    if sys.argv[1] == 'i2c':
        if len(sys.argv) != 6:
            print_usage()
        rows, cols = int(sys.argv[4]), int(sys.argv[5])
        lcd = i2c.CharLCD(sys.argv[2], int(sys.argv[3], 16), cols=cols, rows=rows)
    elif sys.argv[1] == 'gpio':
        if len(sys.argv) != 4:
            print_usage()
        rows, cols = int(sys.argv[2]), int(sys.argv[3])
        lcd = gpio.CharLCD(cols=cols, rows=rows)
    else:
        print_usage()

    print('This tool shows the character map of your LCD on the display.')
    print('Press ctrl+c at any time to abort.\n')

    page = 0
    chars = rows * cols
    text_tpl = 'Displaying page %d (characters %d-%d). Press <ENTER> to continue.'

    try:
        while True:
            offset = page * chars
            start = offset
            end = offset + chars
            lcd.clear()
            for i in range(offset, offset + chars):
                if i > 255:
                    if i > start:
                        safe_input(text_tpl % (page + 1, start, i - 1))
                    else:
                        pass
                    sys.exit(0)
                lcd.write(i)
            safe_input(text_tpl % (page + 1, start, end - 1))
            page += 1
    except KeyboardInterrupt:
        print('Aborting.')
    finally:
        lcd.clear()
        try:
            lcd.backlight_enabled = False
        except ValueError:
            pass
        lcd.close()
        print('Test done. If you have a backlight, it should now be off.')
