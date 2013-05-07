# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import time
import logging
from collections import namedtuple

import RPIO


# Setup logging
log = logging.getLogger(__name__)


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


# PinSet namedtuple
PinSet = namedtuple('PinSet', 'rs rw e d0 d1 d2 d3 d4 d5 d6 d7 mode')


def msleep(milliseconds):
    """Sleep the specified amount of milliseconds."""
    time.sleep(milliseconds / 1000.0)


def usleep(microseconds):
    """Sleep the specified amount of microseconds."""
    time.sleep(microseconds / 1000000.0)


class CharLCD(object):
    def __init__(self, pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
                       numbering_mode=RPIO.BOARD):
        """
        Character LCD controller.

        The default pin numbers are based on the BOARD numbering scheme (1-26).

        You can save 1 pin by not using RW. Set ``pin_rw`` to ``None`` if you
        want this.

        Args:
            pin_rs:
                Pin for register select (RS). Default: 15.
            pin_rw:
                Pin for selecting read or write mode (R/W). Set this to
                ``None`` for read only mode. Default: 18.
            pin_e:
                Pin to start data read or write (E). Default: 16.
            pins_data:
                List of data bus pins in 8 bit mode (DB0-DB7) or in 8 bit mode
                (DB4-DB7) in ascending order. Default: [21, 22, 23, 24].
            numbering_mode:
                Which scheme to use for numbering the GPIO pins.
                Default: RPIO.BOARD (1-26).

        Returns:
            A :class:`CharLCD` instance.

        """
        # Set attributes
        if len(pins_data) == 4:  # 4 bit mode
            self.display_mode = LCD_4BITMODE
            block1 = [None] * 4
        elif len(pins_data) == 8:  # 8 bit mode
            self.display_mode = LCD_8BITMODE
            block1 = pins_data[:4]
        else:
            raise ValueError('There should be exactly 4 or 8 data pins.')
        block2 = pins_data[-4:]
        self.pins = PinSet(rs=pin_rs, rw=pin_rw, e=pin_e,
                           d0=block1[0], d1=block1[1], d2=block1[2], d3=block1[3],
                           d4=block2[0], d5=block2[1], d6=block2[2], d7=block2[3],
                           mode=numbering_mode)

        # Setup GPIO
        log.info('Pin configuration: {!r}'.format(self.pins))
        if self.numbering_mode == RPIO.BOARD:
            log.debug('Numbering mode: BOARD')
        elif self.numbering_mode == RPIO.BCM:
            log.debug('Numbering mode: BCM')
        else:
            log.warning('Numbering mode: Unknown')
        RPIO.setmode(self.numbering_mode)
        for pin in filter(None, self.pins)[:-1]:
            RPIO.setup(pin, RPIO.OUT)

        log.info('Setup complete.')

    def setup(self, rows=4, cols=20, dotsize=8):
        """Initialize display with the specified configuration.

        Args:
            rows:
                Number of display rows (usually 1, 2 or 4). Default: 4.
            cols:
                Number of columns per row (usually 16 or 20). Default 20.
            dotsize:
                Some 1 line displays allow a font height of 10px. Default: 8.

        """
        # Set attributes
        self.rows = rows
        self.cols = cols
        self.dotsize = dotsize

        # Initialization (see manual page 45/46)
        msleep(50)

    def close(self):
        log.info('Cleaning up GPIO...')
        RPIO.cleanup()
