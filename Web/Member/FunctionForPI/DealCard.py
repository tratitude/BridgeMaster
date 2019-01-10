import RPi.GPIO as GPIO
import time
import UltraSonic as US
import ServoWheel as SW
import Servo_9G as S9
import BarcodeScanner as BB


GPIO.setmode(BOARD)
thread1 = threading.Thread(target = BB.GetCode,args=())
thread2 = threading.Thread(target = BB.Scan,args=())
thread1.start()

suits[4] = {'spade','heart','diamond','club'}
number[13] = {'1','2','3','4','5','6','7','8','9','A','B','C','D'}
try:
    while True:
        SW.Clockwise()
        SW.Speed(70)
        while US.Distance()<7:
            SW.CounterClockwise()
            SW.Speed(50)
            while BB.code==None:
                BB.Scan()
#Spade=MGX1,Heart=MGX2,Diamond=MGX3,Club=MGX4 ,X = number
            
            
            