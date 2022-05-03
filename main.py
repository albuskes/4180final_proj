import threading
import serial

def toShoot(rawInput):
    """
    Determines the value of shoot off of mbedInput
    Input: 
    rawInput (bytes[]) : the raw bytes sent from mbed
    """
    strInput = str(rawInput)
    shootChar = strInput[2]
    if shootChar == "1":
        shoot = True
    else:
        shoot = False
    return shoot;


def main():
    shoot = False
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = '/dev/tty.usbmodem1102'
    ser.open()

    while(1):
        rawInput = ser.read(1)
        print(rawInput)
        shoot = toShoot(rawInput)
        print(shoot)
        
if __name__ == "__main__":
    main()



