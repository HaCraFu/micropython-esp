from machine import Pin
from neopixel import NeoPixel
from time import sleep

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, 10)
black = (0,0,0)
color=(20,20,0)

iLed = 0

for i in range(len(np)):
    np[iLed] = black
    iLed += 1
    if iLed > len(np):
        iLed = 0
    np[iLed] = color
    np.write()
    time.sleep(0.1)
    