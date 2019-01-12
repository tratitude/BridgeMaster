import time
import json
import requests
def AddRound(T_id,bid,leader,contract,N,E,W,S,vulnerable,result,declarer,Rnum,score):

    Round = {   
        'T_id':T_id,
        'bid':bid,
        'leader':leader,
        'contract':contract,
        'N':N,
        'E':E,
        'W':W,
        'S':S,
        'vulnerable':vulnerable,
        'result':result,    #declarer's tricksssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
        'declarer':declarer,
        'Rnum':Rnum,    #round number
        'score':score
        }
    
    Data_out = json.dumps(Round)    #encode to JSON
    
    r = requests.post('http://192.168.0.166:8000/Member/Json/',data=Data_out)
    print(r.content)
    # Data = json.loads(Data_out)
    #print(Data['leader']) 


#AddRound(8,"1,d2a2s213s",'N',"3NT","s12f32sd12sad","d13refqewff","f4f23f32fdfs","231fef2f23d32d","None",9,"W",3,750)