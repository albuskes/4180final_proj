from mbedrpc import *

serdev = '/dev/tty.usbmodem1102'
s = serial.Serial(serdev)
mbed = SerialRPC(serdev, 9600)
f.read()

