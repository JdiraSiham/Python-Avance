#Réalisée par : JDIRA Siham 

#Atelier 3 Activité 1:

class Voiture :
    def __init__(self,code,marque,kilometrage):
        self.code=code
        self.marque=marque
        self.kilometrage=kilometrage
    
    def mod_kilo (self,nouvelle_kilometrage):
        self.kilometrage=nouvelle_kilometrage

    def afficher (self):
        print(f"code : {self.code}")
        print(f"marque : {self.marque}")
        print(f"kilometrage : {self.kilometrage}")
        print("")

v1=Voiture('0001','toyota',12500)
v2=Voiture('0002','renault',90000)
v3=Voiture('0003','bmw',675200)

v1.afficher()
v2.afficher()
v3.afficher()

v1.mod_kilo(387000)

v1.afficher()
v2.afficher()
v3.afficher()