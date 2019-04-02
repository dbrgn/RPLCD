# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2018 Danilo Bargen
Copyright (C) 2018 Stephan Helma

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
from __future__ import division, absolute_import, unicode_literals

from collections import namedtuple

import pigpio

from . import common as c
from .lcd import BaseCharLCD
from .compat import range


# https://diarmuid.ie/blog/pwm-exponential-led-fading-on-arduino-or-other-platforms/
# p 101 .. maximum value of the PWM cycle
# m 100 .. number of steps the LED will fade over
# r = m*LOG(2)/LOG(p) = 12.5
# dc = 2**(x/r)-1 with x[0..1] and y[0..255]
PWM = 0.125

PinConfig = namedtuple('PinConfig', 'rs rw e e2 d0 d1 d2 d3 d4 d5 d6 d7 backlight contrast')


class CharLCD(BaseCharLCD):
    def __init__(self, pi,
                       pin_rs=None, pin_rw=None, pin_e=None, pin_e2=None,
                       pins_data=None,
                       pin_backlight=None, backlight_mode='active_low',
                       backlight_pwm=False, backlight_enabled=True,
                       pin_contrast=None, contrast_mode='active_high',
                       contrast_pwm=None, contrast=0.5,
                       cols=20, rows=4, dotsize=8,
                       charmap='A02',
                       auto_linebreaks=True):
        """
        Character LCD controller.

        The pin numbers are based on the BCM numbering scheme!

        You can save 1 pin by not using RW. Set ``pin_rw`` to ``None`` if you
        want this.

        :param pi: A pigpio.pi object to access the GPIOs.
        :type pi: pigpio.pi object
        :param pin_rs: Pin for register select (RS). Default: ``15``.
        :type pin_rs: int
        :param pin_rw: Pin for selecting read or write mode (R/W). Set this to
            ``None`` for read only mode. Default: ``18``.
        :type pin_rw: int
        :param pin_e: Pin to start data read or write (E). Default: ``16``.
        :type pin_e: int
        :param pins_data: List of data bus pins in 8 bit mode (DB0-DB7) or in 4
            bit mode (DB4-DB7) in ascending order. Default: ``[21, 22, 23, 24]``.
        :type pins_data: list of int
        :param pin_backlight: Pin for controlling backlight on/off. Set this to
            ``None`` for no backlight control. Default: ``None``.
        :type pin_backlight: int
        :param backlight_mode: Set this to either ``active_high`` or ``active_low``
            to configure the operating control for the backlight. Has no effect if
            pin_backlight is ``None``.
        :type backlight_mode: str
        :param backlight_pwm: Set this to ``True``, if you want to enable PWM
            for the backlight with the default PWM frequency. Set this to the
            frequency (in Hz) of the PWM for the backlight or to ``False`` to
            disable PWM for the backlight. Default: ``False``. Has no effect
            if pin_backlight is ``None``.
        :type backlight_pwm: bool or int
        :param backlight_enabled: Whether the backlight is enabled initially.
            If backlight_pwm is ``True``, this can be a value between 0 and 1,
            specifying the initial backlight level. Default: ``True``. Has no
            effect if pin_backlight is ``None``.
        :type backlight_enabled: bool or float
        :param pin_contrast: Pin for controlling LCD contrast. Set this to
            ``None`` for no contrast control. Default: ``None``.
        :type pin_contrast: int
        :param contrast_mode: Set this to either ``active_high`` or
            ``active_low`` to configure the operating control for the LCD
            contrast. Has no effect if pin_contrast is ``None``.
        :type contrast_mode: str
        :param contrast_pwm: Set this to the frequency (in Hz) of the PWM for
            the LCD contrast if you want to change the default value. Has no
            effect if pin_contrast is ``None``.
        :type contrast_pwm: int
        :param contrast: A value between 0 and 1, specifying the initial LCD
            contrast. Default: 0.5. Has no effect if pin_contrast is ``None``
        :type contrast: float
        :param rows: Number of display rows (usually 1, 2 or 4). Default: ``4``.
        :type rows: int
        :param cols: Number of columns per row (usually 16 or 20). Default ``20``.
        :type cols: int
        :param dotsize: Some 1 line displays allow a font height of 10px.
            Allowed: ``8`` or ``10``. Default: ``8``.
        :type dotsize: int
        :param charmap: The character map used. Depends on your LCD. This must
            be either ``A00`` or ``A02`` or ``ST0B``. Default: ``A02``.
        :type charmap: str
        :param auto_linebreaks: Whether or not to automatically insert line
            breaks. Default: ``True``.
        :type auto_linebreaks: bool

        """

        # Save the pigpio.pi object
        self.pi = pi

        # Set attributes
        if pin_rs is None:
            raise ValueError('pin_rs is not defined.')
        if pin_e is None:
            raise ValueError('pin_e is not defined.')

        if len(pins_data) == 4:  # 4 bit mode
            self.data_bus_mode = c.LCD_4BITMODE
            block1 = [None] * 4
        elif len(pins_data) == 8:  # 8 bit mode
            self.data_bus_mode = c.LCD_8BITMODE
            block1 = pins_data[:4]
        else:
            raise ValueError('There should be exactly 4 or 8 data pins.')
        block2 = pins_data[-4:]
        self.pins = PinConfig(rs=pin_rs, rw=pin_rw, e=pin_e, e2=pin_e2,
                              d0=block1[0], d1=block1[1], d2=block1[2], d3=block1[3],
                              d4=block2[0], d5=block2[1], d6=block2[2], d7=block2[3],
                              backlight=pin_backlight, contrast=pin_contrast)
        self.backlight_mode = backlight_mode
        self.backlight_pwm = backlight_pwm
        self.contrast_mode = contrast_mode
        self.contrast_pwm = contrast_pwm

        # Call superclass
        super(CharLCD, self).__init__(cols, rows, dotsize,
                                      charmap=charmap,
                                      auto_linebreaks=auto_linebreaks)

        # Set backlight status
        if pin_backlight is not None:
            self.backlight_enabled = backlight_enabled

        # Set contrast
        if pin_contrast is not None:
            self.contrast = contrast

    def _init_connection(self):
        # Setup GPIO
        for pin in list(filter(None, self.pins)):
            self.pi.set_mode(pin, pigpio.OUTPUT)

        # Setup PWM
        if self.pins.backlight and self.backlight_pwm:
            if self.backlight_pwm is not True:
                self.pi.set_PWM_frequency(self.pins.backlight, self.backlight_pwm)
        if self.pins.contrast:
            if self.backlight_pwm not in (None, False, True):
                self.pi.set_PWM_frequency(self.pins.contrast, self.contrast_pwm)

        # Initialization
        c.msleep(50)
        self.pi.write(self.pins.rs, 0)
        self.pi.write(self.pins.e, 0)
        if self.pins.e2 is not None:
            self.pi.write(self.pins.e2, 0)
        if self.pins.rw is not None:
            self.pi.write(self.pins.rw, 0)

        # pigpio script to pulse the enable flag to process data
        enablepulse = [
                'write {pin.e} 0',
                'mics 1',
                'trig {pin.e} 1 1',
                'mics 100']                 # Commands need > 37us to settle

        # pigpio script to write data to the LCD
        piscript = ['write {pin.rs} p0']        # Choose instruction or data mode
        if self.pins.rw is not None:
            # If the RW pin is used, set it to low
            piscript.append('write {pin.rw} 0')
        if self.data_bus_mode == c.LCD_8BITMODE:
            # Script to write 8 bits of data into the data bus.
            piscript.extend(                # Write data in 1 chunk of 8 bits
                    ['write {pin.d0} p1',       # Write 8 bits of data into the data bus
                     'write {pin.d1} p2',
                     'write {pin.d2} p3',
                     'write {pin.d3} p4',
                     'write {pin.d4} p5',
                     'write {pin.d5} p6',
                     'write {pin.d6} p7',
                     'write {pin.d7} p8'])
            piscript.extend(enablepulse)    # Process data
        else:
            piscript.extend(                # Write data in 2 chunks of 4 bits
                    ['write {pin.d4} p5',       # Write 4 bits of data into the data bus
                     'write {pin.d5} p6',
                     'write {pin.d6} p7',
                     'write {pin.d7} p8'])
            piscript.extend(enablepulse)    # Process data
            piscript.extend(
                    ['write {pin.d4} p1',       # Write 4 bits of data into the data bus
                     'write {pin.d5} p2',
                     'write {pin.d6} p3',
                     'write {pin.d7} p4'])
            piscript.extend(enablepulse)    # Process data

        # Make one string and insert the pin values
        piscript = ' '.join(piscript).format(pin=self.pins)
        # Send the string to pigpiod (it expects a byte string)
        self._writescript = self.pi.store_script(bytes(piscript, 'utf-8'))

    def _close_connection(self):

        while self.pi.script_status(self._writescript) == pigpio.PI_SCRIPT_RUNNING:
            c.msleep(10)
        self.pi.delete_script(self._writescript)

        self.pi.stop()

    # Properties

    def _get_backlight_enabled(self):
        if self.pins.backlight is None:
            raise ValueError('You did not configure a GPIO pin for backlight control!')
        if self.backlight_pwm:
            return self._backlight_enabled
        else:
            return bool(self._backlight_enabled)

    def _set_backlight_enabled(self, value):
        if self.pins.backlight is None:
            raise ValueError('You did not configure a GPIO pin for backlight control!')
        if self.backlight_pwm:
            if not ((0 <= value <= 1) or isinstance(value, bool)):
                raise ValueError(
                        'backlight_enabled must be set to a value '
                        'between 0 and 1 or to ``True`` or ``False``, '
                        'if PWM is enabled; got {}'.format(value))
        else:
            if not isinstance(value, bool):
                raise ValueError(
                        'backlight_enabled must be set to ``True`` or ``False``, '
                        'if PWM is not enabled; got: {}'.format(value))
        self._backlight_enabled = value
        if self.backlight_pwm:
            # Convert perceived brightness (as requested by `value`) to duty
            # cycle (see comment above definition of PWM):
            dc = 2**(value / PWM) - 1
            if self.backlight_mode == 'active_low':
                dc = 255 - dc
            self.pi.set_PWM_dutycycle(self.pins.backlight, round(dc))
        else:
            self.pi.write(self.pins.backlight,
                          value ^ (self.backlight_mode == 'active_low'))

    backlight_enabled = property(_get_backlight_enabled, _set_backlight_enabled,
            doc='Turn on/off or set the brightness of the backlight.')

    def _get_contrast(self):
        # We could probably read the current GPIO output state via sysfs, but
        # for now let's just store the state in the class
        if self.pins.contrast is None:
            raise ValueError('You did not configure a GPIO pin for contrast control!')
        return self._contrast

    def _set_contrast(self, value):
        if self.pins.contrast is None:
            raise ValueError('You did not configure a GPIO pin for contrast control!')
        if not (0 <= value <= 1):
            raise ValueError('contrast must be between 0 and 1; got {}'.format(value))
        self._contrast = value
        dc = 255 * value
        if self.contrast_mode == 'active_low':
            dc = 255 - dc
        self.pi.set_PWM_dutycycle(self.pins.contrast, round(dc))

    contrast = property(_get_contrast, _set_contrast,
            doc='Set the LCD contrast.')

    # Low level commands

    def _send(self, value, mode):
        """Send the specified value to the display with automatic 4bit / 8bit
        selection. The rs_mode is either ``RS_DATA`` or ``RS_INSTRUCTION``."""

        # Assemble the parameters sent to the pigpio script
        params = [mode]
        params.extend([(value >> i) & 0x01 for i in range(8)])
        # Switch off pigpio's exceptions, so that we get the return codes
        pigpio.exceptions = False
        while True:
            ret = self.pi.run_script(self._writescript, params)
            if ret >= 0:
                break
            elif ret != pigpio.PI_SCRIPT_NOT_READY:
                raise pigpio.error(pigpio.error_text(ret))
            # If pigpio script is not ready, sleep and try again
            c.usleep(1)
        # Switch on pigpio's exceptions
        pigpio.exceptions = True

    def _send_data(self, value):
        """Send data to the display. """
        self._send(value, c.RS_DATA)

    def _send_instruction(self, value):
        """Send instruction to the display. """
        self._send(value, c.RS_INSTRUCTION)
