import time
from RPLCD.i2c import CharLCD
from RPLCD import common
c = CharLCD(0x27, rows=4, cols=16)
#c.clear()
#for char in 'abcdefghijklmnopqrstuvwxyz0123456789':
#    c._send(ord(char), common.RS_DATA)
c.write_string('abcdefghijklmnopqrstuvwxyz0123456789')
#timeout = 0.0025
#for i in xrange(10000):
#    time.sleep(timeout)
#    c.backlight_enabled = False
#    time.sleep(timeout)
#    c.backlight_enabled = True
c.close()
