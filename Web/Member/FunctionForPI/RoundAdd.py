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
    data = {'declarer': N, 'S': "H7.CA.HQ.C9.CJ.D9.SJ.H4.D7.DT.HK.DJ.DQ", 'contract': '1SXX', 'T_id': 33, 'E': "H9.C2.HA.CK.C7.D3.SQ.HT.DA.D4.S6.S8.SA", 'result': 6, 'N': "HJ.C5.H2.CT.S2.D5.S4.S5.D6.DK.ST.S7.SK", 'vulnerable': "None", 'bid': "N,Pass,Pass,1D,Pass,1S,X,XX,Pass,Pass,Pass", 'score': -50, 'W': "H8.C3.H3.C4.CQ.D2.S3.H5.D8.S9.H6.C6.C8", 'leader': "E", 'Rnum': 0}
    
    Data_out = json.dumps(data)    #encode to JSON
    
    r = requests.post('http://192.168.0.139:8000/Member/Json/',data=Data_out)
    print(r.content)
    # Data = json.loads(Data_out)
    #print(Data['leader']) 


AddRound(8,"1,d2a2s213s",'N',"3NT","s12f32sd12sad","d13refqewff","f4f23f32fdfs","231fef2f23d32d","None",9,"W",3,750)