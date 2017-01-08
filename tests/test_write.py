# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import pytest

from RPLCD.gpio import CharLCD
from RPLCD.common import RS_DATA, RS_INSTRUCTION, LCD_SETDDRAMADDR


def test_write_simple(mocker):
    """
    Write "HelloWorld" to the display.
    """
    lcd = CharLCD()
    send = mocker.patch.object(lcd, '_send')
    text = 'HelloWorld'
    lcd.write_string(text)
    assert send.call_count == len(text)
    calls = [c[0] for c in send.call_args_list]
    assert calls[0] == (72, RS_DATA)
    assert calls[1] == (101, RS_DATA)
    assert calls[2] == (108, RS_DATA)
    assert calls[3] == (108, RS_DATA)
    assert calls[4] == (111, RS_DATA)
    assert calls[5] == (87, RS_DATA)
    assert calls[6] == (111, RS_DATA)
    assert calls[7] == (114, RS_DATA)
    assert calls[8] == (108, RS_DATA)
    assert calls[9] == (100, RS_DATA)


def test_caching(mocker):
    """
    Characters should only be written if they have changed
    """
    lcd = CharLCD()
    send = mocker.patch.object(lcd, '_send')

    lcd.write_string('hello')
    assert send.call_count == 5
    calls = [c[0] for c in send.call_args_list]
    assert calls[0] == (104, RS_DATA)
    assert calls[1] == (101, RS_DATA)
    assert calls[2] == (108, RS_DATA)
    assert calls[3] == (108, RS_DATA)
    assert calls[4] == (111, RS_DATA)

    lcd.home()
    send.reset_mock()

    lcd.write_string('he77o')
    assert send.call_count == 5
    calls = [c[0] for c in send.call_args_list]
    assert calls[0] == (LCD_SETDDRAMADDR | 1, RS_INSTRUCTION)
    assert calls[1] == (LCD_SETDDRAMADDR | 2, RS_INSTRUCTION)
    assert calls[2] == (55, RS_DATA)
    assert calls[3] == (55, RS_DATA)
    assert calls[4] == (LCD_SETDDRAMADDR | 5, RS_INSTRUCTION)


@pytest.mark.parametrize(['charmap', 'ue'], [
    ('A00', 0b11110101),
    ('A02', 0b11111100),
])
def test_charmap(mocker, charmap, ue):
    """
    The charmap should be used. The "ü" Umlaut should be encoded correctly.
    """
    lcd = CharLCD(charmap=charmap)
    send = mocker.patch.object(lcd, '_send')

    text = 'Züri'

    lcd.write_string(text)
    assert send.call_count == 4, 'call count was %d' % send.call_count
    calls = [c[0] for c in send.call_args_list]
    assert calls[0] == (90, RS_DATA)
    assert calls[1] == (ue, RS_DATA)
    assert calls[2] == (114, RS_DATA)
    assert calls[3] == (105, RS_DATA)
