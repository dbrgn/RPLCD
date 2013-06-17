# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import RPIO
from RPLCD import CharLCD
from RPLCD import Alignment, CursorMode, ShiftMode
from RPLCD import cursor, cleared

try:
    input = raw_input
except NameError:
    pass

RPIO.setwarnings(False)


lcd = CharLCD(cols=16, rows=2)

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

with cursor(lcd, 1, 15):
    lcd.write_string('X')
input('The last character on the LCD should now be an "X"')

lcd.display_enabled = False
input('Display should now be blank. ')

with cleared(lcd):
    lcd.write_string('Eggs, Ham\n\rand Spam')
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
lcd.write_string('1\n')
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

print('Test done.')
