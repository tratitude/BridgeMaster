import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)



GPIO.setup(4,GPIO.OUT)

p = GPIO.PWM(4,50)
p.start(7)

def Left():
    p.ChangeDutyCycle(5)
def Right():
    p.ChangeDutyCycle(9)
def Balance():
    p.ChangeDutyCycle(7)
   
#Balance()
