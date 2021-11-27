import time
from Led import *
led=Led()

try:
    led.ledIndex(0x01,255,0,0)      #Red
    led.ledIndex(0x02,255,125,0)    #orange
    led.ledIndex(0x04,255,255,0)    #yellow
    led.ledIndex(0x08,0,255,0)      #green
    led.ledIndex(0x10,0,255,255)    #cyan-blue
    led.ledIndex(0x20,0,0,255)      #blue
    led.ledIndex(0x40,128,0,128)    #purple
    led.ledIndex(0x80,255,255,255)  #white'''
    print ("The LED has been lit, the color is red orange yellow green cyan-blue blue white")
    time.sleep(10)               #wait 3s
    led.colorWipe(led.strip, Color(0,0,0))  #turn off the light
    print ("\nEnd of program")
except KeyboardInterrupt:
    led.colorWipe(led.strip, Color(0,0,0))  #turn off the light
    print ("\nEnd of program")