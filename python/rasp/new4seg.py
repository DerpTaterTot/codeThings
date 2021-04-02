import time
import RPi.GPIO as GPIO
from datetime import datetime

class FourSeg():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        segments =  (3,22,0,9,10,4,5,11)
        for segment in segments:
            GPIO.setup(segment, GPIO.OUT)
            GPIO.output(segment, 0)

        # GPIO ports for the digit 0-3 pins 
        self.digits = (2,17,27,6)
        for digit in self.digits:
            GPIO.setup(digit, GPIO.OUT)
            GPIO.output(digit, 1)

        self.digitBitmap = { '0': 0b00111111, '1': 0b00000110, '2': 0b01011011, '3': 0b01001111, '4': 0b01100110, '5': 0b01101101, '6': 0b01111101, '7': 0b00000111, '8': 0b01111111, '9': 0b01100111, 'G': 0b0111101, 'o': 0b01011100, 'd': 0b01011110, 'J': 0b00011111, 'b': 0b01111100, ' ':0b00000000 }
        self.masks = { 'a': 0b00000001, 'b': 0b00000010, 'c': 0b00000100, 'd': 0b00001000, 'e': 0b00010000, 'f': 0b00100000, 'g': 0b01000000, '.': 0b10000000}
        self.pins = { 'a': 3, 'b': 22, 'c': 0, 'd': 9, 'e': 10, 'f': 4, 'g': 5, '.':11}

    def renderChar(self, c, dig):
        val = self.digitBitmap[c]
        GPIO.output(list(self.pins.values()), GPIO.HIGH)
        
        for k,v in self.masks.items():
            if val&v == v:
                GPIO.output(self.pins[k], GPIO.LOW)
        GPIO.output(self.digits[dig],1)
        time.sleep(0.001)
        GPIO.output(self.digits[dig],0)
    
    def render4chars(self,st):
        #print(st)
        for index in range(4):
            c=st[index]
            self.renderChar(c,index)

    def count(self):
        for x in range(10000):
            for _ in range(100):
                self.render4chars('{0:4d}'.format(x))
                time.sleep(0.01)

    def countv2(self):
        while True:
            x = 0
            while x < 10000:
                while GPIO.input(15) == GPIO.HIGH:
                    self.render4chars('{0:4d}'.format(x))
                    x += 1
                self.render4chars('{0:4d}'.format(x))

            


    def test(self):
        st = '1000'
        while True:
            self.render4chars(st)
            time.sleep(0.001)
    
    def renderTime(self):
        while True:
            now = datetime.now()
            currentTime = now.strftime('%H%M')
            self.render4chars(currentTime)

    def niceExit(self):
        GPIO.output(list(self.pins.values()), GPIO.LOW)
        print("Goodbye")

if __name__ == '__main__':
    try:
        fseg = FourSeg()
    #    fseg.test()
        fseg.countv2()


    except KeyboardInterrupt:
        fseg.niceExit()
    finally:
        GPIO.cleanup()