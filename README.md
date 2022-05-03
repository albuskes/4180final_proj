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
- [Conclusions](#conclusions)

-----
# Project Basics
## Components
- 1x mbed (LPC1768)
- 1x uLCD
- 1x Adafruit Bluefruit
- 1x Raspbery Pi (Server)
- 2x Computers
- 1x Webcam
- 1x Phone with Bluefruit Connect app
## Software
- Python version 3.9 with libraries
  - Pyserial 
  - ....
- Raspberry Pi with
-   .....
## Pinouts and Diagrams
A block diagram has been provided below. 
![plot](./block_diagram_words.png)
We have also provided the appropriate wiring for componenets interactingn with mbed. This will need to be placed on a breadboard with the mbed. 

<b>uLCD</b>
uLCD | mbed | 
--- | --- | 
Seconds | 301 | 

<b>Bluetooth module</b>
Bluetooth | mbed | 
--- | --- | 
Seconds | 301 | 


-----
# Source Code Guide
-----
# Set up Instructions
## Part 0: Network
1. Ensure all devices are connected to the same network (preferably a hotspot or other variety of more "private" network)
## Part 1: Raspberry Pi (Server)
1. Download the Raspberry Pi sourcecode 
1. Connect Raspberry Pi to a computer screen
2. Run the file called handcount.py

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
In the end, we had a functional motion-based controller. It stood to be considerably more difficult than expected in several areas, most notably: speed (latency), data transfer, networking capabilities, and threading. It took a non-trivial amount of time to adjust the game to allow it to run appropriately while still recieving data from both the mbed via serial and the Raspberry Pi via the TCP server. There were also some glitches we never worked out -- there were issues with some library compatibility issues on the mbed side, and threads had to be removed. Unfortunately, this did affect the speed and the amount of capabilities we could do with the mbed (hence the more simplistic stats printed). We fixed a large part of the latency issues by increasing the baud rate of the serial connection from the mbed to computer. However, this introduced some new issues where firing would occur more than once for one phone movement. We remedied this by adding a small wait time to when we sampled the serial input to check for a signal (other ideas we had included variations of polling, but the other method worked better). Overall though, we worked through these issues to provide a near-finished product. While some deviation from the original proposal occurred, this was partly to orient the design more towards an "embedded system," and partly to add some more complexity. The main features of motion control were kept and improved, and the features that required the mbed directly were retained, all except the speaker (which we moved to be just on the computer, in part due to the threading issues on mbed side) and IMU. We ended up using the phone accelerometer instead of the IMU, since the IMU had substantial issues with accuracy. This was a very informative and successsful project overall, especially considering we only had two people to work on it. Some big takeways were that building interconnected systems, especially when they recieve data from different sources, presents many difficulties, and that flexibility and adaptability is very important when working with potentially unforeseen issues.
## Future Work
- Expand movement-based functionality
  - Different hand motions = different "buttons"
- Option for doing button/throwing motion and movement with one hand only
- Fixing occasional glitchiness of movement sensing
- Create some kind of "glove" or other attachment with which to secure phone
- Experiment with designs that use higher-quality IMU than what was available in the lab kits
- Expand into multi-player features
- Improve so that client/servers can be on different networks and still communicate
- Optimize data transfer -- is there a better way to transmit the data than via serial? Or, if still using serial, is there a better way to encode data?

