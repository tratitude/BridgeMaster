import bidding
import mode_select
import oled_config
import time
import GetMyState
import json
import General
#import Game
import show_game
BMBC='999'
game_mode=True #true=classic false=general
round=0
"""
bidding
0=pass
1234567=1234567
F=♠ E=♥ D=♦ C=♣
A=double b=NT
"""
while True:
        mode = mode_select.online()
        if mode:                    #online
            oled_config.fline_print(0,0,"Connecting")
            GetMyState.refresh()
            online=GetMyState.MyConnect(BMBC)
            if(("#") and online['state']=='0'): #time out or interrupt ->general
                time.sleep(1)#General.general()
            else:
                time.sleep(1)     ##Game()
        else:
            time.sleep(1)
            #General.general()
        ##################################################################################
        bid_data=bidding.bidding(4)  ##先喊數字
        print(bid_data[1])
        if(bid_data[1]==0):          ##bid data[0]=all info at bidding [1]=contract [1]=0 all pass
            continue
        ##################################################################################
        show_game.showing(round,bid_data[1])
        
