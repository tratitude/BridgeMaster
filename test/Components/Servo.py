import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Servo():
    def __init__(self, PWM_PIN):
        self.pin = PWM_PIN
        GPIO.setup(self.pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(6)
        
    def Angle(self, x):
        self.pwm.ChangeDutyCycle(x)
        
        
class Seesaw():
    def __init__(self, PWM_PIN, LEFT_VAL, RIGHT_VAL, CENTER_VAL):
        self.seesaw_servo = Servo(PWM_PIN)
        self.left = LEFT_VAL
        self.right = RIGHT_VAL
        self.center = CENTER_VAL
        self.Turn(0)
        
    def Turn(self, x):
        if x==1:
            self.seesaw_servo.Angle(self.left)
        elif x==-1:
            self.seesaw_servo.Angle(self.right)
        else:
            self.seesaw_servo.Angle(10)
            self.seesaw_servo.Angle(self.center)
        
        
"""
    def Left():
        p.ChangeDutyCycle(4)
    def Right():
        p.ChangeDutyCycle(8)
    def Balance():
        p.ChangeDutyCycle(5.9)
"""
    
