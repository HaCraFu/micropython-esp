from machine import Pin
from neopixel import NeoPixel
from time import sleep

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, 10)
color_off = (0,0,0)
color_on = (20,20,0)
 
ledCount = len(np)
iLed = 0

while True:
    for i in range(0, 2*ledCount):
        np[iLed] = color_off

        iLed = i
        if iLed >= ledCount:
            iLed = 2*ledCount - i - 1
            
        print(iLed)
        
        np[iLed] = color_on
        np.write()
        sleep(0.1)
