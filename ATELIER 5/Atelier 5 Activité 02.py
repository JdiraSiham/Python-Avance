#Réalisée par : JDIRA Siham 

#Atelier 5 Activité 2:

#Question 1:
import sqlite3
db =sqlite3.connect("gestion2.db")
db.execute ("create table if not exists formation (Id integrer , titre text)")
db.execute ("create table if not exists etudiant (code integrer , name text, email text)")

#Question 2:
db.execute ("insert into formation (Id,titre) values(?,?)",(1,"Python"))
db.execute ("insert into formation (Id,titre) values(?,?)",(2,"html"))

#Question 3:
db.execute ("insert into etudiant (code,name,email) values(?,?,?)",(1,"youssef","youssef@gmail.com"))
db.execute ("insert into etudiant (code,name,email) values(?,?,?)",(2,"sara","sara@gmail.com"))
db.commit()

#Question 4:
cursor=db.execute("select * from formation")
for row in cursor:
    print(row[0],row[1])
cursor2=db.execute("select * from etudiant")
for row in cursor2:
    print(row[0],row[1],row[2])


#Question 5:
def ins(v1,v2):
    db.execute ("insert into formation (Id,titre) values(?,?)",(v1,v2))
    db.commit()

ins(1,"Python")

#Question 6:
def afficher():
    cursor=db.execute("select * from formation")
    for row in cursor:
        print(row[0],row[1])


afficher()

#Question 7:
def supprimer(Id):
    db.execute("delete from formation where Id= ?",(Id,))
    db.commit()

def modifier(titre,Id):
    db.execute ("update formation set titre =? where Id=?",(titre,Id))
    db.commit()

supprimer(1)
modifier("C",2)

db.close()