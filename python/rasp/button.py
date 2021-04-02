import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    if GPIO.input(15) == GPIO.HIGH:
        print(1)
    else:
        print(0)
    time.sleep(0.1)