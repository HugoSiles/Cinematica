#mov_rect_02
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
pos1_inic.x =-18.
vel1_inic.x =60.0/3.6
ac1 = -1.5
pos2_inic.x=-18.
vel2_inic.x=40./3.6
ac2 = 0.
                 
#genera ventana de pista y objetos en movimiento
scene3=canvas()
scene3.title="                                                        ESCENARIO DEL MOVIMIENTO"
scene3.width=900; scene3.height=450
scene3.autoscale=0
scene3.range=(8)
scene3.foreground=fgcolor
scene3.center=vector(0,0,1)
scene3.background=color.gray(0.9) 
#scene3.lights = [vector(0,0.3,0) ]
scene3.ambient = vector(0.4,0.4,0.4)
scene3.forward=vector(0.,-0.1,-0.06)
scene3.align='left'

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
    pos1_inic.y=-alto_bloque/1.6-3 ; pos1_inic.z=-0.6
    pos2_inic.y=-alto_bloque/1.6-3 ; pos2_inic.z=0.6
    p1= vector(-18,pos1_inic.y,pos1_inic.z)
    p2=vector(-18+0.,pos2_inic.y,pos2_inic.z)
    movil1 = box(pos=p1, axis=pista.axis, length=0.7, height=alto_bloque,
                 width=.6, color=b1color)
    movil2 = box(pos=p2, axis=pista.axis, length=0.6, height=alto_bloque,
                 width=.6, color=b2color)    
objetos()

ejecutar = False
def inicio():
    global ejecutar
    ejecutar = not ejecutar    
    
def nuevo():     #crea una pantalla nueva (reset)
    global scene3, pista,ac1,ac2
         
    scene3.visible = False       
    for obj in scene3.objects:
        obj.visible = False        
    scene3.visible = True    
    X1 = 0
    X2 = 0
    ac1 = -1.5
    ac2 = 0
    vel1_inic.x = 60/3.6
    vel2_inic.x = 40/3.6 
    objetos()
    vel1_Plot.delete()
    vel2_Plot.delete()
    pos1_Plot.delete()
    pos2_Plot.delete()
#Graficos del movimiento

def graficos():
    global pos1_Plot, pos2_Plot, vel1_Plot, vel2_Plot
    pos_graph = graph(canvas=scene3,width=500, height=300, 
            xtitle='t(s)', ytitle='x (m)',xmax=12., xmin=0.,ymax=140,ymin=0, 
            align='left',foreground=fgcolor, background=bgcolor)
    for x in np.arange(0,12.1,.5):
        gcu = gcurve(color = color.orange)
        for y in np.arange(0,140.1,5):
            gcu.plot(pos=(x,y))
    for y in np.arange(0,140.1,5):
            gcu = gcurve(color = color.orange)
            for x in np.arange(0,12.1,0.5):
                gcu.plot(pos=(x,y))     
    pos1_Plot = gcurve(color=b1color)
    pos2_Plot = gcurve(color=b2color)

    vel_graph = graph(canvas=scene3,width=500, height=300, 
            xtitle='t(s)', ytitle='v (m/s)',xmax=12.,xmin=0.,ymax=18,ymin=0, 
            align='left',foreground=fgcolor, background=bgcolor)
    for x in np.arange(0,12.1,.5):
        gcu = gcurve(color = color.orange)
        for y in np.arange(0,18.1,0.6):
            gcu.plot(pos=(x,y))
    for y in np.arange(0,18.1,0.6):
            gcu = gcurve(color = color.orange)
            for x in np.arange(0,12.1,0.5):
                gcu.plot(pos=(x,y))     
    vel1_Plot = gcurve(color=b1color)
    vel2_Plot = gcurve(color=b2color)
    
graficos()

scene3.caption = '\n\n\n\n\n\n\n\n\n                     CONTROLES \n\n\n'
scene3.append_to_caption('              ')
button(text="INICIAR",align='right', bind=inicio)
scene3.append_to_caption('            ')
button(text="NUEVO",align='right', bind=nuevo)

# segmento del movimiento de los objetos

def simulacion():    
    t1 = 0
    deltat = 0.01
    terminar = False
    Vo1 = vel1_inic.x
    Vo2 = vel2_inic.x
    X1 = 0
    X2 = 0
    movil1.vel = vel1_inic
    movil2.vel = vel2_inic
    movil1.pos = pos1_inic
    movil2.pos = pos2_inic
    
    while not terminar:    
        rate(100)    
        if (X1-0.05 < X2 < X1+0.001):
            poscruce = X1            
            tcruce = t1       
        if (t1 < 11.11):            
            X1 = Vo1* t1 + 0.5*ac1* t1**2 
            movil1.pos.x = -18 + (Vo1* t1 + 0.5*ac1* t1**2)/4
            movil1.vel.x = Vo1 + ac1*t1
            pos1_Plot.plot(pos=(t1,X1))
            vel1_Plot.plot(pos=(t1,movil1.vel.x))
            box(pos=vector(movil1.pos.x ,-3.5,movil1.pos.z), axis=pista.axis,
                    size=vector(0.03,0.03,0.04), color=vector(1,0,0))     
            X2 = Vo2 * t1 + 0.5* ac2*t1**2
            movil2.pos.x = -18 + (Vo2* t1 + 0.5* ac2*t1**2)/4  
            movil2.vel.x = Vo2 + ac2*t1
            vel2_Plot.plot(pos=(t1,movil2.vel.x))
            pos2_Plot.plot(pos=(t1,X2))
            box(pos=vector(movil2.pos.x,-3.5,movil2.pos.z), axis=pista.axis,
                    size=vector(0.03,0.03,0.04), color=b2color)        
            t1 = t1 + deltat        
        else: 
            terminar = True
    cruce = label( text="Linea de\n  cruce",xoffset=0,yoffset=-120,
                   pos=vector(2.25,-1,0.),space=70,opacity=0.2, color=color.black)       
    tiempode1 = label(pos=vector(-4,6,0),color=b1color,opacity=0.2,height=13,
                  text="a)Tiempo transcurrido(en s): "+str("%0.3f"%tcruce))
                      
    Posicionde1 = label(pos=vector(-4.4,4.9,0),color=b1color,opacity=0.2,
                  text="b)Distancia Xr (en m): "+str("%0.3f"%X1),height=13)
    deltaX = X2 - X1
    separacion = label(pos=vector(-4.9,3.6,0),color=color.red,opacity=0.2,
            text="c)Separacion (Xa-Xr) (en m): "+str("%0.3f"%deltaX),height=13)
    
while 1:    
    rate(80)
    if ejecutar:
        simulacion()
        ejecutar = not ejecutar



        


