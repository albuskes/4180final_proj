# ECE 4180 Final Project : Movement-based Controller
### Arthur Buskes and Saikanam Siam
Our movement-based control system allows users to control a character in a videogame without using the conventional joystick and buttons. This opens the doors to play videogames for disabled folks without the physical body parts to operate a standard video game controller or the fine motor skills required. The idea started as just the accelerometer aspect, which would be used to activate a "throwing" motion for a Pokemon game. 

-----
# Table of Contents
- [Intro](#ece-4180-final-project--movement-based-controller)
- [Project Basics](#project-basics)
- [Source Code Guide](#source-code-guide)
- [Set up Instructions](#set-up-instructions)
- [Video Demo](#video-demo)
- [Future Work](#future-work)

-----
# Project Basics
## Components
- mbed (LPC1768)
- Raspbery Pi (Server)
- Computer running python game (Client)
- Adafruit Bluefruit
- Webcam
- Phone with Bluefruit Connect app
## Software
- Python version 3.9 with libraries
  - Pyserial
## Pinouts and Diagrams


-----
# Source Code Guide
-----
# Set up Instructions
## Part 1: Raspberry Pi (Server)
1. Connect Raspberry Pi to a computer screen
2. Connect webcame to Raspberry Pi
3. Run _______
## Part 2: Computer to Run Pygame
1. Make sure to have Python 3.x and run the game
## Part 3: Mbed to Pygame connection
This step is focused on connecting the mbed to the python game. This is used to detect shooting via a "throwing" motion. 
1. Ensure that you have downloaded the windows driver onto the mbed to allow opening a COM port (follow instructions at https://os.mbed.com/handbook/Windows-serial-configuration)
2. Plug in mbed to computer
3. Download the mbed code file (INSERT LINK HERE) to the mbed and run it
4. Check which port is being used (for windows, check the device manager and look under "ports")
6. Go to the code up update the port being used INSERT CODE SECTION
## Part 4: Phone
Here, we connect the phone to the mbed via bluetoth so we can read from the phone's accelerometer. 
1. Download the Adafruit Bluefruit Connector app 
2. Connect to the Bluefruit device on your mbed
3. Go to the Controller tab and turn on Accelerometer
----
# Video Demo 
----
# Future Work
- Expand movement-based functionality
  - Different hand motions = different "buttons"
- Option for doing button/throwing motion and movement with one hand only
- Fixing glitchiness of movement sensing
----
# Resources
- Inspiration taken from an open-source GitHub project
