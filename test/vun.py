def vunerable(round):
    v=["None","NS","EW","All"]
    r1=0
    r2=0
    r1=round/4
    r2=round%4
    return  v[int((r1+r2)%4)]
        
