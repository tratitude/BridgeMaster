import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#♣♦♥♠
MATRIX = [
    ['S','H','D','C'],
    ['NT',  3,  6,  9],
    ['X',  2,  5,  8],
    [  0,  1,  4,  7]]

ROW = [ 6, 13, 19, 26]
COL = [12, 16, 20, 21]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 0)

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
def Read_Key():
    Key = -1
    while (Key==-1):
        for j in range(4):
            GPIO.output(COL[j],1)
            for i in range(4):
                if GPIO.input(ROW[i])==1:
                    Key = MATRIX[i][j]
                #time.sleep(0.01)    
            GPIO.output(COL[j],0)
    return Key    

"""
try:
    while (True):
        print (Read_Key())
        time.sleep(0.5)
except KeyboardInterupt:
    GPIO.cleanup()
"""

