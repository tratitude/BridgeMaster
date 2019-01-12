import bidding
import mode_select
from lib import oled_config
import time
from lib import GetMyState
import json
from lib import General
from lib import RoundAdd
from lib import vun
import playing
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
    vunerable=vun.vunerable()
    plat_data=playing.showing(round,bid_data[1],vunerable)
    ################################################################################
    if(round%4==0):
        leader='N'
    elif(round%4==1):
        leader='E'
    elif(round%4==2):
        leader='S'
    else :
        leader='W'    
    RoundAdd.AddRound(online['T_id'],bid_data[0],leader,bid_data[1],,N,S,E,W,vunerable,result,,bid_data[2],round,score)
    round+=1
