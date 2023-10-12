
#! ---------------------------------------------------------------------------------------------------
#!  Author          |   Ryan Woodward
#!  Institution     |   Grand Canyon University
#!  Date            |   10-11-2023
#!  File            |   cycle_colored_lights.py
#! ---------------------------------------------------------------------------------------------------
#!  Description     |   This Python script imports libraries and sets up variables for controlling 
#!                  |   LEDs on an Adafruit Circuit Playground Express. It defines a function 
#!                  |   init_light_cycle that cycles through RGB colors, applying them to LEDs one 
#!                  |   at a time, creating a dynamic lighting effect. When Button 'B' is pressed, 
#!                  |   the script triggers the light cycling effect and turns off all LEDs.
#! ---------------------------------------------------------------------------------------------------


#* ----------------------------------
#*          IMPORTS
#* ----------------------------------

import time                                             #? Provides us with time related operations (i.e. sleep)

from adafruit_circuitplayground.express import cpx      #? This import allows us to reference the LEDs and Buttons

#* ----------------------------------
#*      GLOBAL VARIABLES
#* ----------------------------------

number_of_leds = 10        #? Define the number of LEDs. There are 10 on the Adafruit Circuit Playground Express.
                                            
number_of_cycles = 1       #? Define how many cycles the application will perform for each button press

#? Define the colors the LEDs will become. These are defined in RGB format.
led_colors = [
    (255, 0, 0),      #? Red
    (255, 255, 0),    #? Yellow
    (0, 255, 0),      #? Green
    (0, 0, 255),      #? Blue
    (255, 0, 255)     #? Violet
]

#* ----------------------------------
#*          FUNCTIONS
#* ----------------------------------

"""
    The init_light_cycle function cycles through a set of RGB colors, 
    applying each color to individual LEDs one at a time. It repeats 
    this process a defined number of times, creating a dynamic lighting 
    effect with a brief pause between LED changes.
"""
def init_light_cycle():
    for _ in range(number_of_cycles):               #? Cycle Loop: repeats the rainbow sequence 'n' times.

        for color in led_colors:                    #? Color Loop: Iterates through the colors defined in 'led_colors' array

            for i in range(number_of_leds):         #? LED Loop: Cycles through each LED turning them on/off sequentially.

                cpx.pixels.fill((0, 0, 0))          #? Turns OFF all LEDs
                cpx.pixels[i] = color               #? Sets the LED at index 'i' to the current 'color' variable of the 'led_colors' array.
                cpx.pixels.show()                   #? Turns on the LED at index 'i' ON.
                time.sleep(0.1)                     #? Delay execution for 100 milliseconds

#* ----------------------------------
#*          ENTRY POINT
#* ----------------------------------
while True:                                 #? Infinite While Loop
    
    if cpx.button_b:                        #? Check if Button 'B' has been pressed

        init_light_cycle()                  #? Call Light Cycle Function
    
        cpx.pixels.fill((0, 0, 0))          #? Turns OFF all LEDs




