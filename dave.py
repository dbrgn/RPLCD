#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import sys

import thread
import threading
import time
from RPLCD import CharLCD
from RPLCD import Alignment, CursorMode, ShiftMode
from RPLCD import cursor, cleared
from RPLCD import BacklightMode

import sys, tty, termios

charlock = threading.Lock()
buffersem = threading.Semaphore(0)

try:
    input = raw_input
except NameError:
    pass

try:
    unichr = unichr
except NameError:
    unichr = chr


lcd = CharLCD(cols=16, rows=2, pin_backlight=7, backlight_mode=BacklightMode.active_low)
old_settings = None
new_settings = None
fd = None

lcd.backlight = True
 
try:
    from msvcrt import getch  # try to import Windows version
except ImportError:
    def getch():   # define non-Windows version
        global new_settings, old_settings, fd
        if fd is None:
            fd = sys.stdin.fileno()
        if old_settings is None:
            old_settings = termios.tcgetattr(fd)
        if new_settings is None:
            tty.setraw(sys.stdin.fileno())
            new_settings = termios.tcgetattr(fd)

        if new_settings is not None:
            ch = sys.stdin.read(1)
            return ch
        else:
            return 'X'
 
keybuffer = []

try:
    def keypress():
        global keybuffer
        while True:
            r = getch()
            with charlock:
                keybuffer.append(r)
                buffersem.release()
 
    thread.start_new_thread(keypress, ())

    lcd.cursor_pos=(0,0)
 
    while True:
        wait = False
        buffersem.acquire()
        with charlock:
            key = keybuffer.pop(0)

        if key is not None:
            if key=='a':
                break
    
            lcd.write_string(key)
	
        
finally:
    lcd.backlight = False
    lcd.close()

    if old_settings is not None:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
