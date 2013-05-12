# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from contextlib import contextmanager


@contextmanager
def cursor(lcd, row, col):
    """Context manager to control cursor position.

    Args:
        lcd:
            The CharLCD instance.
        row:
            The target row (0 index based).
        col:
            The target column (0 index based).

    Example:

    >>> with cursor(lcd, 2, 0):
        lcd.write_string('This is the hird row')

    """
    lcd.cursor_pos = (row, col)
    yield


@contextmanager
def cleared(lcd):
    """Context manager to clear display before writing.

    Example:

    >>> with cleared(lcd):
        lcd.write_string('Clear display, wooo!')

    """
    lcd.clear()
    yield
