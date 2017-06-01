
from tkinter import*
import random
from random import randint
import time
import threading
##import pygame
##from pygame.locals import*
##pygame.init()


posx=200
posy=480
posx1=300
posy1=-100
posx2=200
posy2=0


Isc=0


def fin():
    v1.destroy()
###########VENTANA JUEGO############
def salir():
    v2.destroy()

def abrir():
    global fondo2, b, j1, J1,pista1, pista2, var, Isc, Tsc,v2,alias,posx, posy
    global posx1,posx2,posy1,posy2,var1,var2,e1,e2,var1,var2, vidas, Tsc



    
##    pygame.mixer.music.init()
##    pygame.mixer.music.load("gta.mp3")
##    pygame.mixer.music.play(-)

    vidas=1
    
    v1.destroy()
    v2 = Tk()
    v2.title("JUEGO")
    b=Canvas(v2, width=500, height=600)

    fondo2=PhotoImage(file="pista.gif")
    pista1=b.create_image(250,200,image=fondo2)
    pista2=b.create_image(250,-400,image=fondo2)
        
    
    j1=PhotoImage(file="auto1.gif")
    e1=PhotoImage(file="enemigo1.gif")
    e2=PhotoImage(file="enemigo2.gif")

    var=b.create_image(posx,posy,image=j1)
    var1=b.create_image(posx1,posy1,image=e1)
    var2=b.create_image(posx2,posy2,image=e2)
    
    name=Label(v2,text=alias.get(), font=("Agency FB",16)).place(x=15,y=35)
    Tsc=Label(v2, text="POINTS: " + str(Isc), font=("Agency FB",16)).place(x=15,y=60)
    nvidas=Label(v2,text=vidas, font=("Agency FB",16)).place(x=15,y=85)
    info=Label(v2,text="MODO SURVIVAL: ",font=("Agency FB",12),fg="white", bg="SpringGreen3").place(x=0,y=180)
    info2=Label(v2,text="INTENTA HACER ",font=("Agency FB",12),fg="white", bg="SpringGreen3").place(x=0,y=200)
    info3=Label(v2,text="LA MAYOR ",font=("Agency FB",12),fg="white", bg="SpringGreen3").place(x=0,y=220)
    info4=Label(v2,text="CANTIDAD DE ",font=("Agency FB",12),fg="white", bg="SpringGreen3").place(x=0,y=240)
    info5=Label(v2,text="PUNTOS POSIBLES ",font=("Agency FB",12),fg="white", bg="SpringGreen3").place(x=0,y=260)
    info6=Label(v2,text="SIN CHOCAR ",font=("Agency FB",12),fg="white", bg="SpringGreen3").place(x=0,y=280)
    info7=Label(v2,text="CON EL ",font=("Agency FB",12),fg="white", bg="SpringGreen3").place(x=0,y=300)
    info8=Label(v2,text="ENEMIGO",font=("Agency FB",12),fg="white", bg="SpringGreen3").place(x=0,y=320)
    
    pista()
    enemigos()
    colisiones()
    
    sv=Button(v2,text="SAVE",command=save,font=("Agency FB",16)).place(x=15,y=120)
    Exit=Button(v2,text="EXIT",command=salir,font=("Agency FB",16)).place(x=15,y=150)
    
    v2.bind("<a>",left)
    v2.bind("<d>",right)

    b.pack()

##########ENEMIGOS####################
    
def enemigos():
    global b, fondo2, pista1, pista2, var,var1,var2,posx1, posy1, Isc, Tsc, v2
    global posx1,posx2,posy1,posy2, e1, e2, var1, var2, vidas
    
    aleatorio1=random.randint(150,350)
    aleatorio2=random.randint(150,350)
    
    b.move(var1,0,50)
    b.move(var2,0,50)
    
    if(b.coords(var1)[1]>=600 or b.coords(var2)[1]>=600):
        b.delete(var1)
        var1=b.create_image(aleatorio1,posy1,image=e1)
        b.delete(var2)
        var2=b.create_image(aleatorio2,-200,image=e2)
        
    b.after(100,enemigos)
    
##########COLISIONES###########################

