#Réalisée par : JDIRA Siham 

#Atelier 4 Activité 1:

#Question 5:

with open ("amis.txt","r+") as file:
    print(file.read())
    file.close()

#Question 7:

with open ("amis.txt","r+") as file:
    print(file.readline())
    file.close()