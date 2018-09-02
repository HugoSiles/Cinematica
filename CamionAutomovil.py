# problema1.5.py
from vpython import *
import numpy as np
BW=0
if BW==0:
    fgcolor=color.black; bgcolor=color.white
else:
    fgcolor=color.white; bgcolor=color.black
b1color=vector(1,0,0)
b2color=vector(0,0,1)

#cantidades fisicas iniciales
pos1_inic=vector(0,0,0) 
vel1_inic=vector(0,0,0) 
pos2_inic=vector(0,0,0) 
vel2_inic=vector(0,0,0) 

#definir datos iniciales del movimiento
pos1_inic.x = 3 -18 
vel1_inic.x = 0. 
ac1 = 1.2 
pos2_inic.x = -18. 
vel2_inic.x = 0. 
ac2 = 1.8

#genera ventana de pista y objetos en movimiento
scene4=canvas()
scene4.title="                                     CAMION y AUTOMOVIL    Por Hugo Siles A."
scene4.width=900; scene4.height=450
scene4.autoscale=0
scene4.range=(8)
scene4.foreground=fgcolor
scene4.center=vector(0,0,1)
scene4.background=color.gray(0.9) 
#scene3.lights = [vector(0,0.3,0) ]
scene4.ambient = vector(0.4,0.4,0.4)
scene4.forward=vector(0.,-0.1,-0.06)
scene4.align='left'

def objetos():
    global pista,movil1,movil2    
    long_pista=37
    pista = box(pos=vector(0,-4.,0), axis=vector( 1 , 0 ,0), length=long_pista,
                height=.8, width=6, color=vector(0.0,0.8,0.0)) 
    
    for x in np.arange(-18,18.1,2.5):
        cu = curve(color=b2color,radius=0.03)
        cu.append([vector(x,-3.61,-3),vector(x,-3.61,3)]) 
       
     #dibuja posicion inicial de los objetos
    alto_bloque = 0.5
    pos1_inic.y=-alto_bloque/1.6-3 ; pos1_inic.z=-0.5
    pos2_inic.y=-alto_bloque/1.6-3 ; pos2_inic.z=0.5
    p1= vector(-18+7.5,pos1_inic.y,pos1_inic.z)
    p2=vector(-18+0.,pos2_inic.y,pos2_inic.z)
    movil1 = box(pos=p1, axis=pista.axis, length=0.7, height=alto_bloque,
                 width=.6, color=b1color)
    movil2 = box(pos=p2, axis=pista.axis, length=0.6, height=alto_bloque,
                 width=.6, color=b2color)
    
objetos()

#Graficos del movimiento

def graficos():
    global pos1_Plot, pos2_Plot, vel1_Plot, vel2_Plot
    pos_graph = graph(canvas=scene4,width=500, height=300,xtitle='t(s)',
                ytitle='x (m)',xmax=15, xmin=0., ymax=140, ymin=0,align='left',
                foreground=color.black, background=color.white)
    for x in np.arange(0,15.1,0.5):
        gcu = gcurve(color = color.orange)
        for y in np.arange(0,140.1,5):
            gcu.plot(pos=(x,y))
    for y in np.arange(0,140.1,5):
            gcu = gcurve(color = color.orange)
            for x in np.arange(0,15.1,0.5):
                gcu.plot(pos=(x,y))     
    pos1_Plot = gcurve(color=b1color)
    pos2_Plot = gcurve(color=b2color)

    vel_graph = graph(canvas=scene4, width=500, height=300,xtitle='t(s)',
                ytitle='v (m/s)',xmax=15.,xmin=0.,ymax=30,ymin=0,align='left', 
                foreground=color.black, background=color.white)
    for x in np.arange(0,15.1,0.5):
        gcu = gcurve(color = color.orange)
        for y in np.arange(0,30.1,1):
            gcu.plot(pos=(x,y))
    for y in np.arange(0,30.1,1):
            gcu = gcurve(color = color.orange)
            for x in np.arange(0,15.1,0.5):
                gcu.plot(pos=(x,y))     
    vel1_Plot = gcurve(color=b1color)
    vel2_Plot = gcurve(color=b2color)
    
