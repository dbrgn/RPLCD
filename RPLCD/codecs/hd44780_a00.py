"""
The HD4480-A00 character table is a slightly altered form
of the JIS X 0201 codec.
"""
import codecs

decoding_table = (
    '�'       # 0x00 -> User defined (CGRAM)
    '�'       # 0x01 -> User defined (CGRAM)
    '�'       # 0x02 -> User defined (CGRAM)
    '�'       # 0x03 -> User defined (CGRAM)
    '�'       # 0x04 -> User defined (CGRAM)
    '�'       # 0x05 -> User defined (CGRAM)
    '�'       # 0x06 -> User defined (CGRAM)
    '�'       # 0x07 -> User defined (CGRAM)
    '�'       # 0x08
    '�'       # 0x09
    '�'       # 0x0A
    '�'       # 0x0B
    '�'       # 0x0C
    '�'       # 0x0D
    '�'       # 0x0E
    '�'       # 0x0F

    '�'       # 0x10
    '�'       # 0x11
    '�'       # 0x12
    '�'       # 0x13
    '�'       # 0x14
    '�'       # 0x15
    '�'       # 0x16
    '�'       # 0x17
    '�'       # 0x18
    '�'       # 0x19
    '�'       # 0x1A
    '�'       # 0x1B
    '�'       # 0x1C
    '�'       # 0x1D
    '�'       # 0x1E
    '�'       # 0x1F

    ' '       # 0x20 -> SPACE
    '!'       # 0x21 -> EXCLAMATION MARK
    '"'       # 0x22 -> QUOTATION MARK
    '#'       # 0x23 -> NUMBER SIGN
    '$'       # 0x24 -> DOLLAR SIGN
    '%'       # 0x25 -> PERCENT SIGN
    '&'       # 0x26 -> AMPERSAND
    "'"       # 0x27 -> APOSTROPHE
    '('       # 0x28 -> LEFT PARENTHESES
    ')'       # 0x29 -> RIGHT PARENTHESES
    '*'       # 0x2A -> ASTERISK
    '+'       # 0x2B -> PLUS SIGN
    ','       # 0x2C -> COMMA
    '-'       # 0x2D -> HYPHEN-MINUS
    '.'       # 0x2E -> FULL STOP
    '/'       # 0x2F -> SOLIDUS

    '0'       # 0x30 -> DIGIT ZERO
    '1'       # 0x31 -> DIGIT ONE
    '2'       # 0x32 -> DIGIT TWO
    '3'       # 0x33 -> DIGIT THREE
    '4'       # 0x34 -> DIGIT FOUR
    '5'       # 0x35 -> DIGIT FIVE
    '6'       # 0x36 -> DIGIT SIX
    '7'       # 0x37 -> DIGIT SEVEN
    '8'       # 0x38 -> DIGIT EIGHT
    '9'       # 0x39 -> DIGIT NINE
    ':'       # 0x3A -> COLON
    ';'       # 0x3B -> SEMICOLON
    '<'       # 0x3C -> LESS-THAN SIGN
    '='       # 0x3D -> EQUALS SIGN
    '>'       # 0x3E -> GREATER-THAN SIGN
    '?'       # 0x3F -> QUESTION MARK

    '@'       # 0x40 -> COMMERCIAL AT
    'A'       # 0x41 -> LATIN CAPITAL LETTER A
    'B'       # 0x42 -> LATIN CAPITAL LETTER B
    'C'       # 0x43 -> LATIN CAPITAL LETTER C
    'D'       # 0x44 -> LATIN CAPITAL LETTER D
    'E'       # 0x45 -> LATIN CAPITAL LETTER E
    'F'       # 0x46 -> LATIN CAPITAL LETTER F
    'G'       # 0x47 -> LATIN CAPITAL LETTER G
    'H'       # 0x48 -> LATIN CAPITAL LETTER H
    'I'       # 0x49 -> LATIN CAPITAL LETTER I
    'J'       # 0x4A -> LATIN CAPITAL LETTER J
    'K'       # 0x4B -> LATIN CAPITAL LETTER K
    'L'       # 0x4C -> LATIN CAPITAL LETTER L
    'M'       # 0x4D -> LATIN CAPITAL LETTER M
    'N'       # 0x4E -> LATIN CAPITAL LETTER N
    'O'       # 0x4F -> LATIN CAPITAL LETTER O

    'P'       # 0x50 -> LATIN CAPITAL LETTER P
    'Q'       # 0x51 -> LATIN CAPITAL LETTER Q
    'R'       # 0x52 -> LATIN CAPITAL LETTER R
    'S'       # 0x53 -> LATIN CAPITAL LETTER S
    'T'       # 0x54 -> LATIN CAPITAL LETTER T
    'U'       # 0x55 -> LATIN CAPITAL LETTER U
    'V'       # 0x56 -> LATIN CAPITAL LETTER V
    'W'       # 0x57 -> LATIN CAPITAL LETTER W
    'X'       # 0x58 -> LATIN CAPITAL LETTER X
    'Y'       # 0x59 -> LATIN CAPITAL LETTER Y
    'Z'       # 0x5A -> LATIN CAPITAL LETTER Z
    '['       # 0x5B -> LEFT SQUARE BRACKET
    '¥'       # 0x5C -> YEN SIGN
    ']'       # 0x5D -> RIGHT SQUARE BRACKET
    '^'       # 0x5E -> CIRCUMFLEX ACCENT
    '_'       # 0x5F -> LOW LINE

    '`'       # 0x60 -> GRAVE ACCENT
    'a'       # 0x61 -> LATIN SMALL LETTER A
    'b'       # 0x62 -> LATIN SMALL LETTER B
    'c'       # 0x63 -> LATIN SMALL LETTER C
    'd'       # 0x64 -> LATIN SMALL LETTER D
    'e'       # 0x65 -> LATIN SMALL LETTER E
    'f'       # 0x66 -> LATIN SMALL LETTER F
    'g'       # 0x67 -> LATIN SMALL LETTER G
    'h'       # 0x68 -> LATIN SMALL LETTER H
    'i'       # 0x69 -> LATIN SMALL LETTER I
    'j'       # 0x6A -> LATIN SMALL LETTER J
    'k'       # 0x6B -> LATIN SMALL LETTER K
    'l'       # 0x6C -> LATIN SMALL LETTER L
    'm'       # 0x6D -> LATIN SMALL LETTER M
    'n'       # 0x6E -> LATIN SMALL LETTER N
    'o'       # 0x6F -> LATIN SMALL LETTER O

    'p'       # 0x70 -> LATIN SMALL LETTER P
    'q'       # 0x71 -> LATIN SMALL LETTER Q
    'r'       # 0x72 -> LATIN SMALL LETTER R
    's'       # 0x73 -> LATIN SMALL LETTER S
    't'       # 0x74 -> LATIN SMALL LETTER T
    'u'       # 0x75 -> LATIN SMALL LETTER U
    'v'       # 0x76 -> LATIN SMALL LETTER V
    'w'       # 0x77 -> LATIN SMALL LETTER W
    'x'       # 0x78 -> LATIN SMALL LETTER X
    'y'       # 0x79 -> LATIN SMALL LETTER Y
    'z'       # 0x7A -> LATIN SMALL LETTER Z
    '{'       # 0x7B -> LEFT CURLY BRACKET
    '|'       # 0x7C -> VERTICAL LINE
    '}'       # 0x7D -> RIGHT CURLY BRACKET
    '→'       # 0x7E -> RIGHTWARDS ARROW
    '←'       # 0x7F -> LEFTWARDS ARROW

    '�'       # 0x80
    '�'       # 0x81
    '�'       # 0x82
    '�'       # 0x83
    '�'       # 0x84
    '�'       # 0x85
    '�'       # 0x86
    '�'       # 0x87
    '�'       # 0x88
    '�'       # 0x89
    '�'       # 0x8A
    '�'       # 0x8B
    '�'       # 0x8C
    '�'       # 0x8D
    '�'       # 0x8E
    '�'       # 0x8F

    '�'       # 0x90
    '�'       # 0x91
    '�'       # 0x92
    '�'       # 0x93
    '�'       # 0x94
    '�'       # 0x95
    '�'       # 0x96
    '�'       # 0x97
    '�'       # 0x98
    '�'       # 0x99
    '�'       # 0x9A
    '�'       # 0x9B
    '�'       # 0x9C
    '�'       # 0x9D
    '�'       # 0x9E
    '�'       # 0x9F

    '�'       # 0xA0
    '\uFF61'  # 0xA1 -> HALFWIDTH IDEOGRAPHIC FULL STOP
    '\uFF62'  # 0xA2 -> HALFWIDTH LEFT CORNER BRACKET
    '\uFF63'  # 0xA3 -> HALFWIDTH RIGHT CORNER BRACKET
    '\uFF64'  # 0xA4 -> HALFWIDTH IDEOGRAPHIC COMMA
    '\uFF65'  # 0xA5 -> HALFWIDTH KATAKANA MIDDLE DOT
    '\uFF66'  # 0xA6 -> HALFWIDTH KATAKANA LETTER WO
    '\uFF67'  # 0xA7 -> HALFWIDTH KATAKANA LETTER SMALL A
    '\uFF68'  # 0xA8 -> HALFWIDTH KATAKANA LETTER SMALL I
    '\uFF69'  # 0xA9 -> HALFWIDTH KATAKANA LETTER SMALL U
    '\uFF6A'  # 0xAA -> HALFWIDTH KATAKANA LETTER SMALL E
    '\uFF6B'  # 0xAB -> HALFWIDTH KATAKANA LETTER SMALL O
    '\uFF6C'  # 0xAC -> HALFWIDTH KATAKANA LETTER SMALL YA
    '\uFF6D'  # 0xAD -> HALFWIDTH KATAKANA LETTER SMALL YU
    '\uFF6E'  # 0xAE -> HALFWIDTH KATAKANA LETTER SMALL YO
    '\uFF6F'  # 0xAF -> HALFWIDTH KATAKANA LETTER SMALL TU

    '\uFF70'  # 0xB0 -> HALFWIDTH KATAKANA-HIRAGANA PROLONGED SOUND MARK
    '\uFF71'  # 0xB1 -> HALFWIDTH KATAKANA LETTER A
    '\uFF72'  # 0xB2 -> HALFWIDTH KATAKANA LETTER I
    '\uFF73'  # 0xB3 -> HALFWIDTH KATAKANA LETTER U
    '\uFF74'  # 0xB4 -> HALFWIDTH KATAKANA LETTER E
    '\uFF75'  # 0xB5 -> HALFWIDTH KATAKANA LETTER O
    '\uFF76'  # 0xB6 -> HALFWIDTH KATAKANA LETTER KA
    '\uFF77'  # 0xB7 -> HALFWIDTH KATAKANA LETTER KI
    '\uFF78'  # 0xB8 -> HALFWIDTH KATAKANA LETTER KU
    '\uFF79'  # 0xB9 -> HALFWIDTH KATAKANA LETTER KE
    '\uFF7A'  # 0xBA -> HALFWIDTH KATAKANA LETTER KO
    '\uFF7B'  # 0xBB -> HALFWIDTH KATAKANA LETTER SA
    '\uFF7C'  # 0xBC -> HALFWIDTH KATAKANA LETTER SI
    '\uFF7D'  # 0xBD -> HALFWIDTH KATAKANA LETTER SU
    '\uFF7E'  # 0xBE -> HALFWIDTH KATAKANA LETTER SE
    '\uFF7F'  # 0xBF -> HALFWIDTH KATAKANA LETTER SO

    '\uFF80'  # 0xC0 -> HALFWIDTH KATAKANA LETTER TA
    '\uFF81'  # 0xC1 -> HALFWIDTH KATAKANA LETTER TI
    '\uFF82'  # 0xC2 -> HALFWIDTH KATAKANA LETTER TU
    '\uFF83'  # 0xC3 -> HALFWIDTH KATAKANA LETTER TE
    '\uFF84'  # 0xC4 -> HALFWIDTH KATAKANA LETTER TO
    '\uFF85'  # 0xC5 -> HALFWIDTH KATAKANA LETTER NA
    '\uFF86'  # 0xC6 -> HALFWIDTH KATAKANA LETTER NI
    '\uFF87'  # 0xC7 -> HALFWIDTH KATAKANA LETTER NU
    '\uFF88'  # 0xC8 -> HALFWIDTH KATAKANA LETTER NE
    '\uFF89'  # 0xC9 -> HALFWIDTH KATAKANA LETTER NO
    '\uFF8A'  # 0xCA -> HALFWIDTH KATAKANA LETTER HA
    '\uFF8B'  # 0xCB -> HALFWIDTH KATAKANA LETTER HI
    '\uFF8C'  # 0xCC -> HALFWIDTH KATAKANA LETTER HU
    '\uFF8D'  # 0xCD -> HALFWIDTH KATAKANA LETTER HE
    '\uFF8E'  # 0xCE -> HALFWIDTH KATAKANA LETTER HO
    '\uFF8F'  # 0xCF -> HALFWIDTH KATAKANA LETTER MA

    '\uFF90'  # 0xD0 -> HALFWIDTH KATAKANA LETTER MI
    '\uFF91'  # 0xD1 -> HALFWIDTH KATAKANA LETTER MU
    '\uFF92'  # 0xD2 -> HALFWIDTH KATAKANA LETTER ME
    '\uFF93'  # 0xD3 -> HALFWIDTH KATAKANA LETTER MO
    '\uFF94'  # 0xD4 -> HALFWIDTH KATAKANA LETTER YA
    '\uFF95'  # 0xD5 -> HALFWIDTH KATAKANA LETTER YU
    '\uFF96'  # 0xD6 -> HALFWIDTH KATAKANA LETTER YO
    '\uFF97'  # 0xD7 -> HALFWIDTH KATAKANA LETTER RA
    '\uFF98'  # 0xD8 -> HALFWIDTH KATAKANA LETTER RI
    '\uFF99'  # 0xD9 -> HALFWIDTH KATAKANA LETTER RU
    '\uFF9A'  # 0xDA -> HALFWIDTH KATAKANA LETTER RE
    '\uFF9B'  # 0xDB -> HALFWIDTH KATAKANA LETTER RO
    '\uFF9C'  # 0xDC -> HALFWIDTH KATAKANA LETTER WA
    '\uFF9D'  # 0xDD -> HALFWIDTH KATAKANA LETTER N
    '\uFF9E'  # 0xDE -> HALFWIDTH KATAKANA VOICED SOUND MARK
    '\uFF9F'  # 0xDF -> HALFWIDTH KATAKANA SEMI-VOICED SOUND MARK

    'α'       # 0xE0 -> GREEK SMALL LETTER ALPHA
    'ä'       # 0xE1 -> LATIN SMALL LETTER A WITH DIAERESIS
    'β'       # 0xE2 -> GREEK SMALL LETTER BETA
    'ε'       # 0xE3 -> GREEK SMALL LETTER EPSILON
    'μ'       # 0xE4 -> GREEK SMALL LETTER MU
    'σ'       # 0xE5 -> GREEK SMALL LETTER SIGMA
    'ρ'       # 0xE6 -> GREEK SMALL LETTER RHO
    '?'       # 0xE7
    '√'       # 0xE8 -> SQUARE ROOT
    '?'       # 0xE9
    '?'       # 0xEA
    '¤'       # 0xEB -> CURRENCY SIGN
    '¢'       # 0xEC -> CENT SIGN
    '\u2C60'  # 0xED -> LATIN CAPITAL LETTER L WITH DOUBLE Bar
    'ñ'       # 0xEE -> LATIN SMALL LETTER N WITH TILDE
    'ö'       # 0xEF -> LATIN SMALL LETTER O WITH DIAERESIS

    '?'       # 0xF0
    '?'       # 0xF1
    'ϴ'       # 0xF2 -> GREEK SMALL LETTER THETA
    '∞'       # 0xF3 -> INFINITY
    'Ω'       # 0xF4 -> GREEK CAPITAL LETTER OMEGA
    'ü'       # 0xF5 -> LATIN SMALL LETTER U WITH DIAERESIS
    'Σ'       # 0xF6 -> GREEK CAPITAL LETTER SIGMA
    'π'       # 0xF7 -> GREEK SMALL LETTER PI
    '?'       # 0xF8
    '?'       # 0xF9
    '\u5343'  # 0xFA -> CJK UNIFIED IDEOGRAPH 5343
    '\u4E07'  # 0xFB -> CJK UNIFIED IDEOGRAPH 4E07
    '\u5186'  # 0xFC -> CJK UNIFIED IDEOGRAPH 5186
    '÷'       # 0xFD -> DIVISION SIGN
    '�'       # 0xFE
    '■'       # 0xFF -> BLACK SQUARE
)

encoding_table = codecs.charmap_build(decoding_table)
