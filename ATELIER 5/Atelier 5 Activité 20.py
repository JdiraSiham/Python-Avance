#Réalisée par : JDIRA Siham 

#Atelier 5 Activité 20:

#Question 1:
import sqlite3
db =sqlite3.connect("gestion.db")

#Question 4:
db.execute ("create table if not exists person (code integrer , name text)")

#Question 5:
db.execute ("insert into person (code,name) values(?,?)",(10,"Karim"))

db.row_factory=sqlite3.Row
cursor=db.execute("select * from person")
for row in cursor:
    print(row["code"],row["name"])

#Question 6:
db.execute ("insert into person (code,name) values(?,?)",(11,"Amal"))
db.execute ("insert into person (code,name) values(?,?)",(12,"Reda"))

#Question 7:
db.execute("delete from person where code=10")

#Question 8:
db.execute ("update person set name ='Radi' where code=12")

db.close()