graficos()

ejecutar = False
def inicio():
    global ejecutar
    ejecutar = not ejecutar    
    
def nuevo():     #crea una pantalla nueva (reset)
    global scene4, pista
    global Vo2,ac2
     
    scene4.visible = False       
    for obj in scene4.objects:
        obj.visible = False        
    scene4.visible = True    
    
    vel1_Plot.delete()
    vel2_Plot.delete()
    pos1_Plot.delete()
    pos2_Plot.delete()
    X1 = 30
    X2 = 0
    vel1_inic.x = 0.
    vel2_inic.x = 0. 
    objetos()
    
scene4.caption = '\n\n\n\n\n\n\n\n\n                 CONTROLES \n\n\n'
scene4.append_to_caption('             ')
button(text="INICIAR",align='right', bind=inicio)
scene4.append_to_caption('    ')
button(text="NUEVO",align='right', bind=nuevo)

def simulacion():
    #global 
    t1 = 0
    deltat = 0.02
    terminar = False
    Vo1 = vel1_inic.x
    Vo2 = vel2_inic.x
    X1 = 30
    X2 = 0.
    movil1.vel = vel1_inic
    movil2.vel = vel2_inic
    movil1.pos = pos1_inic
    movil2.pos = pos2_inic 
    while not terminar:
        rate(100)
        if (X1 > X2 > X1-0.05):
            poscruce = X1            
            tcruce = t1
            vcruce1=movil1.vel.x
            vcruce2=movil2.vel.x        
        if(t1 <= 12):
            t1 = t1 + deltat
            X1 = 30 + Vo1*t1 + 0.5*ac1*t1**2
            movil1.pos.x = -10.5+ (Vo1* t1 + 0.5*ac1* t1**2)/4       
            movil1.vel.x = Vo1 + ac1* t1
            pos1_Plot.plot(pos=(t1,X1))
            vel1_Plot.plot(pos=(t1,movil1.vel.x))
            box(pos=vector(movil1.pos.x ,-3.6,movil1.pos.z), axis=pista.axis,
                    size=vector(0.03,0.03,0.04), color=vector(1,0,0)) 
           
            X2 = Vo2*t1 + 0.5*ac2*t1**2
            movil2.pos.x = -18 + (Vo2*t1 + 0.5*ac2*t1**2)/4         
            movil2.vel.x = Vo2 + ac2*t1
            vel2_Plot.plot(pos=(t1,movil2.vel.x))
            pos2_Plot.plot(pos=(t1,X2))
            box(pos=vector(movil2.pos.x,-3.6,movil2.pos.z), axis=pista.axis,
                     size=vector(0.03,0.03,0.03), color=vector(0,0,1))
            
        else:    
            terminar = True
        
    poscruce = 90.
    cruce = label( text="Linea de\n  cruce",xoffset=-10,yoffset=-120,
                pos=vector(4.35,-1,0.),space=70,opacity=0.1,color=color.black)
    tiempode1 = label(pos=vector(-4,6,0),color=b2color,opacity=0.1,
            text=" a) Tiempo transcurrido(en s): "+str("%0.2f"%tcruce),height=13)
    Posicionde1 = label(pos=vector(-4.6,4.5,0),color=color.blue,opacity=0.1,
            text=" b) Posicion de cruce (en m): "+str("%0.2f"%poscruce),height=13)
    VelocidadC = label(pos=vector(3,6,0),color=color.blue,opacity=0.1,
            text=" c) Velocidad camion (en m/s): "+str("%0.2f"%vcruce1),height=13)
    VelocidadA = label(pos=vector(3.4,4.5,0),color=color.blue,opacity=0.1,
            text=" Velocidad automovil (en m/s): "+str("%0.2f"%vcruce2),height=13)

while 1:    
    rate(80)
    if ejecutar:
        simulacion()
        ejecutar = not ejecutar
