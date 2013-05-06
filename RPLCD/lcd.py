# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import time
import logging

import RPIO


# Setup logging
log = logging.getLogger(__name__)


class CharLCD(object):

    def __init__(self, cols=20, rows=4,
                       pin_rs=15, pin_e=16, pins_data=[21, 22, 23, 24],
                       numbering_mode=RPIO.BOARD):
        # Set attributes
        self.pin_rs = pin_rs
        self.pin_e = pin_e
        self.pins_data = pins_data
        self.numbering_mode = numbering_mode

        # Setup GPIO
        log.debug('Numbering scheme: {}'.format(self.numbering_mode))
        RPIO.setmode(self.numbering_mode)
        log.debug('RS pin: {}'.format(self.pin_rs))
        RPIO.setup(self.pin_rs, RPIO.OUT)
        log.debug('E pin: {}'.format(self.pin_e))
        RPIO.setup(self.pin_e, RPIO.OUT)
        log.debug('Data pins: {}'.format(self.pin_e))
        for pin in self.pins_data:
            RPIO.setup(pin, RPIO.OUT)

        logging.info('Setup complete.')
