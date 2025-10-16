#Réalisée par : JDIRA Siham 

#Atelier 4 Activité 2:

liste=["a","b","c","d","e"]
with open("alpha.txt","a+") as file3:
    for x in liste :
        file3.write(x+"\n")
    file3.close()
with open ("alpha.txt","r+") as file4:
    print(file4.readlines())
    file4.close()