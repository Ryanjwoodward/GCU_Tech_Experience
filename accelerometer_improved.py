
#! ---------------------------------------------------------------------------------------------------
#!  Author          |   Ryan Woodward
#!  Institution     |   Grand Canyon University
#!  Instructor      |   Prof. Bill Hughes
#!  Course          |   SWE452 - SDLC II
#!  Date            |   10-11-2023
#!  File            |   cycle_colored_lights.py
#! ---------------------------------------------------------------------------------------------------
#!  Description     |   This script expands on the basic_accelerometer by detecting positive and 
#!                  |   negative changes and glow different LEDs for each axis' change in
#!                  |   positive or negative direction.
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
    x, y, z = cp.acceleration  # We are only interested in Y and Z

    #?               *** Y-AXIS  ***
    if y - last_y > threshold:      #? Check for positive change in Y axis.
        cp.pixels[4] = (0, 0, 255)  #? Positive change in Y, LED 4 turns blue
        cp.pixels[0] = (0, 0, 0)    #? Turn LED0 OFF (LED0 glows for negative changes)

    elif y - last_y < -threshold:   #? Check for Negative change in Y axis
        cp.pixels[0] = (0, 0, 255)  #? Negative change in Y, LED 0 turns blue
        cp.pixels[4] = (0, 0, 0)    #? Turn LED4 OFF (LED4 glows for positive changess)
    else:
        cp.pixels[0] = (0, 0, 0)    #? Turn both LED0 and LED4 OFF
        cp.pixels[4] = (0, 0, 0)

    #?               *** Z-AXIS  ***
    if z - last_z > threshold:      #? Check for positive changes in Z axis
        cp.pixels[9] = (0, 255, 0)  #? Positive change in Z, LED 9 turns green
        cp.pixels[5] = (0, 0, 0)    #? Turn off LED 5 (LED5 glows for negative changes)

    elif z - last_z < -threshold:   #? Check for negative changes in Z axis
        cp.pixels[5] = (0, 255, 0)  #? Negative change in Z, LED 5 turns green
        cp.pixels[9] = (0, 0, 0)    #? Turn off LED 9 (LED9 glows for positive changes)

    else:
        cp.pixels[5] = (0, 0, 0)    #? Turn both LED5 and LED9 OFF
        cp.pixels[9] = (0, 0, 0)

    #?               *** X-AXIS  ***
    if x - last_x > threshold:      #? Check for positive changes in X axis
        cp.pixels[2] = (255, 0, 0)  #? Positive change in X, LED 2 turns red
        cp.pixels[7] = (0, 0, 0)    #? Turn off LED 7

    elif x - last_x < -threshold:   #? Check for negative changes in X axis
        cp.pixels[7] = (255, 0, 0)  #? Negative change in X, LED 7 turns red
        cp.pixels[2] = (0, 0, 0)    #? Turn off LED 2
    else:
        cp.pixels[2] = (0, 0, 0)    #? Turn off LED2 and LED7
        cp.pixels[7] = (0, 0, 0)

    last_x, last_y, last_z = x, y, z    #? Set the current readings of the axes to the previous state variables

    time.sleep(0.1)
