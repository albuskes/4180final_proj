# ECE 4180 Final Project : Movement-based Controller
### Arthur Buskes and Saikanam Siam
Our movement-based control system allows users to control a character in a videogame without using the conventional joystick and buttons. This opens the doors to play videogames for disabled folks without the physical body parts to operate a standard video game controller or the fine motor skills required. The idea started as just the accelerometer aspect, which would be used to activate a "throwing" motion for a Pokemon game. However, the project evolved to include motion detection to embody more of an "embedded systems" idea. In addition, this improved controller will allow more functionality and expanded purpose for the disabled.

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
  - ....
- Raspberry Pi with
-   .....
## Pinouts and Diagrams


-----
# Source Code Guide
-----
# Set up Instructions
## Part 0: Network
1. Ensure all devices are connected to the same network (preferably a hotspot or other variety of more "private" network)
## Part 1: Raspberry Pi (Server)
1. Download the Raspberry Pi sourcecode 
1. Connect Raspberry Pi to a computer screen
2. Run the file called (LINK)

## Part 2: Mbed to Pygame connection
1. Ensure that you have downloaded the windows driver onto the mbed to allow opening a COM port (follow instructions at https://os.mbed.com/handbook/Windows-serial-configuration)
2. Plug in mbed to computer
3. Download the mbed code file (INSERT LINK HERE) to the mbed and run it
4. Check which port is being used (for windows, check the device manager and look under "ports") and make note of it

## Part 3: Connect Phone
1. Download the Adafruit Bluefruit Connector app 
2. Connect to the Bluefruit device on your mbed
3. Go to the Controller tab and turn on Accelerometer

## Part 4: Run Pygame
1. Make sure to have Python 3.x downloaded
2. Download source code files for the game
3. Connect the game via TCP to the "Raspberry Pi" connection running the server on your network
4. Go to the code for the game and update the port (found in part 2) being used in the ____ fileINSERT CODE SECTION

----
# Video Demo 
----
# Conclusions
## Results
In the end, we had a functional motion-based controller. It stood to be considerably more difficult than expected in several areas, most notably: speed (latency), data transfer, and threading. 
## Future Work
- Expand movement-based functionality
  - Different hand motions = different "buttons"
- Option for doing button/throwing motion and movement with one hand only
- Fixing glitchiness of movement sensing
----
# Resources
- Inspiration taken from an open-source GitHub project
