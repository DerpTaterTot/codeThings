import RPi.GPIO as GPIO
import time
import sys

red = 0x00FFFF
green = 0xFF00FF
blue = 0xFFFF00
custom = 0x4285F4
custom2 = 0xFBBC05

custom=0xffffff-int(sys.argv[1],16)
custom2=0xffffff-int(sys.argv[2],16)

R = 13
G = 19
B = 26

pins=[]

def setup(Rpin, Gpin, Bpin):
	global p_R, p_G, p_B
	pins = {'pin_R': Rpin, 'pin_G': Gpin, 'pin_B': Bpin}
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
	for i in pins:
		GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
		GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led
	
	p_R = GPIO.PWM(pins['pin_R'], 1000)  # set Frequece to 2KHz
	p_G = GPIO.PWM(pins['pin_G'], 1000)
	p_B = GPIO.PWM(pins['pin_B'], 1000)
	
	p_R.start(100)      # Initial duty Cycle = 100(leds off)
	p_G.start(100)
	p_B.start(100)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def off():
    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)

def setColor(col):   # For example : col = 0x112233
	R_val = (col & 0xff0000) >> 16
	G_val = (col & 0x00ff00) >> 8
	B_val = (col & 0x0000ff) >> 0

	R_val = map(R_val, 0, 255, 0, 100)
	G_val = map(G_val, 0, 255, 0, 100)
	B_val = map(B_val, 0, 255, 0, 100)
	
	p_R.ChangeDutyCycle(100-R_val)     # Change duty cycle
	p_G.ChangeDutyCycle(100-G_val)
	p_B.ChangeDutyCycle(100-B_val)

def loop():
	while True:
		setColor(custom)
		print('custom1')
		time.sleep(1)
		setColor(custom2)
		print('custom2')
		time.sleep(1)

def destroy():
	p_R.stop()
	p_G.stop()
	p_B.stop()
	off()
	GPIO.cleanup()


if __name__ == "__main__":
	try:
		print(sys.argv[1])
		setup(R, G, B)
		loop()
	except KeyboardInterrupt:
		destroy()
        