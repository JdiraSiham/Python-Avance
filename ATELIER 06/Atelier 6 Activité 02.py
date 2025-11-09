#Réalisée par : JDIRA Siham 

#Atelier 6 Activité 2:

from tkinter import *

def calcul():
    v=float(n1.get())+float(n2.get())
    somme.set(v)

fenetre=Tk()
fenetre.geometry("400x300")

v1 = StringVar()
v2 = StringVar()
somme=StringVar()

num1=Label(fenetre, text='Enter Num 1:')
num1.grid(column=0,row=0)
n1=Entry(fenetre,textvariable=v1)
n1.grid(column=1,row=0)

num2=Label(fenetre, text='Enter Num 2:')
num2.grid(column=0,row=1)
n2=Entry(fenetre,textvariable=v2)
n2.grid(column=1,row=1)

sum=Label(fenetre, text='The sum is:')
sum.grid(column=0,row=2)
som=Entry(fenetre,textvariable=somme)
som.grid(column=1,row=2)

quit=Button(fenetre,text="Quit", command=fenetre.quit)
quit.grid(column=0,row=3)

show=Button(fenetre,text="Show", command=calcul)
show.grid(column=1,row=3)

fenetre.mainloop()