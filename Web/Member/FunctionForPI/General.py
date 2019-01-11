#import Servo_9G as S9
#import ServoWheel as SW
#import UltraSonic as US
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
        #while range(card):  #重複發牌 card次
         #   while US.Distance() > 7:  # 判斷超音波感測到停馬達
          #      SW.Clockwise()
           #     SW.Speed(100)
            #SW.CounterClockWise()
        #發到player ，控制牌盒
     #   if player<2:
     #   else:
        #檢查4家是否都發完

        if deal[0]==13 and deal[1]==13 and deal[2]==13 and deal[3]==13:
            break
    print(deal)
general()
