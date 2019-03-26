# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from ..common import sliding_window
from . import hd44780_a00, hd44780_a02, st7066_0b


# Constants used to encode special characters.
# Negative to avoid conflict with regular bytes.
CR = -1
LF = -2


class FoundMultiCharMapping(Exception):
    """
    Exception to escape nested loops.
    """
    pass


class Codec(object):
    def __init__(self, codec):
        assert hasattr(codec, 'replacement_char')
        assert hasattr(codec, 'encoding_table')
        assert hasattr(codec, 'combined_chars_lookahead')
        assert hasattr(codec, 'combined_chars')
        self.codec = codec

    def encode(self, input_):  # type: (str) -> List[int]
        result = []
        window_iter = sliding_window(
            input_, self.codec.combined_chars_lookahead)
        while True:
            try:
                window = next(window_iter)
            except StopIteration:
                break
            char = window[0]
            lookahead = window[1:]

            # First, test for newlines and carriage returns
            if char == '\r':
                result.append(CR)
                continue
            elif char == '\n':
                result.append(LF)
                continue

            # Then, test whether the character starts a multi-char mapping
            try:
                if char in self.codec.combined_chars:
                    mappings = self.codec.combined_chars[char]
                    for mapping in mappings:
                        length = len(mapping[0])
                        if mapping[0] == ''.join(lookahead[:length]):
                            # We got a match! Add the mapping...
                            result.append(mapping[1])
                            # ...and advance iterator to consume the used up lookahead.
                            for _ in range(length):
                                next(window_iter)
                            raise FoundMultiCharMapping()
            except FoundMultiCharMapping:
                continue

            # Otherwise, do a regular lookup in the encoding table
            result.append(self.codec.encoding_table.get(
                char, self.codec.replacement_char))

        return result


class A00Codec(Codec):
    def __init__(self):
        super(A00Codec, self).__init__(hd44780_a00)


class A02Codec(Codec):
    def __init__(self):
        super(A02Codec, self).__init__(hd44780_a02)


class ST0BCodec(Codec):
    def __init__(self):
        super(ST0BCodec, self).__init__(st7066_0b)
