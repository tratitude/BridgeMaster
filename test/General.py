import Servo_9G as S9
import ServoWheel as SW
import UltraSonic as US
import time
import random

def general():
    deal = [0,0,0,0]
    
    #隨機產生一家
    while True:
        player = random.randint(0,3)
        card = random.randint(0,3)  #隨機發0~3張牌
        if deal[player]+card>13:
            continue
        deal[player]+=card
        for i in range(card):  #重複發牌 card次
           distance =  US.Distance()
           while distance > 9:  # 判斷超音波感測到停馬達
                SW.Clockwise()
                SW.Speed(70)
                distance = US.Distance()
                #print(distance)
                time.sleep(0.2)
           SW.CounterClockwise()
           SW.Speed(50)
     #   發到player ，控制牌盒
           if player<2:
               S9.Left()
               time.sleep(0.5)
               S9.Balance()
           else:
               S9.Right()
               time.sleep(0.5)
               S9.Balance()
              # print('test2')
            #檢查4家是否都發完
          # print(card)
        if deal[0]==13 and deal[1]==13 and deal[2]==13 and deal[3]==13:
            SW.Speed(0)
            break
    #print(deal)
#general()
