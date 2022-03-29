from machine import Pin, TouchPad
from neopixel import NeoPixel
from time import sleep

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, 10)

touchPin = TouchPad(Pin(14))

color_off = (0,0,0)
color_on = (20,20,0)
color_start = (40,0,0)

ledCount = len(np)
iLed = 1

while True:
    correctTouchState = True
    np[0] = color_start
    np.write()
    sleep(1)
    np[0] = color_off
    speed = 3
    
    while correctTouchState:
        for i in range(0, 2*ledCount):
            np[iLed] = color_off

            iLed = i
            if iLed >= ledCount:
                iLed = 2*ledCount - i - 1
                            
            np[iLed] = color_on
            np.write()
            
            if iLed == 0 and touchPin.read() > 500:
                correctTouchState = False
                break
            if iLed == ledCount-1 and touchPin.read() < 500:
                correctTouchState = False
                break
            
            sleep(1/speed)
        speed *= 1.5

