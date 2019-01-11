from GetMyState import MyConnect
import BarcodeScanner as BB
import Servo_9G as  S9
import ServoWheel as SW
import UltraSonic as US
import time


def CardTransfer(v):  #把Barcode轉成PBN格式
    point = {
        '1':'A',
        'A':'T',
        'B':'J',
        'C':'Q',
        'D':'K'
    }
    return point[v]

BMBC = '5'   # BridgeMasterBaseCode
try:
    # 持續連線直到進入mode.General/mode.Clasisc/中斷發生
    #Data = MyConnect()
    Data = {'bmbc':'2','state':'2','round':{'N':'K8732.43.K74.AK4','E':'QJ.KQT9.93.QJT75','S':'T54.J652.QJT.986','W':'A96.A87.A8652.32'},
            'from':'15'}
    if Data['state']=='1':      #mode.General
        #Mode('General')
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
            suit = ThisCard[4]   # suit: 1:spade, 2:heart, 3:diamond , 4:club
            point = ThisCard[3]  # 1,2,3....A:10, B:11, C:12, D:13
# Barcode:        1 A B C D
# PBN:            A T J Q K
            point = CardTransfer(point)     #轉成PBN格式
            #N:0/ E:1/ S:2/ W:3
            Player =0
            for i in range(4):
                if   point in Cards[i][suit-1] :                #Card[i]選擇玩家,[suit-1]選擇對應的花色,eg: suit=1,spade
                    Player = i                                #                                  則要找Card[i][0]

#牌盒移動到北0東1/南2西3
#    _____  S  ______
#   ｜    ｜   ｜    ｜
#   ｜  S ｜   ｜  W ｜
# E ｜----｜   ｜----｜ W
#   ｜  E ｜   ｜  N ｜
#   ｜____｜   ｜____｜
#            N
            if Player>1:    #移動到北東
                #Stepper move(100)..

                S9.Left()
                S9.Balance()
            else:
                #Stepper move(-100)..
                S9.Right()
                S9.Balance()
except:
    time.sleep(1)