#Réalisée par : JDIRA Siham 

#Atelier 1 Activité 3:

#Question 1:
a=float(input("saisir la valeur de a : "))
b=float(input("saisir la valeur de b : "))
print("la somme de a et b est :",a+b)
print("la multiplication de a et b est :",a*b)

#Question 2:
a=float(input("saisir la valeur de a : "))
b=float(input("saisir la valeur de b : "))
c=a
a=b
b=c
print("apres permutation a =",a,"b =",b)

#Question 3:
a=float(input("saisir la valeur de a : "))
b=float(input("saisir la valeur de b : "))
c=float(input("saisir la valeur de c : "))
max=a
if b>max:
    max=b
elif c>max:
    max=c
print("le plus grand nombre est :",max)

#Question 4:
l=float(input("saisir une longueur : "))
choix=int(input("ecrire 1 pour convertir en km ou 2 pour convertir en mille : "))
match choix :
    case 1:
        d=l*1.609
        print("la distance en km est : ",d,"km")
    case 2:
        d=l/1.609
        print("la distance en mille est : ",d,"mille")
    case _ :
        print ("choix invalide")

