
def Basic(v,dbl):   #計算牌磴分數
    v0 = int(v[0])
    contract = {
        'S':    dbl*v0*30,
        'H':    dbl*v0*30,
        'D':    dbl*v0*20,
        'C':    dbl*v0*20,
        'NT':   40+dbl*(v0-1)*30
    }
    return contract[v[1:]]

def score(declarer,ns_vulnerable,ew_vulnerable,ns_trick,contract,dbl):
#先判斷攻方為?
    if declarer%2==0:          # NS為攻方
        trick = ns_trick
        vulner = ns_vulnerable
    else:                   # EW為攻方
        trick = 13-ns_trick
        vulner = ew_vulnerable
#判斷有沒有完成合約?
#contract eg. 3NT
    contract0 = int(contract[0])
    if trick-(contract0+6)>=0:       #完成合約
        basic = Basic(contract,dbl)     #計算牌磴分數
        Reward = 50             #計算線位獎分
        if basic>=100:
            Reward = 300
            if vulner:
                Reward = 500
        if contract[0]=='7' and trick==13:
            if vulner:
                Reward += 1500
            else:
                Reward += 1000
        if (contract[0]=='7' or contract[0]=='6') and trick==12:
            if vulner:
                Reward += 750
            else:
                Reward += 500
        Double = 0
        Exceed = (trick-contract0-6)*20               #計算超磴分數
        if contract[1]=='S' or contract[1]=='H' or contract[1]=='N':
            Exceed = (trick-contract0-6)*30
        if dbl==2:
            Double = 50
            Exceed = (trick-contract0-6)*100
            if vulner:
                Exceed = (trick-contract0-6)*200
        elif dbl==4:
            Double = 100
            Exceed = (trick-contract0-6)*200
            if vulner:
                Exceed = (trick-contract0-6)*400
        NS_Score = basic + Reward + Exceed + Double
        print(basic,Reward,Exceed,Double)
        if declarer % 2 == 1:
            NS_Score *= -1
    else:
        if dbl==1:
            Punish = (contract0+6-trick)*50
            if vulner:
                Punish = (contract0+6-trick)*100
        elif dbl==2:
            if vulner:
                if (contract0+6-trick)>=1:
                    Punish = 200
                if  (contract0+6-trick)>=2:
                    Punish += (contract0+5-trick)*300
            else:
                if contract0+6-trick>=1:
                    Punish=100
                if contract0+6-trick>=2:
                    Punish+=200
                if contract0+6-trick >=3:
                    Punish+=200
                if contract0+6-trick >=4:
                    Punish+=(contract0+3-trick)*300
        elif dbl==4:
            if vulner:
                if contract0+6-trick>=1:
                    Punish = 400
                if contract0+6-trick>=2:
                    Punish += (contract0+5-trick)*600
            else:
                if contract0+6-trick>=1:
                    Punish = 200
                if contract0+6-trick>=2:
                    Punish+=400
                if contract0+6-trick>=3:
                    Punish+=400
                if contract0+6-trick>=4:
                    Punish+=(contract0+3-trick)*600
        NS_Score = Punish
        if declarer%2==0:
            NS_Score = -1*Punish
    return NS_Score


Score = score(0,True,False,7,'4D',2)
print(Score)

