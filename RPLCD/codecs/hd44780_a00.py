"""
The HD4480-A00 character table is a slightly altered form
of the JIS X 0201 codec.
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
    '\x00'  # 0x0A
    '\x00'  # 0x0B
    '\x00'  # 0x0C
    '\x00'  # 0x0D
    '\x00'  # 0x0E
    '\x00'  # 0x0F

    '\x00'  # 0x10
    '\x00'  # 0x11
    '\x00'  # 0x12
    '\x00'  # 0x13
    '\x00'  # 0x14
    '\x00'  # 0x15
    '\x00'  # 0x16
    '\x00'  # 0x17
    '\x00'  # 0x18
    '\x00'  # 0x19
    '\x00'  # 0x1A
    '\x00'  # 0x1B
    '\x00'  # 0x1C
    '\x00'  # 0x1D
    '\x00'  # 0x1E
    '\x00'  # 0x1F

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
    '*'     # 0x2A -> ASTERISK
    '+'     # 0x2B -> PLUS SIGN
    ','     # 0x2C -> COMMA
    '-'     # 0x2D -> HYPHEN-MINUS
    '.'     # 0x2E -> FULL STOP
    '/'     # 0x2F -> SOLIDUS

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
    ':'     # 0x3A -> COLON
    ';'     # 0x3B -> SEMICOLON
    '<'     # 0x3C -> LESS-THAN SIGN
    '='     # 0x3D -> EQUALS SIGN
    '>'     # 0x3E -> GREATER-THAN SIGN
    '?'     # 0x3F -> QUESTION MARK

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
    'J'     # 0x4A -> LATIN CAPITAL LETTER J
    'K'     # 0x4B -> LATIN CAPITAL LETTER K
    'L'     # 0x4C -> LATIN CAPITAL LETTER L
    'M'     # 0x4D -> LATIN CAPITAL LETTER M
    'N'     # 0x4E -> LATIN CAPITAL LETTER N
    'O'     # 0x4F -> LATIN CAPITAL LETTER O

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
    'Z'     # 0x5A -> LATIN CAPITAL LETTER Z
    '['     # 0x5B -> LEFT SQUARE BRACKET
    '¥'     # 0x5C -> YEN SIGN
    ']'     # 0x5D -> RIGHT SQUARE BRACKET
    '^'     # 0x5E -> CIRCUMFLEX ACCENT
    '_'     # 0x5F -> LOW LINE

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
    'j'     # 0x6A -> LATIN SMALL LETTER J
    'k'     # 0x6B -> LATIN SMALL LETTER K
    'l'     # 0x6C -> LATIN SMALL LETTER L
    'm'     # 0x6D -> LATIN SMALL LETTER M
    'n'     # 0x6E -> LATIN SMALL LETTER N
    'o'     # 0x6F -> LATIN SMALL LETTER O

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
    'z'     # 0x7A -> LATIN SMALL LETTER Z
    '{'     # 0x7B -> LEFT CURLY BRACKET
    '|'     # 0x7C -> VERTICAL LINE
    '}'     # 0x7D -> RIGHT CURLY BRACKET
    '→'     # 0x7E
    '←'     # 0x7F

    '\x00'  # 0x80
    '\x00'  # 0x81
    '\x00'  # 0x82
    '\x00'  # 0x83
    '\x00'  # 0x84
    '\x00'  # 0x85
    '\x00'  # 0x86
    '\x00'  # 0x87
    '\x00'  # 0x88
    '\x00'  # 0x89
    '\x00'  # 0x8A
    '\x00'  # 0x8B
    '\x00'  # 0x8C
    '\x00'  # 0x8D
    '\x00'  # 0x8E
    '\x00'  # 0x8F

    '\x00'  # 0x90
    '\x00'  # 0x91
    '\x00'  # 0x92
    '\x00'  # 0x93
    '\x00'  # 0x94
    '\x00'  # 0x95
    '\x00'  # 0x96
    '\x00'  # 0x97
    '\x00'  # 0x98
    '\x00'  # 0x99
    '\x00'  # 0x9A
    '\x00'  # 0x9B
    '\x00'  # 0x9C
    '\x00'  # 0x9D
    '\x00'  # 0x9E
    '\x00'  # 0x9F

    '\x00'  # 0xA0
    '｡'     # 0xA1 -> HALFWIDTH IDEOGRAPHIC FULL STOP
    '｢'     # 0xA2 -> HALFWIDTH LEFT CORNER BRACKET
    '｣'     # 0xA3 -> HALFWIDTH RIGHT CORNER BRACKET
    '､'     # 0xA4 -> HALFWIDTH IDEOGRAPHIC COMMA
    '･'     # 0xA5 -> HALFWIDTH KATAKANA MIDDLE DOT
    'ｦ'     # 0xA6 -> HALFWIDTH KATAKANA LETTER WO
    'ｧ'     # 0xA7 -> HALFWIDTH KATAKANA LETTER SMALL A
    'ｨ'     # 0xA8 -> HALFWIDTH KATAKANA LETTER SMALL I
    'ｩ'     # 0xA9 -> HALFWIDTH KATAKANA LETTER SMALL U
    'ｪ'     # 0xAA -> HALFWIDTH KATAKANA LETTER SMALL E
    'ｫ'     # 0xAB -> HALFWIDTH KATAKANA LETTER SMALL O
    'ｬ'     # 0xAC -> HALFWIDTH KATAKANA LETTER SMALL YA
    'ｭ'     # 0xAD -> HALFWIDTH KATAKANA LETTER SMALL YU
    'ｮ'     # 0xAE -> HALFWIDTH KATAKANA LETTER SMALL YO
    'ｯ'     # 0xAF -> HALFWIDTH KATAKANA LETTER SMALL TU

    'ｰ'     # 0xB0 -> HALFWIDTH KATAKANA-HIRAGANA PROLONGED SOUND MARK
    'ｱ'     # 0xB1 -> HALFWIDTH KATAKANA LETTER A
    'ｲ'     # 0xB2 -> HALFWIDTH KATAKANA LETTER I
    'ｳ'     # 0xB3 -> HALFWIDTH KATAKANA LETTER U
    'ｴ'     # 0xB4 -> HALFWIDTH KATAKANA LETTER E
    'ｵ'     # 0xB5 -> HALFWIDTH KATAKANA LETTER O
    'ｶ'     # 0xB6 -> HALFWIDTH KATAKANA LETTER KA
    'ｷ'     # 0xB7 -> HALFWIDTH KATAKANA LETTER KI
    'ｸ'     # 0xB8 -> HALFWIDTH KATAKANA LETTER KU
    'ｹ'     # 0xB9 -> HALFWIDTH KATAKANA LETTER KE
    'ｺ'     # 0xBA -> HALFWIDTH KATAKANA LETTER KO
    'ｻ'     # 0xBB -> HALFWIDTH KATAKANA LETTER SA
    'ｼ'     # 0xBC -> HALFWIDTH KATAKANA LETTER SI
    'ｽ'     # 0xBD -> HALFWIDTH KATAKANA LETTER SU
    'ｾ'     # 0xBE -> HALFWIDTH KATAKANA LETTER SE
    'ｿ'     # 0xBF -> HALFWIDTH KATAKANA LETTER SO

    'ﾀ'     # 0xC0 -> HALFWIDTH KATAKANA LETTER TA
    'ﾁ'     # 0xC1 -> HALFWIDTH KATAKANA LETTER TI
    'ﾂ'     # 0xC2 -> HALFWIDTH KATAKANA LETTER TU
    'ﾃ'     # 0xC3 -> HALFWIDTH KATAKANA LETTER TE
    'ﾄ'     # 0xC4 -> HALFWIDTH KATAKANA LETTER TO
    'ﾅ'     # 0xC5 -> HALFWIDTH KATAKANA LETTER NA
    'ﾆ'     # 0xC6 -> HALFWIDTH KATAKANA LETTER NI
    'ﾇ'     # 0xC7 -> HALFWIDTH KATAKANA LETTER NU
    'ﾈ'     # 0xC8 -> HALFWIDTH KATAKANA LETTER NE
    'ﾉ'     # 0xC9 -> HALFWIDTH KATAKANA LETTER NO
    'ﾊ'     # 0xCA -> HALFWIDTH KATAKANA LETTER HA
    'ﾋ'     # 0xCB -> HALFWIDTH KATAKANA LETTER HI
    'ﾌ'     # 0xCC -> HALFWIDTH KATAKANA LETTER HU
    'ﾍ'     # 0xCD -> HALFWIDTH KATAKANA LETTER HE
    'ﾎ'     # 0xCE -> HALFWIDTH KATAKANA LETTER HO
    'ﾏ'     # 0xCF -> HALFWIDTH KATAKANA LETTER MA

    'ﾐ'     # 0xD0 -> HALFWIDTH KATAKANA LETTER MI
    'ﾑ'     # 0xD1 -> HALFWIDTH KATAKANA LETTER MU
    'ﾒ'     # 0xD2 -> HALFWIDTH KATAKANA LETTER ME
    'ﾓ'     # 0xD3 -> HALFWIDTH KATAKANA LETTER MO
    'ﾔ'     # 0xD4 -> HALFWIDTH KATAKANA LETTER YA
    'ﾕ'     # 0xD5 -> HALFWIDTH KATAKANA LETTER YU
    'ﾖ'     # 0xD6 -> HALFWIDTH KATAKANA LETTER YO
    'ﾗ'     # 0xD7 -> HALFWIDTH KATAKANA LETTER RA
    'ﾘ'     # 0xD8 -> HALFWIDTH KATAKANA LETTER RI
    'ﾙ'     # 0xD9 -> HALFWIDTH KATAKANA LETTER RU
    'ﾚ'     # 0xDA -> HALFWIDTH KATAKANA LETTER RE
    'ﾛ'     # 0xDB -> HALFWIDTH KATAKANA LETTER RO
    'ﾜ'     # 0xDC -> HALFWIDTH KATAKANA LETTER WA
    'ﾝ'     # 0xDD -> HALFWIDTH KATAKANA LETTER N
    'ﾞ'     # 0xDE -> HALFWIDTH KATAKANA VOICED SOUND MARK
    'ﾟ'     # 0xDF -> HALFWIDTH KATAKANA SEMI-VOICED SOUND MARK

    'α'     # 0xE0
    'ä'     # 0xE1
    'β'     # 0xE2
    'ε'     # 0xE3
    'μ'     # 0xE4
    'σ'     # 0xE5
    'ρ'     # 0xE6
    '?'     # 0xE7
    '√'     # 0xE8
    '?'     # 0xE9
    '?'     # 0xEA
    '¤'     # 0xEB
    '¢'     # 0xEC
    'Ⱡ'     # 0xED
    'ñ'     # 0xEE
    'ö'     # 0xEF

    '?'     # 0xF0
    '?'     # 0xF1
    'ϴ'     # 0xF2
    '∞'     # 0xF3
    'Ω'     # 0xF4
    'ü'     # 0xF5
    'Σ'     # 0xF6
    'π'     # 0xF7
    '?'     # 0xF8
    '?'     # 0xF9
    '?'     # 0xFA
    '?'     # 0xFB
    '?'     # 0xFC
    '÷'     # 0xFD
    '?'     # 0xFE
    '■'     # 0xFF
)

encoding_table = codecs.charmap_build(decoding_table)
