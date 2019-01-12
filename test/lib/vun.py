def vunerable(round):
    v=["None","NS","EW","All"]
    vunerable=""
    r1=0
    r2=0
    r1=round/4
    r2=round%4
    return  v[(r1+r2)%4]
        