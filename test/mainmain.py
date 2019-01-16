import RPi.GPIO
import Components.Servo as Servo
import Components.UltraSonic as Sonic
import Components.DC_Motor as DCM
import time

RPi.GPIO.setwarnings(False)
WHEEL = DCM.DC_Motor(17, 27, 22)
SENSOR = Sonic.Ultra_Sonic(23, 24)
SEESAW = Servo.Seesaw(4, 7.5, 4.5, 6)

#SEESAW.seesaw_servo.Angle(0)
#def Deal_Card_Random():

def clean_gpio():
    RPi.GPIO.cleanup()
    exit()
    
#clean_gpio()

def seesaw_test():
    while (True):
        SEESAW.Turn(-1)
        time.sleep(1)
        SEESAW.Turn(0)
        time.sleep(1)
        SEESAW.Turn(1)
        time.sleep(1)
        SEESAW.Turn(0)
        time.sleep(1)


High_Speed = 100
Low_Speed = 60
Diff_Speed = 0.1
V = High_Speed

while (True):
    
    WHEEL.Speed(V)
    #print(SENSOR.Distance())
    if SENSOR.Distance()<7:
        time.sleep(0.4)
        WHEEL.CCW()
        SEESAW.Turn(-1)
        V = High_Speed
        time.sleep(0.5)
        SEESAW.Turn(0)
        time.sleep(0.5)
        
    else:
        WHEEL.CW()
        SEESAW.Turn(0)
        V = max(V-Diff_Speed, 0)
            
    #time.sleep(0.01)
    """
    a = input()
    if a == 'z':
        WHEEL.CW()
    elif a == 'x':
        WHEEL.CCW()
    else:
        WHEEL.Speed(int(a))
    """

clean_gpio()
#seesaw_test()
#process()

RPi.GPIO.cleanup()
