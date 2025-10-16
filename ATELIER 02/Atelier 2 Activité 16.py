#Réalisée par : JDIRA Siham 

#Atelier 2 Activité 16:

#Question 1:
l3=[5,6,2,7,3]
print(f"1). les elements de la liste l3 sont: ")
for j in l3:
    print(j)

#Question 2:
s=0
for i in l3:
    s+=i
print(f"2). la somme des elements de la liste est : {s}")

#Question 3:
p=1
for i in range(2,5):
    p*=l3[i]
print(f"3). le produit est : {p}")

#Question 4:
max=l3[0]
min=l3[0]
for i in l3:
    if i>max:
        max=i
    if i<min:
        min=i
print(f"4). le max est : {max} et le min est : {min}")

#Question 5:
multiples=0
for i in l3:
    if i%3==0:
        multiples+=1
print(f"5). le nombre de multiple de 3 est : {multiples}")

#Question 6:
l3.reverse()

print(f"6). la liste a l'envers : {l3}")
