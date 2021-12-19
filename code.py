# @MTBMaker lab addressable RGB LED example  
# Example uses Trinket M0 and a 5mm through hole (breadboard friendly) neopixel
# cycle through RGB colors, withs a short pause
import time
import board
import neopixel

pixelPin = board.A4
numPixels = 1
singleNeo = neopixel.NeoPixel(pixelPin, numPixels, brightness=0.2)

#5mm Neopixel is GRB (not RGB). Change as needed for other LED configurations
RED = (0,255,0)
BLUE = (0,0,255)
GREEN = (255,0,0)

pauseDuration = 2

while True:
    singleNeo.fill(RED)
    singleNeo.show()
    time.sleep(pauseDuration)
    singleNeo.fill(BLUE)
    singleNeo.show()
    time.sleep(pauseDuration)
    singleNeo.fill(GREEN)
    singleNeo.show()
    time.sleep(pauseDuration)