
def CardTransfer(v):  #把Barcode轉成PBN格式
    point = {
        '1':'A',
        'A':'T',
        'B':'J',
        'C':'Q',
        'D':'K'
    }
    return point[v]

point  = 'C'
point = CardTransfer(point)
print(point)
