# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import pytest

from RPLCD.gpio import CharLCD


try:
    unichr = unichr
except NameError:  # Python 3
    unichr = chr


SP = 32  # Space


@pytest.fixture
def get_lcd(mocker, charlcd_kwargs):
    def _func(cols, rows, auto_linebreaks):
        lcd = CharLCD(cols=cols, rows=rows, auto_linebreaks=auto_linebreaks, **charlcd_kwargs)
        mocker.patch.object(lcd, '_send_data')
        mocker.patch.object(lcd, '_send_instruction')
        return lcd
    return _func


def test_auto_linebreaks(get_lcd):
    """
    Simple auto linebreak.
    """
    lcd = get_lcd(16, 2, True)
    for i in range(48, 67):
        lcd.write_string(unichr(i))
    assert lcd._content[0] == [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    assert lcd._content[1] == [64, 65, 66, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP]


def test_no_auto_linebreaks(get_lcd):
    """
    Auto linebreaks disabled.
    """
    lcd = get_lcd(16, 2, False)
    for i in range(48, 67):
        lcd.write_string(unichr(i))
    assert lcd._content[0] == [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    assert lcd._content[1] == [SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP]


def test_auto_linebreaks_no_ignore_lf(get_lcd):
    """
    Do not ignore manual \n after auto linebreak.
    """
    lcd = get_lcd(16, 2, True)
    lcd.write_string('a' * 16)  # Fill up line
    lcd.write_string('\nb')
    assert lcd._content[0] == [98, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97]
    assert lcd._content[1] == [SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP, SP]


def test_auto_linebreaks_no_ignore_double_lf(get_lcd):
    """
    Do not ignore manual \n\n after auto linebreak.
    """
    lcd = get_lcd(20, 4, True)
    lcd.write_string('a' * 20)  # Fill up line
    lcd.write_string('\n\nb')
    assert lcd._content[0] == [97] * 20
    assert lcd._content[1] == [SP] * 20
    assert lcd._content[2] == [SP] * 20
    assert lcd._content[3] == [98] + [SP] * 19


@pytest.mark.parametrize('pattern', ['\r\n', '\n\r'])
def test_auto_linebreaks_ignore_crlf(get_lcd, pattern):
    """
    Ignore manual \r\n and \n\r after auto linebreak.
    """
    lcd = get_lcd(20, 4, True)
    lcd.write_string('a' * 20)  # Fill up line
    lcd.write_string(pattern)
    lcd.write_string('b')
    assert lcd._content[0] == [97] * 20
    assert lcd._content[1] == [98] + [SP] * 19
    assert lcd._content[2] == [SP] * 20
    assert lcd._content[3] == [SP] * 20
