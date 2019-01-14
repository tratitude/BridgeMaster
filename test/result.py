from lib import oled_config
from lib import Keypad
import time
def print_result(round,total_score,new_score):
    oled_config.fline_print(3,0,"Round:")
    oled_config.fline_print(10,0,str(round))
    oled_config.fline_print(1,1,"NS:"+str(total_score))
    oled_config.fline_print(1,1,"EW:"+str(-total_score))
    oled_config.fline_reverse(7,3,"WIN")
    if new_score<0:
        oled_config.fline_print(8,1,"-"+str(-new_score))
        oled_config.fline_print(8,1,"+"+str(-new_score))
        oled_config.fline_reverse(4,3,"EW")
    else:
        oled_config.fline_print(8,1,"+"+str(new_score))
        oled_config.fline_print(8,1,"-"+str(new_score))
        oled_config.fline_reverse(4,3,"NS")
    while True:
        read1=''
        read1=Keypad.Read_Key()
        time.sleep(0.6)
        if read1 != '' :
            break