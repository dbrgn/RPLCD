# -*- coding: utf-8 -*-
"""
The HD4480-A02 character table.
"""
# flake8: noqa
from __future__ import print_function, division, absolute_import, unicode_literals

# Character shown if no mapping was found
replacement_char = 0x20  # SPACE

# Table with 1:1 mapping
encoding_table = {

    '\u0000': 0x00,  # User defined (CGRAM)
    '\u0001': 0x01,  # User defined (CGRAM)
    '\u0002': 0x02,  # User defined (CGRAM)
    '\u0003': 0x03,  # User defined (CGRAM)
    '\u0004': 0x04,  # User defined (CGRAM)
    '\u0005': 0x05,  # User defined (CGRAM)
    '\u0006': 0x06,  # User defined (CGRAM)
    '\u0007': 0x07,  # User defined (CGRAM)

    '▶':      0x10,  # BLACK RIGHT-POINTING TRIANGLE
    '◀':      0x11,  # BLACK LEFT-POINTING TRIANGLE
    '“':      0x12,  # LEFT DOUBLE QUOTATION MARK
    '”':      0x13,  # RIGHT DOUBLE QUOTATION MARK
    '\u23EB': 0x14,  # BLACK UP-POINTING DOUBLE TRIANGLE
    '\u23EC': 0x15,  # BLACK DOWN-POINTING DOUBLE TRIANGLE
    '●':      0x16,  # BLACK CIRCLE
    '↲':      0x17,  # DOWNWARDS ARROW WITH TIP LEFTWARDS
    '↑':      0x18,  # UPWARDS ARROW
    '↓':      0x19,  # DOWNWARDS ARROW
    '→':      0x1a,  # RIGHTWARDS ARROW
    '←':      0x1b,  # LEFTWARDS ARROW
    '≤':      0x1c,  # LESS-THAN OR EQUAL TO
    '≥':      0x1d,  # GREATER-THAN OR EQUAL TO
    '▲':      0x1e,  # BLACK UP-POINTING TRIANGLE
    '▼':      0x1f,  # BLACK DOWN-POINTING TRIANGLE

    '\u0020': 0x20,  # SPACE
    '\u00A0': 0x20,  # NO-BREAK SPACE
    '!':      0x21,  # EXCLAMATION MARK
    '"':      0x22,  # QUOTATION MARK
    '#':      0x23,  # NUMBER SIGN
    '$':      0x24,  # DOLLAR SIGN
    '%':      0x25,  # PERCENT SIGN
    '&':      0x26,  # AMPERSAND
    "'":      0x27,  # APOSTROPHE
    '(':      0x28,  # LEFT PARENTHESES
    ')':      0x29,  # RIGHT PARENTHESES
    '*':      0x2a,  # ASTERISK
    '+':      0x2b,  # PLUS SIGN
    ',':      0x2c,  # COMMA
    '\u002d': 0x2d,  # HYPHEN-MINUS
    '\u2010': 0x2d,  # HYPHEN
    '\u2011': 0x2d,  # NON-BREAKING HYPHEN
    '\u2012': 0x2d,  # FIGURE DASH
    '\u2013': 0x2d,  # EN DASH
    '\u2014': 0x2d,  # EM DASH
    '\u2015': 0x2d,  # HORIZONTAL BAR
    '.':      0x2e,  # FULL STOP
    '/':      0x2f,  # SOLIDUS

    '0':      0x30,  # DIGIT ZERO
    '1':      0x31,  # DIGIT ONE
    '2':      0x32,  # DIGIT TWO
    '3':      0x33,  # DIGIT THREE
    '4':      0x34,  # DIGIT FOUR
    '5':      0x35,  # DIGIT FIVE
    '6':      0x36,  # DIGIT SIX
    '7':      0x37,  # DIGIT SEVEN
    '8':      0x38,  # DIGIT EIGHT
    '9':      0x39,  # DIGIT NINE
    ':':      0x3a,  # COLON
    ';':      0x3b,  # SEMICOLON
    '<':      0x3c,  # LESS-THAN SIGN
    '=':      0x3d,  # EQUALS SIGN
    '>':      0x3e,  # GREATER-THAN SIGN
    '?':      0x3f,  # QUESTION MARK

    '@':      0x40,  # COMMERCIAL AT
    'A':      0x41,  # LATIN CAPITAL LETTER A
    'B':      0x42,  # LATIN CAPITAL LETTER B
    'C':      0x43,  # LATIN CAPITAL LETTER C
    'D':      0x44,  # LATIN CAPITAL LETTER D
    'E':      0x45,  # LATIN CAPITAL LETTER E
    'F':      0x46,  # LATIN CAPITAL LETTER F
    'G':      0x47,  # LATIN CAPITAL LETTER G
    'H':      0x48,  # LATIN CAPITAL LETTER H
    'I':      0x49,  # LATIN CAPITAL LETTER I
    'J':      0x4a,  # LATIN CAPITAL LETTER J
    'K':      0x4b,  # LATIN CAPITAL LETTER K
    'L':      0x4c,  # LATIN CAPITAL LETTER L
    'M':      0x4d,  # LATIN CAPITAL LETTER M
    'N':      0x4e,  # LATIN CAPITAL LETTER N
    'O':      0x4f,  # LATIN CAPITAL LETTER O

    'P':      0x50,  # LATIN CAPITAL LETTER P
    'Q':      0x51,  # LATIN CAPITAL LETTER Q
    'R':      0x52,  # LATIN CAPITAL LETTER R
    'S':      0x53,  # LATIN CAPITAL LETTER S
    'T':      0x54,  # LATIN CAPITAL LETTER T
    'U':      0x55,  # LATIN CAPITAL LETTER U
    'V':      0x56,  # LATIN CAPITAL LETTER V
    'W':      0x57,  # LATIN CAPITAL LETTER W
    'X':      0x58,  # LATIN CAPITAL LETTER X
    'Y':      0x59,  # LATIN CAPITAL LETTER Y
    'Z':      0x5a,  # LATIN CAPITAL LETTER Z
    '[':      0x5b,  # LEFT SQUARE BRACKET
    '\\':     0x5c,  # REVERSE SOLIDUS
    ']':      0x5d,  # RIGHT SQUARE BRACKET
    '^':      0x5e,  # CIRCUMFLEX ACCENT
    '_':      0x5f,  # LOW LINE

    '`':      0x60,  # GRAVE ACCENT
    'a':      0x61,  # LATIN SMALL LETTER A
    'b':      0x62,  # LATIN SMALL LETTER B
    'c':      0x63,  # LATIN SMALL LETTER C
    'd':      0x64,  # LATIN SMALL LETTER D
    'e':      0x65,  # LATIN SMALL LETTER E
    'f':      0x66,  # LATIN SMALL LETTER F
    'g':      0x67,  # LATIN SMALL LETTER G
    'h':      0x68,  # LATIN SMALL LETTER H
    'i':      0x69,  # LATIN SMALL LETTER I
    'j':      0x6a,  # LATIN SMALL LETTER J
    'k':      0x6b,  # LATIN SMALL LETTER K
    'l':      0x6c,  # LATIN SMALL LETTER L
    'm':      0x6d,  # LATIN SMALL LETTER M
    'n':      0x6e,  # LATIN SMALL LETTER N
    'o':      0x6f,  # LATIN SMALL LETTER O

    'p':      0x70,  # LATIN SMALL LETTER P
    'q':      0x71,  # LATIN SMALL LETTER Q
    'r':      0x72,  # LATIN SMALL LETTER R
    's':      0x73,  # LATIN SMALL LETTER S
    't':      0x74,  # LATIN SMALL LETTER T
    'u':      0x75,  # LATIN SMALL LETTER U
    'v':      0x76,  # LATIN SMALL LETTER V
    'w':      0x77,  # LATIN SMALL LETTER W
    'x':      0x78,  # LATIN SMALL LETTER X
    'y':      0x79,  # LATIN SMALL LETTER Y
    'z':      0x7a,  # LATIN SMALL LETTER Z
    '{':      0x7b,  # LEFT CURLY BRACKET
    '|':      0x7c,  # VERTICAL LINE
    '}':      0x7d,  # RIGHT CURLY BRACKET
    '~':      0x7e,  # TILDE
    '⌂':      0x7f,  # HOUSE

    'Б':      0x80,  # CYRILLIC CAPITAL LETTER BE
    'Д':      0x81,  # CYRILLIC CAPITAL LETTER DE
    'Ж':      0x82,  # CYRILLIC CAPITAL LETTER ZHE
    'З':      0x83,  # CYRILLIC CAPITAL LETTER ZE
    'И':      0x84,  # CYRILLIC CAPITAL LETTER I
    'Й':      0x85,  # CYRILLIC CAPITAL LETTER SHORT I
    'Л':      0x86,  # CYRILLIC CAPITAL LETTER EL
    'П':      0x87,  # CYRILLIC CAPITAL LETTER PE
    'У':      0x88,  # CYRILLIC CAPITAL LETTER U
    'Ц':      0x89,  # CYRILLIC CAPITAL LETTER TSE
    'Ч':      0x8a,  # CYRILLIC CAPITAL LETTER CHE
    'Ш':      0x8b,  # CYRILLIC CAPITAL LETTER SHA
    'Щ':      0x8c,  # CYRILLIC CAPITAL LETTER SHCHA
    'Ъ':      0x8d,  # CYRILLIC CAPITAL LETTER HARD SIGN
    'Ы':      0x8e,  # CYRILLIC CAPITAL LETTER YERU
    'Э':      0x8f,  # CYRILLIC CAPITAL LETTER E

    'α':      0x90,  # GREEK SMALL LETTER ALPHA
    '♪':      0x91,  # EIGHTH NOTE
    'Γ':      0x92,  # GREEK CAPITAL LETTER GAMMA
    'π':      0x93,  # GREEK SMALL LETTER PI
    'Σ':      0x94,  # GREEK CAPITAL LETTER SIGMA
    '\u2211': 0x94,  # N-ARY SUMMATION
    'σ':      0x95,  # GREEK SMALL LETTER SIGMA
    '♬':      0x96,  # BEAMED SIXTEENTH NOTES
    'τ':      0x97,  # GREEK SMALL LETTER TAU
    '\U0001F514': 0x98,  # BELL
    'θ':      0x99,  # GREEK SMALL LETTER THETA
    '\u03A9': 0x9a,  # GREEK CAPITAL LETTER OMEGA
    '\u2126': 0x9a,  # OHM SIGN
    'δ':      0x9b,  # GREEK SMALL LETTER DELTA
    '∞':      0x9c,  # INFINITY
    '\u2661': 0x9d,  # WHITE HEART SUIT
    '\u2665': 0x9d,  # BLACK HEART SUIT
    '\u2764': 0x9d,  # HEAVY BLACK HEART
    'ε':      0x9e,  # GREEK SMALL LETTER EPSILON
    '\u2229': 0x9f,  # INTERSECTION

    '\u2016': 0xa0,  # DOUBLE VERTICAL LINE
    '¡':      0xa1,  # INVERTED EXCLAMATION MARK
    '¢':      0xa2,  # CENT SIGN
    '£':      0xa3,  # POUND SIGN
    '¤':      0xa4,  # CURRENCY SIGN
    '¥':      0xa5,  # YEN SIGN
    '¦':      0xa6,  # BROKEN BAR
    '§':      0xa7,  # SECTION SIGN
    'ƒ':      0xa8,  # LATIN SMALL LETTER F WITH HOOK
    '©':      0xa9,  # COPYRIGHT SIGN
    'ª':      0xaa,  # FEMININE ORDINAL INDICATOR
    '«':      0xab,  # LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    'Ю':      0xac,  # CYRILLIC CAPITAL LETTER YU
    'Я':      0xad,  # CYRILLIC CAPITAL LETTER YA
    '®':      0xae,  # REGISTERED SIGN
    '´':      0xaf,  # ACUTE ACCENT

    'ᴼ':      0xb0,  # MODIFIER LETTER CAPITAL O
    '±':      0xb1,  # PLUS-MINUS SIGN
    '²':      0xb2,  # SUPERSCRIPT TWO
    '³':      0xb3,  # SUPERSCRIPT THREE
    'μ':      0xb5,  # GREEK SMALL LETTER MU
    '¶':      0xb6,  # PILCROW SIGN
    '·':      0xb7,  # MIDDLE DOT
    'ω':      0xb8,  # GREEK SMALL LETTER OMEGA
    '¹':      0xb9,  # SUPERSCRIPT ONE
    'º':      0xba,  # MASCULINE ORDINAL INDICATOR
    '»':      0xbb,  # RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    '¼':      0xbc,  # VULGAR FRACTION ONE QUARTER
    '½':      0xbd,  # VULGAR FRACTION ONE HALF
    '¾':      0xbe,  # VULGAR FRACTION THREE QUARTERS
    '¿':      0xbf,  # INVERTED QUESTION MARK

    'À':      0xc0,  # LATIN CAPITAL LETTER A WITH GRAVE
    'Á':      0xc1,  # LATIN CAPITAL LETTER A WITH ACUTE
    'Â':      0xc2,  # LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    'Ã':      0xc3,  # LATIN CAPITAL LETTER A WITH TILDE
    'Ä':      0xc4,  # LATIN CAPITAL LETTER A WITH DIAERESIS
    'Å':      0xc5,  # LATIN CAPITAL LETTER A WITH RING ABOVE
    'Æ':      0xc6,  # LATIN CAPITAL LETTER AE
    'Ç':      0xc7,  # LATIN CAPITAL LETTER C WITH CEDILLA
    'È':      0xc8,  # LATIN CAPITAL LETTER E WITH GRAVE
    'É':      0xc9,  # LATIN CAPITAL LETTER E WITH ACUTE
    'Ê':      0xca,  # LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    'Ë':      0xcb,  # LATIN CAPITAL LETTER E WITH DIAERESIS
    'Ì':      0xcc,  # LATIN CAPITAL LETTER I WITH GRAVE
    'Í':      0xcd,  # LATIN CAPITAL LETTER I WITH ACUTE
    'Î':      0xce,  # LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    'Ï':      0xcf,  # LATIN CAPITAL LETTER I WITH DIAERESIS

    'Ð':      0xd0,  # LATIN CAPITAL LETTER ETH
    'Ñ':      0xd1,  # LATIN CAPITAL LETTER N WITH TILDE
    'Ò':      0xd2,  # LATIN CAPITAL LETTER O WITH GRAVE
    'Ó':      0xd3,  # LATIN CAPITAL LETTER O WITH ACUTE
    'Ô':      0xd4,  # LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    'Õ':      0xd5,  # LATIN CAPITAL LETTER O WITH TILDE
    'Ö':      0xd6,  # LATIN CAPITAL LETTER O WITH DIAERESIS
    '×':      0xd7,  # MULTIPLICATION SIGN
    'Φ':      0xd8,  # GREEK CAPITAL LETTER PHI
    'Ù':      0xd9,  # LATIN CAPITAL LETTER U WITH GRAVE
    'Ú':      0xda,  # LATIN CAPITAL LETTER U WITH ACUTE
    'Û':      0xdb,  # LATIN CAPITAL LETTER U WITH CIRCUMFLEX
    'Ü':      0xdc,  # LATIN CAPITAL LETTER U WITH DIAERESIS
    'Ý':      0xdd,  # LATIN CAPITAL LETTER Y WITH ACUTE
    'Þ':      0xde,  # LATIN CAPITAL LETTER THORN
    'ß':      0xdf,  # LATIN SMALL LETTER SHARP S

    'à':      0xe0,  # LATIN SMALL LETTER A WITH GRAVE
    'á':      0xe1,  # LATIN SMALL LETTER A WITH ACUTE
    'â':      0xe2,  # LATIN SMALL LETTER A WITH CIRCUMFLEX
    'ã':      0xe3,  # LATIN SMALL LETTER A WITH TILDE
    'ä':      0xe4,  # LATIN SMALL LETTER A WITH DIAERESIS
    'å':      0xe5,  # LATIN SMALL LETTER A WITH RING ABOVE
    'æ':      0xe6,  # LATIN SMALL LETTER AE
    'ç':      0xe7,  # LATIN SMALL LETTER C WITH CEDILLA
    'è':      0xe8,  # LATIN SMALL LETTER E WITH GRAVE
    'é':      0xe9,  # LATIN SMALL LETTER E WITH ACUTE
    'ê':      0xea,  # LATIN SMALL LETTER E WITH CIRCUMFLEX
    'ë':      0xeb,  # LATIN SMALL LETTER E WITH DIAERESIS
    'ì':      0xec,  # LATIN SMALL LETTER I WITH GRAVE
    'í':      0xed,  # LATIN SMALL LETTER I WITH ACUTE
    'î':      0xee,  # LATIN SMALL LETTER I WITH CIRCUMFLEX
    'ï':      0xef,  # LATIN SMALL LETTER I WITH DIAERESIS

    'ð':      0xf0,  # LATIN SMALL LETTER ETH
    'ñ':      0xf1,  # LATIN SMALL LETTER N WITH TILDE
    'ò':      0xf2,  # LATIN SMALL LETTER O WITH GRAVE
    'ó':      0xf3,  # LATIN SMALL LETTER O WITH ACUTE
    'ô':      0xf4,  # LATIN SMALL LETTER O WITH CIRCUMFLEX
    'õ':      0xf5,  # LATIN SMALL LETTER O WITH TILDE
    'ö':      0xf6,  # LATIN SMALL LETTER O WITH DIAERESIS
    '÷':      0xf7,  # DIVISION SIGN
    'ø':      0xf8,  # LATIN SMALL LETTER O WITH STROKE
    'ù':      0xf9,  # LATIN SMALL LETTER U WITH GRAVE
    'ú':      0xfa,  # LATIN SMALL LETTER U WITH ACUTE
    'û':      0xfb,  # LATIN SMALL LETTER U WITH CIRCUMFLEX
    'ü':      0xfc,  # LATIN SMALL LETTER U WITH DIAERESIS
    'ý':      0xfd,  # LATIN SMALL LETTER Y WITH ACUTE
    'þ':      0xfe,  # LATIN SMALL LETTER THORN
    'ÿ':      0xff,  # LATIN SMALL LETTER Y WITH DIAERESIS

}

# Table with combined mappings
combined_chars_lookahead = 0
combined_chars = {}
