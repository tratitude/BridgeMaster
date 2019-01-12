import json
import requests
import time
import oled_config
import oled_config
import Keypad

def refresh(str1,str2,str3,str4):
        oled_config.clsr()
        oled_config.fline_print(0,0,str1)
        oled_config.fline_print(0,1,str2)
        oled_config.fline_print(0,2,str3)
        oled_config.fline_print(0,3,str4)
            #BMBC為str
def MyConnect(BMBC):    #向Server請求資料，5秒請求1次直到狀態為隨機/指定
    t=1
    while True:
        try:
            #print('test')
            r = requests.post('http://192.168.0.166:8000/Member/State/',data=BMBC,timeout=10)
        #xcept:
            #print('test')
            data = r.content.decode('utf-8')
            data = json.loads(data)
#            print(type(data))
            if(data['state']!=None):
               # print(data)
# return data = { 'bmbc': BMBC,
#              'from': roundID,                                             --onlyforClassic
#              'round': {'N': Ncard, 'E': Ecard, 'S': Scard, 'W': Wcard },  --onlyforClassic
#               'state': GameMode
#               }
                return data
            time.sleep(2)
            refresh("","","%d times" %t,"Login on Web")
          #  oled_config.fline_print(0,2,"%d times" % t)
            #oled_config.fline_print(0,3,"Login on Web")
            t+=1
        except requests.Timeout as e:
            #print(e)
            refresh("Connect Failed","","","")
            time.sleep(5)
            #oled_config.fline_print(0,3," Connect Failed ")
            
            
#print(MyConnect('143'))
