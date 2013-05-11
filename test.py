# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from RPLCD import CharLCD, Direction, CursorMode, ShiftMode


lcd = CharLCD()

lcd.setup()
raw_input('Display should be blank. ')

lcd.cursor_mode = CursorMode.blink
raw_input('The cursor should now blink. ')

lcd.cursor_mode = CursorMode.line
raw_input('The cursor should now be a line. ')

lcd.write_string('Hello world!')
raw_input('"Hello world!" should be on the LCD. ')

lcd.home()
raw_input('Cursor should now be at initial position. ')

lcd.cursor_pos = (1, 0)
lcd.write_string('2')
lcd.cursor_pos = (2, 0)
lcd.write_string('3')
lcd.cursor_pos = (3, 0)
lcd.write_string('4')
raw_input('Lines 2, 3 and 4 should now be labelled with the right numbers. ')

lcd.clear()
raw_input('Display should now be clear, cursor should be at initial position. ')

#lcd.close()
