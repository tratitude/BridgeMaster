import score
def get_leader(round):
    if(round%4==0):
        return 'N'
    elif(round%4==1):
        return 'E'
    elif(round%4==2):
        return 'S'
    else :
        return 'W'

#score(declarer,ns_vulnerable,ew_vulnerable,ns_trick,contract,dbl)
def get_score(declarer,vunerable,ns_trick,contract):
    l=len(contract)
    if(contract[l-1]=='x'):
        if(contract[l-2]=='x'):
            double=4
        else:
            double=2
    else:
        double=1
    
    if(vunerable=='None'):
        return score.score(declarer,0,0,ns_trick,contract,double)
    elif(vunerable=='NS'):
        return score.score(declarer,1,0,ns_trick,contract,double)
    elif(vunerable=="EW"):
        return score.score(declarer,0,1,ns_trick,contract,double)
    else:
        return score.score(declarer,1,1,ns_trick,contract,double)

def get_trick(play_data,declarer):
    if(declarer==0 or declarer==2):
        return play_data[4]
    else :
        return play_data[5]
