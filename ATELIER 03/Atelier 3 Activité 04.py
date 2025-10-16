#Réalisée par : JDIRA Siham 

#Atelier 3 Activité 4:

class Personne:
    def __init__(self,nom,adresse):
        self.nom=nom
        self.adresse=adresse

    def afficher(self):
        print(f"nom est : {self.nom}")
        print(f"adresse est : {self.adresse}")

class Employe(Personne):
    def __init__(self,nom,adresse,cnss):
        self.cnss=cnss
        Personne.__init__(self,nom,adresse)

    def afficher(self):
        Personne.afficher(self)
        print(f"cnss est : {self.cnss}")

class Enseignant(Personne):
    def __init__(self,nom,adresse,cnops):
        self.cnops=cnops
        Personne.__init__(self,nom,adresse)

    def afficher(self):
        Personne.afficher(self)
        print(f"cnops est : {self.cnops}")

class Etudiant(Personne):
    def __init__(self,nom,adresse,cne):
        self.cne=cne
        Personne.__init__(self,nom,adresse)
        
    def afficher(self):
        Personne.afficher(self)
        print(f"cne est : {self.cne}")

p=Employe('ismail','casablanca','7000')
p.afficher()
Personne.afficher(p)