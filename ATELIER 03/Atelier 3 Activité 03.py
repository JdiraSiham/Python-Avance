#Réalisée par : JDIRA Siham 

#Atelier 3 Activité 3:

class Employe:
    def __init__(self, identifiant, nom, prenom, dateNaissance, dateEmbauche, salaire):
        self.__identifiant = identifiant
        self.__nom = nom
        self.__prenom = prenom
        self.__dateNaissance = dateNaissance
        self.__dateEmbauche = dateEmbauche
        self.__salaire = salaire

    def get_identifiant(self):
        return self.__identifiant

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_dateNaissance(self):
        return self.__dateNaissance

    def get_dateEmbauche(self):
        return self.__dateEmbauche

    def get_salaire(self):
        return self.__salaire

    def age(self, annee_actuelle):
        age = annee_actuelle - self.__dateNaissance
        print(f"L'âge de l'employé est : {age} ans")
        print("")

    def anciennete(self, annee_actuelle):
        anciennete = annee_actuelle - self.__dateEmbauche
        print(f"L'ancienneté de l'employé est : {anciennete} ans")
        print("")

    def afficher(self):
        print(f"Identifiant : {self.__identifiant}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Date de naissance : {self.__dateNaissance}")
        print(f"Date d'embauche : {self.__dateEmbauche}")
        print(f"Salaire : {self.__salaire}")
        print("")

e1 = Employe('0001', 'JDIRA', 'Siham', 1995, 2019, 10000)
e2 = Employe('0002', 'REDA', 'Ismail', 1999, 2020, 18500)

e1.afficher()
e1.age(2025)
e1.anciennete(2025)

e2.afficher()
e2.age(2025)
e2.anciennete(2025)