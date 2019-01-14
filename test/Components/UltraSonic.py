import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

class Ultra_Sonic():
    def __init__(self, TRIGGER_PIN, ECHO_PIN):
        self.trigger = TRIGGER_PIN
        self.echo = ECHO_PIN
        
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)


    def Distance(self):
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)
        
        StartTime = time.time()
        StopTime = time.time()
        
        while GPIO.input(self.echo) == 0:
            StartTime = time.time()
            #print('test')
        while GPIO.input(self.echo) == 1:
            StopTime = time.time()
        
        TimeElapsed = StopTime-StartTime
        distance = (TimeElapsed*34300)/2
        
        return distance

"""	
try:
    sonic = Ultra_Sonic(23, 24)
   # print("1")
    while True:
       # print("2")
        dist = sonic.Distance()
        #print("3")
        print("Measured Distance = %.1f cm" %dist)
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stop by user")
    GPIO.cleanup()
"""
