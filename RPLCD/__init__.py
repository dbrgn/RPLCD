import warnings

from .common import Alignment, CursorMode, ShiftMode, BacklightMode
from .contextmanagers import cursor, cleared
from .gpio import CharLCD as GpioCharLCD


class CharLCD(GpioCharLCD):
    def __init__(self, *args, **kwargs):
        warnings.warn("Using RPLCD.CharLCD directly is deprecated. " +
                      "Use RPLCD.gpio.CharLCD instead!", DeprecationWarning)
        super(CharLCD, self).__init__(*args, **kwargs)
