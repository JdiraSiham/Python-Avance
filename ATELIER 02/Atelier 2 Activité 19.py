#Réalisée par : JDIRA Siham 

#Atelier 2 Activité 19:

#Question 1:
def F1 (): 
    n1=int(input("Saisir combien de fois afficher Bonjour : "))
    for x in range(n1):
        print("Bonjour")
F1()

#Question 2:
def F2 ():
    n2=int(input("Saisir un nombre pour tester si il est divisible par 10 : "))
    if n2%10==0:
        print(f"{n2} est divisible par 10")
    else:
         print(f"{n2} n'est pas divisible par 10")
F2()

#Question 3:
def F4():
    n4=int(input("Saisir un nombre pour calculer son factoriel : "))
    f=1
    for x in range(1,n4+1):
        f*=x
    print(f"le factoriel de {n4} est : {f}")
F4()

#Question 4:
def F3():
    chaine=input("Saisir une chaine de caractere pour compter le nombre de voyelle : ")
    voyelle=['a','e','i','o','y','u']
    m=0
    for lettre in chaine :
        for v in voyelle :
            if lettre==v:
                m+=1
    print(f"le nombre de voyelle dans {chaine} est {m}")
F3()

#Question 5:
def F5 ():
    n5=int(input("Saisir un nombre pour afficher sa table de multiplication : "))
    for i in range (11):
        print(f"{n5}x{i} = {n5*i}")
F5()

#Question 6:
def F6 ():
    mot=input("Saisir un mot pour afficher son nombre de caractere : ")
    print(f"{mot} contient {len(mot)} caracteres")
F6()

#Question 7:
def F7():
    n7=int(input("Saisir l'ordre n de la suite Fibonacci : "))
    x=1
    y=1
    for j in range (n7):
        z=x+y
        print(f"{x}+{y}={z}")
        x=y
        y=z

F7()
