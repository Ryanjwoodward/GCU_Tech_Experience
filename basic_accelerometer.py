
#! ---------------------------------------------------------------------------------------------------
#!  Author          |   Ryan Woodward
#!  Institution     |   Grand Canyon University
#!  Instructor      |   Prof. Bill Hughes
#!  Course          |   SWE452 - SDLC II
#!  Date            |   10-11-2023
#!  File            |   basic_accelerometer.py
#! ---------------------------------------------------------------------------------------------------
#!  Description     |   This script employs the Adafruit Circuit Playground and its accelerometer to 
#!                  |   create a motion-sensitive lighting effect. It continuously monitors the 
#!                  |   accelerometer data in the X, Y, and Z axes and lights up LEDs (Red for X, 
#!                  |   Blue for Y, Green for Z) when the acceleration change exceeds a specified 
#!                  |   threshold. The LEDs turn off when there is no significant motion. 
#!                  |   This process repeats indefinitely with a short delay between updates.
#! ---------------------------------------------------------------------------------------------------

#* ----------------------------------
#*          IMPORTS
#* ----------------------------------

import time
from adafruit_circuitplayground import cp


#* ----------------------------------
#*         GLOBAL VARIABLES
#* ----------------------------------
cp.pixels.brightness = 0.1                 #? Set the brightness of the LEDs to Full
cp.pixels.fill((0, 0, 0))                  #? To begin the application turn the LEDs OFF
cp.pixels.show()                           #? Set the above settings to the LEDs

last_x, last_y, last_z = cp.acceleration   #? To begin the application set these to the current reading of the accelerometer
threshold = 2.0                            #? The threshold of change in the Axes in order for an LED to be set HIGH


#* ----------------------------------
#*        APPLICATION LOOP
#* ----------------------------------
while True:
    x, y, z = cp.acceleration               #? Read the x,y, and z axes and save them.

    if abs(x - last_x) > threshold:         #? Compares the Change in X to the Threshold. If Delta > Threshold Lights will be HIGH
        cp.pixels[0] = (255, 0, 0)          #? Set LED0 to Red
    else:
        cp.pixels[0] = (0, 0, 0)            #? Turn LED0 OFF

    if abs(y - last_y) > threshold:         #? Compares the Change in X to the Threshold. If Delta > Threshold Lights will be HIGH
        cp.pixels[1] = (0, 0, 255)          #? Turn LED1 to Blue
    else:
        cp.pixels[1] = (0, 0, 0)            #? Turn LED1 OFF

    if abs(z - last_z) > threshold:         #? Compares the Change in X to the Threshold. If Delta > Threshold Lights will be HIGH
        cp.pixels[2] = (0, 255, 0)          #? Turn LED2 to Green
    else:
        cp.pixels[2] = (0, 0, 0)            #? Turn LED2 OFF

    last_x, last_y, last_z = x, y, z        #? Assign the latest Axes readings to the previous variables.s

    time.sleep(0.1)
