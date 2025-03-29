#!/usr/bin/env python
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


def run(lcd, rows, cols):
    print('This tool shows the character map of your LCD on the display.')
    print('Press ctrl+c at any time to abort.\n')

    page = 0
    chars = rows * cols
    text_tpl = 'Displaying page %d (characters %d-%d). Press <ENTER> to continue.'

    try:
        while True:
            offset = page * chars
            start = offset
            end = offset + chars
            lcd.clear()
            for i in range(offset, offset + chars):
                if i > 255:
                    if i > start:
                        input(text_tpl % (page + 1, start, i - 1))
                    else:
                        pass
                    sys.exit(0)
                lcd.write(i)
            input(text_tpl % (page + 1, start, end - 1))
            page += 1
    except KeyboardInterrupt:
        print('Aborting.')
    finally:
        lcd.clear()
        try:
            lcd.backlight_enabled = False
        except ValueError:
            pass
        lcd.close()
        print('Test done. If you have a programmable backlight, it should now be off.')


if __name__ == '__main__':
    print('This is a submodule of `rplcd-tests`, please run it instead.')
