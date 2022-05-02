"""
from mbedrpc import *

serdev = '/dev/tty.usbmodem1102'
s = serial.Serial(serdev)
mbed = SerialRPC(serdev, 9600)
"""
import serial

def toShoot(rawInput):
    """
    Determines the value of shoot off of mbedInput
    Input: 
    rawInput (bytes[]) : the raw bytes sent from mbed
    """
    strInput = str(rawInput)
    shootChar = strInput[2]
    if shootChar == "F":
        shoot = False
    else:
        shoot = True
    return shoot;


def main():
    shoot = False
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = '/dev/tty.usbmodem1102'
    ser.open()

    while(1):
        rawInput = ser.readline()
        shoot = toShoot(rawInput)
        print(shoot)
        
if __name__ == "__main__":
    main()



