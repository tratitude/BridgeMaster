##method function
from lib import oled_config
from lib import GetMyState
from lib import General
from lib import RoundAdd
from lib import vun
from lib import method
##main proc
import bidding
import mode_select
import playing
import result
##python lib
import json
import time
total_score=0  #NS
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
        online=GetMyState.MyConnect(BMBC)
        if(("#") and online['state']=='0'): #time out or interrupt ->general
            time.sleep(1)#General.general()
        else:
            time.sleep(1)     ##Game()
    else:
        time.sleep(1)     ##Game()
    ##################################################################################  bidding
    bid_data=bidding.bidding(round%4)  ##先喊數字
    if(bid_data[1]==0):          ##bid data[0]=all info at bidding [1]=contract [1]=0 all pass [2]=declarer
        continue
    ##################################################################################  playing
    vunerable=vun.vunerable(round)
    play_data=playing.showing(round,bid_data[1],vunerable,bid_data[2])
    ################################################################################    push data to DB
    leader=method.get_leader(round) 
    new_score=method.get_score(bid_data[2],vunerable,play_data[4],bid_data[1]) #NS
    total_score+=new_score
    trick=method.get_trick(play_data,bid_data[2])
    RoundAdd.AddRound(online['T_id'],bid_data[0],leader,bid_data[1],play_data[0]
    ,play_data[1],play_data[2],play_data[3],vunerable,trick,bid_data[2],round,total_score)
    #################################################################################### print result
    result.print_result(round,total_score,new_score)
    round+=1
