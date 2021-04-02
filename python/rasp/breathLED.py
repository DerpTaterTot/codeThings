import RPi.GPIO as GPIO
from time import sleep

ledPIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPIN, GPIO.OUT)
GPIO.output(ledPIN, GPIO.LOW)

pwm = GPIO.PWM(ledPIN, 1000)
pwm.start(0)

try:
	while True:
		for dc in range(0, 101, 4): # Increase duty cycle: 0~100   
			pwm.ChangeDutyCycle(dc ** 2 / 100)     # Change duty cycle
			sleep(0.1)
			
		for dc in range(100, -1, -4): # Decrease duty cycle: 100~0
			pwm.ChangeDutyCycle(dc ** 2 / 100)
			sleep(0.1)

except KeyboardInterrupt:
	pwm.stop()
	GPIO.output(ledPIN, GPIO.LOW)    # turn off all leds
	GPIO.cleanup()
