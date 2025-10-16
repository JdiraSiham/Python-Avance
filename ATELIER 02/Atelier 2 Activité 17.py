#Réalisée par : JDIRA Siham 

#Atelier 2 Activité 17:

t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Janvier', 'Février', 'Mars','Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre','Novembre','Décembre']
for i in range(12):
    t2.insert(2*i+1,t1[i])

print(t2)
