"""
from mbedrpc import *

serdev = '/dev/tty.usbmodem1102'
s = serial.Serial(serdev)
mbed = SerialRPC(serdev, 9600)
"""
from asyncio.windows_events import NULL
from tkinter import mainloop
import serial
import threading
import time 
shoot = False
ser = NULL
import pickle

def toShoot(rawInput):
    """
    Determines the value of shoot off of mbedInput
    Input: 
    rawInput (bytes[]) : the raw bytes sent from mbed
    """
    strInput = str(rawInput)
    
    shootChar = strInput[2]
    #print(shootChar)
    if shootChar == "0":
        shoot = False
    else:
        shoot = True
    return shoot


def serialInit():
    global shoot
    global ser
    shoot = False
    ser = serial.Serial()
    ser.baudrate = 115200
    #ser.port = '/dev/tty.usbmodem1102'
    ser.port = 'COM8'
    ser.open()

def main():
    serialInit()
    x = threading.Thread(target = threadSerial(), args = (), daemon= True )
    x.daemon = True
    x.start()

    print("Hello world")
    

   

def threadSerial():
    while(1):
        rawInput = ser.read(1)
        #print(rawInput)
        shoot = toShoot(rawInput)

        
        print(shoot)
        with open('file.pkl', 'wb') as file:
      
        # A new file will be created
            pickle.dump(shoot, file)
        
if __name__ == "__main__":
    main()
    print("Hellow World")
    
    #mainLoop()



