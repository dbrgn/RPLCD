"""
Copyright (C) 2013-2023 Danilo Bargen

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

import sys

# Import supported tests
from . import show_charmap, testsuite_20x4, testsuite_16x2

# Globals
options = {}
no_default = object()


def print_usage(error=None):
    print('Usage: %s i2c <test> <options>' % sys.argv[0])
    print('       %s gpio <test> <options>' % sys.argv[0])
    print('       %s pigpio <text> <options>' % sys.argv[0])
    print('')
    print('<test> Which test to run:')
    print('')
    print('   show_charmap - Displays all characters in the charmap')
    print('   testsuite    - Tests display formatting, 20x4 and 16x2 displays supported.')
    print('')
    # Options for i2c mode
    if (len(sys.argv) > 1) and (sys.argv[1] == 'i2c'):
        print('<options> i2c options:')
        print('')
        print('   expander - Supported I²C port expanders are PCF8574, MCP23008 and MCP23017')
        print('   addr     - The I²C address (in hex format) can be found with')
        print('              `i2cdetect 1` from the i2c-tools package.')
        print('   port     - The I²C port. For the first RPi with 256MB RAM this is 0, else 1')
        print('              Default: 1')
        print('   cols     - The number of columns on your LCD, e.g. 16')
        print('   rows     - The number of rows on your LCD, e.g. 2')
        print('   charmap  - Which character map to use. Either A00 or A02. If your display')
        print('              contains Japanese characters, it probably uses the A00 charmap,')
        print('              otherwise A02. Default: A00')
        print('')
        print('   Expander specific options:')
        print('')
        print('   MCP23017: gpio_bank - Either A or B')
        print('')
        print('Examples:')
        print('')
        print(
            sys.argv[0] + ' i2c testsuite expander=PCF8574 addr=0x27 port=1 '
            'cols=20 rows=4 charmap=A00'
        )
        print(
            sys.argv[0] + ' i2c testsuite expander=MCP23017 addr=0x20 port=1 '
            'kols=20 rows=4 charmap=A00 gpio_bank=A'
        )

    # Options for GPIO mode
    elif (len(sys.argv) > 1) and (sys.argv[1] == 'gpio'):
        print('<options> gpio options:')
        print('')
        print('   mode    - GPIO numbering mode, either BOARD or BCM')
        print('   cols    - The number of columns on your LCD, e.g. 16')
        print('   rows    - The number of rows on your LCD, e.g. 2')
        print('   rs      - RS pin number')
        print('   rw      - RW pin number. Default: None')
        print('   e       - E pin number')
        print('   bl      - Backlight pin number. Default: None')
        print('   data    - Data (d0-d7) gpio pin numbers, 4 or 8 numbers depending')
        print('             on if you want 4 or 8 bit mode, separated by commas.')
        print('             Example: data=1,2,3,4,5,6,7,8 (for 8-bit mode)')
        print('                      data=5,6,7,8 (for 4-bit mode)')
        print('   charmap - Which character map to use. Either A00 or A02. If your display')
        print('             contains Japanese characters, it probably uses the A00 charmap,')
        print('             otherwise A02. Default: A00')
        print('')
        print('Example:')
        print('')
        print(
            sys.argv[0] + ' gpio testsuite cols=20 rows=4 mode=BCM rs=15 rw=None e=16 '
            'bl=None data=21,22,23,24 charmap=A00'
        )
    # Options for PIGPIO mode
    elif (len(sys.argv) > 1) and (sys.argv[1] == 'pigpio'):
        print('<options> pigpio options:')
        print('')
        print('   host    - Host name of the Pi on which the pigpio daemon is running.')
        print('             Default: $PIGPIO_ADDR or localhost')
        print('   port    - Port number on which the pigpio daemon is listening.')
        print('             Default: $PIGPIO_PORT or 8888')
        print('   cols    - The number of columns on your LCD, e.g. 16')
        print('   rows    - The number of rows on your LCD, e.g. 2')
        print('   rs      - RS pin number')
        print('   rw      - RW pin number. Default: None')
        print('   e       - E pin number')
        print('   bl      - Backlight pin number. Default: None')
        print('   data    - Data (d0-d7) gpio pin numbers, 4 or 8 numbers depending')
        print('             on if you want 4 or 8 bit mode, separated by commas.')
        print('             Example: data=1,2,3,4,5,6,7,8 (for 8-bit mode)')
        print('                      data=5,6,7,8 (for 4-bit mode)')
        print('   charmap - Which character map to use. Either A00 or A02. If your display')
        print('             contains Japanese characters, it probably uses the A00 charmap,')
        print('             otherwise A02. Default: A00')
        print('')
        print('Note:')
        print('')
        print('Please start the pigpio daemon before running the tests.')
        print('')
        print('Example:')
        print('')
        print(
            sys.argv[0] + ' pigpio testsuite cols=20 rows=4 rs=15 rw=None e=16 '
            'bl=None data=21,22,23,24 charmap=A00'
        )
    else:
        print('<options> For info about options run:')
        print('')
        print('   %s i2c' % sys.argv[0])
        print('   %s gpio' % sys.argv[0])
        print('   %s pigpio' % sys.argv[0])
        print('')
    if error is not None:
        print('\nError: ' + error)
    sys.exit(1)


def options_pop(value, default=no_default):
    """Pops value from options with error checking
    value: which option to pop and check.
    default: optional, sets a default if not defined.
    returns: a string corresponding to the option on the command line
    """
    global options
    try:
        # If no default value is defined
        if default is no_default:
            return_value = options.pop(value)
        else:
            return_value = options.pop(value, default)
    except KeyError:
        print_usage('Option %s is not defined.' % value)
    except ValueError as e:
        print_usage('The value for %s is not valid.\n%s' % (value, e))
    except Exception as e:
        raise e
    if return_value == '':
        print_usage("Option %s can't be blank." % value)
    return return_value


def run():
    if len(sys.argv) < 3:
        print_usage()

    lcdmode = sys.argv[1]
    test = sys.argv[2]

    # Parse options into a dictionary
    global options
    try:
        options = dict([arg.split('=', 1) for arg in sys.argv[3:]])
    except ValueError:
        print_usage('Malformed option detected, must be in the form option=value')

    # Common options
    cols = int(options_pop('cols'))
    rows = int(options_pop('rows'))
    charmap = options_pop('charmap', 'A00')
    if lcdmode == 'i2c':
        from RPLCD import i2c

        if len(sys.argv) < 5:
            print_usage()

        # i2c options, pop all required options, pass remaining options to expander_params
        i2c_expander = options_pop('expander')
        address = int(options_pop('addr'), 16)
        port = int(options_pop('port', '1'))
        try:
            lcd = i2c.CharLCD(
                i2c_expander,
                address,
                port=port,
                charmap=charmap,
                cols=cols,
                rows=rows,
                expander_params=options,
            )
        except IOError:
            print_usage(
                'IOError: Usually caused by the wrong i2c address/port '
                'or device not connected properly'
            )
    elif lcdmode == 'gpio':
        import RPi.GPIO as GPIO
        from RPLCD import gpio

        if len(sys.argv) < 8:
            print_usage()

        # gpio options
        mode = options_pop('mode')
        if mode == 'BCM':
            numbering_mode = GPIO.BCM
        elif mode == 'BOARD':
            numbering_mode = GPIO.BOARD
        else:
            print_usage('Invalid GPIO numbering mode: %s, must be either BOARD or BCM' % mode)

        data = options_pop('data')
        rs = int(options_pop('rs'))
        e = int(options_pop('e'))
        rw = options_pop('rw', 'None')
        rw = None if rw == 'None' else int(rw)
        bl = options_pop('bl', 'None')
        bl = None if bl == 'None' else int(bl)

        # Parse data pins into a list
        pins_data = {}
        pins_data = data.split(',')
        # Convert data pins to int
        pins_data = [int(pin) for pin in pins_data]
        lcd = gpio.CharLCD(
            pin_rs=rs,
            pin_rw=rw,
            pin_e=e,
            pins_data=pins_data,
            pin_backlight=bl,
            numbering_mode=numbering_mode,
            cols=cols,
            rows=rows,
            charmap=charmap,
        )
    elif lcdmode == 'pigpio':
        from pigpio import pi
        from RPLCD import pigpio

        if len(sys.argv) < 7:
            print_usage()

        # pigpio options
        host = options_pop('host')
        port = options_pop('port')
        if host == 'None':
            pi = pi()
        elif port == 'None':
            pi = pi(host)
        else:
            pi = pi(host, port)

        data = options_pop('data')
        rs = int(options_pop('rs'))
        e = int(options_pop('e'))
        rw = options_pop('rw', 'None')
        rw = None if rw == 'None' else int(rw)
        bl = options_pop('bl', 'None')
        bl = None if bl == 'None' else int(bl)

        # Parse data pins into a list
        pins_data = {}
        pins_data = data.split(',')
        # Convert data pins to int
        pins_data = [int(pin) for pin in pins_data]
        lcd = pigpio.CharLCD(
            pi,
            pin_rs=rs,
            pin_rw=rw,
            pin_e=e,
            pins_data=pins_data,
            pin_backlight=bl,
            cols=cols,
            rows=rows,
            charmap=charmap,
        )
    else:
        print_usage(
            'Connection type %s is not supported. Must be either i2c, gpio or pigpio' % lcdmode
        )

    # Run selected test
    if test == 'show_charmap':
        show_charmap.run(lcd, rows, cols)
    elif test == 'testsuite':
        if cols == 20 and rows == 4:
            testsuite_20x4.run(lcd)
        elif cols == 16 and rows == 2:
            testsuite_16x2.run(lcd)
        else:
            print_usage('%sx%s displays are not supported in this test.' % (cols, rows))
    else:
        print_usage("Test '%s' is not supported." % test)
