from machine import Pin, TouchPad
from neopixel import NeoPixel
from time import sleep

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, 10)

touchPin = TouchPad(Pin(14))

color_off = (0,0,0)
color_on = (20,20,0)


while True:
    # t.read() liefert Wert zwischen ca 100 (berührt) und 1000 (frei)
    numLeds = (1000 - touchPin.read()) / 100
    for iLed in range(len(np)):
        if iLed <= numLeds:
            np[iLed] = color_on
        else:
            np[iLed] = color_off
        np.write()
