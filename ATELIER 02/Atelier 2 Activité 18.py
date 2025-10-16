#Réalisée par : JDIRA Siham 

#Séance 2 Activité 18:

machines = {
"m1": "192.168.0.1",
"m2": "192.168.0.2",
"m3": "192.168.0.3",
"m4": "192.168.0.4",
"m5": "192.168.0.5"
}

#Question 1:
print(f"1). l'adresse IP de la machine 2 est {machines["m2"]}")

#Question 2:
print(f"2). le nombre de machines reoertoriees dans le dictionnaire est {len(machines)}")

#Question 3:
machines["m6"]='192.168.0.6'
print(f"3). apres l'ajout de m6 : {machines}")

#Question 4:
del machines["m4"]
print(f"4). apres la suppression de m4 : {machines}")

#Question 5:
print(f"5). la machine 5 est dans le dictionnaire ? {"m5" in machines}")

#Question 6:
x=input("6). entrez le nom d'une machine : ")
if x in machines :
    print(f"l'adresse IP de la machine {x} est : {machines[x]}")
else :
    print(f"la machine {x} n'est pas repertoiree")