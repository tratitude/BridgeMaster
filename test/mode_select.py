import Keypad
import oled_config

def online():
    oled_config.clsr()    
    oled_config.fline_print(0,0,"Select Mode")
    oled_config.fline_print(0,2,"1. Online")    
    oled_config.fline_print(0,3,"2. Offline")
    while True:
        RK=Keypad.Read_Key()
        if RK==1:
            return True
        elif RK==2:
            return False
        
#print(online())
