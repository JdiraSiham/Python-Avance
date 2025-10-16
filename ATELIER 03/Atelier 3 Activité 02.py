#Réalisée par : JDIRA Siham 

#Atelier 3 Activité 2:

class Etudiant :
    def __init__ (self,matricule,nom,prenom,note):
        self.matricule=matricule
        self.nom=nom
        self.prenom=prenom
        self.note=note
    
    def afficher(self):
        print(f"La matricule de l'étudiant : {self.matricule}")
        print(f"Le nom de l'étudiant : {self.nom}")
        print(f"Le prénom de l'étudiant : {self.prenom}")
        print(f"La note de l'étudiant : {self.note}")
        print("")
    
    def somme(self,etudiant):
        print(f"La somme des notes des : {self.note + etudiant.note}")
        print("")
    
    def moyenne(self,etudiant):
        s=self.note + etudiant.note
        m=s/2
        print(f"La moyenne est : {m}")
        print("")

e1=Etudiant('0001','JDIRA','Siham',15)
e2=Etudiant('0002','AIT','Salma',16)

e1.afficher()
e2.afficher()

e1.somme(e2)
e1.moyenne(e2)