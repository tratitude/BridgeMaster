import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

en = 29
in1 = 31
in2 = 33

GPIO.setup(en,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)

pwm = GPIO.PWM(en,500)
pwm.start(100)

def Clockwise():
    GPIO.output(in1,True)
    GPIO.output(in2,False)
    
def CounterClockwise():
    GPIO.output(in1,False)
    GPIO.output(in2,True)

def Speed(s):
   pwm.ChangeDutyCycle(s)
   