import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

en = 11
in1 = 8
in2 = 7

GPIO.setup(en,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)


pwm = GPIO.PWM(en,500)
pwm.start(0)

def Clockwise():
    GPIO.output(in1,False)
    GPIO.output(in2,True)
    
def CounterClockwise():
    GPIO.output(in1,True)
    GPIO.output(in2,False)
def Speed(s):
   pwm.ChangeDutyCycle(s)
   
#Clockwise()
Speed(0)