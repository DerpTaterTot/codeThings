import RPi.GPIO as GPIO
from time import sleep

ledRED = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledRED, GPIO.OUT)


GPIO.output(ledRED, GPIO.HIGH)
sleep(10)
GPIO.output(ledRED, GPIO.LOW)