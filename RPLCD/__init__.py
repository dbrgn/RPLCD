import warnings

from .contextmanagers import cursor, cleared  # noqa


__version__ = '1.3.1'


class CharLCD:
    def __new__(cls, *args, **kwargs):
        from .gpio import CharLCD as GpioCharLCD
        warnings.warn("Using RPLCD.CharLCD directly is deprecated. " +
                      "Use RPLCD.gpio.CharLCD instead!", DeprecationWarning)
        return GpioCharLCD(*args, **kwargs)
