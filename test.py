# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import logging

import RPIO

from RPLCD import CharLCD, Cursor


logging.basicConfig(level=logging.DEBUG)


lcd = CharLCD(cols=20, rows=4,
              pin_rs=15, pin_e=16, pins_data=[21, 22, 23, 24],
              numbering_mode=RPIO.BOARD)
