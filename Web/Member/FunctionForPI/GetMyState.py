import json
import requests
import time
            #BMBC為str
def MyConnect(BMBC):    #向Server請求資料，5秒請求1次直到狀態為隨機/指定
        while True:
            r = requests.post('http://localhost:8000/Member/State/',data=BMBC)
            #print(r.content)
            if(r.content!=b'None'):
                data = json.loads(r.content)
                print(data)
                if data['state']=='1':  ## 隨機模式
                    return 1
                elif data['state']=='2':    ##指定模式
                    return data
            time.sleep(5)
#MyConnect('143')