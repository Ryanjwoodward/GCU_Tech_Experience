
#! ---------------------------------------------------------------------------------------------------
#!  Author          |   Ryan Woodward
#!  Institution     |   Grand Canyon University
#!  Instructor      |   Prof. Bill Hughes
#!  Course          |   SWE452 - SDLC II
#!  Date            |   10-11-2023
#!  File            |   cycle_colored_lights.py
#! ---------------------------------------------------------------------------------------------------
#!  Description     |  
#!                  |
#!                  |
#! ---------------------------------------------------------------------------------------------------

#* ----------------------------------
#*          IMPORTS
#* ----------------------------------

from adafruit_circuitplayground.express import cpx      #? This import allows us to reference the LEDs and Buttons

#* ----------------------------------
#*      GLOBAL VARIABLES
#* ----------------------------------

cpx.pixels.brightness = 0.1                             #? Set LED Brightness to full
cpx.pixels.fill((0, 0, 0))                              #? Turn of all LEDs by Default
cpx.pixels.show()                                       #? Write above data to LEDs

#* ----------------------------------
#*          FUNCTIONS
#* ----------------------------------

def init_btn_leds():

    while True:                            # loop
        if cpx.button_b:                   # if button is pushed then everything in hanging indent is executed
            print("Button B Pressed!")     # prints text in the serial monitor
            cpx.pixels[0] = (255, 0, 0)    # sets a single neopixel to given color pixel[number] = (R,G,B)
            cpx.pixels[1] = (255, 0, 0)
            cpx.pixels[2] = (255, 0, 0)
            cpx.pixels[3] = (255, 0, 0)
            cpx.pixels[4] = (255, 0, 0)
        if cpx.button_a:                   # button is pushed
            print("Button A Pressed!")
            cpx.pixels[5] = (0, 0, 255)
            cpx.pixels[6] = (0, 0, 255)
            cpx.pixels[7] = (0, 0, 255)
            cpx.pixels[8] = (0, 0, 255)
            cpx.pixels[9] = (0, 0, 255)
        if not(cpx.button_a or cpx.button_b):
            cpx.pixels.fill((0, 0, 0))              # will turn the lights off when buttons arent pressed

        cpx.pixels.show()                       # sends accumulated data to pixels

#* ----------------------------------
#*          ENTRY POINT
#* ----------------------------------
init_btn_leds()