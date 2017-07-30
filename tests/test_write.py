# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import pytest

from RPLCD.gpio import CharLCD
from RPLCD.common import LCD_SETDDRAMADDR


def test_write_simple(mocker, charlcd_kwargs):
    """
    Write "HelloWorld" to the display.
    """
    lcd = CharLCD(**charlcd_kwargs)
    send_data = mocker.patch.object(lcd, '_send_data')
    text = 'HelloWorld'
    lcd.write_string(text)
    assert send_data.call_count == len(text)
    calls = [c[0] for c in send_data.call_args_list]
    assert calls[0] == (72,)
    assert calls[1] == (101,)
    assert calls[2] == (108,)
    assert calls[3] == (108,)
    assert calls[4] == (111,)
    assert calls[5] == (87,)
    assert calls[6] == (111,)
    assert calls[7] == (114,)
    assert calls[8] == (108,)
    assert calls[9] == (100,)


def test_caching(mocker, charlcd_kwargs):
    """
    Characters should only be written if they have changed
    """
    lcd = CharLCD(**charlcd_kwargs)
    send_data = mocker.patch.object(lcd, '_send_data')
    send_instruction = mocker.patch.object(lcd, '_send_instruction')

    lcd.write_string('hello')
    assert send_data.call_count == 5
    data_calls = [c[0] for c in send_data.call_args_list]
    assert data_calls[0] == (104,)
    assert data_calls[1] == (101,)
    assert data_calls[2] == (108,)
    assert data_calls[3] == (108,)
    assert data_calls[4] == (111,)

    lcd.home()
    send_data.reset_mock()
    send_instruction.reset_mock()

    lcd.write_string('he77o')
    assert send_data.call_count == 2
    assert send_instruction.call_count == 3
    data_calls = [c[0] for c in send_data.call_args_list]
    instruction_calls = [c[0] for c in send_instruction.call_args_list]
    assert instruction_calls[0] == (LCD_SETDDRAMADDR | 1,)
    assert instruction_calls[1] == (LCD_SETDDRAMADDR | 2,)
    assert data_calls[0] == (55,)
    assert data_calls[1] == (55,)
    assert instruction_calls[2] == (LCD_SETDDRAMADDR | 5,)


@pytest.mark.parametrize(['charmap', 'ue'], [
    ('A00', 0b11110101),
    ('A02', 0b11111100),
])
def test_charmap(mocker, charmap, ue, charlcd_kwargs):
    """
    The charmap should be used. The "ü" Umlaut should be encoded correctly.
    """
    lcd = CharLCD(charmap=charmap, **charlcd_kwargs)
    send = mocker.patch.object(lcd, '_send_data')

    text = 'Züri'

    lcd.write_string(text)
    assert send.call_count == 4, 'call count was %d' % send.call_count
    calls = [c[0] for c in send.call_args_list]
    assert calls[0] == (90,)
    assert calls[1] == (ue,)
    assert calls[2] == (114,)
    assert calls[3] == (105,)


@pytest.mark.parametrize(['rows', 'cols'], [
    (2, 16),
    (4, 20),
])
def test_write_newline(mocker, rows, cols, charlcd_kwargs):
    """
    Write text containing CR/LF chars to the display.
    """
    lcd = CharLCD(rows=rows, cols=cols, **charlcd_kwargs)
    send_data = mocker.patch.object(lcd, '_send_data')
    send_instruction = mocker.patch.object(lcd, '_send_instruction')
    text = '\nab\n\rcd'
    lcd.write_string(text)
    assert send_data.call_count + send_instruction.call_count == len(text)
    data_calls = [c[0] for c in send_data.call_args_list]
    instruction_calls = [c[0] for c in send_instruction.call_args_list]
    assert instruction_calls[0] == (0x80 + 0x40,), instruction_calls
    assert data_calls[0] == (97,), data_calls
    assert data_calls[1] == (98,), data_calls
    if rows == 2:
        assert instruction_calls[1] == (0x80 + 2,), instruction_calls
        assert instruction_calls[2] == (0x80 + 0,), instruction_calls
    else:
        assert instruction_calls[1] == (0x80 + cols + 2,), instruction_calls
        assert instruction_calls[2] == (0x80 + cols + 0,), instruction_calls
    assert data_calls[2] == (99,), data_calls
    assert data_calls[3] == (100,), data_calls
