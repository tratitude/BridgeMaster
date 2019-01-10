import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

9G = 7

GPIO.setup(9G,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(5.9)

def Left():
    p.ChangeDutyCycle(4)
def Right():
    p.ChangeDutyCycle(8)
def Balance():
    p.ChangeDutyCycle(5.9)
   
    
