from pynput import keyboard
import time
import BarcodeScanner as BB



def on_press(a):
    #try:
    global count
    global s
    if a!=keyboard.Key.shift and a!=keyboard.Key.enter :
        #print('{0}'.format(a))
        count = count+1
        s = s+str(a.char)
        if count==4:
            return False
    
    #except AttributeError:
        #print('{0}'.format(key))

def on_release(key):
    #print('{0}'.format(key))
    time.sleep(0.1)
    
while True:
    count = 0
    s = ""
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        #while True:
        #print('test')
        BB.Scan()
        time.sleep(1)
    print(s)
    listener.join()
        







