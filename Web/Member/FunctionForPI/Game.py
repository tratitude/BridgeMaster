from GetMyState import MyConnect

import time

BMBC = '5'   # BridgeMasterBaseCode
try:
    # 持續連線直到進入mode.General/mode.Clasisc/中斷發生
    #Data = MyConnect()
    Data = {'bmbc':'2','state':'2','round':{'N':'K8732.43.K74.AK4','E':'QJ.KQT9.93.QJT75','S':'T54.J652.QJT.986','W':'A96.A87.A8652.32'},
            'from':'15'}
    if Data['state']=='1':      #mode.General
        time.sleep(2)
    else:                       #mode.Classic
        #先將4家牌整理出來
        round = Data['round']
        Card = []
        for key in round:
            Card.append(round[key])
        ##開始發牌##
        while  range(52):
            #出一張牌 上馬達
            #判斷超音波感測到停止 停馬達
            #啟動Barcode直到掃進來
except:
    time.sleep(1)