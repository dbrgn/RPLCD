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

from RPLCD import gpio, i2c
from RPLCD import Alignment, CursorMode, ShiftMode

try:
    input = raw_input
except NameError:
    pass


def print_usage():
    print('Usage: %s i2c <expander> <addr> <charmap>' % sys.argv[0])
    print('       %s gpio <charmap>' % sys.argv[0])
    print('')
    print('<expander>  Supported I²C port expanders are PCF8574 and MCP23008')
    print('<addr>      The I²C address (in hex format) can be found with')
    print('            `i2cdetect 1` from the i2c-tools package.')
    print('<charmap>   Charmap can be either A00 or A02. If your display contains Japanese')
    print('            characters, it probably uses the A00 charmap, otherwise A02.')
    print('')
    sys.exit(1)


# Parse command line parameters
if len(sys.argv) < 2:
    print_usage()
if sys.argv[1] == 'i2c':
    if len(sys.argv) != 5:
        print_usage()
    lcd = i2c.CharLCD(sys.argv[2], int(sys.argv[3], 16), cols=16, rows=2, charmap=sys.argv[4])
elif sys.argv[1] == 'gpio':
    if len(sys.argv) != 3:
        print_usage()
    lcd = gpio.CharLCD(cols=16, rows=2, charmap=sys.argv[2])
else:
    print_usage()


lcd.backlight = True
input('Display should be blank. ')

lcd.cursor_mode = CursorMode.blink
input('The cursor should now blink. ')

lcd.cursor_mode = CursorMode.line
input('The cursor should now be a line. ')

lcd.write_string('Hello world!')
input('"Hello world!" should be on the LCD. ')

assert lcd.cursor_pos == (0, 12), 'cursor_pos should now be (0, 12)'

lcd.cursor_pos = (0, 15)
lcd.write_string('1')
lcd.cursor_pos = (1, 15)
lcd.write_string('2')
assert lcd.cursor_pos == (0, 0), 'cursor_pos should now be (0, 0)'
input('Lines 1 and 2 should now be labelled with the right numbers on the right side. ')

lcd.clear()
input('Display should now be clear, cursor should be at initial position. ')

lcd.cursor_pos = (0, 5)
lcd.write_string('12345')
input('The string should have a left offset of 5 characters. ')

lcd.write_shift_mode = ShiftMode.display
lcd.cursor_pos = (1, 5)
lcd.write_string('12345')
input('Both strings should now be at column 0. ')

lcd.write_shift_mode = ShiftMode.cursor
lcd.cursor_pos = (1, 5)
lcd.write_string(lcd.write_shift_mode.name)
input('The string "cursor" should now be on the second row, column 0. ')

lcd.home()
input('Cursor should now be at initial position. Everything should be shifted to the right by 5 characters. ')

lcd.cursor_pos = (1, 15)
lcd.write_string('X')
input('The last character on the LCD should now be an "X"')

lcd.display_enabled = False
input('Display should now be blank. ')

lcd.clear()
lcd.write_string('Eggs, Ham')
lcd.crlf()
lcd.write_string('and Spam')
lcd.display_enabled = True
input('Display should now show "Eggs, Ham and Spam" with a line break after "Ham". ')

lcd.shift_display(4)
input('Text should now be shifted to the right by 4 characters. ')
lcd.shift_display(-4)
input('Shift should now be undone. ')

lcd.text_align_mode = Alignment.right
lcd.write_string(' Spam')
input('The word "Spam" should now be inverted. ')

lcd.text_align_mode = Alignment.left
lcd.write_string(' Wurscht')
input('The word "mapS" should now be replaced with "Wurscht". ')

lcd.clear()
lcd.write_string('1')
lcd.lf()
lcd.write_string('2\n')
lcd.cursor_pos = (0, 2)
lcd.write_string('3\n')
lcd.write_string('4')
lcd.cursor_pos = (0, 4)
lcd.write_string('5\n')
lcd.write_string('6')
input('The numbers 1-6 should now be displayed in a zig zag line starting in the top left corner. ')

lcd.clear()
lcd.write_string('This will wrap around both lines')
input('Text should nicely wrap around lines. ')

lcd.clear()
lcd.cursor_mode = CursorMode.hide
lcd.write_string('Paris: 21°C\n\rZürich: 18°C')
print('Text should now show "Paris: 21°C, Zürich: 18°C" without any encoding issues.', end='')
input()

# Test custom chars
lcd.clear()
happy = (0b00000, 0b01010, 0b01010, 0b00000, 0b10001, 0b10001, 0b01110, 0b00000)
sad = (0b00000, 0b01010, 0b01010, 0b00000, 0b01110, 0b10001, 0b10001, 0b00000)
lcd.create_char(0, sad)
lcd.write_string('\x00')
lcd.create_char(1, happy)
lcd.write_string('\x01')
input('You should now see a sad and a happy face next to each other. ')
lcd.create_char(0, happy)
lcd.home()
lcd.write_string('\x00')
input('Now both faces should be happy. ')

lcd.clear()
lcd.write_string('1234567890123456\r\n2nd line')
input('The first line should be filled with numbers, the second line should show "2nd line"')

lcd.clear()
lcd.write_string('999456\n\r\n123')
input('The display should show "123456" on the first line')

lcd.clear()
try:
    lcd.backlight_enabled = False
except ValueError:
    pass
lcd.close()
print('Test done. If you have a programmable backlight, it should now be off.')
