from lib import oled_config
from lib import Keypad
import time
##return data [0]=bid [1]=contract(pass=0) [2]=declarer
<<<<<<< HEAD


=======
>>>>>>> stage
def trans(x):
    position = {
        '0':'N',
         '1':'E',
          '2':'S',
           '3':'W'
    }    
    return position[str(x%4)]
#♣♦♥♠
def KeyTran(x):
    key = {
        'S':'♠',
        'H':'♥',
        'D':'♦',
        'C':'♣',
        'NT':'♛'
    }
    if x in key:
        return key[x]
    return x
def refresh(str1,str2,str3,str4):
        oled_config.clsr()
        oled_config.fline_print(0,0,str1)
        oled_config.fline_print(0,1,str2)
        oled_config.fline_print(0,2,str3)
        oled_config.fline_print(0,3,str4)
def bidding(first):
    r_data=[]
    data=""
    str1="N:"
    str2="E:"
    str3="W:"
    str4="S:"
    refresh(str1,str2,str3,str4)
    current=first
    p=0
    contract=""
    declarer=0
    while True:
        read1=Keypad.Read_Key()
        time.sleep(0.6)
        if read1==0:       #read p
            p=p+1
            if(current==first):       #first bidding
                data+=trans(current) 
            if(current%4==0):
                str1+=" P "
            elif(current%4==1):
                str2+=" P "
            elif(current%4==2):
                str3+=" P "
            else:
                str4+=" P "
            data=data+','+'P'
            refresh(str1,str2,str3,str4)
            if(current==(4+first) and p==4):#4 pass
                r_data.append(data)
                r_data.append(0)
                return r_data
            elif(current>=(4+first) and p==3):
                r_data.append(data)
                r_data.append(contract)
                declarer=declarer%4
                r_data.append(declarer)
                return r_data
            current+=1
            continue
        if read1=='X':
            if contract[len(contract)-1]=='X':
                if(current%4==0):
                    str1+=" XX "
                elif(current%4==1):
                    str2+=" XX "
                elif(current%4==2):
                    str3+=" XX "
                else:
                    str4+=" XX "
                data=data+','+'XX'
            else:
                if(current%4==0):
                    str1+=" X "
                elif(current%4==1):
                    str2+=" X "
                elif(current%4==2):
                    str3+=" X "
                else:
                    str4+=" X "
                data=data+','+'X'
            if(current%4==0):
                str1+=" X "
            elif(current%4==1):
                str2+=" X "
            elif(current%4==2):
                str3+=" X "
            else:
                str4+=" X "
            data=data+','+'X'
            if current>declarer:
                contract+='X'
            refresh(str1,str2,str3,str4)
            current+=1
            p=0
            continue
        read2=Keypad.Read_Key()
        oled2=KeyTran(read2)
        if(current==first):       #first bidding
            data+=trans(current)
        data = data+','+str(read1)+str(read2)
        oled=str(read1)+str(oled2)
        contract=str(read1)+str(read2)
        if(current%4==0):
            str1=str1+" "+oled
        elif(current%4==1):
            str2=str2+" "+oled
        elif(current%4==2):
            str3=str3+" "+oled
        else:
            str4=str4+" "+oled
        p=0
        declarer = current
        current+=1
        refresh(str1,str2,str3,str4)
        
#print(bidding(4))
