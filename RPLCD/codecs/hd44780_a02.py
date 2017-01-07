"""
The HD4480-A02 character table.
"""
import codecs

decoding_table = (
    '\x00'  # 0x00 -> User defined (CGRAM)
    '\x00'  # 0x01 -> User defined (CGRAM)
    '\x00'  # 0x02 -> User defined (CGRAM)
    '\x00'  # 0x03 -> User defined (CGRAM)
    '\x00'  # 0x04 -> User defined (CGRAM)
    '\x00'  # 0x05 -> User defined (CGRAM)
    '\x00'  # 0x06 -> User defined (CGRAM)
    '\x00'  # 0x07 -> User defined (CGRAM)
    '\x00'  # 0x08
    '\x00'  # 0x09
    '\x00'  # 0x0a
    '\x00'  # 0x0b
    '\x00'  # 0x0c
    '\x00'  # 0x0d
    '\x00'  # 0x0e
    '\x00'  # 0x0f

    '?'     # 0x10
    '?'     # 0x11
    '?'     # 0x12
    '?'     # 0x13
    '?'     # 0x14
    '?'     # 0x15
    '?'     # 0x16
    '?'     # 0x17
    '?'     # 0x18
    '?'     # 0x19
    '?'     # 0x1a
    '?'     # 0x1b
    '?'     # 0x1c
    '?'     # 0x1d
    '?'     # 0x1e
    '?'     # 0x1f

    ' '     # 0x20 -> SPACE
    '!'     # 0x21 -> EXCLAMATION MARK
    '"'     # 0x22 -> QUOTATION MARK
    '#'     # 0x23 -> NUMBER SIGN
    '$'     # 0x24 -> DOLLAR SIGN
    '%'     # 0x25 -> PERCENT SIGN
    '&'     # 0x26 -> AMPERSAND
    "'"     # 0x27 -> APOSTROPHE
    '('     # 0x28 -> LEFT PARENTHESES
    ')'     # 0x29 -> RIGHT PARENTHESES
    '*'     # 0x2a -> ASTERISK
    '+'     # 0x2b -> PLUS SIGN
    ','     # 0x2c -> COMMA
    '-'     # 0x2d -> HYPHEN-MINUS
    '.'     # 0x2e -> FULL STOP
    '/'     # 0x2f -> SOLIDUS

    '0'     # 0x30 -> DIGIT ZERO
    '1'     # 0x31 -> DIGIT ONE
    '2'     # 0x32 -> DIGIT TWO
    '3'     # 0x33 -> DIGIT THREE
    '4'     # 0x34 -> DIGIT FOUR
    '5'     # 0x35 -> DIGIT FIVE
    '6'     # 0x36 -> DIGIT SIX
    '7'     # 0x37 -> DIGIT SEVEN
    '8'     # 0x38 -> DIGIT EIGHT
    '9'     # 0x39 -> DIGIT NINE
    ':'     # 0x3a -> COLON
    ';'     # 0x3b -> SEMICOLON
    '<'     # 0x3c -> LESS-THAN SIGN
    '='     # 0x3d -> EQUALS SIGN
    '>'     # 0x3e -> GREATER-THAN SIGN
    '?'     # 0x3f -> QUESTION MARK

    '@'     # 0x40 -> COMMERCIAL AT
    'A'     # 0x41 -> LATIN CAPITAL LETTER A
    'B'     # 0x42 -> LATIN CAPITAL LETTER B
    'C'     # 0x43 -> LATIN CAPITAL LETTER C
    'D'     # 0x44 -> LATIN CAPITAL LETTER D
    'E'     # 0x45 -> LATIN CAPITAL LETTER E
    'F'     # 0x46 -> LATIN CAPITAL LETTER F
    'G'     # 0x47 -> LATIN CAPITAL LETTER G
    'H'     # 0x48 -> LATIN CAPITAL LETTER H
    'I'     # 0x49 -> LATIN CAPITAL LETTER I
    'J'     # 0x4a -> LATIN CAPITAL LETTER J
    'K'     # 0x4b -> LATIN CAPITAL LETTER K
    'L'     # 0x4c -> LATIN CAPITAL LETTER L
    'M'     # 0x4d -> LATIN CAPITAL LETTER M
    'N'     # 0x4e -> LATIN CAPITAL LETTER N
    'O'     # 0x4f -> LATIN CAPITAL LETTER O

    'P'     # 0x50 -> LATIN CAPITAL LETTER P
    'Q'     # 0x51 -> LATIN CAPITAL LETTER Q
    'R'     # 0x52 -> LATIN CAPITAL LETTER R
    'S'     # 0x53 -> LATIN CAPITAL LETTER S
    'T'     # 0x54 -> LATIN CAPITAL LETTER T
    'U'     # 0x55 -> LATIN CAPITAL LETTER U
    'V'     # 0x56 -> LATIN CAPITAL LETTER V
    'W'     # 0x57 -> LATIN CAPITAL LETTER W
    'X'     # 0x58 -> LATIN CAPITAL LETTER X
    'Y'     # 0x59 -> LATIN CAPITAL LETTER Y
    'Z'     # 0x5a -> LATIN CAPITAL LETTER Z
    '['     # 0x5b -> LEFT SQUARE BRACKET
    '\\'    # 0x5c -> REVERSE SOLIDUS
    ']'     # 0x5d -> RIGHT SQUARE BRACKET
    '^'     # 0x5e -> CIRCUMFLEX ACCENT
    '_'     # 0x5f -> LOW LINE

    '`'     # 0x60 -> GRAVE ACCENT
    'a'     # 0x61 -> LATIN SMALL LETTER A
    'b'     # 0x62 -> LATIN SMALL LETTER B
    'c'     # 0x63 -> LATIN SMALL LETTER C
    'd'     # 0x64 -> LATIN SMALL LETTER D
    'e'     # 0x65 -> LATIN SMALL LETTER E
    'f'     # 0x66 -> LATIN SMALL LETTER F
    'g'     # 0x67 -> LATIN SMALL LETTER G
    'h'     # 0x68 -> LATIN SMALL LETTER H
    'i'     # 0x69 -> LATIN SMALL LETTER I
    'j'     # 0x6a -> LATIN SMALL LETTER J
    'k'     # 0x6b -> LATIN SMALL LETTER K
    'l'     # 0x6c -> LATIN SMALL LETTER L
    'm'     # 0x6d -> LATIN SMALL LETTER M
    'n'     # 0x6e -> LATIN SMALL LETTER N
    'o'     # 0x6f -> LATIN SMALL LETTER O

    'p'     # 0x70 -> LATIN SMALL LETTER P
    'q'     # 0x71 -> LATIN SMALL LETTER Q
    'r'     # 0x72 -> LATIN SMALL LETTER R
    's'     # 0x73 -> LATIN SMALL LETTER S
    't'     # 0x74 -> LATIN SMALL LETTER T
    'u'     # 0x75 -> LATIN SMALL LETTER U
    'v'     # 0x76 -> LATIN SMALL LETTER V
    'w'     # 0x77 -> LATIN SMALL LETTER W
    'x'     # 0x78 -> LATIN SMALL LETTER X
    'y'     # 0x79 -> LATIN SMALL LETTER Y
    'z'     # 0x7a -> LATIN SMALL LETTER Z
    '{'     # 0x7b -> LEFT CURLY BRACKET
    '|'     # 0x7c -> VERTICAL LINE
    '}'     # 0x7d -> RIGHT CURLY BRACKET
    '~'     # 0x7e -> TILDE
    '?'     # 0x7f

    '?'     # 0x80
    '?'     # 0x81
    '?'     # 0x82
    '?'     # 0x83
    '?'     # 0x84
    '?'     # 0x85
    '?'     # 0x86
    '?'     # 0x87
    '?'     # 0x88
    '?'     # 0x89
    '?'     # 0x8a
    '?'     # 0x8b
    '?'     # 0x8c
    '?'     # 0x8d
    '?'     # 0x8e
    '?'     # 0x8f

    '?'     # 0x90
    '?'     # 0x91
    '?'     # 0x92
    '?'     # 0x93
    '?'     # 0x94
    '?'     # 0x95
    '?'     # 0x96
    '?'     # 0x97
    '?'     # 0x98
    '?'     # 0x99
    '?'     # 0x9a
    '?'     # 0x9b
    '?'     # 0x9c
    '?'     # 0x9d
    '?'     # 0x9e
    '?'     # 0x9f

    '?'     # 0xa0
    '?'     # 0xa1
    '?'     # 0xa2
    '?'     # 0xa3
    '?'     # 0xa4
    '?'     # 0xa5
    '?'     # 0xa6
    '?'     # 0xa7
    '?'     # 0xa8
    '?'     # 0xa9
    '?'     # 0xaa
    '?'     # 0xab
    '?'     # 0xac
    '?'     # 0xad
    '?'     # 0xae
    '?'     # 0xaf

    '?'     # 0xb0
    '?'     # 0xb1
    '?'     # 0xb2
    '?'     # 0xb3
    '?'     # 0xb4
    '?'     # 0xb5
    '?'     # 0xb6
    '?'     # 0xb7
    '?'     # 0xb8
    '?'     # 0xb9
    '?'     # 0xba
    '?'     # 0xbb
    '?'     # 0xbc
    '?'     # 0xbd
    '?'     # 0xbe
    '?'     # 0xbf

    '?'     # 0xc0
    '?'     # 0xc1
    '?'     # 0xc2
    '?'     # 0xc3
    '?'     # 0xc4
    '?'     # 0xc5
    '?'     # 0xc6
    '?'     # 0xc7
    '?'     # 0xc8
    '?'     # 0xc9
    '?'     # 0xca
    '?'     # 0xcb
    '?'     # 0xcc
    '?'     # 0xcd
    '?'     # 0xce
    '?'     # 0xcf

    '?'     # 0xd0
    '?'     # 0xd1
    '?'     # 0xd2
    '?'     # 0xd3
    '?'     # 0xd4
    '?'     # 0xd5
    '?'     # 0xd6
    '?'     # 0xd7
    '?'     # 0xd8
    '?'     # 0xd9
    '?'     # 0xda
    '?'     # 0xdb
    '?'     # 0xdc
    '?'     # 0xdd
    '?'     # 0xde
    '?'     # 0xdf

    '?'     # 0xe0
    '?'     # 0xe1
    '?'     # 0xe2
    '?'     # 0xe3
    '?'     # 0xe4
    '?'     # 0xe5
    '?'     # 0xe6
    '?'     # 0xe7
    '?'     # 0xe8
    '?'     # 0xe9
    '?'     # 0xea
    '?'     # 0xeb
    '?'     # 0xec
    '?'     # 0xed
    '?'     # 0xee
    '?'     # 0xef

    '?'     # 0xf0
    '?'     # 0xf1
    '?'     # 0xf2
    '?'     # 0xf3
    '?'     # 0xf4
    '?'     # 0xf5
    '?'     # 0xf6
    '?'     # 0xf7
    '?'     # 0xf8
    '?'     # 0xf9
    '?'     # 0xfa
    '?'     # 0xfb
    '?'     # 0xfc
    '?'     # 0xfd
    '?'     # 0xfe
    '?'     # 0xff
)

encoding_table = codecs.charmap_build(decoding_table)
