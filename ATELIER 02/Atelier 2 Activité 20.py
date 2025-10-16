#Réalisée par : JDIRA Siham 

#Atelier 2 Activité 20:

adresses_ip=["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]

classes={
"192.168.0.1" : "classe C",
"10.0.0.1" : "classe A",
"172.16.0.1" : "classe B",
"200.100.50.1" : "adresse IP publique",
"169.254.0.1" : "adresse IP de lien local (APIPA)"
}

#Question 1 :
print(f"1). le premier adresse dans la liste est : {adresses_ip[0]}")

#Question 2 :
print(f"2). le dernier adresse dans la liste est : {adresses_ip[-1]}")

#Question 3 :
print(f"3). le troisieme adresse dans la liste est : {adresses_ip[2]}")

#Question 4 :
adresses_ip.append('172.31.0.1')
print(f"4). Apres l'ajout de l'adresse IP 172.31.0.1 la nouvelle liste est : {adresses_ip}")

#Question 5 :
adresses_ip.remove('200.100.50.1')
print(f"5). Apres la suppression de l'adresse IP 200.100.50.1 la nouvelle liste est : {adresses_ip}")

#Question 6 :
print(f"6). le nombre d'adresses IP restants apres la modification est : {len(adresses_ip)}")

#Question 7 :
print(f"7). l'adresse IP '192.168.0.1' est present dans la liste ? {'192.168.0.1'in adresses_ip}")

#Question 8:
print(f"8). la classe d'adresse IP 10.0.0.1 est : {classes['10.0.0.1'] }")

#Question 9:
adresses_ip.sort()
print(f"9). la liste triée : {adresses_ip}")

#Question 10:
print("10). ")
for ip in classes:
    if classes[ip]== 'classe C':
        print(f"{ip} appartient a la classe C")
    else:
        print(f"{ip} n'appartient pas a la classe C")

#Question 11:
n=0
for ip in classes:
    if classes[ip]== 'adresse IP de lien local (APIPA)':
       n+=1

print(f"11). le nombre d'adresse IP de lien local (APIPA) sont : {n}")
