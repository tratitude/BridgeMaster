
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
from .ddsTable import ddsTable       # ddsTable function description is at bottom

# Create your views here.
def dds(request, R_id):
    round = rounds.objects.get(pk=R_id)
    if round is not None:
        if round.dds_result is None:
            fo = open("Web/DDS/ddsTable/ddsDB.dds", "w")
            fo.write("N:" + round.N + " " + round.E + " " + round.S + " " + round.W + "\n")
            fo.close()
            ddsTable.ddsTable("Web/DDS/ddsTable/ddsDB.dds", "Web/DDS/ddsTable/ddsResult.dds")
            fo = open("Web/DDS/ddsTable/ddsResult.dds", "r")
            ddsR = fo.read(60)
            fo.close()
            round.dds_result = ddsR
            round.save()

        N = card(round.N)
        E = card(round.E)
        S = card(round.S)
        W = card(round.W)
    return render(request, "DDS/dds.html", locals())
class card():
    def __init__(self, str):
        round = str.split('.')
        self.Spade = round[0]
        self.Hart = round[1]
        self.Diamond = round[2]
        self.Club = round[3]
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