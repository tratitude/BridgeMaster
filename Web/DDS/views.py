from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.contrib.sessions.models import Session
from django.views import View
from Member.models import rounds,table
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from django.http import HttpResponse
from django.db.models	 import Q
import math
#from .ddsTable import ddsTable       # ddsTable function description is at bottom

# Create your views here.
def dds(request, R_id):
    try :
        round = rounds.objects.get(pk=R_id)
    except :
        print(str(R_id) + '   has no rounds\n')
    try :
        N_play = round.N_play.split('.')
        E_play = round.E_play.split('.')
        S_play = round.S_play.split('.')
        W_play = round.W_play.split('.')
        if round.leader == 'N':
            lead = N_play[0]
        elif round.leader == 'E':
            lead = E_play[0]
        elif round.leader == 'S':
            lead = S_play[0]
        elif round.leader == 'W':
            lead = W_play[0]
    except :
        print('has no played record\n')
    if round.dds_result is None :
        print('Here is dds result\n')
        fo = open("Web/DDS/ddsTable/ddsDB.dds", "w")
        fo.write("N:" + round.N + " " + round.E + " " + round.S + " " + round.W + "\n")
        fo.close()
        ddsTable.ddsTable("Web/DDS/ddsTable/ddsDB.dds", "Web/DDS/ddsTable/ddsResult.dds")
        fo = open("Web/DDS/ddsTable/ddsResult.dds", "r")
        ddsR = fo.read(60)
        fo.close()
        round.dds_result = ddsR
        round.save()
    '''
    N = card(round.N)
    E = card(round.E)
    S = card(round.S)
    W = card(round.W)
    
    b = round.bid.split(',')
    dealer = b[0]

    dds_result = round.dds_result.split(' ')
    del dds_result[len(dds_result) -1]

    bid_suit = deck_suit(b)

        
    return render(request, "DDS/dds.html", locals())
class card():
    def __init__(self, str):
        round = str.split('.')
        self.Spade = round[0]
        self.Hart = round[1]
        self.Diamond = round[2]
        self.Club = round[3]

class bid(list):
    def __init__(self, suit, num):
        self.num = num
        self.suit = suit
    '''
    def __str__(self):
        return (str(self.num)+self.suit)
    '''
def deck_suit(b):
    dealer = b[0]
    del b[0]
    if dealer == 'E':
        b.insert(0, '')
    if dealer == 'S':
        b.insert(0, '')
        b.insert(0, '')
    if dealer == 'W':
        b.insert(0, '')
        b.insert(0, '')
        b.insert(0, '')
    bid_round = math.ceil(len(b) / 4)
    for i in range(len(b)-1, bid_round*4 - 1):
        b.append('')
    
    bid_suit = []
    for bb in b:
        if(len(bb) == 0):
            bid_suit.append(('', ''))
        elif(bb == 'X'):
            bid_suit.append(bid(bb, bb))
        elif(bb[1] == 'S'):
            bid_suit.append(bid('S', bb[0]))
        elif(bb[1] == 'H'):
            bid_suit.append(bid('H', bb[0]))
        elif(bb[1] == 'D'):
            bid_suit.append(bid('D', bb[0]))
        elif(bb[1] == 'C'):
            bid_suit.append(bid('C', bb[0]))
        else:
            bid_suit.append(bid(bb, bb))
    #print(bid_suit)
    return bid_suit

'''
# ddsTable("input file", "output file")
-----------------------
## ddsDB.txt format
N:|     Spade    | |     Hart     | |    Diamond   | |     Club     |
ex: 
N:73.QJT.AQ54.T752 QT6.876.KJ9.AQ84 5.A95432.7632.K6 AKJ9842.K.T8.J93
-----------------------
## ddsResult.txt format (file contain only digit, just for expaination)
    North South East  West
NT    4     4     8     8
S     3     3    10    10
H     9     9     4     4
D     8     8     4     4
C     3     3     9     9
'''
