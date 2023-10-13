//! ---------------------------------------------------------------------------------------------------
//!  Author          |   Ryan Woodward
//!  Institution     |   Grand Canyon University
//!  Instructor      |   Prof. Bill Hughes
//!  Course          |   SWE452 - SDLC II
//!  Date            |   10-11-2023
//!  File            |   leds_and_button.ino
//! ---------------------------------------------------------------------------------------------------
//!  Description     |  This code controls the LEDs on an Adafruit Circuit Playground board. When the 
//!                  |  left button is pressed, it lights up LEDs 0 to 4 in red, when the right button 
//!                  |  is pressed, it lights up LEDs 5 to 9 in blue, and if no button is pressed, it 
//!                  |  turns off all LEDs. The LED display is updated continuously to reflect these changes.
//! ---------------------------------------------------------------------------------------------------

//* ----------------------------------
//*          IMPORTS
//* ----------------------------------

#include <Adafruit_CircuitPlayground.h> 

//* ----------------------------------
//*          SETUP FUNCTION
//* ----------------------------------

void setup() {
  CircuitPlayground.begin();                           //? Initialize the Circuit Playground hardware.
  CircuitPlayground.setBrightness(255);                //? Set the brightness of the built-in LEDs to full (255).
}

//* ----------------------------------
//*          LOOP FUNCTION
//* ----------------------------------
void loop() {
  while (true) { 
    if (CircuitPlayground.leftButton()) {              //? Check if the left button on the Circuit Playground is pressed.
      for (int i = 0; i < 5; i++) {
        CircuitPlayground.setPixelColor(i, 255, 0, 0); //? Set LEDs 0-5 to the color Red.
      }
      CircuitPlayground.strip.show();                  //? Update the LED display to reflect the changes.
    }
    else if (CircuitPlayground.rightButton()) {        //? Check if the right button on the Circuit Playground is pressed.
 
      for (int i = 5; i < 10; i++) {
        CircuitPlayground.setPixelColor(i, 0, 0, 255); //? Set LEDs 6-9 to the color Blue
      }
      CircuitPlayground.strip.show();                  //? Update the LED display to reflect the changes.
    }
    else {
      CircuitPlayground.clearPixels();                 //? Turn off all LEDs 
      CircuitPlayground.strip.show();                  //? Update the LED display to reflect the changes.
    }
  }
}


