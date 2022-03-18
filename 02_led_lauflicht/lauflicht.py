from machine import Pin
from neopixel import NeoPixel
from time import sleep

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, 10)
color_off = (0,0,0)
color_on = (20,20,0)

iLed = 0

while True:
    for _ in range(len(np)):
        np[iLed] = color_off
        iLed += 1
        if iLed > len(np):
            iLed = 0
        np[iLed] = color_on
        np.write()
        sleep(0.1)