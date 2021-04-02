import time
import RPi.GPIO as GPIO

class FourSeg():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

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
        for index in range(4):
            c=st[index]
            self.renderChar(c,index)

    def test(self):
        st = 'Good'
        while True:
            self.render4chars(st)
            time.sleep(0.001)
    
    def renderSentence(self, sentence):
        while True:
            i = 0
            while i < len(sentence):
                for _ in range(200):
                    self.render4chars(sentence[i:i+4])
                    time.sleep(0.01)
                i += 4

    def niceExit(self):
        GPIO.output(list(self.pins.values()), GPIO.LOW)
        print("Goodbye")

if __name__ == '__main__':
    try:
        fseg = FourSeg()
    #    fseg.test()
        while True:
            for integer in range(10000):
                a = format(integer, ' 4d')
#                print('number:', a)
                for _ in range(100):
                    fseg.render4chars(a)
                    time.sleep(0.01)

    except KeyboardInterrupt:
        fseg.niceExit()
    finally:
        GPIO.cleanup()