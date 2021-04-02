from gpiozero import LED
from time import sleep

ledRED = LED(2)
ledGREEN = LED(4)
ledBLUE = LED(17)

sltime = 0.5

while True:
    ledBLUE.off()
    ledRED.on()
    sleep(sltime)

    ledRED.off()
    ledGREEN.on()
    sleep(sltime)

    ledGREEN.off()
    ledBLUE.on()
    sleep(sltime)
