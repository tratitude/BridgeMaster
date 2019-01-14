import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class DC_Motor():
    def __init__(self, ENABLER, OUT_PIN1, OUT_PIN2):
        self.en = ENABLER
        self.out_1 = OUT_PIN1
        self.out_2 = OUT_PIN2

        GPIO.setup(self.en, GPIO.OUT)
        GPIO.setup(self.out_1, GPIO.OUT)
        GPIO.setup(self.out_2, GPIO.OUT)

        self.pwm = GPIO.PWM(self.en, 500)
        self.pwm.start(100)
        self.pwm.ChangeDutyCycle(0)

    def CW(self):
        GPIO.output(self.out_1, True)
        GPIO.output(self.out_2, False)
        
    def CCW(self):
        GPIO.output(self.out_1, False)
        GPIO.output(self.out_2, True)

    def Speed(self, s):
        self.pwm.ChangeDutyCycle(s)
   
