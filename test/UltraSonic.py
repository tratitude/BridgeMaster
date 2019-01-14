import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 14
GPIO_ECHO = 15

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def Distance():
    GPIO.output(GPIO_TRIGGER,True)
    
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(GPIO_ECHO)==0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO)==1:
        StopTime = time.time()
    
    TimeElasped = StopTime-StartTime
    distance = (TimeElasped*34300)/2
    
    return distance

    
#try:
 #   while True:
  #      dist = Distance()
   #     print("Measured Distance = %.1f cm" %dist)
    #    time.sleep(1)

#except KeyboardInterrupt:
 #   print("Measurement stop by user")
  #  GPIO.cleanup()
