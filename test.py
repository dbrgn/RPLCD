# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import time

import RPIO

from RPLCD import CharLCD


#lcd = CharLCD(pin_rs=15, pin_e=16, pins_data=[21, 22, 23, 24], numbering_mode=RPIO.BOARD)
lcd = CharLCD(pin_rs=15, pin_e=16, pins_data=[21, 22, 23, 24], numbering_mode=RPIO.BOARD)
lcd.setup(cols=20, rows=4, dotsize=8)
lcd.turn_on()

for char in 'Hello world! Hello world! Hello world!':
    lcd.write(ord(char))

lcd.close(clear=False)
