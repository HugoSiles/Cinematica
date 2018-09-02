
from vpython import *
from IPython.display import clear_output
#import numpy as np
BW = 0
if BW==0:
    fgcolor=color.black; bgcolor=color.white
else:
    fgcolor=color.white; bgcolor=color.black

#genera ventana de  objetos 
scene = canvas()
scene.title="                                   SISTEMAS DE REFERENCIA   Por Hugo Siles A."
scene.width=900
scene.height=300
scene.range=(10)
scene.foreground=fgcolor
scene.center=vector(0,0.1,0)
scene.background=(bgcolor) 
#; scene.lights = [vector(0,0.2,0) ]
scene.ambient = vector(0.7,0.7,0) 
scene.forward=vector(0.,0,-0.1)
scene.autoscale = 0
scene.align = 'left'

def objetos():

    label1 = label(pos=vector(-10.,-7.5,0),color=color.red,opacity=0.1,font='sans',
                text=" Sistema de referencia 3D",height=16, box=False)
    label2 = label(pos=vector(14.,-7.5,0),color=color.red,opacity=0.1,font='sans',
                text=" Sistema de referencia 2D",height=16, box=False)
    eje0_x = curve(pos=[(-12,0,0),(-2,0,0)],radius=0.06,
                color = vector(0,0,0))
    pointerx = arrow(pos=vector(-2,0,0), axis=vector(0.8,0,0),
                color = vector(0,0,0),shaftwidth=.11,headwidth=0.4)
    eje0_y= curve(pos=[(-12,0,0), (-12,8,0)],color = vector(0,0,0),
                radius=0.06)
    pointery = arrow(pos=vector(-12,8,0), axis=vector(0,0.8,0),
                color = vector(0,0,0), shaftwidth=.1,headwidth=0.3)
    eje0_z = curve(pos=[(-12,0,0),(-17.,-5,0)],radius=0.06,
                color = vector(0,0,0))
    pointerz = arrow(pos=vector(-17,-5,0), axis=vector(-0.45,-0.5,0),
                color = vector(0,0,0), shaftwidth=.08,headwidth=0.3)
    coordX = label(pos=vector(-2,-1,0),font='sans', text=" x ",height=16,
                   box=False)
    coordY = label(pos=vector(-13,8,0), font='sans', text=" y ",height=16,                   
                   box=False)
    coordZ = label(pos=vector(-18.5,-5.,0), font='sans', text=" z ",height=16,                   
                   box=False)
    dist3DXo = label(pos=vector(-3,1,0),font='sans', text=" xo ",height=16,
                   box=False)
    dist3DYo = label(pos=vector(-13.2,6.2,0),font='sans', text=" yo ",height=16,
                   box=False)
    dist3DZo = label(pos=vector(-16.8,-3.,0),font='sans', text=" zo ",height=16,
                   box=False)
    
    puntoAA = label(pos=vector(-6.,3.5,0),font='sans', text=" A ",height=16,
                   box=False)
    for i in range(-4,3,1):
        distanciax_z=curve(pos=[(-7,i,0),(-7,i+0.5,0)],radius=0.06,
                    color=vector(0,0,1))
    for i in range(-16,-7,1):
        distanciay_z=curve(pos=[(i,-4,0),(i+0.5,-4,0)],radius=0.06,
                         color=vector(0,0,1))
    for i in range(0,4,1):
        distanciax_y=curve(pos=[(-3.3-i+0.45,-i,0),(-3.3-i,-i-0.5,0)],radius=0.06,
                         color=vector(0,0,1))
    for i in range(0,5,1):
        j=i*0.8
        distanciax_y=curve(pos=[(-7.5-i+0.45,3+j-0.5,0),(-7.5-i,3+j-0.2,0)],radius=0.06,
                         color=vector(0,0,1))
    
    eje1_x = curve(pos=[(8,-3,0),(21,-3,0)],radius=0.06,color = vector(0,0,0))
    pointer1x = arrow(pos=vector(21,-3,0), axis=vector(1.2,0,0),
                color = vector(0,0,0),shaftwidth=.1,headwidth=0.3)
    eje0_y = curve(pos=[(8,-3,0),(8,8,0)],radius=0.06,color = vector(0,0,0))
    pointer1y = arrow(pos=vector(8,8,0), axis=vector(0.,1.,0),
                color = vector(0,0,0),shaftwidth=.1,headwidth=0.3)
    coordX = label(pos=vector(21,-4,0),font='sans', text=" x ",height=16,
                   box=False)
    coordY = label(pos=vector(7.,8,0), font='sans', text=" y ",height=16,
                   box=False)
    distanciaXo = label(pos=vector(17.5,-4.,0),font='sans', text=" xo ",height=16,
                   box=False)
    distanciaYo = label(pos=vector(6.6,2.5,0), font='sans', text=" yo ",height=16,
                   box=False)
    puntoA = label(pos=vector(18.5,3.5,0),font='sans', text=" A ",height=16,
                   box=False)
    for i in range(8,18,1):
        distanciax=curve(pos=[(i,2.5,0),(i+0.5,2.5,0)],radius=0.06,
                         color=vector(0,0,1))
    for i in range(-3,3,1):
        distanciay=curve(pos=[(17.5,i,0),(17.5,i+0.5,0)],radius=0.06,
                         color=vector(0,0,1))
objetos()    
