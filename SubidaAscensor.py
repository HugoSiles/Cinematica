
from vpython import *

BW=0
if BW==0:
    fgcolor=color.black; bgcolor=color.white
else:
    fgcolor=color.white; bgcolor=color.black
b1color=color.red
b2color=vector(0,0,1)

#genera ventana de edificio y objetos en movimiento
scene5=canvas()
scene5.title="                                 SUBIDA DE ASCENSOR     Por Hugo Siles Alvarado"
scene5.width=750; scene5.height=500
#scene.autoscale=0
scene5.range=(80)
scene5.foreground=fgcolor
scene5.center=vector(20,40,0)
scene5.background=vector(0.85,0.9,0.9)
scene5.ambient = vector(0.3,0.3,0.2)
scene5.align='left'    
distant_light(direction=vector(0,10,-10), color=color.gray(0.85))

def objetos():
    global caja
    ground = box(pos=vector(20,-8,0),size=vector(250,2,50), color=vector(0.6,0.6,0.5))
    edificio = box(size=vector(28,97,10),pos=vector(20,42,0),color=vector(0.8,0.4,0))
    terraza = box(size=vector(45.5,2,10),pos=vector(28.75,91,0),color=vector(0.8,0.4,0))
    muro = box(size=vector(7,97,10),pos=vector(48.,42,0),color=vector(0.8,0.4,0))
    #f = frame(pos=(4.5,-90,0))
    caja1=box(size=vector(1,8,4),pos=vector(36,-2.5,0),color=color.red)
    caja2=box(size=vector(1,8,4),pos=vector(42,-2.5,0),color=color.red)
    caja3=box(size=vector(6,1,4),pos=vector(39,1.,0),color=color.red)
    caja4=box(size=vector(6,1,4),pos=vector(39,-6.,0),color=color.red)
    caja5=box(size=vector(6,4,1),pos=vector(39.1,-4,-1.5),color=color.orange)
    caja=compound([caja1,caja2,caja3,caja4,caja5])
    
    lineaVc = curve(pos=[(20,-2,5.), (20,88.,5.)],color = color.cyan,
                      radius=0.4)
    lineaVi = curve(pos=[(10,-2,5.), (10,88,5.)],color = color.cyan,
                      radius=0.4)
    lineaVd = curve(pos=[(30,-2,5.), (30,88,5.)],color = color.cyan,
                      radius=0.4)
    for y  in arange(-2,91,6.0):
        cu = curve(color=color.cyan,radius=0.4)
        cu.append([vector(10,y,5),vector(30,y,5)])
    for y  in arange(-2,91,6.0):
        cu = curve(color=color.cyan,radius=0.4)
        cu.append([vector(44.5,y,5),vector(50.5,y,5)])    
         
    cuerda1 = curve(pos=[(36.5,-3,0),(36.5,90,0)],color=color.black,radius=0.3)    
    cuerda2 = curve(pos=[(41.5,-3,0),(41.5,90,0)],color=color.black,radius=0.3)
objetos()


ejecutar = False
def inicio():
    global ejecutar
    ejecutar = not ejecutar 

def nuevo():   
    global scene5, ang        
    # clean up the main scene    
    scene.visible = False             
    for obj in scene5.objects:
        obj.visible = False          
    scene5.visible = True    
    objetos()
##*************************************
##Define fucniones de los botones de control
##*************************************
scene5.caption = '\n\n\n\n\n\n\n               CONTROLES \n\n\n\n'
scene5.append_to_caption('             ')
button(text="INICIAR",align='right', bind=inicio)
scene5.append_to_caption('    ')
button(text="NUEVO",align='right', bind=nuevo)

#Graficos del movimiento    
def graficos():
    global pos1_Plot,vel1_Plot
    pos_graph = graph(canvas=scene5, width=500, height=280,
             xtitle='t(s)', ytitle='y (m)', xmax=20., xmin=0., ymax=60, ymin=0,
             align = 'left', foreground=fgcolor, background=bgcolor)
    for x in arange(0,20.1,1):
        gcu = gcurve(color = color.orange)
        for y in arange(0,60.1,5):
            gcu.plot(pos=(x,y))
    for y in arange(0,60.1,5):
            gcu = gcurve(color = color.orange)
            for x in arange(0,20.1,1):
                gcu.plot(pos=(x,y))     
    pos1_Plot = gcurve(color=b1color)

    vel_graph = graph(canva=scene5,width=500, height=280,
             xtitle='t(s)', ytitle='v (m/s)', xmax=20., xmin=0., ymax=6, ymin=0,
             align = 'left', foreground=fgcolor, background=bgcolor)
    for x in arange(1,20.1,1):
        gcu = gcurve(color = color.orange)
        for y in arange(0,6.1,0.5):
            gcu.plot(pos=(x,y))
    for y in arange(0,6.1,0.5):
            gcu = gcurve(color = color.orange)
            for x in arange(0,20.1,1):
                gcu.plot(pos=(x,y))     
    vel1_Plot = gcurve(color=b1color)
graficos()

def simulacion():
    
    segs = 0
    segs1 = 0
    segs2 = 0
    dt = .01
    #velocidad del asensor 
    Vo = 0    
    ac = 0.875 # m/s^2
    finished = False
    while not finished:
    # go thru the loop no more than 100 times/s
        rate(200) 
        segs += dt
        caja.pos.x=39
        asc = vector(22,caja.pos.y,0)
        if segs <=5:        
            caja.pos.y=-2.5+(0.5*ac*segs**2)*1.7
            Vo = ac*segs
            y1 = caja.pos.y
        elif 5< segs <=12:
            segs1 += dt
            caja.pos.y = y1+(Vo*segs1)*1.7        
            y2 = caja.pos.y
            V2 = Vo
            #print 'hola'
        else:        
            segs2 += dt
            Vo = V2-ac*segs2
            caja.pos.y = y2+(V2*segs2-0.5*ac*segs2**2)*1.7
        
        pos1_Plot.plot(pos=(segs,caja.pos.y/1.7+1.5 ))
        vel1_Plot.plot(pos=(segs,Vo)) 
     
    # and ball.pos.y-2 <= 0):
        if (segs > 17):
            finished = True       
    aceleracion = label(pos=vector(-60,80,0),color=color.blue,opacity=0.2,
                text="a)Aceleracion (en m/s^2): "+str("%0.3f"%ac),height=12)
    VelocidadMax = label(pos=vector(-60,70.2,0),color=color.blue,opacity=0.2,
                text="b)Velocidad maxima (en m/s): "+str("%0.3f"%V2),height=12)

while 1:    
    rate(80)
    if ejecutar:
        simulacion()
        ejecutar = not ejecutar

#simulacion()
