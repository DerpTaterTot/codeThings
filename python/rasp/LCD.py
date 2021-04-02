import Adafruit_CharLCD as LCD
import time

lcd = LCD.Adafruit_CharLCD(18, 23, 4, 17, 27, 22, 16, 2, 4)

msg = "HOME"

lcd.message(msg)

try:
    while True:
        end = len(msg)
        location = 0
        while 16 - end > 0:sudo 
            lcd.move_right()
            location += 1
            time.sleep(0.5)
            end += 1
        while location != 0:
            lcd.move_left()
            location -= 1
            time.sleep(0.5)

except KeyboardInterrupt:
    lcd.clear()


