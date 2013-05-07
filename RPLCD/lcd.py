# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import time
import logging

import RPIO


# Setup logging
log = logging.getLogger(__name__)


class CharLCD(object):

    # Commands
    LCD_CLEARDISPLAY = 0x01
    LCD_RETURNHOME = 0x02
    LCD_ENTRYMODESET = 0x04
    LCD_DISPLAYCONTROL = 0x08
    LCD_CURSORSHIFT = 0x10
    LCD_FUNCTIONSET = 0x20
    LCD_SETCGRAMADDR = 0x40
    LCD_SETDDRAMADDR = 0x80

    # Flags for display entry mode
    LCD_ENTRYRIGHT = 0x00
    LCD_ENTRYLEFT = 0x02
    LCD_ENTRYSHIFTINCREMENT = 0x01
    LCD_ENTRYSHIFTDECREMENT = 0x00

    # Flags for display on/off control
    LCD_DISPLAYON = 0x04
    LCD_DISPLAYOFF = 0x00
    LCD_CURSORON = 0x02
    LCD_CURSOROFF = 0x00
    LCD_BLINKON = 0x01
    LCD_BLINKOFF = 0x00

    # Flags for display/cursor shift
    LCD_DISPLAYMOVE = 0x08
    LCD_CURSORMOVE = 0x00

    # Flags for display/cursor shift
    LCD_DISPLAYMOVE = 0x08
    LCD_CURSORMOVE = 0x00
    LCD_MOVERIGHT = 0x04
    LCD_MOVELEFT = 0x00

    # Flags for function set
    LCD_8BITMODE = 0x10
    LCD_4BITMODE = 0x00
    LCD_2LINE = 0x08
    LCD_1LINE = 0x00
    LCD_5x10DOTS = 0x04
    LCD_5x8DOTS = 0x00

    def __init__(self, cols=20, rows=4,
                       pin_rs=15, pin_e=16, pins_data=[21, 22, 23, 24],
                       numbering_mode=RPIO.BOARD):
        # Set attributes
        self.pin_rs = pin_rs
        self.pin_e = pin_e
        self.pins_data = pins_data
        self.numbering_mode = numbering_mode

        # Setup GPIO
        if self.numbering_mode == RPIO.BOARD:
            log.debug('Numbering mode: BOARD')
        elif self.numbering_mode == RPIO.BCM:
            log.debug('Numbering mode: BCM')
        else:
            log.warning('Numbering mode: Unknown')
        RPIO.setmode(self.numbering_mode)
        log.debug('RS pin: {}'.format(self.pin_rs))
        RPIO.setup(self.pin_rs, RPIO.OUT)
        log.debug('E pin: {}'.format(self.pin_e))
        RPIO.setup(self.pin_e, RPIO.OUT)
        log.debug('Data pins: {}'.format(self.pins_data))
        for pin in self.pins_data:
            RPIO.setup(pin, RPIO.OUT)

        log.info('Setup complete.')

    def close(self):
        log.info('Cleaning up GPIO...')
        RPIO.cleanup()
