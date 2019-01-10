import RPi.GPIO as GPIO
import time
import threading


GPIO.setmode(GPIO.BOARD)

BB = 35

GPIO.setup(BB,GPIO.OUT)

def Scan():
    time.sleep(1)
    GPIO.output(BB,True)
    time.sleep(1)
    GPIO.output(BB,False)
    time.sleep(0.1)
  
    
def GetCode():
    while True:
        code = input("Code:")
        print(code)
        time.sleep(1)
        
    
#thread1 = threading.Thread(target = GetCode,args=())
#thread2 = threading.Thread(target = Scan,args=())

#thread1.start()
#time.sleep(1)
#thread2.start()
#thread1.join()
#thread2.join()
