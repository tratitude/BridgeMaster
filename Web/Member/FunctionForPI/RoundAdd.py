import time
import json
import requests
def AddRound(Event,Site,Date,T_id,bid,leader,contract,N,E,W,S,vulnerable,result,declarer,Rnum,score):

    Round = {
        'Event':Event,
        'Site':Site,
        'Date':Date,
        'T_id':T_id,
        'bid':bid,
        'leader':leader,
        'contract':contract,
        'N':N,
        'E':E,
        'W':W,
        'S':S,
        'vulnerable':vulnerable,
        'result':result,
        'declarer':declarer,
        'Rnum':Rnum,
        'score':score
        }
    Data_out = json.dumps(Round)    #encode to JSON
    r = requests.post('http://localhost:8000/Member/Json/',data=Data_out)
    # Data = json.loads(Data_out)
    #print(Data['leader']) 


#AddRound(8,"1,d2a2s213s",'N',"3NT","s12f32sd12sad","d13refqewff","f4f23f32fdfs","231fef2f23d32d","None",9,"W",3,750)
