# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import warnings
from contextlib import contextmanager


@contextmanager
def cursor(lcd, row, col):
    """
    Context manager to control cursor position. DEPRECATED.
    """
    warnings.warn('The `cursor` context manager is deprecated', DeprecationWarning)
    lcd.cursor_pos = (row, col)
    yield


@contextmanager
def cleared(lcd):
    """
    Context manager to clear display before writing. DEPRECATED.
    """
    warnings.warn('The `cursor` context manager is deprecated', DeprecationWarning)
    lcd.clear()
    yield
