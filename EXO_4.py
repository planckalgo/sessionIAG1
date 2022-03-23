Capital=100
Taux=0.043
Duree=20
Intpre=0
for i in range(1,20):
    interet=float((Capital*Taux*Duree)+Intpre)
    Intpre=interet
print('Interet accumulé pendant 20 ans: ',interet,' Euro')
