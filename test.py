from RPLCD.i2c import CharLCD
c = CharLCD(0x27, rows=4, cols=16)
c.write_string('abcdefghijklmnopqrstuvwxyz')
c.close()
