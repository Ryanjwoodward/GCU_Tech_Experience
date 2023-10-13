
"""
    AUTHOR: Ryan Woodward

    Use this file to validate the setup of Circuit PY

    It just blinks several LEDs Purple infinitely

"""

# Import the necessary library
from adafruit_circuitplayground.express import cpx
import time

# Set LED Brightness
cpx.pixels.brightness = 0.1

# Define the color (purple) and the number of blinks
purple = (128, 0, 128)
num_blinks = 3

while True:
    for _ in range(num_blinks):
        # Turn on LEDs 0, 2, 4, 5, 7, and 9
        cpx.pixels[0] = purple
        cpx.pixels[2] = purple
        cpx.pixels[4] = purple
        cpx.pixels[5] = purple
        cpx.pixels[7] = purple
        cpx.pixels[9] = purple
        cpx.pixels.show()

        # Wait for a brief duration
        time.sleep(0.75)

        # Turn off all LEDs
        cpx.pixels.fill((0, 0, 0))
        cpx.pixels.show()

        # Wait for another brief duration
        time.sleep(1)

    # Sleep for 3 seconds before repeating the pattern
    time.sleep(3)
