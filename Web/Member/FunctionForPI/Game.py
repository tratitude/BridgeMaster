from GetMyState import MyConnect
import BarcodeScanner as BB
import Servo_9G as  S9
import ServoWheel as SW
import UltraSonic as US
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
        Cards = []
        for key in round:
            Cards.append(round[key])
        for i in range(4):
            Card = Cards[i].split('.')
            Cards[i] = Card
        ##開始發牌##
        while  range(52):
            #出一張牌 上馬達
            while US.Distance()>7:    #判斷超音波感測到停馬達
                SW.Clockwise()
                SW.Speed(100)
            SW.CounterClockWise()
            #啟動Barcode直到掃進來
            ThisCard = BB.Scan()
            #N/E/S/W

            
except:
    time.sleep(1)