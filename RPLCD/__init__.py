import warnings

from .contextmanagers import cursor, cleared
from .gpio import CharLCD as GpioCharLCD


__version__ = '1.0.0'


class CharLCD(GpioCharLCD):
    def __init__(self, *args, **kwargs):
        warnings.warn("Using RPLCD.CharLCD directly is deprecated. " +
                      "Use RPLCD.gpio.CharLCD instead!", DeprecationWarning)
        super(CharLCD, self).__init__(*args, **kwargs)
