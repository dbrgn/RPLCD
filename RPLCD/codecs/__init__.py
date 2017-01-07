import codecs

import hd44780_a00
import hd44780_a02


class HD44780A00Codec(codecs.Codec):
    def encode(self, input_, errors='strict'):
        return codecs.charmap_encode(input_, errors, hd44780_a00.encoding_table)

    def decode(self, input_, errors='strict'):
        return codecs.charmap_decode(input_, errors, hd44780_a00.decoding_table)


class HD44780A02Codec(codecs.Codec):
    def encode(self, input_, errors='strict'):
        return codecs.charmap_encode(input_, errors, hd44780_a02.encoding_table)

    def decode(self, input_, errors='strict'):
        return codecs.charmap_decode(input_, errors, hd44780_a02.decoding_table)


def lookup(name):
    if name in ['hd44780-a00', 'hd44780a00']:
        return codecs.CodecInfo(
            name='hd44780-a00',
            encode=HD44780A00Codec().encode,
            decode=HD44780A00Codec().decode,
        )
    elif name in ['hd44780-a02', 'hd44780a02']:
        return codecs.CodecInfo(
            name='hd44780-a02',
            encode=HD44780A02Codec().encode,
            decode=HD44780A02Codec().decode,
        )
    else:
        return None


codecs.register(lookup)
