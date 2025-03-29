"""
The ST7066_0B character table.
"""

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

    '±':      0x10,  # PLUS-MINUS SIGN
    '≡':      0x11,  # IDENTICAL TO
    '\u23B2': 0x12,  # SUMMATION TOP
    '\u23B3': 0x13,  # SUMMATION BOTTOM
    '\u239B': 0x14,  # LEFT PARENTHESIS UPPER HOOK
    '\u239D': 0x15,  # LEFT PARENTHESIS LOWER HOOK
    '\u239E': 0x16,  # RIGHT PARENTHESIS UPPER HOOK
    '\u23A0': 0x17,  # RIGHT PARENTHESIS LOWER HOOK
    '\u23B0': 0x18,  # UPPER LEFT OR LOWER RIGHT CURLY BRACKET SECTION
    '\u23B1': 0x19,  # UPPER RIGHT OR LOWER LEFT CURLY BRACKET SECTION
    '\u2248': 0x1a,  # ALMOST EQUAL TO
    '\u222B': 0x1b,  # INTEGRAL
    '\u208C': 0x1c,  # SUBSCRIPT EQUALS SIGN
    '\u02F7': 0x1d,  # MODIFIER LETTER LOW TILDE
    '²':      0x1e,  # SUPERSCRIPT TWO
    '³':      0x1f,  # SUPERSCRIPT THREE

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

    '‘':      0x60,  # LEFT SINGLE QUOTATION MARK
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

    'Ç':      0x80,  # LATIN CAPITAL LETT
    'ü':      0x81,  # LATIN SMALL LETTER U WITH DIAERESIS
    'é':      0x82,  # LATIN SMALL LETTER E WITH ACUTE
    'â':      0x83,  # LATIN SMALL LETTER A WITH CIRCUMFLEX
    'ä':      0x84,  # LATIN SMALL LETTER A WITH DIAERESIS
    'à':      0x85,  # LATIN SMALL LETTER A WITH GRAVE
    'å':      0x86,  # LATIN SMALL LETTER A WITH RING ABOVE
    'ç':      0x87,  # LATIN SMALL LETTER C WITH CEDILLA
    'ê':      0x88,  # LATIN SMALL LETTER E WITH CIRCUMFLEX
    'ë':      0x89,  # LATIN SMALL LETTER E WITH DIAERESIS
    'è':      0x8a,  # LATIN SMALL LETTER E WITH GRAVE
    'ï':      0x8b,  # LATIN SMALL LETTER I WITH DIAERESIS
    'î':      0x8c,  # LATIN SMALL LETTER I WITH CIRCUMFLEX
    'ì':      0x8d,  # LATIN SMALL LETTER I WITH GRAVE
    'Ä':      0x8e,  # LATIN CAPITAL LETTER A WITH DIAERESIS
    'Å':      0x8f,  # LATIN CAPITAL LETTER A WITH RING ABOVE

    'É':      0x90,  # LATIN CAPITAL LETTER E WITH ACUTE
    'æ':      0x91,  # LATIN SMALL LETTER AE
    'Æ':      0x92,  # LATIN CAPITAL LETTER AE
    'ô':      0x93,  # LATIN SMALL LETTER O WITH CIRCUMFLEX
    'ö':      0x94,  # LATIN SMALL LETTER O WITH DIAERESIS
    'ò':      0x95,  # LATIN SMALL LETTER O WITH GRAVE
    'û':      0x96,  # LATIN SMALL LETTER U WITH CIRCUMFLEX
    'ù':      0x97,  # LATIN SMALL LETTER U WITH GRAVE
    'ÿ':      0x98,  # LATIN SMALL LETTER Y WITH DIAERESIS
    'Ö':      0x99,  # LATIN CAPITAL LETTER O WITH DIAERESIS
    'Ü':      0x9a,  # LATIN CAPITAL LETTER U WITH DIAERESIS
    'ñ':      0x9b,  # LATIN SMALL LETTER N WITH TILDE
    'Ñ':      0x9c,  # LATIN CAPITAL LETTER N WITH TILDE
    'ª':      0x9d,  # FEMININE ORDINAL INDICATOR
    'º':      0x9e,  # MASCULINE ORDINAL INDICATOR
    '¿':      0x9f,  # INVERTED QUESTION MARK

    'á':      0xa0,  # LATIN SMALL LETTER A WITH ACUTE
    'í':      0xa1,  # LATIN SMALL LETTER I WITH ACUTE
    'ó':      0xa2,  # LATIN SMALL LETTER O WITH ACUTE
    'ú':      0xa3,  # LATIN SMALL LETTER U WITH ACUTE
    '¢':      0xa4,  # CENT SIGN
    '£':      0xa5,  # POUND SIGN
    '¥':      0xa6,  # YEN SIGN
    'Я':      0xa7,  # CYRILLIC CAPITAL LETTER YA, WRONG
    'ƒ':      0xa8,  # LATIN SMALL LETTER F WITH HOOK
    '¡':      0xa9,  # INVERTED EXCLAMATION MARK
    'Ã':      0xaa,  # LATIN CAPITAL LETTER A WITH TILDE
    'ã':      0xab,  # LATIN SMALL LETTER A WITH TILDE
    'Õ':      0xac,  # LATIN CAPITAL LETTER O WITH TILDE
    'õ':      0xad,  # LATIN SMALL LETTER O WITH TILDE
    'Ø':      0xae,  # LATIN CAPITAL LETTER O WITH STROKE
    'ø':      0xaf,  # LATIN SMALL LETTER O WITH STROKE

    '˙':      0xb0,  # DOT ABOVE
    '¨':      0xb1,  # DIARESIS
    '°':      0xb2,  # DEGREE SIGN
    '`':      0xb3,  # GRAVIS
    '´':      0xb4,  # ACUTE ACCENT
    '½':      0xb5,  # VULGAR FRACTION ONE HALF
    '¼':      0xb6,  # VULGAR FRACTION ONE QUARTER
    '×':      0xb7,  # MULTIPLICATION SIGN
    '÷':      0xb8,  # DIVISION SIGN
    '≤':      0xb9,  # LESS-THAN OR EQUAL TO
    '≥':      0xba,  # GREATER-THAN OR EQUAL TO
    '«':      0xbb,  # LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    '»':      0xbc,  # RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    '≠':      0xbd,  # NOT EQUAL TO
    '√':      0xbe,  # SQUARE ROOT
    '⁻':      0xbf,  # SUPERSCRIPT MINUS

    '⌠':      0xc0,  # TOP HALF INTEGRAL
    '⌡':      0xc1,  # BOTTOM HALF INTEGRAL
    '∞':      0xc2,  # INFINITY
    '\u25F8': 0xc3,  # UPPER LEFT TRIANGLE
    '↲':      0xc4,  # DOWNWARDS ARROW WITH TIP LEFTWARDS
    '↑':      0xc5,  # UPWARDS ARROW
    '↓':      0xc6,  # DOWNWARDS ARROW
    '→':      0xc7,  # RIGHTWARDS ARROW
    '←':      0xc8,  # LEFTWARDS ARROW
    '┌':      0xc9,  # BOX DRAWINGS LIGHT DOWN AND RIGHT
    '┐':      0xca,  # BOX DRAWINGS LIGHT DOWN AND LEFT
    '└':      0xcb,  # BOX DRAWINGS LIGHT UP AND RIGHT
    '┘':      0xcc,  # BOX DRAWINGS LIGHT UP AND LEFT
    '●':      0xcd,  # BLACK CIRCLE
    '®':      0xce,  # REGISTERED SIGN
    '©':      0xcf,  # COPYRIGHT SIGN

    '™':      0xd0,  # TRADE MARK SIGN
    '†':      0xd1,  # DAGGER
    '§':      0xd2,  # SECTION SIGN
    '¶':      0xd3,  # PILCROW SIGN
    'Γ':      0xd4,  # GREEK CAPITAL LETTER GAMMA
    '◿':     0xd5,  # LOWER RIGHT TRIANGLE
    'Δ':      0xd5,  # GREEK CAPITAL LETTER DELTA
    'Θ':      0xd6,  # GREEK CAPITAL LETTER THETA
    'Λ':      0xd7,  # GREEK CAPITAL LETTER LAMBDA
    'Ξ':      0xd8,  # GREEK CAPITAL LETTER XI
    'Π':      0xd9,  # GREEK CAPITAL LETTER PI
    'Σ':      0xda,  # GREEK CAPITAL LETTER SIGMA
    'Υ':      0xdb,  # GREEK CAPITAL LETTER UPSILON
    'Φ':      0xdc,  # GREEK CAPITAL LETTER PHI
    'Ψ':      0xdd,  # GREEK CAPITAL LETTER PSI
    'Ω':      0xde,  # GREEK CAPITAL LETTER OMEGA
    'α':      0xdf,  # GREEK SMALL LETTER ALPHA

    'ß':      0xe0,  # LATIN SMALL LETTER SHARP S (FAKE)
    'β':      0xe0,  # GREEK SMALL LETTER BETA
    'γ':      0xe1,  # GREEK SMALL LETTER GAMMA
    'δ':      0xe2,  # GREEK SMALL LETTER DELTA
    'ε':      0xe3,  # GREEK SMALL LETTER EPSILON
    'ζ':      0xe4,  # GREEK SMALL LETTER ZETA
    'η':      0xe5,  # GREEK SMALL LETTER ETA
    'θ':      0xe6,  # GREEK SMALL LETTER THETA
    'ι':      0xe7,  # GREEK SMALL LETTER IOTA
    'κ':      0xe8,  # GREEK SMALL LETTER KAPPA
    'λ':      0xe9,  # GREEK SMALL LETTER LAMBDA
    'μ':      0xea,  # GREEK SMALL LETTER MU
    'ν':      0xeb,  # GREEK SMALL LETTER NU
    'ξ':      0xec,  # GREEK SMALL LETTER XI
    'π':      0xed,  # GREEK SMALL LETTER PI
    'ρ':      0xee,  # GREEK SMALL LETTER RHO
    'σ':      0xef,  # GREEK SMALL LETTER SIGMA

    'τ':      0xf0,  # GREEK SMALL LETTER TAU
    'υ':      0xf1,  # GREEK SMALL LETTER UPSILON
    'χ':      0xf2,  # GREEK SMALL LETTER CHI
    'ψ':      0xf3,  # GREEK SMALL LETTER PSI
    'ω':      0xf4,  # GREEK SMALL LETTER OMEGA
    '▼':     0xf5,  # BLACK DOWN-POINTING TRIANGLE
    '▶':     0xf6,  # BLACK RIGHT-POINTING TRIANGLE
    '◀':     0xf7,  # BLACK LEFT-POINTING TRIANGLE
    '\U0001D411':     0xf8,  # MATHEMATICAL BOLD CAPITAL R
    '↤':     0xf9,  # LEFTWARDS ARROW FROM BAR
    '\U0001D405':     0xfa,  # MATHEMATICAL BOLD CAPITAL F
    '⇥':     0xfb,  # RIGHTWARDS ARROW FROM BAR
    '☐':     0xfc,  # BALLOT BOX
    '━':     0xfd,  # BOX DRAWINGS HEAVY HORIZONTAL
    '\U0001F142': 0xfe,  # SQUARED LATIN CAPITAL LETTER S
    '\U0001F13F': 0xff  # SQUARED LATIN CAPITAL LETTER P
}

# Table with combined mappings
combined_chars_lookahead = 0
combined_chars = {}