def colisiones():
    global b, fondo2, pista1, pista2, var,var1,var2,posx1, posy1, Isc, Tsc, v2
    global posx1,posx2,posy1,posy2, e1, e2, var1, var2, salir, posx, posy, vidas

    cxCe = b.coords(var1)[0]
    cyCe= b.coords(var1)[1]

    cxC = b.coords(var)[0]
    cyC= b.coords(var)[1]

    cxCe1=b.coords(var2)[0]
    cyCe1=b.coords(var2)[1]


    if(cxC >= cxCe-21 and cxC<=cxCe+21 and cyC>=cyCe-49 and cyC<=cyCe+49):
        v2.destroy()
        v4=Tk()
        v4.geometry("600x400")
        f= Canvas(v4, height= 600, width= 400)
        v4.title("END OF THE ROAD!!")
        fondo4=PhotoImage(file="you_lose.gif")
        Endimagen=Label(v4,image=fondo4).place(x=0,y=0)
        Tsc=Label(v4, text="tu puntaje total ha sido de: " + str(Isc), font=("Agency FB",16)).place(x=15,y=30)
        c.pack()

    if(cxC>=cxCe1-21 and cxC<=cxCe1+21 and cyC>=cyCe1-47 and cyC<=cyCe+47): 
        v2.destroy()
        v3=Tk()
        v3.geometry("600x400")
        d= Canvas(v3, height= 600, width= 400)
        v3.title("END OF THE ROAD!!")
        fondo3=PhotoImage(file="you_lose.gif")
        Endimagen=Label(v3,image=fondo3).place(x=0,y=0)
        Tsc=Label(v3, text="tu puntaje total ha sido de: " + str(Isc), font=("Agency FB",16)).place(x=15,y=30)
        c.pack()
    
    b.after(100,colisiones)
        
    
##########FUNCIONES DE MOVIMIENTO##############
def right(event):
    global b, posx, posy, push, var
    if(posx<350):
        b.delete(var)
        posx=posx+10
        var=b.create_image(posx,posy,image=j1)
    elif(posx>=350):
        b.delete(var)
        posx=posx-8
        var=b.create_image(posx,posy,image=j1)

def left(event):
    global b, var, push,j1, posx, posy
    if(posx>150):
        b.delete(var)
        posx=posx-10
        var=b.create_image(posx,posy,image=j1)
    elif(posx<=150):
        b.delete(var)
        posx=posx+8
        var=b.create_image(posx,posy,image=j1)

def pista():
    global b, fondo2, pista1, pista2, var,posx1, posy1, Isc, Tsc, v2 
    
    b.move(pista1,0,25)
    b.move(pista2,0,25)
    if(b.coords(pista1)[1]>=850 or b.coords(pista2)[1]>=850):
        b.delete(pista1)
        pista1=b.create_image(250,-240,image=fondo2)
        b.delete(pista2)
        pista2=b.create_image(250,300,image=fondo2)
        b.delete(var)
        var=b.create_image(posx,posy,image=j1)
    Isc=Isc+2
    Tsc=Label(v2, text="Puntos"+str(Isc),font=("Agency FB",16)).place(x=15,y=60)
    b.after(100,pista)

##########SAVE & LOAD#################
def save():
    global alias, Isc,Tsc,posx,posy,var,posy1,posx1,posy2,posx2

    c=open("archivo.txt","w")
    c.write(alias.get()+"\n")
    c.write(str(posx)+"\n")
    c.write(str(posy)+"\n")
    c.write(str(posx1)+"\n")
    c.write(str(posy1)+"\n")
    c.write(str(posx2)+"\n")
    c.write(str(posy2)+"\n")
    c.write(str(Isc)+"\n")
    c.close()

    
def cargar():
    global alias, posx, posy, Isc, Tsc, posx1,posy1,posx2,posy2
    q=open("archivo.txt","r")
    nombre=q.readline().strip()
    posx=int(q.readline().strip())
    posy=int(q.readline().strip())
    posx1=int(q.readline().strip())
    posy1=int(q.readline().strip())
    posx2=int(q.readline().strip())
    pos=int(q.readline().strip())
    Isc=int(q.readline().strip())
    alias.set(nombre)
    
    
##########VENTANA MENU#################
v1 = Tk()
v1.geometry("600x400")
a = Canvas(v1, height= 600, width= 400)
v1.title("MENU CARRITOS")
fondo1=PhotoImage(file="intro.gif")
limagen=Label(v1,image=fondo1).place(x=0,y=0)

intro=Label(text="BIENVENIDO A RACING CARS",font=("Agency FB",35)).place(x=50,y=120)
Nusuario=Label(text="Usuario: ",font=("Agency FB",16)).place(x=150,y=250)

alias=StringVar()
txtUser = Entry(v1,textvariable=alias, font=("Agency FB",16)).place(x=250,y=250)

boton1=Button(v1,text="Play",command=abrir,font=("Agency FB",14),width=10).place(x=320,y=365)
boton2=Button(v1,text="Exit",command=fin,font=("Agency FB",14),width=10).place(x=450,y=365)
boton3=Button(v1,text="Load",command=cargar,font=("Agency FB",14),width=10).place(x=190,y=365)

a.pack()
v1.mainloop()
