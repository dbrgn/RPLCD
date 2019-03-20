# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import pytest

from RPLCD import codecs


@pytest.mark.parametrize(['input_', 'result_a00', 'result_a02', 'result_st0b'], [
    # Empty
    ('', [], [], []),
    # Single char, obvious mapping
    (' ', [32], [32], [32]),
    ('a', [97], [97], [97]),
    # Single char, different mapping depending on charmap
    ('α', [224], [144], [223]),
    # Single char, only available on some charmaps
    ('♡', [32], [157], [32]),
    ('❤', [32], [157], [32]),
    ('°', [223], [32], [178]),
    # Multiple 1:1 mapped chars
    ('asdf', [97, 115, 100, 102], [97, 115, 100, 102], [97, 115, 100, 102]),
    # Combined mapping
    ('\u207B\u00B9', [233], [32, 185], [191, 32]),
    ('as\u207B\u00B9df', [97, 115, 233, 100, 102], [97, 115, 32, 185, 100, 102], [97, 115, 191, 32, 100, 102]),
    ('\u207B', [32], [32], [191]),
    ('\u207Ba', [32, 97], [32, 97], [191, 97]),
    # Containing newlines and carriage returns
    ('a\r\nb', [97, codecs.CR, codecs.LF, 98], [97, codecs.CR, codecs.LF, 98], [97, codecs.CR, codecs.LF, 98]),
])
def test_encode(input_, result_a00, result_a02, result_st0b):
    a00 = codecs.A00Codec()
    a02 = codecs.A02Codec()
    st0b = codecs.ST0BCodec()

    assert a00.encode(input_) == result_a00, \
            'A00: Input %r encoded to %s' % (input_, a00.encode(input_))

    assert a02.encode(input_) == result_a02, \
            'A02: Input %r encoded to %s' % (input_, a02.encode(input_))
    
    assert st0b.encode(input_) == result_st0b, \
            'ST0B: Input %r encoded to %s' % (input_, st0b.encode(input_))
