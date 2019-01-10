Data = {'bmbc':'2','state':'2','round':{'N':'K8732.43.K74.AK4','E':'QJ.KQT9.93.QJT75','S':'T54.J652.QJT.986','W':'A96.A87.A8652.32'},
            'from':'15'}
round = Data['round']
Cards = []
for key in round:
    Cards.append(round[key])

for i in range(4):
    Card = Cards[i].split('.')
    Cards[i] = Card
print(Cards[2])